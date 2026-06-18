"""
B10 — reading queue as a frontier-ordered capture inbox.

The manual high/normal tag is demoted to a capture-time `hint`; ordering is derived
from the concept frontier (a queued item's priority = its subject's frontier
priority_score). Un-ingested captures (no node) carry frontier_score=None and sort
last. Legacy `### High`/`### Normal` queue.md files still parse (section → hint).
"""

import pytest


@pytest.mark.integration
def test_add_to_queue_writes_flat_capture_entry(appmod, isolated_wiki):
    res = appmod.tool_add_to_queue(reference="Some Paper", reason="looks useful",
                                   priority="high")
    assert res["success"] and res["hint"] == "high"
    text = (isolated_wiki.wiki / "queue.md").read_text()
    assert "## Queue" in text
    assert "### High" not in text and "### Normal" not in text   # no priority sections
    assert "(captured:" in text and "(hint: high)" in text


@pytest.mark.integration
def test_queue_ordered_by_frontier_not_manual_tag(appmod, isolated_wiki):
    # An un-ingested capture flagged high, and an ingested node (entropy) flagged normal.
    appmod.tool_add_to_queue(reference="Unread Paper", reason="capture", priority="high")
    appmod.tool_add_to_queue(source_iri="pkis:concept:entropy", reason="seen",
                             priority="normal")
    appmod.STORE.invalidate_nodes(); appmod.STORE.invalidate_graph()

    q = appmod.tool_get_reading_queue()
    assert isinstance(q, list) and len(q) == 2
    # The ingested node has a frontier score; the un-ingested capture does not — so
    # despite its "high" hint, the capture sorts AFTER the scored item.
    assert q[0]["slug"] == "entropy" and q[0]["frontier_score"] is not None
    assert q[1]["frontier_score"] is None
    # The manual tag survives only as an informational hint.
    assert q[1]["hint"] == "high"


@pytest.mark.integration
def test_legacy_high_normal_sections_still_parse(appmod, isolated_wiki):
    (isolated_wiki.wiki / "queue.md").write_text(
        "# Reading Queue\n\n### High\n- [ ] [[entropy]] — legacy high\n"
        "\n### Normal\n- [ ] [[bayesian-inference]] — legacy normal\n")
    appmod.STORE.invalidate_nodes(); appmod.STORE.invalidate_graph()
    q = appmod.tool_get_reading_queue()
    by_slug = {it["slug"]: it for it in q}
    assert by_slug["entropy"]["hint"] == "high"        # section → hint
    assert by_slug["bayesian-inference"]["hint"] == "normal"


@pytest.mark.integration
def test_priority_filter_matches_recorded_hint(appmod, isolated_wiki):
    appmod.tool_add_to_queue(reference="A", reason="a", priority="high")
    appmod.tool_add_to_queue(reference="B", reason="b", priority="normal")
    high = appmod.tool_get_reading_queue(priority="high")
    assert all((it["hint"] or "normal") == "high" for it in high)
    assert any(it["hint"] == "high" for it in high)
