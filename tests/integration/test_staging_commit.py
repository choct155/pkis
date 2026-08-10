"""
Seam I — staging → commit, the two-phase write (ARCHITECTURE_AUDIT.md §7 Seam I).

create_*_stub / create_bridge_note write to wiki/staging/; commit_staged_node
promotes to the live graph + git (or discards). The recovery script fill_missing.py
exists because a mid-run restart once lost creates, so the round-trip is pinned.
Stubs pass suggest_sources=False to stay offline.
"""

import pytest


def _seed_catalog(env):
    # commit_staged_node git-adds index.md + log.md alongside the promoted node.
    (env.wiki / "index.md").write_text("# Index\n")
    (env.wiki / "log.md").write_text("# Log\n")


@pytest.mark.integration
def test_stage_list_commit_round_trip(appmod, isolated_wiki):
    _seed_catalog(isolated_wiki)
    staged = appmod.tool_create_node_stub(knowledge_type="concept",
                                          title="Round Trip Concept", suggest_sources=False)
    sid = staged["staged_id"]

    listed = appmod.tool_get_staged_nodes()
    assert sid in {n["staged_id"] for n in listed}

    res = appmod.tool_commit_staged_node(staged_id=sid)
    assert res["status"] == "committed"
    assert appmod.find_node_path("round-trip-concept") is not None      # promoted live
    assert sid not in {n["staged_id"] for n in appmod.tool_get_staged_nodes()}  # consumed


@pytest.mark.integration
def test_discard_action_removes_staged_without_promoting(appmod, isolated_wiki):
    _seed_catalog(isolated_wiki)
    staged = appmod.tool_create_node_stub(knowledge_type="concept",
                                          title="Discard Me", suggest_sources=False)
    res = appmod.tool_commit_staged_node(staged_id=staged["staged_id"], action="discard")
    assert res["status"] == "discarded"
    assert appmod.find_node_path("discard-me") is None  # no orphan left live


@pytest.mark.integration
def test_commit_removes_a_tracked_staged_file_from_git(appmod, isolated_wiki):
    """Regression: if a staged file ever became tracked in git (e.g. swept into a
    broad `git add -A` checkpoint), promoting it must COMMIT the staging file's
    removal. Otherwise it lingers in HEAD, is restored on the next server reset,
    and re-surfaces in the inbox as a perpetual 'needs approval' (the DREAM bug)."""
    import subprocess
    _seed_catalog(isolated_wiki)
    staged = appmod.tool_create_node_stub(knowledge_type="concept",
                                          title="Regression Concept", suggest_sources=False)
    sid = staged["staged_id"]
    staged_path = appmod.STAGING_DIR / "regression-concept.md"
    assert staged_path.exists()

    # Simulate the stray checkpoint that tracked the staged file in HEAD.
    repo = str(appmod.REPO_DIR)
    subprocess.run(["git", "-C", repo, "add", str(staged_path)], check=True, capture_output=True)
    subprocess.run(["git", "-C", repo, "commit", "-m", "checkpoint: sweep staging"],
                   check=True, capture_output=True)
    assert appmod._git_tracked(staged_path)             # precondition: now tracked

    res = appmod.tool_commit_staged_node(staged_id=sid)
    assert res["status"] == "committed"
    assert not staged_path.exists()                     # gone from disk
    assert not appmod._git_tracked(staged_path)         # AND removal committed to HEAD


@pytest.mark.integration
def test_commit_resolves_fuzzy_links(appmod, isolated_wiki):
    """A bridge note staged with fuzzy refs is promoted with confirmed_links
    resolving them — the commit accepts and applies the resolution map."""
    _seed_catalog(isolated_wiki)
    staged = appmod.tool_create_bridge_note(
        rationale="Entropy underlies Bayesian surprise.",
        linked_node_refs=["entropy", "bayesian-inference"],
        proposed_edge_type="uses",
    )
    res = appmod.tool_commit_staged_node(
        staged_id=staged["staged_id"],
        confirmed_links={"entropy": "pkis:concept:entropy",
                         "bayesian-inference": "pkis:concept:bayesian-inference"},
    )
    assert res["status"] == "committed"
