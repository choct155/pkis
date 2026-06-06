#!/usr/bin/env python3
"""Generalized reader-payload builder for the PKIS read+listen tool.

  reader_build.py <slug> [extract|narrate|full] [max_segments]
  reader_build.py <arxiv_id> <slug> [stage] [max_segments]   # back-compat

The builder is SLUG-DRIVEN: it loads the source node and routes by what input exists:
  • arXiv id in source_url     → ar5iv HTML  (best quality: real LaTeX from alttext)
  • PDF in the doc store        → Claude PDF document-block extraction (prompt-cached)
  • http(s) source_url          → fetch + bs4 strip + Claude extraction
All three routes emit the same [{id,title,paper_md}] segment shape, then share the
narrate → Piper TTS → mp3 backend.

Stages:
  extract  — route + segment, print paper_md per section (no narration/TTS).
  narrate  — extract + Claude narration; print narration per section (no TTS).
  full     — extract + narrate + Piper TTS -> audio.mp3 + payload.json.
  revoice  — re-TTS an already-built reader from payload.json's saved narration
             with the current PIPER_MODEL (no extraction, no Claude calls);
             overwrites audio.mp3 + recomputes timestamps. Use to switch voices.

Runs on the VPS in the app venv (imports `app` to reuse the Anthropic client + graph tools).
Env for full/revoice: PIPER, PIPER_MODEL, LD_LIBRARY_PATH, OUTDIR (defaults to WIKI_DIR/reader/<slug>).
"""
import os, sys, re, json, html, time, base64, glob, subprocess, tempfile, shutil, wave, urllib.request

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

import app  # reuse anthropic_client, tool_get_related, load_node, find_node_path_by_iri, WIKI_DIR, DOCS_DIR

MODEL = "claude-sonnet-4-6"               # narration: quality-critical
EXTRACT_MODEL = os.environ.get("EXTRACT_MODEL", "claude-haiku-4-5")  # PDF/HTML transcription: cheap, mechanical
SKIP_TITLES = ("references", "acknowledg", "appendix", "bibliography", "supplementary")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)")


# ── small helpers ─────────────────────────────────────────────────────────
def _collapse(s):
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" *\n *", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _resp_text(resp):
    return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text").strip()


# per-model token accounting (in, out) for a cost estimate at the end of a build
_USAGE = {}
_PRICE = {"claude-sonnet-4-6": (3.0, 15.0), "claude-haiku-4-5": (1.0, 5.0)}


def _cost_summary():
    total = 0.0
    lines = []
    for m, (ti, to) in _USAGE.items():
        pin, pout = _PRICE.get(m, (3.0, 15.0))
        c = ti / 1e6 * pin + to / 1e6 * pout
        total += c
        lines.append(f"  {m}: in={ti:,} out={to:,} -> ${c:.3f}")
    return "\n".join(lines) + f"\n  TOTAL ~${total:.3f}"


def _create(**kw):
    """messages.create with backoff on 429 — the org's input-tokens-per-minute limit is low,
    so a big PDF/extraction call can transiently exceed it; sleep and retry rather than crash."""
    last = None
    for attempt in range(7):
        try:
            resp = app.anthropic_client.messages.create(**kw)
            try:
                u = resp.usage
                acc = _USAGE.setdefault(kw.get("model"), [0, 0])
                acc[0] += getattr(u, "input_tokens", 0); acc[1] += getattr(u, "output_tokens", 0)
            except Exception:
                pass
            return resp
        except Exception as e:
            last = e
            msg = str(e).lower()
            if "rate_limit" in msg or "429" in msg or getattr(e, "status_code", None) == 429:
                wait = 20 * (attempt + 1)
                try:
                    ra = e.response.headers.get("retry-after")
                    if ra:
                        wait = max(wait, int(float(ra)) + 2)
                except Exception:
                    pass
                print(f"  rate-limited; sleeping {wait}s (attempt {attempt + 1}/7)")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"rate-limit retries exhausted: {last}")


def _parse_json(t):
    """Tolerant JSON extraction from a model response (strips code fences / prose)."""
    t = t.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\n", "", t)
        t = re.sub(r"\n```\s*$", "", t)
    i, j = t.find("{"), t.rfind("}")
    if i == -1 or j == -1:
        raise ValueError("no JSON object in response")
    return json.loads(t[i:j + 1])


def _slugify(title, i):
    s = re.sub(r"[^a-z0-9]+", "-", (title or "").lower()).strip("-")[:24]
    return s or f"s{i}"


def _segs_from_sections(sections, max_seg):
    """Build segments from a list of {title, markdown} dicts (PDF/HTML routes)."""
    segs = []
    for sec in sections:
        title = _collapse(str(sec.get("title") or ""))
        md = (sec.get("markdown") or sec.get("paper_md") or "").strip()
        if len(md) < 60:
            continue
        if title and any(k in title.lower() for k in SKIP_TITLES):
            continue
        segs.append({"id": _slugify(title, len(segs)),
                     "title": title or f"Section {len(segs) + 1}", "paper_md": md})
        if len(segs) >= max_seg:
            break
    return segs


# ── route 1: ar5iv HTML (arXiv) ────────────────────────────────────────────
def fetch_ar5iv(arxiv_id):
    url = f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "PKIS-Reader/1.0 (pkis@pkis.dev)"})
    return urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")


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


def extract_segments(htmltext, max_segments=40):
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


def fetch_arxiv_pdf(arxiv_id, dest):
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "PKIS-Reader/1.0 (pkis@pkis.dev)"})
    data = urllib.request.urlopen(req, timeout=60).read()
    with open(dest, "wb") as f:
        f.write(data)
    return dest


def arxiv_route(arxiv_id, max_seg):
    print(f"  route=arxiv ar5iv {arxiv_id}")
    try:
        htmltext = fetch_ar5iv(arxiv_id)
        segs = extract_segments(htmltext, max_seg)
    except Exception as e:
        print(f"  ar5iv fetch failed: {e}")
        segs, htmltext = [], ""
    if segs:
        title_el = BeautifulSoup(htmltext, "html.parser").find("h1")
        title = _collapse(title_el.get_text(" ", strip=True)) if title_el else ""
        return segs, title
    # ar5iv gave us nothing (no HTML render for this paper) → fall back to the arXiv PDF
    print(f"  ar5iv yielded 0 segments; falling back to arXiv PDF for {arxiv_id}")
    tmp = tempfile.mkdtemp()
    try:
        pdf = fetch_arxiv_pdf(arxiv_id, os.path.join(tmp, f"{arxiv_id}.pdf"))
        return pdf_route(pdf, max_seg)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ── shared faithful-extraction prompt (PDF + HTML routes) ───────────────────
# Output is SENTINEL-DELIMITED, not JSON: faithful markdown is full of LaTeX backslashes,
# quotes, and newlines that routinely break JSON string escaping. Raw text between sentinels
# sidesteps all of that. (The document is also sent once per call to respect the 30k ITPM tier.)
SEC = "<<<SECTION>>>"
TIT = "<<<TITLE>>>"
EXTRACT_SYSTEM = (
    "You extract the FAITHFUL full text of a document (a paper, book chapter, or article) into "
    "ordered sections for a read-along listening tool.\n"
    "RULES:\n"
    "1. Preserve the author's ACTUAL wording verbatim where it is prose — do NOT summarize or "
    "paraphrase. The text is read alongside the audio, so it must match the source.\n"
    "2. Render mathematics as inline $LaTeX$ or display $$LaTeX$$, reconstructing each equation "
    "faithfully.\n"
    "3. Split at the document's natural section/subsection headings, in reading order. Drop "
    "front-matter, running heads/footers, page numbers, site chrome/nav, reference lists, and "
    "acknowledgments; KEEP figure/table captions as plain text.\n"
    "4. OUTPUT FORMAT (not JSON): first line is exactly '" + TIT + " <document title>'. Then for "
    "each section, a line that is exactly '" + SEC + " <section heading>' followed by the "
    "section's faithful markdown on the lines beneath it. Output nothing else — no JSON, no fences."
)


def _parse_sections(text):
    """Parse the sentinel-delimited extraction format into (title, [{title, markdown}])."""
    title = ""
    parts = text.split(SEC)
    m = re.search(re.escape(TIT) + r"\s*(.+)", parts[0])
    if m:
        title = m.group(1).strip()
    sections = []
    for p in parts[1:]:
        p = p.strip()
        if not p:
            continue
        head, _, body = p.partition("\n")
        sections.append({"title": head.strip().lstrip("#").strip(), "markdown": body.strip()})
    return title, sections


# ── route 2: PDF document-block extraction (page-chunked) ───────────────────
# A PDF block costs ~2.5k input tokens/page (text + a rendered image per page), so a long
# document in ONE request exceeds the org's 30k tokens/minute tier. Split into small page
# ranges, vision-extract each (math fidelity preserved), and stitch sections across chunks.
CHUNK_PAGES = 6


def _split_pdf(data, chunk_pages):
    import io, pypdf
    reader = pypdf.PdfReader(io.BytesIO(data))
    n = len(reader.pages)
    chunks = []
    for start in range(0, n, chunk_pages):
        end = min(start + chunk_pages, n)
        w = pypdf.PdfWriter()
        for i in range(start, end):
            w.add_page(reader.pages[i])
        buf = io.BytesIO(); w.write(buf)
        chunks.append((start + 1, end, buf.getvalue()))
    return n, chunks


def _extract_pdf_doc(b64, instr):
    resp = _create(
        model=EXTRACT_MODEL, max_tokens=12000, system=EXTRACT_SYSTEM,
        messages=[{"role": "user", "content": [
            {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": b64}},
            {"type": "text", "text": instr + " Output ONLY the delimited text."}]}])
    if getattr(resp, "stop_reason", "") == "max_tokens":
        print("  WARNING: a chunk hit max_tokens — its tail may be truncated")
    return _parse_sections(_resp_text(resp))  # (title, sections)


def _norm_title(s):
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def pdf_route(pdf_path, max_seg):
    print(f"  route=pdf {pdf_path}")
    data = open(pdf_path, "rb").read()
    if len(data) > 40 * 1024 * 1024:
        raise SystemExit("PDF too large (>40MB); split it first")
    npages, chunks = _split_pdf(data, CHUNK_PAGES)
    print(f"  pdf: {npages} pages -> {len(chunks)} chunk(s) of <= {CHUNK_PAGES}p")
    if len(chunks) == 1:
        ctitle, sections = _extract_pdf_doc(base64.standard_b64encode(data).decode(),
                                            "Extract this document per the rules.")
        return _segs_from_sections(sections, max_seg), _collapse(ctitle)
    title, merged = "", []
    for idx, (lo, hi, cdata) in enumerate(chunks):
        instr = (f"This is pages {lo}-{hi} of a {npages}-page document. Extract the sections that "
                 "appear on these pages. A section may begin before or continue past this chunk — "
                 "extract whatever of it is present here.")
        ctitle, sections = _extract_pdf_doc(base64.standard_b64encode(cdata).decode(), instr)
        if idx == 0:
            title = _collapse(ctitle)
        added = 0
        for sec in sections:
            st = _collapse(str(sec.get("title") or ""))
            md = (sec.get("markdown") or "").strip()
            if not md:
                continue
            # stitch a section that spanned the chunk boundary back onto the previous one
            if merged and (not st or _norm_title(st) == _norm_title(merged[-1]["title"])):
                merged[-1]["markdown"] += "\n\n" + md
            else:
                merged.append({"title": st, "markdown": md}); added += 1
        print(f"  chunk p{lo}-{hi}: +{added} new sections (total {len(merged)})")
    return _segs_from_sections(merged, max_seg), title


# ── route 3: web HTML extraction (single call) ──────────────────────────────
def fetch_html(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; PKIS-Reader/1.0)"})
    return urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")


def html_route(url, max_seg):
    print(f"  route=html {url}")
    try:
        raw = fetch_html(url)
    except Exception as e:
        raise SystemExit(f"HTML fetch failed ({e}) — likely paywalled or blocked")
    soup = BeautifulSoup(raw, "html.parser")
    for t in soup(["script", "style", "nav", "header", "footer", "aside", "form", "noscript", "svg"]):
        t.decompose()
    main = soup.find("article") or soup.find("main") or soup.body or soup
    text = _collapse(main.get_text("\n", strip=True))[:60000]
    if len(text) < 400:
        raise SystemExit("HTML extraction yielded too little text (landing page, paywall, or JS-rendered?)")
    resp = _create(
        model=EXTRACT_MODEL, max_tokens=12000, system=EXTRACT_SYSTEM,
        messages=[{"role": "user", "content":
                   f"DOCUMENT TEXT (extracted from {url}):\n\n{text}\n\nOutput ONLY the delimited text."}])
    ctitle, sections = _parse_sections(_resp_text(resp))
    return _segs_from_sections(sections, max_seg), _collapse(ctitle)


# ── router ─────────────────────────────────────────────────────────────────
def load_source_node(slug):
    iri = f"pkis:source:{slug}"
    try:
        path = app.find_node_path_by_iri(iri)
    except Exception:
        path = None
    if not path:
        cand = str(app.WIKI_DIR / "sources" / f"{slug}.md")
        path = cand if os.path.exists(cand) else None
    return app.load_node(path) if path else {}


def find_docstore_pdf(slug):
    d = os.path.join(str(app.DOCS_DIR), "sources", slug)
    pdfs = sorted(glob.glob(os.path.join(d, "*.pdf")))
    return pdfs[0] if pdfs else None


def route_segments(slug, max_seg, forced_arxiv=None):
    node = load_source_node(slug)
    fm = node.get("frontmatter", {}) if isinstance(node, dict) else {}
    url = str(fm.get("source_url") or fm.get("url") or "")
    arx = forced_arxiv or (ARXIV_RE.search(url).group(1) if ARXIV_RE.search(url) else None)
    if arx:
        segs, title = arxiv_route(arx, max_seg)
    else:
        pdf = find_docstore_pdf(slug)
        if pdf:
            segs, title = pdf_route(pdf, max_seg)
        elif url.startswith("http"):
            segs, title = html_route(url, max_seg)
        else:
            raise SystemExit(f"no narratable input for {slug} "
                             "(no arXiv id, no doc-store PDF, no http source_url)")
    title = title or _collapse(str(node.get("title") or "")) or slug
    return segs, title


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
    resp = _create(
        model=MODEL, max_tokens=1200,
        system=NARRATION_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
    return _resp_text(resp)


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


def encode_mp3(wav_path, mp3_path, bitrate=64):
    """Encode a wav to mp3 with lameenc (no ffmpeg). ~64 kbps mono speech ≈ 0.5 MB/min."""
    import lameenc
    with wave.open(wav_path, "rb") as w:
        ch, sr = w.getnchannels(), w.getframerate()
        pcm = w.readframes(w.getnframes())
    enc = lameenc.Encoder()
    enc.set_bit_rate(bitrate)
    enc.set_in_sample_rate(sr)
    enc.set_channels(ch)
    enc.set_quality(3)
    with open(mp3_path, "wb") as f:
        f.write(enc.encode(pcm) + enc.flush())


def revoice(slug):
    """Re-render an already-built reader's audio with the current PIPER_MODEL,
    reusing the saved narration in payload.json — no extraction, no Claude calls.
    Recomputes per-section timestamps (durations shift with a new voice) and
    overwrites audio.mp3 + payload.json in place."""
    piper = os.environ.get("PIPER", "piper")
    model = os.environ["PIPER_MODEL"]
    outdir = os.environ.get("OUTDIR", str(app.WIKI_DIR / "reader" / slug))
    payload_path = os.path.join(outdir, "payload.json")
    with open(payload_path) as f:
        payload = json.load(f)
    secs = payload.get("sections", [])
    if not secs:
        raise SystemExit(f"no sections in {payload_path} — nothing to revoice")
    print(f"revoicing {slug}: {len(secs)} sections with {os.path.basename(model)}")
    tmp = tempfile.mkdtemp()
    try:
        wavs, t = [], 0.0
        for s in secs:
            wav = os.path.join(tmp, f"{s['id']}.wav")
            p = subprocess.run([piper, "--model", model, "--output_file", wav],
                               input=s["narration"], text=True, capture_output=True)
            if p.returncode != 0:
                raise RuntimeError(f"piper failed {s['id']}: {p.stderr[:300]}")
            d = wav_duration(wav); wavs.append(wav)
            s["t_start"] = round(t, 2); s["t_end"] = round(t + d, 2)
            t += d
            print(f"  tts [{s['id']}] -> {t:.1f}s")
        tmp_wav = os.path.join(tmp, "full.wav")
        concat_wavs(wavs, tmp_wav)
        encode_mp3(tmp_wav, os.path.join(outdir, "audio.mp3"))
        payload["total_duration"] = round(t, 2)
        with open(payload_path, "w") as f:
            json.dump(payload, f, indent=2)
        print(f"revoiced {slug}: {t:.1f}s total -> {outdir}/audio.mp3")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(1)
    STAGES = ("extract", "narrate", "full", "revoice")
    # back-compat: <arxiv_id> <slug> [stage] [max]
    forced_arxiv = None
    if re.match(r"^\d+\.\d+$", args[0]) and len(args) >= 2 and args[1] not in STAGES:
        forced_arxiv, slug = args[0], args[1]
        rest = args[2:]
    else:
        slug = args[0]
        rest = args[1:]
    stage = rest[0] if rest else "extract"
    max_seg = int(rest[1]) if len(rest) > 1 else 40

    if stage == "revoice":
        revoice(slug)
        return

    print(f"routing {slug} …")
    segs, title = route_segments(slug, max_seg, forced_arxiv=forced_arxiv)
    title = os.environ.get("READER_TITLE") or title  # per-chapter title override for book splits
    print(f"extracted {len(segs)} segments — title={title!r}")
    for s in segs:
        print(f"  [{s['id']}] {s['title']}  ({len(s['paper_md'])} chars)")

    if stage == "extract":
        print("\n--- first 3 segments (paper_md preview) ---")
        for s in segs[:3]:
            print(f"\n### {s['title']}\n{s['paper_md'][:600]}")
        print("\n=== token usage (extract) ===\n" + _cost_summary())
        return

    if not segs:
        raise SystemExit("no segments extracted — nothing to narrate")

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
        tmp_wav = os.path.join(tmp, "full.wav")
        concat_wavs(wavs, tmp_wav)
        encode_mp3(tmp_wav, os.path.join(outdir, "audio.mp3"))
        stale = os.path.join(outdir, "audio.wav")
        if os.path.exists(stale):
            os.remove(stale)
        payload = {
            "slug": slug, "title": title,
            "source_iri": source_iri, "audio_url": f"/pkis-api/reader/{slug}/audio.mp3",
            "total_duration": round(t, 2), "sections": meta,
        }
        with open(os.path.join(outdir, "payload.json"), "w") as f:
            json.dump(payload, f, indent=2)
        print(f"DONE: {outdir}  ({t:.1f}s, {len(meta)} sections)")
        print("=== token usage (full build) ===\n" + _cost_summary())
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
