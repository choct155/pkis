#!/usr/bin/env python3
"""Repair node CREATES lost to a mid-run service restart — idempotent & SAFE.

The Phase-C driver's enrichment step APPENDS to sections, so re-running the whole
driver would duplicate the 442 enrichments. This script only (a) creates proposed
nodes that aren't live yet and (b) re-runs the idempotent edge batch (so edges to
the just-filled nodes land). It never touches enrichments. Reuses the driver's
helpers (call_tool / node_is_live / normalize_edge / TYPE_MAP).

Usage:
  set -a; . /home/pkis/.env; set +a
  /home/pkis/venv/bin/python fill_missing.py /home/pkis/proposals/newbooks_wave.json
"""
import json
import re
import sys
import time

import mackay_phasec_driver as drv


def main(path):
    chapters = json.load(open(path))
    if isinstance(chapters, dict):
        chapters = [chapters]

    # dedup nodes by slug (first wins) exactly as the driver does
    nodes = {}
    for ch in chapters:
        for n in ch.get("new_nodes", []):
            slug = (n.get("slug") or "").strip()
            title = (n.get("title") or n.get("canonical_title") or "").strip()
            if not slug and title:
                slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
            if not slug or not title:
                continue
            kt = drv.TYPE_MAP.get(n.get("knowledge_type") or n.get("node_type") or "concept", "concept")
            nodes.setdefault(slug, {
                "knowledge_type": kt, "title": title, "slug": slug,
                "definition": n.get("definition", ""), "domain": n.get("domain", []),
                "tags": n.get("tags", []), "sources": [ch.get("chapter", "")],
            })

    created = live = 0
    failed = []
    for slug, n in nodes.items():
        iri = f"pkis:{n['knowledge_type']}:{slug}"
        if drv.node_is_live(iri):
            live += 1
            continue
        try:
            stub = drv.call_tool("create_node_stub", {
                "knowledge_type": n["knowledge_type"], "title": n["title"], "slug": slug,
                "definition": n["definition"], "domain": n["domain"],
                "tags": n["tags"], "sources": n["sources"],
            })
            drv.call_tool("commit_staged_node", {"staged_id": stub["staged_id"]})
            created += 1
            print(f"CREATE (fill): {iri}")
        except Exception as ex:  # noqa: BLE001
            failed.append(slug)
            print(f"FAIL create {slug}: {ex}")
        time.sleep(0.2)

    # re-run the idempotent edge batch so edges to filled nodes land
    all_edges = []
    for ch in chapters:
        for e in ch.get("edges", []):
            ne = drv.normalize_edge(e)
            if ne:
                all_edges.append(ne)
    if all_edges:
        try:
            res = drv.call_tool("add_connections", {
                "edges": all_edges, "commit_message": "gap-fill: re-assert edges after restart"})
            print(f"EDGES: added={res.get('added')} skipped={res.get('skipped')} errors={res.get('errors')}")
        except Exception as ex:  # noqa: BLE001
            print(f"FAIL edges: {ex}")

    print(f"== fill: created={created} already_live={live} failed={len(failed)} ==")
    if failed:
        print("FAILED:", failed)


if __name__ == "__main__":
    main(sys.argv[1])
