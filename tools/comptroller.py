#!/usr/bin/env python3
"""
Comptroller — usage/cost reporting CLI (Roster Phase 4).

Reads the SQLite usage store (see usage.py + COMPTROLLER.md) and produces cost
reports by origin / model / project for a time window. Pure Python, no LLM call —
this is the "one agent that does not require Claude". Schedulable via cron.

Subcommands:
  init                         create + seed the store (idempotent)
  report {daily|weekly|monthly|ytd}
                               write a report .md for the window; optionally append
                               a budget alert to wiki/inbox.md on threshold crossing

Run on the VPS as e.g.:
  python3 tools/comptroller.py init --db /home/pkis/usage/usage.sqlite
  python3 tools/comptroller.py report weekly --db /home/pkis/usage/usage.sqlite \
      --out /home/pkis/usage --inbox /home/pkis/pkis-wiki/wiki/inbox.md
"""

import argparse
import glob
import json
import os
import sys
from datetime import datetime, timedelta, timezone

# Import the shared usage module from the repo root regardless of CWD.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import usage  # noqa: E402


# --------------------------------------------------------------------------- #
# Window computation
# --------------------------------------------------------------------------- #

def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat()


def compute_window(kind: str, now: datetime, billing_start_day: int = 1):
    """Return (start_dt, end_dt, label) for the named window. `end` is exclusive.

    daily   -> the previous full UTC day
    weekly  -> the trailing 7 days up to now
    monthly -> the current billing period (from billing_start_day to now)
    ytd     -> Jan 1 of now's year to now
    """
    now = now.astimezone(timezone.utc)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if kind == "daily":
        start = midnight - timedelta(days=1)
        return start, midnight, "daily"
    if kind == "weekly":
        return now - timedelta(days=7), now, "weekly"
    if kind == "monthly":
        day = min(billing_start_day, now.day) if now.day >= billing_start_day else billing_start_day
        # Period start = billing_start_day of this month, or last month if we're before it.
        if now.day >= billing_start_day:
            start = midnight.replace(day=billing_start_day)
        else:
            prev = (midnight.replace(day=1) - timedelta(days=1))
            start = prev.replace(day=billing_start_day)
        return start, now, "monthly"
    if kind == "ytd":
        return midnight.replace(month=1, day=1), now, "ytd"
    raise ValueError(f"unknown window: {kind}")


# --------------------------------------------------------------------------- #
# Report rendering
# --------------------------------------------------------------------------- #

def _table(rows, headers):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def render_report(db_path, kind, now, *, report_date=None):
    """Build the report markdown + a summary dict (no file I/O)."""
    cfg = usage.get_config(db_path)
    billing_day = int(cfg.get("billing_cycle_start_day", "1") or "1")
    fixed_monthly = float(cfg.get("max_plan_monthly_usd", "0") or "0")

    start, end, label = compute_window(kind, now, billing_day)
    events = usage.events_between(db_path, _iso(start), _iso(end))
    variable = usage.total_cost(events)
    # Fixed cost only enters monthly rollups as a line item.
    fixed = fixed_monthly if kind == "monthly" else 0.0
    total = round(fixed + variable, 6)
    headroom = round(fixed_monthly - variable, 2)

    rdate = report_date or now.astimezone(timezone.utc).date().isoformat()
    lines = [
        f"# Comptroller Report — {rdate} [{label}]",
        "",
        "## Budget Summary",
        f"Period: {start.date().isoformat()} to {end.date().isoformat()}",
        f"Fixed cost (Max Plan): ${fixed:.2f}",
        f"Variable cost (API): ${variable:.2f}",
        f"Total: ${total:.2f}",
        f"Remaining headroom (vs monthly fixed): ${headroom:.2f}",
        "",
        "## Variable Cost Breakdown",
        "",
        "### By Origin",
    ]
    by_origin = usage.aggregate(events, "origin")
    lines.append(_table(
        [[k, v["calls"], v["input_tokens"], v["output_tokens"], f"${v['cost']:.4f}"]
         for k, v in by_origin.items()] or [["(none)", 0, 0, 0, "$0.0000"]],
        ["Origin", "Calls", "Input Tokens", "Output Tokens", "Cost"]))

    lines += ["", "### By Model"]
    by_model = usage.aggregate(events, "model")
    lines.append(_table(
        [[k, v["calls"], f"${v['cost']:.4f}"] for k, v in by_model.items()]
        or [["(none)", 0, "$0.0000"]],
        ["Model", "Calls", "Cost"]))

    lines += ["", "### By Project"]
    by_project = usage.aggregate(events, "project")
    lines.append(_table(
        [[k, f"${v['cost']:.4f}",
          f"{(v['cost'] / variable * 100 if variable else 0):.1f}%"]
         for k, v in by_project.items()] or [["(none)", "$0.0000", "0.0%"]],
        ["Project", "Cost", "% of Variable"]))

    summary = {
        "kind": label, "start": _iso(start), "end": _iso(end),
        "variable": variable, "fixed": fixed, "total": total,
        "headroom": headroom, "events": len(events), "report_date": rdate,
        "fixed_monthly": fixed_monthly,
    }
    return "\n".join(lines) + "\n", summary


# --------------------------------------------------------------------------- #
# Inbox budget alert
# --------------------------------------------------------------------------- #

def _alert_line(summary, threshold):
    return (f"- [ ] Weekly variable cost ${summary['variable']:.2f} — exceeds "
            f"threshold ${threshold:.2f} ({summary['report_date']}) [Comptroller]")


def maybe_alert(summary, threshold_frac=0.5, *, inbox_path=None, queue_path=None):
    """If weekly variable cost exceeds threshold_frac * monthly fixed budget, emit a
    budget-alert line. Returns the line (or None).

    Two delivery modes, both safe w.r.t. the deploy cron's `git pull`:
      * queue_path (DEFAULT, single-pusher): append to a file OUTSIDE the git repo
        (e.g. /home/pkis/usage/budget_alerts.md). The Auditor folds pending lines
        into wiki/inbox.md ## Budget on its next run, via its own commit+push — so
        the Comptroller never touches the repo and there is no second pusher.
      * inbox_path (manual use): append straight into wiki/inbox.md ## Budget. Only
        for an interactive run where a human owns the resulting commit.
    """
    if summary["kind"] != "weekly":
        return None
    budget = summary.get("fixed_monthly", 0.0)
    if budget <= 0:
        return None
    threshold = threshold_frac * budget
    if summary["variable"] <= threshold:
        return None
    line = _alert_line(summary, threshold)
    if queue_path:
        _append_queue(queue_path, line)
    if inbox_path:
        _append_under_heading(inbox_path, "## Budget", line)
    return line


def _append_queue(queue_path, line):
    """Append a line to the alert queue file (plain append; idempotent on exact line)."""
    existing = ""
    if os.path.exists(queue_path):
        with open(queue_path, encoding="utf-8") as fh:
            existing = fh.read()
    if line in existing:
        return
    os.makedirs(os.path.dirname(queue_path) or ".", exist_ok=True)
    header = "" if existing else "# Comptroller budget alerts (pending fold-in by Auditor → inbox ## Budget)\n\n"
    with open(queue_path, "a", encoding="utf-8") as fh:
        fh.write(header + line + "\n")


# Back-compat alias (older callers / tests).
def maybe_alert_inbox(inbox_path, summary, threshold_frac=0.5):
    return maybe_alert(summary, threshold_frac, inbox_path=inbox_path)


def _append_under_heading(path, heading, line):
    """Insert `line` at the end of the section started by `heading` (before the next
    `## ` heading or EOF). Idempotent: skips if the exact line already present."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if line in text:
        return
    lines = text.splitlines()
    try:
        h = next(i for i, ln in enumerate(lines) if ln.strip() == heading)
    except StopIteration:
        # Heading missing — append a new section at EOF.
        lines += ["", heading, line]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        return
    # Find the next top-level heading after h, else EOF.
    nxt = len(lines)
    for i in range(h + 1, len(lines)):
        if lines[i].startswith("## "):
            nxt = i
            break
    insert_at = nxt
    # Trim trailing blank lines within the section so the new line sits snug.
    while insert_at - 1 > h and not lines[insert_at - 1].strip():
        insert_at -= 1
    lines.insert(insert_at, line)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


# --------------------------------------------------------------------------- #
# Claude Code transcript ingest (secondary origin)
# --------------------------------------------------------------------------- #

def ingest_claude_code(db_path, projects_dir):
    """Ingest per-turn usage from Claude Code session transcripts
    (~/.claude/projects/<proj>/<session>.jsonl). Each assistant turn carries a
    `requestId` (one API call) used as the dedup key, so re-runs are idempotent.

    NOTE (cross-machine): transcripts live where Claude Code RUNS (a workstation),
    while the canonical store is on the VPS. Run this against whichever store you
    want Claude Code costs in; syncing the two stores is out of scope. Returns
    (ingested, skipped).
    """
    usage.init_store(db_path)
    seen = usage.existing_dedup_keys(db_path, "claude-code")
    ingested = skipped = 0
    for fp in glob.glob(os.path.join(projects_dir, "**", "*.jsonl"), recursive=True):
        try:
            fh = open(fp, encoding="utf-8")
        except OSError:
            continue
        with fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("type") != "assistant":
                    continue
                msg = d.get("message") or {}
                u = msg.get("usage") or {}
                if not u:
                    continue
                key = d.get("requestId") or d.get("uuid")
                if not key or key in seen:
                    skipped += 1
                    continue
                seen.add(key)
                cwd = d.get("cwd") or ""
                project = os.path.basename(cwd) or "claude-code"
                try:
                    usage.insert_event(
                        db_path,
                        emitted_at=d.get("timestamp") or "",
                        origin="claude-code", project=project,
                        model=msg.get("model", "") or "",
                        input_tokens=u.get("input_tokens", 0),
                        output_tokens=u.get("output_tokens", 0),
                        cache_read_tokens=u.get("cache_read_input_tokens", 0),
                        cache_write_tokens=u.get("cache_creation_input_tokens", 0),
                        attributes={"dedup_key": key,
                                    "session": d.get("sessionId"), "cwd": cwd},
                    )
                    ingested += 1
                except Exception:
                    skipped += 1
    return ingested, skipped


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

DEFAULT_DB = os.environ.get("PKIS_USAGE_DB", "/home/pkis/usage/usage.sqlite")


def main(argv=None):
    p = argparse.ArgumentParser(description="PKIS Comptroller — usage cost reporting")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("init", help="create + seed the usage store")
    pi.add_argument("--db", default=DEFAULT_DB)

    pg = sub.add_parser("ingest-claude-code",
                        help="import Claude Code session-transcript usage (dedup by requestId)")
    pg.add_argument("--db", default=DEFAULT_DB)
    pg.add_argument("--projects-dir",
                    default=os.path.expanduser("~/.claude/projects"))

    pr = sub.add_parser("report", help="render a cost report")
    pr.add_argument("window", choices=["daily", "weekly", "monthly", "ytd"])
    pr.add_argument("--db", default=DEFAULT_DB)
    pr.add_argument("--out", default=None, help="dir to write comptroller_report_*.md")
    pr.add_argument("--inbox", default=None,
                    help="wiki/inbox.md — append alert directly (manual use; human owns the commit)")
    pr.add_argument("--alert-queue", default=None,
                    help="file OUTSIDE the repo for budget alerts; Auditor folds into inbox (scheduled use)")
    pr.add_argument("--threshold-frac", type=float, default=0.5)
    pr.add_argument("--print", action="store_true", dest="to_stdout",
                    help="print the report to stdout (for on-demand invocation)")

    args = p.parse_args(argv)

    if args.cmd == "init":
        usage.seed_pricing(args.db)
        print(f"initialized usage store at {args.db}")
        return 0

    if args.cmd == "ingest-claude-code":
        ingested, skipped = ingest_claude_code(args.db, args.projects_dir)
        print(f"ingested {ingested} Claude Code turns ({skipped} skipped/dup) into {args.db}")
        return 0

    if args.cmd == "report":
        now = datetime.now(timezone.utc)
        report, summary = render_report(args.db, args.window, now)
        if args.out:
            os.makedirs(args.out, exist_ok=True)
            fname = os.path.join(
                args.out, f"comptroller_report_{summary['report_date']}.md")
            with open(fname, "w", encoding="utf-8") as fh:
                fh.write(report)
            print(f"wrote {fname}")
        if args.inbox or args.alert_queue:
            alerted = maybe_alert(summary, args.threshold_frac,
                                  inbox_path=args.inbox, queue_path=args.alert_queue)
            if alerted:
                print(f"budget alert emitted -> {args.alert_queue or args.inbox}")
        if args.to_stdout or not args.out:
            print(report)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
