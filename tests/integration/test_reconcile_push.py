"""
Layer 2 — tools/reconcile_push.py, the confirmed reconciliation step.

Contract: without --confirm it reports the divergence and recommendation and
changes NOTHING (the "drop back to discuss" state); with --confirm it pushes the
retained local commit. Exercised end-to-end via subprocess against a fixture repo
with a bare remote, in the common "local commit not yet pushed" state (the state
a GitPushError leaves behind once the cause clears).
"""

import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / "tools" / "reconcile_push.py"


def _remote_log(remote):
    return subprocess.run(["git", "-C", str(remote), "log", "--oneline"],
                          capture_output=True, text=True).stdout


@pytest.mark.integration
def test_dry_run_reports_but_does_not_push(isolated_wiki):
    repo, remote = isolated_wiki.repo, isolated_wiki.remote
    # Create a local commit that is NOT pushed (origin behind by 1).
    p = isolated_wiki.wiki / "concepts" / "entropy.md"
    p.write_text(p.read_text() + "\nlocal-only edit\n")
    subprocess.run(["git", "-C", str(repo), "commit", "-am", "local-only commit"],
                   check=True, capture_output=True)

    out = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(repo)],
                         capture_output=True, text=True)
    assert out.returncode == 0
    assert "RECOMMENDATION [push]" in out.stdout
    assert "dry-run" in out.stdout
    # Nothing pushed — the commit is still local-only.
    assert "local-only commit" not in _remote_log(remote)


@pytest.mark.integration
def test_confirm_pushes_the_retained_commit(isolated_wiki):
    repo, remote = isolated_wiki.repo, isolated_wiki.remote
    p = isolated_wiki.wiki / "concepts" / "entropy.md"
    p.write_text(p.read_text() + "\nlocal-only edit\n")
    subprocess.run(["git", "-C", str(repo), "commit", "-am", "retained commit to reconcile"],
                   check=True, capture_output=True)

    out = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(repo), "--confirm"],
                         capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    assert "Reconciled and pushed." in out.stdout
    assert "retained commit to reconcile" in _remote_log(remote)


@pytest.mark.integration
def test_in_sync_repo_is_a_noop(isolated_wiki):
    out = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(isolated_wiki.repo)],
                         capture_output=True, text=True)
    assert out.returncode == 0
    assert "RECOMMENDATION [noop]" in out.stdout
