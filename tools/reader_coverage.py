#!/usr/bin/env python3
"""reader_coverage.py — narration-build coverage across the PKIS source corpus.

Answers "which content has a narration build and which doesn't" at a glance. Reads
the same paths the app uses (config.WIKI_DIR / DOCS_DIR, READER_DIR = env or
WIKI_DIR/reader), so run it with the server's environment to see the live picture.

  python tools/reader_coverage.py                # summary table
  python tools/reader_coverage.py --outstanding  # + list narratable papers not built
  python tools/reader_coverage.py --json         # machine-readable (same data as the
                                                 # /pkis-api/reader/coverage endpoint)
"""
import os
import re
import json
import sys
from pathlib import Path

import frontmatter
import config

WIKI = Path(config.WIKI_DIR)
DOCS = Path(config.DOCS_DIR) / "sources"
READER = Path(os.environ.get("READER_DIR", str(WIKI / "reader")))
ARXIV = re.compile(r"arxiv\.org/(?:abs|pdf)/[0-9]+\.[0-9]+")
CHAPTER = re.compile(r"-ch\d+$|-(epilogue|intro|appendix)$")


def _reader_state(slug: str) -> str:
    d = READER / slug
    if (d / "payload.json").exists():
        return "ready"
    sp = d / "status.json"
    if sp.exists():
        try:
            return json.loads(sp.read_text()).get("state", "unknown")
        except Exception:
            return "unknown"
    return "none"


def survey() -> dict:
    """One row per source node with its narratability + build state."""
    rows = []
    for f in sorted((WIKI / "sources").glob("*.md")):
        slug = f.stem
        try:
            fm = frontmatter.load(str(f)).metadata
        except Exception:
            fm = {}
        url = str(fm.get("source_url") or fm.get("url") or "")
        has_pdf = (DOCS / slug).is_dir() and any((DOCS / slug).glob("*.pdf"))
        rows.append({
            "slug": slug,
            "title": str(fm.get("title") or slug),
            "narratable": bool(ARXIV.search(url)) or has_pdf,
            "on_demand": bool(CHAPTER.search(slug)),   # book chapters build on demand
            "state": _reader_state(slug),
        })
    ready = sum(r["state"] == "ready" for r in rows)
    # Outstanding = narratable, not a book chapter, and not already ready.
    outstanding = [r for r in rows if r["narratable"] and not r["on_demand"] and r["state"] != "ready"]
    by_state = {}
    for r in rows:
        by_state[r["state"]] = by_state.get(r["state"], 0) + 1
    return {
        "total_sources": len(rows),
        "ready": ready,
        "by_state": by_state,
        "narratable": sum(r["narratable"] for r in rows),
        "outstanding_count": len(outstanding),
        "outstanding": [
            {"slug": r["slug"], "state": r["state"], "title": r["title"][:70]}
            for r in sorted(outstanding, key=lambda r: (r["state"], r["slug"]))
        ],
    }


def main():
    data = survey()
    if "--json" in sys.argv:
        print(json.dumps(data, indent=2))
        return
    pct = round(100 * data["ready"] / max(data["total_sources"], 1))
    print(f"Narration coverage: {data['ready']}/{data['total_sources']} sources ready ({pct}%)")
    print("  by state: " + ", ".join(f"{k}={v}" for k, v in sorted(data["by_state"].items())))
    print(f"  narratable papers still unbuilt: {data['outstanding_count']}")
    if "--outstanding" in sys.argv and data["outstanding"]:
        print("\nOutstanding (narratable, not yet built):")
        for r in data["outstanding"]:
            print(f"  [{r['state']:8s}] {r['slug']:44s} {r['title']}")


if __name__ == "__main__":
    main()
