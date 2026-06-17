"""
Seam G — graph build ↔ search fusion (ARCHITECTURE_AUDIT.md §7 Seam G).

Pure ranking logic worth pinning: rrf_score (reciprocal-rank fusion) and the
EDGE_WEIGHTS table that structural ranking depends on. We do NOT assert exact
search relevance (not worth the brittleness) — only the fusion math and the
edge-weight contract.
"""

import pytest


@pytest.mark.unit
def test_rrf_score_formula(appmod):
    # RRF = 1 / (k + rank); rank 0 with default k=60 → 1/60.
    assert appmod.rrf_score(0) == pytest.approx(1.0 / 60)
    assert appmod.rrf_score(9, k=60) == pytest.approx(1.0 / 69)


@pytest.mark.unit
def test_rrf_score_is_monotonic_decreasing(appmod):
    scores = [appmod.rrf_score(r) for r in range(10)]
    assert scores == sorted(scores, reverse=True)
    assert all(s > 0 for s in scores)


@pytest.mark.unit
def test_edge_weights_cover_advertised_predicates(appmod):
    """Every predicate add_connections accepts must have a structural weight, or
    it's silently dropped from ranking (the audit's Seam-G silent-failure mode)."""
    # The predicates add_connections advertises (app.py add_connections inputSchema enum).
    advertised_predicates = {
        "prerequisite-of", "uses", "specializes", "generalizes", "extends",
        "applies", "instantiates", "contrasts-with", "analogous-to", "illustrated-by",
    }
    missing = advertised_predicates - set(appmod.EDGE_WEIGHTS)
    assert not missing, f"predicates with no EDGE_WEIGHTS entry (dropped from ranking): {sorted(missing)}"


@pytest.mark.unit
def test_edge_weights_are_normalized_range(appmod):
    assert all(0 < w <= 1.0 for w in appmod.EDGE_WEIGHTS.values())


@pytest.mark.unit
def test_search_wiki_index_finds_seeded_term(appmod, isolated_wiki):
    """search_wiki_index (BM25-only hidden tool) uses STORE's bm25 cache after C-1c."""
    appmod.STORE.invalidate_search()
    iris = {r["iri"] for r in appmod.tool_search_wiki_index("entropy")}
    assert "pkis:concept:entropy" in iris


@pytest.mark.unit
def test_hybrid_search_finds_seeded_term(appmod, isolated_wiki):
    """hybrid_search('entropy') over the fixture wiki surfaces the entropy node.
    BM25-only (semantic disabled in tests), so this is deterministic. Asserts
    presence, not an exact rank."""
    appmod._bm25_index = None  # force rebuild against the isolated wiki
    results = appmod.hybrid_search("entropy", max_results=10)
    iris = {r["iri"] for r in results}
    assert "pkis:concept:entropy" in iris
