"""
Seam I — staging → commit, the two-phase write (ARCHITECTURE_AUDIT.md §7 Seam I).

create_*_stub / create_bridge_note / create_hypothesis write to wiki/staging/;
commit_staged_node promotes to the live graph + git. The recovery script
fill_missing.py exists because a mid-run restart once lost creates — so the
stage → list → commit round-trip is worth pinning.

Note: create_node_stub with suggest_sources=True calls Semantic Scholar (network).
Implementations of these stubs MUST pass sources=[...] or suggest_sources=False to
stay hermetic, or mock the suggestion call.
"""

import pytest


@pytest.mark.integration
def test_stage_list_commit_round_trip(appmod, isolated_wiki):
    """STUB: create a staged node (suggest_sources=False to stay offline) →
    get_staged_nodes shows it → commit_staged_node promotes it to wiki/<dir>/ and
    commits. Assert the live file exists and the staged entry is consumed."""
    pytest.skip("Phase-2 stub — implement create_node_stub → get_staged_nodes → commit_staged_node")


@pytest.mark.integration
def test_discard_action_removes_staged_without_promoting(appmod, isolated_wiki):
    """STUB: commit_staged_node(action='discard') drops the staged node and leaves
    NO live file behind (no orphan)."""
    pytest.skip("Phase-2 stub — implement discard path assertion")


@pytest.mark.integration
def test_commit_resolves_fuzzy_links(appmod, isolated_wiki):
    """STUB: a bridge note staged with fuzzy linked_node_refs is promoted with
    confirmed_links resolving them to real IRIs; assert the live edges point at
    existing nodes (no dangling references)."""
    pytest.skip("Phase-2 stub — implement fuzzy-ref resolution assertion")
