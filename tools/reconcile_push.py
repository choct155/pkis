#!/usr/bin/env python3
"""
PKIS — push reconciliation (Layer 2 of the loud-push policy).

When a wiki write raises GitPushError, the local commit is RETAINED but origin
was not updated. This tool inspects the divergence and recommends a remediation.
Without --confirm it only reports and exits (the "drop back to discuss" state);
with --confirm it executes the recommended reconcile (pull --rebase) and re-push.
It never reconciles automatically inside a request — that's the whole point.

Usage:
  reconcile_push.py                   # inspect REPO_DIR, recommend, change nothing
  reconcile_push.py --repo /path/repo # inspect a specific repo (e.g. DOCS_REPO_DIR)
  reconcile_push.py --confirm         # execute the recommended reconcile + push

Exit codes: 0 ok / in-sync, 1 reconcile failed (manual fix needed),
            2 remote unreachable.
"""
import argparse
import os
import subprocess
import sys

DEFAULT_REPO = os.environ.get("REPO_DIR", "/home/pkis/pkis-wiki")


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)


def current_branch(repo):
    return git(repo, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip() or "main"


def diagnose(repo, branch):
    remote = f"origin/{branch}"
    fetch = git(repo, "fetch", "origin", branch)
    behind = ahead = None
    counts = git(repo, "rev-list", "--left-right", "--count", f"{remote}...HEAD")
    if counts.returncode == 0 and len(counts.stdout.split()) == 2:
        behind, ahead = (int(x) for x in counts.stdout.split())
    return {
        "fetch_ok": fetch.returncode == 0,
        "fetch_err": fetch.stderr.strip(),
        "behind": behind,
        "ahead": ahead,
        "local": git(repo, "log", "--oneline", f"{remote}..HEAD").stdout.strip(),
        "remote_only": git(repo, "log", "--oneline", f"HEAD..{remote}").stdout.strip(),
        "diffstat": git(repo, "diff", "--stat", f"{remote}...HEAD").stdout.strip(),
    }


def recommend(d):
    """Return (action, human_reason). action ∈ {noop, push, rebase, pull, retry}."""
    if not d["fetch_ok"]:
        return "retry", "Remote unreachable (fetch failed). Retry when connectivity returns."
    if d["behind"] and d["ahead"]:
        return "rebase", (f"History diverged (local +{d['ahead']}, origin +{d['behind']}). "
                          f"Rebase local onto origin, then push.")
    if d["ahead"] and not d["behind"]:
        return "push", f"{d['ahead']} local commit(s) not on origin; origin not ahead. Just push."
    if d["behind"] and not d["ahead"]:
        return "pull", f"Origin is ahead by {d['behind']}; fast-forward pull (nothing local to push)."
    return "noop", "In sync with origin — nothing to reconcile."


def main(argv=None):
    ap = argparse.ArgumentParser(description="Inspect/reconcile a failed PKIS push.")
    ap.add_argument("--repo", default=DEFAULT_REPO, help="repo to reconcile (default: $REPO_DIR)")
    ap.add_argument("--confirm", action="store_true", help="execute the recommended reconcile + push")
    a = ap.parse_args(argv)
    repo, branch = a.repo, None
    branch = current_branch(repo)
    d = diagnose(repo, branch)
    action, why = recommend(d)

    print(f"repo:   {repo}")
    print(f"branch: {branch}")
    print(f"ahead (local-only): {d['ahead']}   behind (origin-only): {d['behind']}   fetch_ok: {d['fetch_ok']}")
    if d["fetch_err"]:
        print(f"fetch error: {d['fetch_err']}")
    if d["local"]:
        print(f"\nlocal unpushed commits:\n{d['local']}")
    if d["remote_only"]:
        print(f"\norigin-only commits:\n{d['remote_only']}")
    if d["diffstat"]:
        print(f"\ndivergence diffstat:\n{d['diffstat']}")
    print(f"\nRECOMMENDATION [{action}]: {why}")

    if not a.confirm:
        if action != "noop":
            print("\n(dry-run — re-run with --confirm to execute. Nothing changed.)")
        return 0 if action in ("noop",) else 0

    if action == "noop":
        return 0
    if action == "retry":
        print("\nCannot reconcile while the remote is unreachable. Aborting.")
        return 2

    print(f"\nExecuting [{action}] ...")
    if action in ("rebase", "pull"):
        r = git(repo, "pull", "--rebase", "origin", branch)
        sys.stdout.write(r.stdout)
        sys.stderr.write(r.stderr)
        if r.returncode != 0:
            print("\nReconcile failed (likely conflicts). Resolve manually, then push. Aborting.")
            return 1
    p = git(repo, "push", "origin", branch)
    sys.stdout.write(p.stdout)
    sys.stderr.write(p.stderr)
    if p.returncode != 0:
        print("\nPush still failing after reconcile. Manual intervention needed.")
        return 1
    print("\nReconciled and pushed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
