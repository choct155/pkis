#!/usr/bin/env python3
"""Nightly standing-eval runner (C-1f).

Replays the accumulated owner query set (captured from deliberate searches/asks)
through the profile suite, one profile at a time, logging every run to the
experiment store under a shared `nightly:<date>` batch id. Pure data generation —
winner verdicts are intentionally HELD until the feedback tap has signal, so this
job asserts no "best" regime; it only records metrics + traces per (query,profile).

Run by cron nightly:
  0 3 * * * cd /home/pkis/pkis-wiki && set -a && . /home/pkis/.env && set +a \
            && /home/pkis/venv/bin/python tools/nightly_eval.py >> /home/pkis/nightly_eval.log 2>&1

Manual:
  WIKI_DIR=$PWD/wiki REPO_DIR=$PWD python tools/nightly_eval.py [--date 2026-06-24] [--limit N]
"""
import argparse
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app  # noqa: E402

# Four isolation profiles + the full-stack default as the baseline reference.
STANDING_PROFILES = ["default", "lexical_only", "dense_only", "rerank", "graph_rerank"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="batch date label (default: today, UTC)")
    ap.add_argument("--limit", type=int, default=1000, help="max queries to replay")
    ap.add_argument("--max-results", type=int, default=10)
    ap.add_argument("--profiles", help="comma-separated override of the profile suite")
    args = ap.parse_args()

    date = args.date or datetime.date.today().isoformat()
    batch_id = f"nightly:{date}"
    profiles = ([p.strip() for p in args.profiles.split(",") if p.strip()]
                if args.profiles else STANDING_PROFILES)

    queries = app.experiments.list_queries(app.EXPERIMENT_DB_PATH, limit=args.limit)
    print(f"[{batch_id}] {len(queries)} queries x {len(profiles)} profiles "
          f"= {len(queries) * len(profiles)} runs")
    if not queries:
        print("no captured queries yet — nothing to do.")
        return

    runs = 0
    for q in queries:
        for prof in profiles:
            try:
                app.run_search(q["query"], profile=prof, max_results=args.max_results,
                               comparison_id=batch_id, log=True)
                runs += 1
            except Exception as e:  # one bad (query,profile) must not abort the batch
                print(f"  ! {prof} / {q['query'][:40]!r}: {e}")
    print(f"[{batch_id}] logged {runs} runs -> {app.EXPERIMENT_DB_PATH}")


if __name__ == "__main__":
    main()
