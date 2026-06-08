#!/usr/bin/env python3
"""Phase-C write driver for MacKay ITILA node extraction.

Reads a proposals JSON file (an array of per-chapter objects, each with
new_nodes / enrichments / edges as produced by the proposal subagents) and
executes the writes SERIALLY against the localhost MCP endpoint — the same
validated create_node_stub -> commit_staged_node -> add_connections -> edit_node
path the connector uses. Serial execution respects the single git lock.

Normalizes plural knowledge_type values, dedups new nodes by slug (merging
sources), attaches the chapter source, creates+commits each node (skipping any
slug already live), then batch-adds all edges and applies enrichments. Idempotent
for edges (add_connections is idempotent); skips create for already-live slugs so
re-runs are safe.

Usage:
  set -a; . /home/pkis/.env; set +a
  /home/pkis/venv/bin/python mackay_phasec_driver.py /home/pkis/proposals/wave1.json
"""
import json
import os
import sys
import time
import urllib.request

MCP_URL = "http://127.0.0.1:5000/mcp"
WRITE_KEY = os.environ.get("PKIS_MCP_WRITE_KEY", "")

TYPE_MAP = {
    "concept": "concept", "concepts": "concept",
    "technique": "technique", "techniques": "technique",
    "result": "result", "results": "result",
    "framework": "framework", "frameworks": "framework",
    "problem": "problem", "problems": "problem",
    "principle": "principle", "principles": "principle",
}

_rpc_id = 0


def rpc(method, params, auth=False):
    global _rpc_id
    _rpc_id += 1
    body = {"jsonrpc": "2.0", "id": _rpc_id, "method": method, "params": params}
    data = json.dumps(body).encode()
    req = urllib.request.Request(MCP_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    if auth:
        req.add_header("Authorization", f"Bearer {WRITE_KEY}")
    with urllib.request.urlopen(req, timeout=120) as r:
        resp = json.loads(r.read())
    if "error" in resp and resp["error"]:
        raise RuntimeError(f"{method} error: {resp['error']}")
    return resp["result"]


def call_tool(name, args, auth=True):
    res = rpc("tools/call", {"name": name, "arguments": args}, auth=auth)
    # tools/call wraps the payload as content[0].text (JSON string)
    txt = res["content"][0]["text"]
    try:
        return json.loads(txt)
    except (json.JSONDecodeError, TypeError):
        return txt


def node_is_live(iri):
    try:
        res = call_tool("get_node", {"iri": iri}, auth=False)
        return isinstance(res, dict) and res.get("frontmatter")
    except Exception:
        return False


def get_section_body(content, section):
    """Return the existing body under '## <section>' (empty if absent)."""
    import re
    m = re.search(r"^##[ \t]+" + re.escape(section) + r"[ \t]*\n", content, re.M)
    if not m:
        return None
    rest = content[m.end():]
    nxt = re.search(r"\n##\s", rest)
    return (rest[:nxt.start()] if nxt else rest).strip()


def resolve_iri(slug):
    """Find the live IRI for a slug across knowledge types (for enrichment fetch)."""
    for kt in ("concept", "technique", "result", "framework", "problem", "principle"):
        iri = f"pkis:{kt}:{slug}"
        if node_is_live(iri):
            return iri
    return None


def main(path):
    chapters = json.load(open(path))
    if isinstance(chapters, dict):
        chapters = [chapters]

    # 1) Consolidate + normalize new_nodes (dedup by slug, merge sources).
    nodes_by_slug = {}
    all_edges = []
    all_enrich = []
    for ch in chapters:
        src = f"mackay-itila-{ch['chapter']}"  # e.g. mackay-itila-ch08
        for n in ch.get("new_nodes", []):
            slug = n["slug"]
            kt = TYPE_MAP.get(n["knowledge_type"], n["knowledge_type"])
            if slug in nodes_by_slug:
                if src not in nodes_by_slug[slug]["sources"]:
                    nodes_by_slug[slug]["sources"].append(src)
                continue
            nodes_by_slug[slug] = {
                "knowledge_type": kt, "title": n["title"], "slug": slug,
                "definition": n.get("definition", ""),
                "domain": n.get("domain", []), "tags": n.get("tags", []),
                "sources": [src],
            }
        for e in ch.get("edges", []):
            all_edges.append({k: e[k] for k in ("subject", "target", "predicate", "note") if k in e})
        for en in ch.get("enrichments", []):
            all_enrich.append(en)

    print(f"== {len(nodes_by_slug)} new nodes, {len(all_edges)} edges, {len(all_enrich)} enrichments ==\n")

    # 2) Create + commit each node (skip if already live).
    created, skipped, failed = [], [], []
    for slug, n in nodes_by_slug.items():
        iri = f"pkis:{n['knowledge_type']}:{slug}"
        if node_is_live(iri):
            print(f"SKIP (live): {iri}")
            skipped.append(slug)
            continue
        try:
            stub = call_tool("create_node_stub", {
                "knowledge_type": n["knowledge_type"], "title": n["title"],
                "slug": slug, "definition": n["definition"],
                "domain": n["domain"], "tags": n["tags"], "sources": n["sources"],
            })
            sid = stub["staged_id"]
            res = call_tool("commit_staged_node", {"staged_id": sid})
            print(f"CREATE: {res.get('iri', iri)}  {res.get('git_commit', '?')}")
            created.append(slug)
        except Exception as ex:
            print(f"FAIL create {slug}: {ex}")
            failed.append(slug)
        time.sleep(0.2)

    # 3) Batch-add edges (idempotent; bad targets reported, not fatal).
    if all_edges:
        try:
            res = call_tool("add_connections", {
                "edges": all_edges,
                "commit_message": "MacKay Phase C: wire chapter edges",
            })
            print(f"\nEDGES: added={res.get('added')} skipped={res.get('skipped')} errors={res.get('errors')}")
            for r in res.get("results", []):
                if r.get("status") != "added":
                    print(f"  edge {r.get('status')}: {r.get('subject')} -{r.get('predicate')}-> {r.get('target')}")
        except Exception as ex:
            print(f"FAIL edges: {ex}")

    # 4) Apply enrichments via edit_node section_updates. APPEND to an existing
    #    section (so we never clobber the original body); create it if absent.
    for en in all_enrich:
        slug = en.get("slug")
        section = en.get("section")
        addition = en.get("addition", "")
        if not (slug and section and addition):
            continue
        # Agents sometimes prefix the section name with '## '; strip it so we
        # don't produce a double-hash heading ("## ## Title").
        section = section.lstrip("#").strip()
        try:
            iri = resolve_iri(slug)
            if not iri:
                print(f"FAIL enrich {slug}: not live")
                continue
            node = call_tool("get_node", {"iri": iri}, auth=False)
            existing = get_section_body(node.get("content", ""), section)
            new_body = (existing + "\n\n" + addition) if existing else addition
            call_tool("edit_node", {
                "iri": iri,
                "section_updates": {section: new_body},
                "commit_message": f"MacKay Phase C enrichment: {slug} / {section}",
            })
            print(f"ENRICH: {slug} :: {section} ({'appended' if existing else 'new'})")
        except Exception as ex:
            print(f"FAIL enrich {slug}/{section}: {ex}")
        time.sleep(0.2)

    print(f"\n== created={len(created)} skipped={len(skipped)} failed={len(failed)} ==")
    if failed:
        print("FAILED:", failed)


if __name__ == "__main__":
    main(sys.argv[1])
