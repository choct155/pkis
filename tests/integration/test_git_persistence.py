"""
Seam C — tool_* ↔ git persistence (ARCHITECTURE_AUDIT.md §7 Seam C).

Consolidated contract (decided during Phase 2): all write tools push through a
single helper, _git_commit_and_push. A push failure is LOUD — it raises
GitPushError carrying divergence diagnostics + a recommendation — and the local
commit is RETAINED so no work is lost. Reconciliation is a separate, confirmed
step (tools/reconcile_push.py), never silent.

These tests pin that contract on a real fixture git repo with a bare remote.
"""

import re
import subprocess

import frontmatter
import pytest


def _break_remote(repo):
    """Point origin at a non-existent remote so push (and fetch) fail."""
    subprocess.run(
        ["git", "-C", str(repo), "remote", "set-url", "origin",
         str(repo.parent / "does-not-exist.git")],
        check=True, capture_output=True,
    )


# --------------------------------------------------------------------------- #
# The centralized helper directly.
# --------------------------------------------------------------------------- #

@pytest.mark.integration
def test_commit_and_push_success(appmod, isolated_wiki):
    p = isolated_wiki.wiki / "concepts" / "entropy.md"
    p.write_text(p.read_text() + "\nAppended line.\n")
    res = appmod._git_commit_and_push([p], "test: helper happy path")
    assert res["committed"] is True
    assert res["pushed"] is True
    assert res["sha"]
    remote_log = subprocess.run(
        ["git", "-C", str(isolated_wiki.remote), "log", "--oneline"],
        capture_output=True, text=True).stdout
    assert "test: helper happy path" in remote_log


@pytest.mark.integration
def test_commit_and_push_nothing_to_commit_is_noop(appmod, isolated_wiki):
    """An idempotent write (no file change) must not error or push a phantom
    commit — it returns committed=False, pushed=True (nothing to send)."""
    p = isolated_wiki.wiki / "concepts" / "entropy.md"  # unchanged
    res = appmod._git_commit_and_push([p], "test: should be a no-op")
    assert res["committed"] is False
    assert res["pushed"] is True


@pytest.mark.integration
def test_commit_and_push_raises_loudly_with_diagnostics_on_push_failure(appmod, isolated_wiki):
    p = isolated_wiki.wiki / "concepts" / "entropy.md"
    p.write_text(p.read_text() + "\nEdit while remote unreachable.\n")
    _break_remote(isolated_wiki.repo)

    with pytest.raises(appmod.GitPushError) as ei:
        appmod._git_commit_and_push([p], "test: push must fail loudly")

    diag = ei.value.diagnostics
    assert diag["sha"], "diagnostics must name the retained commit"
    assert diag["recommendation"], "diagnostics must include a remediation recommendation"
    assert "branch" in diag

    # Commit is RETAINED locally (no work lost).
    head = subprocess.run(
        ["git", "-C", str(isolated_wiki.repo), "log", "-1", "--format=%s"],
        capture_output=True, text=True).stdout.strip()
    assert head == "test: push must fail loudly"


# --------------------------------------------------------------------------- #
# Through the write tools (proves the consolidation reaches each call site).
# --------------------------------------------------------------------------- #

@pytest.mark.integration
def test_edit_node_round_trips_to_disk_and_pushes(appmod, isolated_wiki):
    res = appmod.tool_edit_node(
        slug="bayesian-inference",
        section_updates={"Definition": "Updated definition body for the round-trip test."},
        frontmatter_updates={"understanding": 5},
        commit_message="test: round-trip edit",
    )
    assert res["status"] == "edited"
    assert res["git_commit"] and res["git_pushed"] is True

    path = isolated_wiki.wiki / "concepts" / "bayesian-inference.md"
    post = frontmatter.load(str(path))
    assert "Updated definition body for the round-trip test." in post.content
    assert post.metadata["understanding"] == 5
    assert post.metadata["date_updated"]


@pytest.mark.integration
def test_edit_node_raises_loudly_on_push_failure_and_retains_commit(appmod, isolated_wiki):
    """The headline behavior: a failed push surfaces as a raised GitPushError,
    NOT a {status: edited, git_pushed: False} success payload. No sneaky
    divergence — the caller knows immediately."""
    _break_remote(isolated_wiki.repo)
    with pytest.raises(appmod.GitPushError):
        appmod.tool_edit_node(
            slug="entropy",
            section_updates={"Definition": "Edit made while the remote is unreachable."},
            commit_message="test: edit push should fail loudly",
        )
    # The edit is still on disk and committed locally.
    head = subprocess.run(
        ["git", "-C", str(isolated_wiki.repo), "log", "-1", "--format=%s"],
        capture_output=True, text=True).stdout.strip()
    assert head == "test: edit push should fail loudly"
    assert "remote is unreachable" in (isolated_wiki.wiki / "concepts" / "entropy.md").read_text()


@pytest.mark.integration
def _advance_remote(isolated_wiki, tmp_path, *, rel_path, content):
    """Clone the bare remote, commit a change at rel_path, push it — so the main
    repo's origin/main is now AHEAD by one commit (the B11 race precondition)."""
    clone = tmp_path / "remote-mover"
    subprocess.run(["git", "clone", "-q", str(isolated_wiki.remote), str(clone)],
                   check=True, capture_output=True)
    subprocess.run(["git", "-C", str(clone), "config", "user.email", "m@x.local"], check=True)
    subprocess.run(["git", "-C", str(clone), "config", "user.name", "Mover"], check=True)
    f = clone / rel_path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content)
    subprocess.run(["git", "-C", str(clone), "add", "-A"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(clone), "commit", "-q", "-m", "remote: advance"],
                   check=True, capture_output=True)
    subprocess.run(["git", "-C", str(clone), "push", "-q", "origin", "HEAD"],
                   check=True, capture_output=True)


@pytest.mark.integration
def test_push_race_auto_reconciles_disjoint_change(appmod, isolated_wiki, tmp_path):
    """B11: when the remote moved with a DISJOINT change (the common 15-min-cron
    race), a rejected push is auto-healed by pull --rebase + retry — no raise."""
    # Remote advances on a different file than the write touches.
    _advance_remote(isolated_wiki, tmp_path,
                    rel_path="OTHER.md", content="remote-only edit\n")
    p = isolated_wiki.wiki / "concepts" / "entropy.md"
    p.write_text(p.read_text() + "\nlocal disjoint edit.\n")

    res = appmod._git_commit_and_push([p], "test: disjoint write during race")
    assert res["committed"] is True and res["pushed"] is True

    # Remote now has BOTH our commit and the mover's file (clean rebase + push).
    log = subprocess.run(["git", "-C", str(isolated_wiki.remote), "log", "--oneline"],
                         capture_output=True, text=True).stdout
    assert "disjoint write during race" in log and "remote: advance" in log


@pytest.mark.integration
def test_push_race_genuine_conflict_still_raises(appmod, isolated_wiki, tmp_path):
    """B11 guard: a CONFLICTING remote change (same file) is NOT silently merged —
    pull --rebase fails, the rebase is aborted, and GitPushError is raised with the
    local commit retained (the loud-divergence guarantee survives)."""
    _advance_remote(isolated_wiki, tmp_path,
                    rel_path="wiki/concepts/entropy.md", content="REMOTE rewrite of entropy\n")
    p = isolated_wiki.wiki / "concepts" / "entropy.md"
    p.write_text("LOCAL rewrite of entropy\n")

    with pytest.raises(appmod.GitPushError):
        appmod._git_commit_and_push([p], "test: conflicting write during race")

    # No rebase left in progress; the local commit is retained (HEAD is our commit).
    status = subprocess.run(["git", "-C", str(isolated_wiki.repo), "status", "--porcelain=2", "--branch"],
                            capture_output=True, text=True).stdout
    assert "rebase" not in status.lower()
    head_msg = subprocess.run(["git", "-C", str(isolated_wiki.repo), "log", "-1", "--pretty=%s"],
                              capture_output=True, text=True).stdout
    assert "conflicting write during race" in head_msg


@pytest.mark.integration
def test_push_is_centralized_to_one_helper(appmod):
    """After consolidation, _git_commit_and_push is the ONLY site that runs
    `git push`. Guards against a new write path reintroducing its own (silent)
    push and resurrecting the copy-paste drift the audit flagged."""
    src = open(appmod.__file__).read()
    push_sites = re.findall(r'"git",\s*"-C",[^\]]*?"push"', src)
    assert len(push_sites) == 1, f"expected exactly one `git push` site, found {len(push_sites)}"


@pytest.mark.integration
def test_edit_node_full_body_and_frontmatter(appmod, isolated_wiki):
    """The viewer edit path: tool_edit_node replaces the full body + a frontmatter
    field, then commits. (Was broken: the viewer mis-routed to staged/commit.)"""
    res = appmod.tool_edit_node(
        iri="pkis:concept:entropy",
        frontmatter_updates={"understanding": 4},
        content="## Definition\n\nEdited via the viewer.\n",
        commit_message="test: edit entropy",
    )
    assert res["status"] == "edited" and res["git_pushed"] is True
    import frontmatter as _fm
    p = _fm.load(str(isolated_wiki.wiki / "concepts" / "entropy.md"))
    assert p["understanding"] == 4
    assert "Edited via the viewer." in p.content
