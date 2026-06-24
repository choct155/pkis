#!/usr/bin/env python3
"""Offline retrieval-lab harness.

Run a query set through N search profiles, print a metrics + latency table, and
log every run to the experiment store — the same code path as the live lab
(`app.run_search`), so offline and in-app numbers are comparable.

Usage:
  WIKI_DIR=$PWD/wiki REPO_DIR=$PWD python tools/search_harness.py queries.json \
      --profiles default,lexical_only,dense_only,rerank
  python tools/search_harness.py --query "monte carlo" --profiles default,rerank

queries.json: a JSON list of query strings, or {"queries": [...]}.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app  # noqa: E402  (heavy import: brings up STORE + the real search path)


def _load_queries(path):
    data = json.load(open(path))
    return data["queries"] if isinstance(data, dict) else data


def _fmt(x):
    return f"{x:9.3f}" if isinstance(x, (int, float)) else f"{str(x):>9}"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("queries", nargs="?", help="JSON file: list of query strings")
    ap.add_argument("--query", action="append", help="inline query (repeatable)")
    ap.add_argument("--profiles", default="default",
                    help="comma-separated profile names (default: 'default')")
    ap.add_argument("--max-results", type=int, default=10)
    ap.add_argument("--no-log", action="store_true", help="don't write experiment rows")
    args = ap.parse_args()

    queries = list(args.query or [])
    if args.queries:
        queries += _load_queries(args.queries)
    if not queries:
        ap.error("provide a queries file or at least one --query")
    profiles = [p.strip() for p in args.profiles.split(",") if p.strip()]

    cid = app.uuid.uuid4().hex[:12]
    cols = ["coherence", "redundancy", "n_comp", "retr_ms", "eval_ms", "n"]
    print(f"{'query':32} {'profile':14} " + " ".join(f"{c:>9}" for c in cols))
    print("-" * (32 + 1 + 14 + 1 + 10 * len(cols)))
    for q in queries:
        for p in profiles:
            col = app.run_search(q, profile=p, max_results=args.max_results,
                                 comparison_id=cid, log=not args.no_log)
            m = col["metrics"]
            row = [m.get("coherence"), m.get("redundancy"), m.get("n_components"),
                   col["retrieval_ms"], col["eval_ms"], len(col["results"])]
            print(f"{q[:32]:32} {col['profile_name'][:14]:14} " + " ".join(_fmt(x) for x in row))

    if not args.no_log:
        print(f"\ncomparison_id: {cid}  →  {app.EXPERIMENT_DB_PATH}")


if __name__ == "__main__":
    main()
