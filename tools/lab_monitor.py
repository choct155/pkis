#!/usr/bin/env python3
"""lab_monitor.py — PKIS Lab Assistant: scheduled DESCRIPTIVE monitoring.

Computes a dated, descriptive snapshot of PKIS's own research data (node counts,
coverage, hypothesis-status distribution, cluster health, staged-node throughput),
appends it to an append-only JSONL store kept OUT of the wiki, and flags drift
(idle clusters, stuck staged nodes, status swings) into the wiki/inbox.md Lab lane
for the human to drain.

Posture (non-negotiable, per Lab_Assistant_Canonical_Spec): descriptive/analytical
only. It never decides a hypothesis is confirmed/refuted, never writes live wiki
content, never asserts causality, and has zero awareness of any external system.

Decoupled by design: imports only `config` (no Anthropic client, no graph build),
so it is cheap to schedule and fully testable against any wiki directory.

    python tools/lab_monitor.py            # compute, write JSONL, flag drift to inbox
    python tools/lab_monitor.py --dry-run  # compute + print only, no writes
"""
import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone, date
from pathlib import Path

import frontmatter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import config  # noqa: E402  (lightweight: path/edge constants only)

SCHEMA_VERSION = "v0.1"
STALE_CLUSTER_DAYS = int(os.environ.get("LAB_STALE_CLUSTER_DAYS", "28"))
STALE_STAGED_HOURS = int(os.environ.get("LAB_STALE_STAGED_HOURS", "168"))  # 7 days


# ── helpers ───────────────────────────────────────────────────────────────────
def _iter_nodes(folder: Path):
    """Yield (path, metadata) for every *.md node in a folder (skips dotfiles)."""
    if not folder.exists():
        return
    for p in sorted(folder.glob("*.md")):
        if p.name.startswith("."):
            continue
        try:
            yield p, frontmatter.load(str(p)).metadata
        except Exception:
            continue


def _days_since(datestr, ref: date) -> int | None:
    try:
        return (ref - date.fromisoformat(str(datestr)[:10])).days
    except Exception:
        return None


def _git_head(repo_dir) -> str:
    try:
        return subprocess.run(["git", "-C", str(repo_dir), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return ""


# ── snapshot computation (pure: reads disk, returns a dict) ─────────────────────
def compute_snapshot(wiki_dir: Path, repo_dir=None, now: datetime = None) -> dict:
    wiki_dir = Path(wiki_dir)
    now = now or datetime.now(timezone.utc)
    today = now.date()

    node_counts = {}
    coverage_vals, understanding_vals = [], []
    for folder in config.KNOWLEDGE_DIRS:
        d = wiki_dir / folder
        ntype = config.FOLDER_TO_TYPE.get(folder, folder)
        cnt = 0
        for _p, fm in _iter_nodes(d):
            cnt += 1
            if isinstance(fm.get("coverage"), (int, float)):
                coverage_vals.append(fm["coverage"])
            if isinstance(fm.get("understanding"), (int, float)):
                understanding_vals.append(fm["understanding"])
        node_counts[ntype] = cnt

    # hypothesis status distribution (by status / cluster / role) — robust to any
    # status vocabulary (buckets by whatever string is present).
    hyp_status, hyp_role = Counter(), Counter()
    hyp_by_cluster = Counter()
    for _p, fm in _iter_nodes(wiki_dir / "hypotheses"):
        hyp_status[str(fm.get("status", "unspecified"))] += 1
        hyp_role[str(fm.get("research_program_role", "unspecified"))] += 1
        for c in (fm.get("cluster_membership") or []) or [fm.get("research_program_cluster")]:
            if c:
                hyp_by_cluster[str(c)] += 1

    # cluster health: frontier count + staleness
    clusters = {}
    for _p, fm in _iter_nodes(wiki_dir / "clusters"):
        slug = _p.stem
        clusters[slug] = {
            "frontier_count": len(fm.get("frontier_hypotheses") or []),
            "staleness_days": _days_since(fm.get("date_updated"), today),
            "status": str(fm.get("status", "unspecified")),
        }

    # staged-node throughput
    staging = wiki_dir / "staging"
    staged = [p for p in staging.glob("*.md")] if staging.exists() else []
    oldest_staged_hours = None
    for p in staged:
        try:
            sa = frontmatter.load(str(p)).metadata.get("staged_at", "")
            dt = datetime.fromisoformat(str(sa).replace("Z", "+00:00"))
            age = (now - dt).total_seconds() / 3600.0
            oldest_staged_hours = age if oldest_staged_hours is None else max(oldest_staged_hours, age)
        except Exception:
            continue

    def _avg(xs):
        return round(sum(xs) / len(xs), 3) if xs else None

    return {
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "schema_version": SCHEMA_VERSION,
        "git_head": _git_head(repo_dir or wiki_dir),
        "node_counts": node_counts,
        "total_nodes": sum(node_counts.values()),
        "avg_coverage": _avg(coverage_vals),
        "avg_understanding": _avg(understanding_vals),
        "hypothesis_status": dict(hyp_status),
        "hypothesis_role": dict(hyp_role),
        "hypotheses_by_cluster": dict(hyp_by_cluster),
        "clusters": clusters,
        "staged_count": len(staged),
        "oldest_staged_hours": round(oldest_staged_hours, 1) if oldest_staged_hours is not None else None,
        "finding_count": node_counts.get("finding", 0),
    }


# ── drift flags (absolute + delta-vs-previous) ──────────────────────────────────
def detect_drift(prev: dict | None, curr: dict) -> list[str]:
    flags = []
    for slug, c in (curr.get("clusters") or {}).items():
        sd = c.get("staleness_days")
        if sd is not None and sd >= STALE_CLUSTER_DAYS:
            flags.append(f"Cluster `{slug}` idle {sd}d (>= {STALE_CLUSTER_DAYS}d).")
    osh = curr.get("oldest_staged_hours")
    if osh is not None and osh >= STALE_STAGED_HOURS:
        flags.append(f"A staged node has waited {osh/24:.1f}d for review (>= {STALE_STAGED_HOURS/24:.0f}d).")
    if prev:
        for status in set(prev.get("hypothesis_status", {})) | set(curr.get("hypothesis_status", {})):
            d = curr.get("hypothesis_status", {}).get(status, 0) - prev.get("hypothesis_status", {}).get(status, 0)
            if d:
                flags.append(f"Hypothesis status `{status}` changed by {d:+d} since last snapshot.")
    return flags


# ── persistence + inbox ─────────────────────────────────────────────────────────
def _snapshot_file(lab_dir: Path, now: datetime) -> Path:
    return Path(lab_dir) / f"lab_monitoring_{now.strftime('%Y-%m-%d')}.jsonl"


def load_previous(lab_dir: Path) -> dict | None:
    lab_dir = Path(lab_dir)
    files = sorted(lab_dir.glob("lab_monitoring_*.jsonl")) if lab_dir.exists() else []
    for f in reversed(files):
        lines = [ln for ln in f.read_text().splitlines() if ln.strip()]
        if lines:
            try:
                return json.loads(lines[-1])
            except Exception:
                continue
    return None


def write_snapshot(record: dict, lab_dir: Path, now: datetime) -> Path:
    lab_dir = Path(lab_dir)
    lab_dir.mkdir(parents=True, exist_ok=True)
    f = _snapshot_file(lab_dir, now)
    with open(f, "a") as fh:
        fh.write(json.dumps(record) + "\n")
    return f


def append_inbox_flags(flags: list[str], wiki_dir: Path, now: datetime) -> None:
    if not flags:
        return
    inbox = Path(wiki_dir) / "inbox.md"
    text = inbox.read_text() if inbox.exists() else "# Inbox\n"
    if "## Lab" not in text:
        text = text.rstrip() + "\n\n## Lab\n"
    stamp = now.strftime("%Y-%m-%d")
    block = "".join(f"- [{stamp}] {f}\n" for f in flags)
    text = text.replace("## Lab\n", f"## Lab\n{block}", 1)
    inbox.write_text(text)


def main():
    ap = argparse.ArgumentParser(description="PKIS Lab Assistant descriptive monitor")
    ap.add_argument("--dry-run", action="store_true", help="compute + print only; no writes")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    wiki_dir = config.WIKI_DIR
    lab_dir = Path(os.environ.get("PKIS_LAB_DIR", "/home/pkis/lab"))

    snapshot = compute_snapshot(wiki_dir, config.REPO_DIR, now=now)
    prev = load_previous(lab_dir)
    flags = detect_drift(prev, snapshot)

    print(json.dumps(snapshot, indent=2))
    if flags:
        print("\nDrift flags:")
        for f in flags:
            print(f"  - {f}")

    if not args.dry_run:
        out = write_snapshot(snapshot, lab_dir, now)
        append_inbox_flags(flags, wiki_dir, now)
        print(f"\nWrote snapshot -> {out}; {len(flags)} flag(s) to inbox.")


if __name__ == "__main__":
    main()
