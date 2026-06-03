#!/usr/bin/env python3
"""Generalized reader-payload builder for the PKIS read+listen tool.

  reader_build.py <arxiv_id> <slug> [extract|narrate|full] [max_segments]

Stages:
  extract  — fetch ar5iv, segment, print paper_md per section (no Claude/TTS).
  narrate  — extract + Claude narration; print narration per section (no TTS).
  full     — extract + narrate + Piper TTS -> audio.wav + payload.json.

Runs on the VPS in the app venv (imports `app` to reuse the Anthropic client + graph tools).
Env for full: PIPER, PIPER_MODEL, LD_LIBRARY_PATH, OUTDIR (defaults to WIKI_DIR/reader/<slug>).
"""
import os, sys, re, json, html, subprocess, tempfile, shutil, wave, urllib.request

# Load the service's env (ANTHROPIC_API_KEY etc.) BEFORE importing app — app builds the
# Anthropic client at import time, so the key must be present first.
_envfile = os.environ.get("PKIS_ENV", "/home/pkis/.env")
if os.path.exists(_envfile):
    for _line in open(_envfile):
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

from bs4 import BeautifulSoup, NavigableString, Tag

import app  # reuse anthropic_client, tool_get_related, load_node, find_node_path_by_iri

MODEL = "claude-sonnet-4-6"
SKIP_TITLES = ("references", "acknowledg", "appendix", "bibliography", "supplementary")


# ── ar5iv fetch + segmentation ────────────────────────────────────────────
def fetch_ar5iv(arxiv_id):
    url = f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "PKIS-Reader/1.0 (pkis@pkis.dev)"})
    return urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")


def _collapse(s):
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" *\n *", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def render_md(node):
    """Render a section's own content as markdown (math from alttext), skipping nested
    <section> (each subsection becomes its own segment) and citations/figures."""
    parts = []
    for child in node.children:
        if isinstance(child, NavigableString):
            t = str(child)
            if t.strip():
                parts.append(html.unescape(t))
            continue
        if not isinstance(child, Tag):
            continue
        cls = child.get("class") or []
        name = child.name
        if name == "section":
            continue
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            continue
        if name == "math":
            tex = (child.get("alttext") or "").strip()
            if tex:
                disp = child.get("display") == "block"
                parts.append(f"\n\n$$\n{tex}\n$$\n\n" if disp else f" ${tex}$ ")
            continue
        if "ltx_equation" in cls or "ltx_equationgroup" in cls or "ltx_eqn" in " ".join(cls):
            for m in child.find_all("math"):
                tex = (m.get("alttext") or "").strip()
                if tex:
                    parts.append(f"\n\n$$\n{tex}\n$$\n\n")
            continue
        if name in ("cite",) or "ltx_bibliography" in cls or "ltx_figure" in cls or name == "figure":
            continue
        if name in ("p",) or "ltx_para" in cls or "ltx_p" in cls:
            parts.append("\n\n" + render_md(child) + "\n\n")
            continue
        parts.append(render_md(child))
    return _collapse("".join(parts))


def extract_segments(htmltext, max_segments=12):
    soup = BeautifulSoup(htmltext, "html.parser")
    article = soup.find("article") or soup.body or soup
    segs = []
    for sec in article.find_all("section"):
        cls = sec.get("class") or []
        if not any(c.startswith("ltx_") for c in cls):
            continue
        h = sec.find(["h1", "h2", "h3", "h4"])
        title = _collapse(h.get_text(" ", strip=True)) if h else (sec.get("id") or "")
        if not title or any(k in title.lower() for k in SKIP_TITLES):
            continue
        md = render_md(sec)
        if len(md) < 60:   # skip near-empty parent shells / stubs
            continue
        segs.append({"id": sec.get("id") or re.sub(r"[^a-z0-9]+", "-", title.lower())[:20],
                     "title": title, "paper_md": md})
        if len(segs) >= max_segments:
            break
    return segs


# ── PKIS consolidation context ────────────────────────────────────────────
def pkis_context(source_iri):
    try:
        rel = app.tool_get_related(iri=source_iri, direction="both", max_hops=1)
    except Exception:
        return []
    out = []
    for r in rel:
        iri = r["iri"]
        _, nt, _ = app.parse_iri(iri)
        if nt in ("source", "bridge-note"):
            continue
        cov = 0
        try:
            p = app.find_node_path_by_iri(iri)
            if p:
                cov = app.load_node(p).get("coverage", 0)
        except Exception:
            pass
        out.append({"title": r.get("canonical_title", iri), "type": nt, "coverage": cov})
    return out[:14]


NARRATION_SYSTEM = (
    "You generate the spoken LISTENING NARRATION for one section of a research paper, for a "
    "knowledge worker who will hear it on a commute and read the paper alongside.\n\n"
    "HARD RULES:\n"
    "1. This is AUDIO. TRANSLATE math and algorithms into intelligible spoken meaning — never "
    "read raw symbols. For PROSE, stay CLOSE to the section's actual wording (lightly cleaned "
    "for the ear); do NOT over-paraphrase prose.\n"
    "2. TEACH: motivate each step, name the tradeoff (what is traded for what, why a form is "
    "forced), and connect outward to adjacent ideas.\n"
    "3. Tight: ~45-110 seconds of speech. Spell tricky acronyms for the ear (K-L divergence, "
    "M-C-M-C; for ELBO say 'the ELBO').\n"
    "4. PKIS CONSOLIDATION: the listener has an existing knowledge graph (nodes listed). Where "
    "this section genuinely touches one, weave a brief callout — name the node; if its coverage "
    "is low (<=2 of 5), note it's worth deepening. Only where relevant; never force it.\n"
    "5. Output ONLY the narration text — no headings, no markdown, no stage directions."
)


def narrate(seg, ctx):
    nodes = "\n".join(f"- {n['title']} — {n['type']} — coverage {n['coverage']}/5" for n in ctx) or "(none)"
    user = (f"SECTION TITLE: {seg['title']}\n\nSECTION CONTENT (paper text + LaTeX):\n{seg['paper_md']}\n\n"
            f"LISTENER'S EXISTING RELATED NODES:\n{nodes}")
    resp = app.anthropic_client.messages.create(
        model=MODEL, max_tokens=1200,
        system=NARRATION_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text").strip()


# ── TTS (Piper) ───────────────────────────────────────────────────────────
def wav_duration(path):
    with wave.open(path, "rb") as w:
        return w.getnframes() / float(w.getframerate())


def concat_wavs(paths, out):
    with wave.open(paths[0], "rb") as w0:
        params = w0.getparams()
    with wave.open(out, "wb") as o:
        o.setparams(params)
        for p in paths:
            with wave.open(p, "rb") as w:
                o.writeframes(w.readframes(w.getnframes()))


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    arxiv_id, slug = sys.argv[1], sys.argv[2]
    stage = sys.argv[3] if len(sys.argv) > 3 else "extract"
    max_seg = int(sys.argv[4]) if len(sys.argv) > 4 else 12

    print(f"fetching ar5iv {arxiv_id} …")
    segs = extract_segments(fetch_ar5iv(arxiv_id), max_seg)
    print(f"extracted {len(segs)} segments")
    for s in segs:
        print(f"  [{s['id']}] {s['title']}  ({len(s['paper_md'])} chars)")

    if stage == "extract":
        print("\n--- first 3 segments (paper_md preview) ---")
        for s in segs[:3]:
            print(f"\n### {s['title']}\n{s['paper_md'][:600]}")
        return

    source_iri = f"pkis:source:{slug}"
    ctx = pkis_context(source_iri)
    print(f"\nPKIS context: {len(ctx)} related nodes")

    for s in segs:
        s["narration"] = narrate(s, ctx)
        print(f"  narrated [{s['id']}] ({len(s['narration'])} chars)")

    if stage == "narrate":
        for s in segs[:3]:
            print(f"\n### {s['title']}\nNARRATION: {s['narration']}")
        return

    # full: TTS + payload
    piper = os.environ.get("PIPER", "piper")
    model = os.environ["PIPER_MODEL"]
    outdir = os.environ.get("OUTDIR", str(app.WIKI_DIR / "reader" / slug))
    os.makedirs(outdir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    try:
        wavs, meta, t = [], [], 0.0
        for s in segs:
            wav = os.path.join(tmp, f"{s['id']}.wav")
            p = subprocess.run([piper, "--model", model, "--output_file", wav],
                               input=s["narration"], text=True, capture_output=True)
            if p.returncode != 0:
                raise RuntimeError(f"piper failed {s['id']}: {p.stderr[:300]}")
            d = wav_duration(wav); wavs.append(wav)
            meta.append({"id": s["id"], "title": s["title"], "paper_md": s["paper_md"],
                         "narration": s["narration"], "t_start": round(t, 2), "t_end": round(t + d, 2)})
            t += d
            print(f"  tts [{s['id']}] {d:.1f}s -> {t:.1f}s")
        concat_wavs(wavs, os.path.join(outdir, "audio.wav"))
        soup = BeautifulSoup(fetch_ar5iv(arxiv_id), "html.parser")
        title_el = soup.find("h1")
        payload = {
            "slug": slug, "title": _collapse(title_el.get_text(" ", strip=True)) if title_el else slug,
            "source_iri": source_iri, "audio_url": f"/pkis-api/reader/{slug}/audio.wav",
            "total_duration": round(t, 2), "sections": meta,
        }
        with open(os.path.join(outdir, "payload.json"), "w") as f:
            json.dump(payload, f, indent=2)
        print(f"DONE: {outdir}  ({t:.1f}s, {len(meta)} sections)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
