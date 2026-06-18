#!/usr/bin/env python3
"""Phase-C MINING — Sonnet proposal generation per chapter (server-side, metered).

For each extracted chapter (reader payload `paper_md`), ask claude-sonnet-4-6 to
propose the reusable knowledge nodes / edges / enrichments it introduces, as a
strict JSON object the existing driver (mackay_phasec_driver.py) consumes. Reuses
the live node inventory for dedup + edge targets. Idempotent (skips chapters whose
proposal JSON already exists); continues past failures; backs off on 429 (the org's
input-tokens-per-minute ceiling is low, so this runs in slow waves — run detached).

Usage:
  set -a; . /home/pkis/.env; set +a
  nohup /home/pkis/venv/bin/python mine_proposals.py \
        bishop-prml goodfellow-deeplearning murphy-pml1-intro murphy-pml2-advanced \
        > /home/pkis/mine_proposals.log 2>&1 &
  # then: mackay_phasec_driver.py over the combined proposals/*.json
"""
import glob
import json
import os
import re
import sys
import time

import anthropic

# Comptroller accounting (best-effort). Bootstrap repo root so `usage` imports; no-op
# if unavailable so mining never breaks.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
try:
    from usage import log_usage
    from config import USAGE_DB_PATH
except Exception:  # pragma: no cover - defensive
    def log_usage(*_a, **_k):
        return False
    USAGE_DB_PATH = None

WIKI = "/home/pkis/pkis-wiki/wiki"
READER = f"{WIKI}/reader"
PROPOSALS = "/home/pkis/proposals"
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 12000
KNOWLEDGE_DIRS = ["concepts", "techniques", "results", "frameworks", "problems", "principles"]

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

SYSTEM = """You are an expert knowledge engineer building a personal research wiki \
(PKIS) of ML / statistics / probability / information-theory. You read one textbook \
chapter and extract the reusable, canonical KNOWLEDGE OBJECTS it introduces — not a \
summary, but durable nodes a researcher would cite across papers.

Six knowledge types: concept, technique, result, framework, problem, principle.

Call the submit_proposal tool with new_nodes, edges, and enrichments.

RULES
- new_nodes: 5-15 genuinely NEW, central objects from THIS chapter that are NOT already \
in the EXISTING-NODES list. Prefer reusable method/result/concept nodes over chapter-specific trivia.
- knowledge_type ∈ {concept, technique, result, framework, problem, principle}. slug is kebab-case.
- definition: start with the precise statement — a $$LaTeX$$ display formula or formal \
definition — then ONE intuition sentence, then a `### Why it matters` subsection, optionally one \
more `### Subsection`. ~120-300 words. Use `###` for subsections; do NOT begin with `##` or `## Definition`.
- edges: wire new nodes to each other AND to EXISTING nodes (use their exact slugs as targets). \
predicate ∈ {prerequisite-of, uses, specializes, generalizes, extends, applies, instantiates, \
contrasts-with, analogous-to}. subject/target are bare slugs.
- enrichments: for EXISTING nodes this chapter materially deepens, append a short passage \
(0-5 total). section is usually "Definition" or "Connections".
- Dedup hard: if a concept already exists in EXISTING-NODES, do NOT recreate it — link or enrich it."""


TOOL = {
    "name": "submit_proposal",
    "description": "Submit the knowledge nodes, edges and enrichments extracted from the chapter.",
    "input_schema": {
        "type": "object",
        "properties": {
            "new_nodes": {"type": "array", "items": {"type": "object", "properties": {
                "knowledge_type": {"type": "string"}, "title": {"type": "string"},
                "slug": {"type": "string"}, "definition": {"type": "string"},
                "domain": {"type": "array", "items": {"type": "string"}},
                "tags": {"type": "array", "items": {"type": "string"}},
            }, "required": ["knowledge_type", "title", "slug", "definition"]}},
            "edges": {"type": "array", "items": {"type": "object", "properties": {
                "subject": {"type": "string"}, "target": {"type": "string"},
                "predicate": {"type": "string"}, "note": {"type": "string"},
            }, "required": ["subject", "target", "predicate"]}},
            "enrichments": {"type": "array", "items": {"type": "object", "properties": {
                "slug": {"type": "string"}, "section": {"type": "string"},
                "addition": {"type": "string"},
            }, "required": ["slug", "section", "addition"]}},
        },
        "required": ["new_nodes", "edges", "enrichments"],
    },
}


def inventory():
    rows = []
    for d in KNOWLEDGE_DIRS:
        for p in sorted(glob.glob(f"{WIKI}/{d}/*.md")):
            rows.append(os.path.basename(p)[:-3])
    return rows


def paper_text(slug):
    pj = f"{READER}/{slug}/payload.json"
    if not os.path.isfile(pj):
        return None, None
    d = json.load(open(pj))
    body = "\n\n".join(f"## {s.get('title','')}\n{s.get('paper_md','')}"
                       for s in d.get("sections", []))
    return d.get("title", slug), body


def tool_input(resp):
    for b in resp.content:
        if b.type == "tool_use" and b.name == "submit_proposal":
            return b.input
    raise RuntimeError("model did not call submit_proposal")


def call(messages, system):
    delay = 15
    for attempt in range(7):
        try:
            resp = client.messages.create(
                model=MODEL, max_tokens=MAX_TOKENS, system=system, messages=messages,
                tools=[TOOL], tool_choice={"type": "tool", "name": "submit_proposal"})
            log_usage(USAGE_DB_PATH, resp, origin="pkis-mine-proposals", project="pkis",
                      attributes={"script": "mine_proposals"})
            return resp
        except anthropic.RateLimitError:
            print(f"    429 — backoff {delay}s", flush=True)
            time.sleep(delay); delay = min(delay * 2, 240)
        except anthropic.APIStatusError as e:
            if e.status_code in (429, 529):
                print(f"    {e.status_code} — backoff {delay}s", flush=True)
                time.sleep(delay); delay = min(delay * 2, 240)
            else:
                raise
    raise RuntimeError("exhausted retries")


def process(slug, inv_text):
    out = f"{PROPOSALS}/{slug}.json"
    if os.path.isfile(out):
        return "skip"
    title, body = paper_text(slug)
    if not body or len(body) < 400:
        return "empty"
    user = (f"EXISTING-NODES (do not recreate; valid edge targets):\n{inv_text}\n\n"
            f"CHAPTER: {title}  (source slug: {slug})\n\n{body}")
    resp = call([{"role": "user", "content": user}], SYSTEM)
    data = dict(tool_input(resp))
    data["chapter"] = slug
    json.dump(data, open(out, "w"), ensure_ascii=False, indent=1)
    nn = len(data.get("new_nodes", []))
    ne = len(data.get("edges", []))
    en = len(data.get("enrichments", []))
    u = resp.usage
    return f"ok nodes={nn} edges={ne} enrich={en} (in={u.input_tokens} out={u.output_tokens})"


def main(books):
    os.makedirs(PROPOSALS, exist_ok=True)
    inv = inventory()
    inv_text = ", ".join(inv)
    print(f"inventory: {len(inv)} existing nodes (~{len(inv_text)//4} tok)", flush=True)
    slugs = []
    for b in books:
        mp = f"{PROPOSALS}/{b}_map.json"
        if os.path.isfile(mp):
            slugs += list(json.load(open(mp)).keys())
        else:
            slugs += [os.path.basename(d) for d in glob.glob(f"{READER}/{b}-*")]
    slugs = sorted(set(slugs))
    print(f"chapters to mine: {len(slugs)}", flush=True)
    ok = skip = fail = 0
    for i, s in enumerate(slugs, 1):
        try:
            r = process(s, inv_text)
            print(f"[{i}/{len(slugs)}] {s}: {r}", flush=True)
            if r.startswith("ok"):
                ok += 1
            else:
                skip += 1
        except Exception as e:  # noqa: BLE001
            print(f"[{i}/{len(slugs)}] {s}: FAIL {e}", flush=True)
            fail += 1
        time.sleep(1.0)
    print(f"\n== mined ok={ok} skip={skip} fail={fail} of {len(slugs)} ==", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or ["bishop-prml", "goodfellow-deeplearning",
                          "murphy-pml1-intro", "murphy-pml2-advanced"])
