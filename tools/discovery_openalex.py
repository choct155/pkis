#!/usr/bin/env python3
"""Proactive discovery — OpenAlex cite-graph expansion, gated by the frontier.

High signal-to-noise comes from letting the wiki BE the filter:
  1. FRONTIER  — pull the top under-covered, high-inbound concepts (what you're
     trying to learn next) and embed them (bge-small, the same model the server
     uses) into a frontier matrix.
  2. SEEDS     — the existing sources most relevant to that frontier (by cosine),
     so we expand from material you already chose to ingest.
  3. EXPAND    — for each seed, ask OpenAlex for recent works that CITE it
     (cite-graph forward expansion = newer work building on your sources).
  4. GATE      — every candidate must pass: RELEVANCE (cosine to nearest frontier
     concept >= tau), NOVELTY (not already a source; not already in the inbox),
     and have a real abstract. Each survivor carries a graph-grounded REASON.
  5. RANK      — relevance x citation-authority x recency x frontier-priority.

Writes the ranked survivors to discovery_inbox.json and prints an eval table.
Standalone (no app.py import); reads frontier/nodes via the localhost REST API
and the wiki source files directly. Free APIs only (OpenAlex polite pool).

Usage:
  set -a; . /home/pkis/.env; set +a
  /home/pkis/venv/bin/python discovery_openalex.py [--limit 15] [--tau 0.55]
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

import anthropic
import numpy as np

RATIONALE_MODEL = "claude-sonnet-4-6"   # the rationale is the centrepiece — quality matters
RATIONALE_TOOL = {
    "name": "rationale",
    "description": "Explain, for a researcher curating a personal ML/stats knowledge base, "
                   "why this paper is (or isn't) worth reading and how it fits their graph.",
    "input_schema": {"type": "object", "properties": {
        "why": {"type": "string"}, "gap": {"type": "string"}, "fits": {"type": "string"},
        "questions": {"type": "string"}, "agenda": {"type": "string"}},
        "required": ["why", "gap", "fits", "questions", "agenda"]},
}

WIKI = "/home/pkis/pkis-wiki/wiki"
SOURCES_DIR = f"{WIKI}/sources"
INBOX_PATH = "/home/pkis/discovery_inbox.json"
PRIOR_PATH = "/home/pkis/discovery_prior.json"
API = "http://127.0.0.1:5000/pkis-api"
OPENALEX = "https://api.openalex.org/works"
MAILTO = "choct155@gmail.com"
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

N_FRONTIER = 25       # top frontier concepts to target
N_SEEDS = 25          # frontier-relevant existing sources to expand from
CITED_PER_SEED = 25   # recent citing works to pull per seed
FROM_YEAR = 2021      # recency floor for candidates
MIN_CITES = 3         # candidate must have at least this many citations
MAX_PER_SEED = 7      # cap so a single review-paper seed can't flood the list

# Domain gate — the single biggest S/N lever. A paper can be semantically "about"
# variational inference yet be an applied bio/cyber/chem study that merely cites a
# method review. Keep only candidates whose OpenAlex field is methodological/CS-math.
ALLOW_FIELDS = {"Computer Science", "Mathematics", "Decision Sciences",
                "Economics, Econometrics and Finance"}
# Even within CS, OpenAlex tags applied work (cyber, audio, imaging, clinical,
# networking) — deny the clearly-applied subfields. Tunable; relax if the frontier
# shifts toward e.g. vision. Residual in-bucket noise is left to the feedback loop.
DENY_SUBFIELDS = {"Information Systems", "Computer Networks and Communications",
                  "Human-Computer Interaction", "Software", "Hardware and Architecture",
                  "Health Informatics", "Signal Processing",
                  "Computer Vision and Pattern Recognition", "Information Systems and Management"}


# ── small helpers ────────────────────────────────────────────────────────────
def http_json(url, data=None, timeout=40):
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
    if data:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def parse_frontmatter(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    if not m:
        return {}, txt
    fm, body = {}, m.group(2)
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip()
    return fm, body


def reconstruct_abstract(inv):
    if not inv:
        return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs:
            pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))


def arxiv_id_from(url):
    m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url or "")
    return m.group(1) if m else ""


# ── 1. frontier matrix ───────────────────────────────────────────────────────
def load_frontier(model):
    fr = http_json(f"{API}/frontier", data=json.dumps({}).encode())
    fr = [n for n in fr if n.get("node_type") in (None, "concept", "technique",
          "result", "framework", "principle")][:N_FRONTIER]
    texts, meta = [], []
    for n in fr:
        node = http_json(f"{API}/node", data=json.dumps({"iri": n["iri"]}).encode())
        body = (node.get("content") or "")[:1200]
        texts.append(f"{n['canonical_title']}\n{body}")
        meta.append({
            "iri": n["iri"], "title": n["canonical_title"],
            "coverage": n.get("coverage", 0), "understanding": n.get("understanding", 0),
            "priority_score": n.get("priority_score", 0), "domain": n.get("domain", []),
            "inbound_refs": n.get("inbound_refs", 0),
        })
    vecs = model.encode(texts, normalize_embeddings=True)
    return np.asarray(vecs, dtype=np.float32), meta


# ── 2. seeds: existing sources most relevant to the frontier ─────────────────
def load_sources():
    out = []
    for p in glob.glob(f"{SOURCES_DIR}/*.md"):
        fm, body = parse_frontmatter(p)
        title = (fm.get("title") or "").strip().strip('"')
        if not title:
            continue
        out.append({
            "slug": os.path.basename(p)[:-3], "title": title,
            "doi": (fm.get("doi") or "").strip().strip('"'),
            "url": (fm.get("source_url") or "").strip(),
            "summary": body[:600],
        })
    return out


def pick_seeds(sources, F, model):
    texts = [f"{s['title']}\n{s['summary']}" for s in sources]
    V = np.asarray(model.encode(texts, normalize_embeddings=True), dtype=np.float32)
    sims = (V @ F.T).max(axis=1)              # each source's best frontier cosine
    order = np.argsort(-sims)
    seeds = []
    for i in order:
        s = sources[i]
        if s["doi"] or arxiv_id_from(s["url"]) or len(s["title"]) > 12:
            s = dict(s, frontier_sim=float(sims[i]))
            seeds.append(s)
        if len(seeds) >= N_SEEDS:
            break
    return seeds


# ── 3. OpenAlex resolve + forward cite expansion ─────────────────────────────
def oa_get(url):
    sep = "&" if "?" in url else "?"
    try:
        return http_json(f"{url}{sep}mailto={MAILTO}")
    except Exception:
        return None


def resolve_work(seed):
    if seed["doi"]:
        d = seed["doi"].replace("https://doi.org/", "")
        r = oa_get(f"{OPENALEX}/doi:{urllib.parse.quote(d)}")
        if r and r.get("id"):
            return r
    ax = arxiv_id_from(seed["url"])
    if ax:
        r = oa_get(f"{OPENALEX}?filter=" + urllib.parse.quote(f"doi:10.48550/arxiv.{ax}"))
        if r and r.get("results"):
            return r["results"][0]
    # title search fallback
    r = oa_get(f"{OPENALEX}?search={urllib.parse.quote(seed['title'])}&per-page=1")
    if r and r.get("results"):
        w = r["results"][0]
        if norm_title(w.get("title"))[:40] == norm_title(seed["title"])[:40]:
            return w
    return None


def cited_by(work_id):
    wid = work_id.split("/")[-1]
    flt = f"cites:{wid},from_publication_date:{FROM_YEAR}-01-01,cited_by_count:>{MIN_CITES}"
    r = oa_get(f"{OPENALEX}?filter={flt}&sort=cited_by_count:desc&per-page={CITED_PER_SEED}")
    return (r or {}).get("results", []) or []


# ── enrichment: links · clusters/hypotheses · LLM rationale ──────────────────
def load_clusters(model):
    """Research clusters + an embedding of each thesis, to map candidates onto the
    user's actual research agenda."""
    try:
        cl = http_json(f"{API}/clusters", data=json.dumps({}).encode())
    except Exception:
        return [], None
    if not cl:
        return [], None
    texts = [f"{c.get('title', '')}. {c.get('thesis', '')}" for c in cl]
    M = np.asarray(model.encode(texts, normalize_embeddings=True), dtype=np.float32)
    return cl, M


def search_links(c, k=6):
    """Top existing PKIS nodes this paper relates to (reuses the deployed hybrid search)."""
    q = f"{c['title']} {c.get('abstract', '')[:400]}"
    try:
        res = http_json(f"{API}/search",
                        data=json.dumps({"query": q, "max_results": k}).encode())
    except Exception:
        return []
    return [{"iri": r.get("iri"), "title": r.get("canonical_title"),
             "type": r.get("node_type"), "score": round(r.get("score", 0) or 0, 3)}
            for r in (res or []) if r.get("iri")]


def gen_rationale(client, c, gap, links, cluster):
    """LLM rationale grounded in the gap, the linked nodes, and the matched cluster."""
    link_titles = ", ".join(l["title"] for l in links[:6] if l.get("title")) or "(few existing)"
    if cluster:
        cl_txt = f"{cluster.get('title')}: {cluster.get('thesis', '')}"
        hyps = "; ".join(h.get("title", "") for h in (cluster.get("_fh") or [])[:3]) or "(none)"
    else:
        cl_txt, hyps = "(no strongly-matching research cluster)", "(n/a)"
    system = ("You advise a researcher curating a personal knowledge base (PKIS) in machine "
              "learning, statistics and probability. Given a candidate paper and how it maps onto "
              "their existing graph, explain crisply and SPECIFICALLY why (or whether) to read it. "
              "Ground every claim in the provided gap / nodes / cluster — no generic praise. "
              "Call the rationale tool.")
    user = (f"PAPER: {c['title']}\nABSTRACT: {c.get('abstract', '')[:1300]}\n\n"
            f"BEST-MATCH FRONTIER GAP: “{gap['title']}” — coverage {gap['coverage']}/5, "
            f"{gap.get('inbound_refs', 0)} other nodes depend on it.\n"
            f"EXISTING PKIS NODES IT RELATES TO: {link_titles}\n"
            f"RESEARCH CLUSTER: {cl_txt}\nCLUSTER HYPOTHESES: {hyps}\n\n"
            "Fill each field (1-2 sentences, concrete): why=why read it now; gap=the specific gap it "
            "closes; fits=how it connects to the named existing nodes; questions=1-2 questions it could "
            "answer for this base; agenda=how it bears on the research cluster/hypotheses above.")
    try:
        resp = client.messages.create(
            model=RATIONALE_MODEL, max_tokens=700, system=system,
            messages=[{"role": "user", "content": user}],
            tools=[RATIONALE_TOOL], tool_choice={"type": "tool", "name": "rationale"})
        for b in resp.content:
            if b.type == "tool_use":
                return dict(b.input)
    except Exception as e:
        print(f"  rationale fail: {e}", flush=True)
    return {}


def enrich(fresh, model, client):
    """Attach links, cluster/hypothesis fit, and an LLM rationale to each fresh pick."""
    clusters, cmat = load_clusters(model)
    for idx, c in enumerate(fresh, 1):
        c["links"] = search_links(c)
        cluster = None
        if clusters and cmat is not None:
            cv = np.asarray(model.encode([f"{c['title']}\n{c.get('abstract', '')[:600]}"],
                                         normalize_embeddings=True)[0], dtype=np.float32)
            sims = cmat @ cv
            j = int(np.argmax(sims))
            if float(sims[j]) > 0.30:
                cluster = clusters[j]
                fh = [h for h in cluster.get("hypotheses", []) if h.get("is_frontier")] \
                    or cluster.get("hypotheses", [])
                cluster["_fh"] = fh
                c["clusters"] = [{"slug": cluster.get("slug"), "title": cluster.get("title"),
                                  "thesis": cluster.get("thesis"),
                                  "relevance": round(float(sims[j]), 3)}]
                c["hypotheses"] = [{"title": h.get("title"), "status": h.get("status"),
                                    "cluster": cluster.get("slug")} for h in fh[:4]]
        c["rationale"] = gen_rationale(client, c, c["nearest_frontier"], c.get("links", []), cluster)
        print(f"  enriched {idx}/{len(fresh)}: {c['title'][:46]} "
              f"(links={len(c.get('links', []))}, cluster={'y' if cluster else 'n'})", flush=True)
        time.sleep(0.3)


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--tau", type=float, default=0.55)
    args = ap.parse_args()

    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMBED_MODEL, device="cpu")

    print("[1/4] frontier …", flush=True)
    F, fmeta = load_frontier(model)
    print(f"      {len(fmeta)} frontier concepts")

    print("[2/4] seeds …", flush=True)
    sources = load_sources()
    seeds = pick_seeds(sources, F, model)
    print(f"      {len(sources)} sources -> {len(seeds)} frontier-relevant seeds")
    known_dois = {s["doi"].lower() for s in sources if s["doi"]}
    known_titles = {norm_title(s["title"]) for s in sources}

    print("[3/4] OpenAlex cite-graph expansion …", flush=True)
    cands = {}  # openalex id -> candidate
    dropped_field = 0
    for k, seed in enumerate(seeds):
        w = resolve_work(seed)
        if not w:
            continue
        added_here = 0
        for c in cited_by(w["id"]):
            cid = c["id"]
            doi = (c.get("doi") or "").replace("https://doi.org/", "").lower()
            nt = norm_title(c.get("title"))
            if not nt or nt in known_titles or (doi and doi in known_dois):
                continue  # novelty gate (already ingested)
            if cid in cands:
                cands[cid]["via_seeds"].append(seed["title"])
                continue
            if added_here >= MAX_PER_SEED:
                continue  # don't let one seed flood the pool
            pt = c.get("primary_topic") or {}
            field = ((pt.get("field") or {}).get("display_name") or "")
            subfield = ((pt.get("subfield") or {}).get("display_name") or "")
            if field not in ALLOW_FIELDS or subfield in DENY_SUBFIELDS:
                dropped_field += 1
                continue  # DOMAIN GATE — drop applied bio/cyber/chem/imaging/etc.
            abstract = reconstruct_abstract(c.get("abstract_inverted_index"))
            if len(abstract) < 80:
                continue  # need real content to gate on
            added_here += 1
            cands[cid] = {
                "field": field, "subfield": subfield,
                "primary_topic": (pt.get("display_name") or ""),
                "openalex_id": cid, "title": c.get("title"), "doi": doi,
                "year": c.get("publication_year"), "cited_by": c.get("cited_by_count", 0),
                "venue": (((c.get("primary_location") or {}).get("source") or {})
                          .get("display_name") or ""),
                "authors": ", ".join(a["author"]["display_name"]
                                     for a in (c.get("authorships") or [])[:4]),
                "url": (c.get("primary_location") or {}).get("landing_page_url")
                       or c.get("id"),
                "abstract": abstract, "via_seeds": [seed["title"]],
            }
        time.sleep(0.15)
        if (k + 1) % 5 == 0:
            print(f"      {k + 1}/{len(seeds)} seeds, {len(cands)} raw candidates", flush=True)

    print(f"      domain gate dropped {dropped_field} off-field (bio/cyber/chem/etc.)", flush=True)
    print(f"[4/4] relevance-gating {len(cands)} candidates (tau={args.tau}) …", flush=True)
    items = list(cands.values())
    if not items:
        print("no candidates"); return
    V = np.asarray(model.encode([f"{c['title']}\n{c['abstract']}" for c in items],
                                normalize_embeddings=True), dtype=np.float32)
    S = V @ F.T  # candidate x frontier cosine
    # Learned prior: per-signal accept/dismiss multipliers from past decisions.
    prior = {}
    try:
        prior = json.load(open(PRIOR_PATH))
    except Exception:
        prior = {}

    def prior_mult(sig):
        ms = [prior[d][str(v)] for d, v in sig.items()
              if v and d in prior and str(v) in prior[d]]
        if not ms:
            return 1.0
        g = float(np.exp(np.mean(np.log(ms))))   # geometric mean — taste nudges, never dominates
        return max(0.2, min(3.0, g))

    scored = []
    for i, c in enumerate(items):
        j = int(np.argmax(S[i]))
        sim = float(S[i, j])
        if sim < args.tau:
            continue  # relevance gate
        fr = fmeta[j]
        # Fit DOMINATES (sim**2): this is a learning tool, not a popularity chart —
        # a bullseye 30-cite paper should beat a tangential 2000-cite survey.
        # Authority/recency are gentle tie-breakers; the learned prior reweights taste.
        recency = 1.0 + 0.08 * max(0, c["year"] - FROM_YEAR if c["year"] else 0)
        authority = 1.0 + 0.05 * np.log1p(c["cited_by"])
        signals = {"venue": c.get("venue", ""), "field": c.get("field", ""),
                   "subfield": c.get("subfield", ""), "primary_topic": c.get("primary_topic", ""),
                   "domain": (fr["domain"][0] if fr.get("domain") else "")}
        pm = prior_mult(signals)
        score = (sim ** 2) * authority * recency * (1.0 + 0.01 * fr["priority_score"]) * pm
        c.update({
            "id": c["openalex_id"],
            "sim": round(sim, 3),
            "nearest_frontier": {"iri": fr["iri"], "title": fr["title"],
                                 "coverage": fr["coverage"], "understanding": fr["understanding"],
                                 "inbound_refs": fr.get("inbound_refs", 0),
                                 "priority_score": fr.get("priority_score", 0)},
            "score": round(float(score), 4), "prior_mult": round(pm, 2), "signals": signals,
            "reason": (f"fills frontier gap “{fr['title']}” "
                       f"(coverage {fr['coverage']}/5, understanding {fr['understanding']}/5); "
                       f"sim {sim:.2f}; cites your “{c['via_seeds'][0]}”; "
                       f"{c['venue'] or 'preprint'} {c['year']}, cited {c['cited_by']}×"),
            "status": "pending",
            "discovered_at": dt.datetime.utcnow().isoformat() + "Z",
            "channel": "openalex-cite",
        })
        scored.append(c)
    scored.sort(key=lambda x: -x["score"])

    # MERGE into the existing inbox: keep DECIDED candidates (so dismissed/accepted
    # never resurface), replace stale pending with the fresh top-K.
    existing = {}
    try:
        for c in json.load(open(INBOX_PATH)).get("candidates", []):
            existing[c.get("id")] = c
    except Exception:
        pass
    decided = {i: c for i, c in existing.items() if c.get("status") in ("accepted", "dismissed")}
    decided_titles = {norm_title(c.get("title")) for c in decided.values()}
    fresh = [c for c in scored
             if c["id"] not in decided and norm_title(c["title"]) not in decided_titles][:args.limit]

    # PRIORITY: rank 1..N by score, with a human note explaining the gap's weight.
    for rank, c in enumerate(fresh, 1):
        nf = c["nearest_frontier"]
        c["priority"] = rank
        c["priority_note"] = (
            f"{nf.get('inbound_refs', 0)} nodes depend on “{nf['title']}”, "
            f"yet it's only {nf['coverage']}/5 covered — "
            + ("a high-leverage gap." if nf.get("inbound_refs", 0) >= 20
               else "a moderate gap."))

    # ENRICH the fresh picks: links, cluster/hypothesis fit, LLM rationale.
    if fresh:
        print(f"[5/5] enriching {len(fresh)} picks (links · clusters · rationale) …", flush=True)
        try:
            client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
            enrich(fresh, model, client)
        except Exception as e:
            print(f"  enrichment skipped: {e}", flush=True)

    candidates = list(decided.values()) + fresh

    json.dump({"generated_at": dt.datetime.utcnow().isoformat() + "Z",
               "channel": "openalex-cite", "tau": args.tau,
               "candidates": candidates}, open(INBOX_PATH, "w"), ensure_ascii=False, indent=1)

    print(f"\n==== {len(scored)} passed gate; {len(fresh)} new pending + "
          f"{len(decided)} kept-decided → {INBOX_PATH} ====\n")
    for r, c in enumerate(fresh, 1):
        print(f"{r:2d}. [{c['score']:.3f}] (x{c['prior_mult']}) {c['title']}")
        print(f"     {c['authors']} · {c['venue'] or 'preprint'} {c['year']} · {c['field']} · cited {c['cited_by']}×")
        print(f"     → {c['nearest_frontier']['title']} (cov {c['nearest_frontier']['coverage']}/5) "
              f"· sim {c['sim']} · via {c['via_seeds'][0][:50]}")
        print(f"     {c['url']}\n")


if __name__ == "__main__":
    main()
