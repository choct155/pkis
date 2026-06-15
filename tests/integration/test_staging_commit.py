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
