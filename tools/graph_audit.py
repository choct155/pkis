#!/usr/bin/env python3
"""Graph-gaps audit — find orphaned concept-side nodes (zero graph edges) and SUGGEST
typed edges to wire each into the graph. Writes editable suggestions to graph_gaps.json,
surfaced in the owner inbox "Graph gaps" lane where each can be approved (applies the
edges via add_connections) or edited first. Concept-side only — standalone sources are
handled by link_sources_driver.py.

  python tools/graph_audit.py            # audit + write pending items
  python tools/graph_audit.py --dry      # print, no write
"""
import os, sys, json, hashlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
_envfile = os.environ.get("PKIS_ENV", "/home/pkis/.env")
if os.path.exists(_envfile):
    for _l in open(_envfile):
        _l = _l.strip()
        if _l and not _l.startswith("#") and "=" in _l:
            _k, _v = _l.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

import app  # noqa: E402

GAPS_PATH = os.environ.get("PKIS_GRAPH_GAPS_PATH", "/home/pkis/graph_gaps.json")
MODEL = "claude-haiku-4-5"
CONCEPTISH = ["concepts", "techniques", "results", "principles", "frameworks", "problems"]

PROMPT = """You are the PKIS Architect wiring an ORPHANED node (it has zero graph edges) \
into the knowledge graph. Propose typed edges FROM the orphan TO candidate nodes \
(direction: subject=orphan, predicate, target=candidate). Use ONLY these predicates:
{preds}
Be CONSERVATIVE: 1-3 edges, only where the relation is specific and real; omit weak \
matches. Prefer the most precise predicate.

ORPHAN
title: {title}
type: {ntype}
definition: {definition}

CANDIDATES (iri | title | excerpt)
{candidates}

Return ONLY a JSON array of edges like
[{{"target":"<candidate iri>","predicate":"<one of the listed predicates>"}}].
Empty array if none genuinely fit."""


def orphans():
    nodes = app.load_all_nodes()
    G = app.get_graph()
    deg = {n["iri"]: 0 for n in nodes}
    for u, v, _d in G.edges(data=True):
        for x in (u, v):
            if x in deg:
                deg[x] += 1
    return [n for n in nodes if deg.get(n["iri"], 0) == 0 and n["node_type"] in CONCEPTISH]


def suggest(n):
    fm = n.get("frontmatter", {})
    q = (fm.get("title", "") + ". " + (n.get("content") or "")).strip()[:1000]
    cands = [c for c in app.hybrid_search(q, node_types=CONCEPTISH, max_results=14)
             if c["iri"] != n["iri"]]
    if not cands:
        return []
    preds = "\n".join(f"  {p} — weight {w}" for p, w in app.EDGE_WEIGHTS.items())
    cand_lines = "\n".join(
        f"{c['iri']} | {c['canonical_title']} | {(c.get('excerpt') or '')[:120]}" for c in cands)
    prompt = PROMPT.format(preds=preds, title=fm.get("title", n["slug"]), ntype=n["node_type"],
                           definition=(n.get("content") or "").strip()[:800] or "(stub)",
                           candidates=cand_lines)
    resp = app.anthropic_client.messages.create(
        model=MODEL, max_tokens=300, messages=[{"role": "user", "content": prompt}])
    app.log_usage(app.USAGE_DB_PATH, resp, origin="pkis-architect-gaps", project="pkis",
                  attributes={"node": n["slug"]})
    txt = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text").strip()
    txt = txt[txt.find("["): txt.rfind("]") + 1] if "[" in txt else "[]"
    try:
        raw = json.loads(txt)
    except Exception:
        return []
    valid = {c["iri"] for c in cands}
    titles = {c["iri"]: c["canonical_title"] for c in cands}
    out = []
    for e in raw if isinstance(raw, list) else []:
        t, p = e.get("target", ""), e.get("predicate", "")
        if t in valid and p in app.EDGE_WEIGHTS:
            out.append({"target": t, "predicate": p, "target_title": titles.get(t, t)})
    return out


def main():
    dry = "--dry" in sys.argv
    prev = {}
    if os.path.exists(GAPS_PATH):
        try:
            prev = {x["id"]: x for x in json.load(open(GAPS_PATH)).get("items", [])}
        except Exception:
            prev = {}
    items = []
    for n in orphans():
        iid = "gap-" + hashlib.sha1(n["iri"].encode()).hexdigest()[:12]
        old = prev.get(iid)
        if old and old.get("status") in ("accepted", "dismissed"):
            items.append(old)            # respect prior decisions; don't resurface
            continue
        sugg = suggest(n)
        items.append({"id": iid, "iri": n["iri"], "slug": n["slug"],
                      "title": n.get("frontmatter", {}).get("title", n["slug"]),
                      "node_type": n["node_type"], "suggestions": sugg, "status": "pending"})
        print(f"  {n['slug']}: {len(sugg)} suggested edge(s)")
    out = {"items": items}
    npend = sum(1 for x in items if x.get("status") == "pending")
    if dry:
        print(json.dumps(out, indent=2)[:3000]); print(f"[{npend} pending]"); return
    json.dump(out, open(GAPS_PATH, "w"), indent=2)
    print(f"wrote {GAPS_PATH}: {npend} pending gap items")


if __name__ == "__main__":
    main()
