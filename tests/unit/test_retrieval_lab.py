"""Retrieval lab (C-1e) — staged pipeline, profiles, metrics, experiment store.

Pins the contracts that the lab depends on: profile merge semantics, the staged
search trace, neutrality of the default profile vs. the old hybrid_search, the
reference-free metric math, and the experiment store round-trip.
"""

import networkx as nx
import numpy as np
import pytest

import experiments
import metrics


# ── profile merge ──

@pytest.mark.unit
def test_merge_profile_is_partial_and_nondestructive(appmod):
    merged = appmod.merge_search_profile({"retrievers": {"dense": False}})
    assert merged["retrievers"] == {"lexical": True, "dense": False}   # sub-key merge
    assert merged["fusion"]["k"] == 60                                  # untouched default
    # default object itself is never mutated
    assert appmod.DEFAULT_SEARCH_PROFILE["retrievers"]["dense"] is True


@pytest.mark.unit
def test_resolve_profile_named_inline_and_unknown(appmod):
    assert appmod.resolve_search_profile(None)[1] == "default"
    assert appmod.resolve_search_profile("lexical_only")[1] == "named:lexical_only"
    assert appmod.resolve_search_profile({"name": "x"})[1] == "inline"
    # unknown name falls back to default rather than erroring
    assert appmod.resolve_search_profile("nope")[1] == "default"


# ── staged pipeline ──

@pytest.mark.unit
def test_search_trace_records_stages(appmod, isolated_wiki):
    trace = {}
    appmod.STORE.search("entropy", trace=trace, max_results=5)
    names = [s["name"] for s in trace["stages"]]
    assert names == ["retrieve:lexical", "retrieve:dense", "fuse:rrf", "assemble"]
    assert all(isinstance(s["ms"], (int, float)) for s in trace["stages"])


@pytest.mark.unit
def test_lexical_only_profile_skips_dense_stage(appmod, isolated_wiki):
    trace = {}
    appmod.STORE.search("entropy", profile={"retrievers": {"dense": False}},
                        trace=trace, max_results=5)
    assert "retrieve:dense" not in [s["name"] for s in trace["stages"]]


@pytest.mark.unit
def test_hybrid_search_equals_default_profile(appmod, isolated_wiki):
    a = [r["iri"] for r in appmod.STORE.hybrid_search("entropy", max_results=8)]
    b = [r["iri"] for r in appmod.STORE.search("entropy", max_results=8)]
    assert a == b


@pytest.mark.unit
def test_unknown_reranker_is_skipped(appmod, isolated_wiki):
    # must not raise — just logs and passes candidates through
    res = appmod.STORE.search("entropy", profile={"rerankers": ["does_not_exist"]}, max_results=3)
    assert isinstance(res, list)


@pytest.mark.unit
def test_cross_encoder_reranks_head_preserving_set(appmod, isolated_wiki):
    """With a stub cross-encoder (no model download), the top-N head is reordered
    by predicted score while the result set is preserved."""
    store = appmod.STORE
    base = [r["iri"] for r in store.search("entropy", max_results=5)]

    class StubCE:  # scores ascending → last candidate ranks highest
        def predict(self, pairs):
            return list(range(len(pairs)))

    store._get_cross_encoder = lambda name: StubCE()
    trace = {}
    reranked = [r["iri"] for r in store.search(
        "entropy",
        profile={"rerankers": ["cross_encoder"], "reranker_params": {"cross_encoder": {"top_n": 5}}},
        trace=trace, max_results=5)]
    assert any(s["name"] == "rerank:cross_encoder" for s in trace["stages"])
    assert set(base) == set(reranked)
    if len(base) > 1:
        assert base != reranked            # order changed
        assert reranked == base[::-1]      # exactly reversed by the ascending stub


# ── metrics ──

@pytest.mark.unit
def test_structural_coherence_connected_vs_scattered():
    g = nx.DiGraph()
    g.add_edge("a", "b", edge_type="uses")
    g.add_edge("b", "c", edge_type="uses")
    g.add_node("z")
    connected = metrics.structural_coherence(["a", "b", "c"], g)
    assert connected["coherence"] == 1.0 and connected["n_components"] == 1
    scattered = metrics.structural_coherence(["a", "z"], g)
    assert scattered["coherence"] == 0.5 and scattered["n_components"] == 2


@pytest.mark.unit
def test_structural_coherence_typed_only_drops_related_edges():
    g = nx.DiGraph()
    g.add_edge("a", "b", edge_type="related")  # weak wikilink edge
    assert metrics.structural_coherence(["a", "b"], g, typed_only=True)["coherence"] == 0.5
    assert metrics.structural_coherence(["a", "b"], g, typed_only=False)["coherence"] == 1.0


@pytest.mark.unit
def test_redundancy_and_groundedness_math():
    near = np.array([[1, 0, 0], [0.99, 0.01, 0]], dtype=float)
    assert metrics.redundancy(near)["redundancy"] > 0.99
    assert metrics.redundancy(np.eye(3))["redundancy"] == pytest.approx(0.0, abs=1e-6)
    g = metrics.groundedness(np.array([[1, 0, 0]], float), np.array([[1, 0, 0], [0, 1, 0]], float))
    assert g["groundedness"] == pytest.approx(1.0)
    assert metrics.groundedness(np.empty((0, 3)), np.eye(3))["groundedness"] is None


# ── experiment store ──

@pytest.mark.unit
def test_experiment_store_roundtrip(tmp_path):
    db = tmp_path / "exp.sqlite"
    cid = "cmp1"
    for prof in ("default", "lexical_only"):
        experiments.log_experiment(db, {
            "comparison_id": cid, "paradigm": "search", "query": "q",
            "profile_name": prof, "profile": {"name": prof},
            "corpus_head": "abc123", "n_results": 3,
            "retrieval_ms": 1.0, "eval_ms": 0.1, "eval_cost_usd": 0.0,
            "total_cost_usd": 0.0, "metrics": {"coherence": 0.5},
            "trace": [{"name": "fuse:rrf"}], "payload": {"results": []},
        })
    rows = experiments.list_experiments(db, comparison_id=cid)
    assert len(rows) == 2
    assert rows[0]["metrics"]["coherence"] == 0.5           # JSON decoded back
    assert rows[0]["profile"]["name"] in ("default", "lexical_only")
    assert experiments.list_experiments(db, paradigm="ask") == []


@pytest.mark.unit
def test_personalized_pagerank_boosts_connected_node(appmod):
    g = nx.DiGraph()
    g.add_edge("s", "x", weight=1.0)
    g.add_edge("x", "s", weight=1.0)
    g.add_node("z")  # isolated
    store = appmod.STORE
    store._ppr_out = None
    try:
        ppr = store._personalized_pagerank(g, {"s": 1.0}, alpha=0.85)
        assert ppr["x"] > ppr["z"]   # a seed's neighbour beats an isolated node
        assert ppr["s"] > 0
    finally:
        store._ppr_out = None  # don't leak the toy adjacency to other tests


@pytest.mark.unit
def test_graph_rerank_runs_and_blend_zero_is_baseline(appmod, isolated_wiki):
    base = [r["iri"] for r in appmod.STORE.search("entropy", max_results=5)]
    trace = {}
    g = appmod.STORE.search("entropy", profile={"rerankers": ["graph"]}, trace=trace, max_results=5)
    assert any(s["name"] == "rerank:graph" for s in trace["stages"])
    assert isinstance(g, list)
    # blend=0 → pure first-stage order, so identical to the baseline (scale-free check)
    b0 = [r["iri"] for r in appmod.STORE.search(
        "entropy", profile={"rerankers": ["graph"], "reranker_params": {"graph": {"blend": 0.0}}}, max_results=5)]
    assert b0 == base


@pytest.mark.unit
def test_path_between_resolves_and_self_connects(appmod, isolated_wiki):
    assert appmod._resolve_anchor("entropy") == "pkis:concept:entropy"
    r = appmod.tool_path_between("entropy", "entropy")
    assert r["connected"] and r["a"]["iri"] == r["b"]["iri"] == "pkis:concept:entropy"


@pytest.mark.unit
def test_query_log_dedup_and_listing(tmp_path):
    db = tmp_path / "exp.sqlite"
    assert experiments.log_query(db, "Monte Carlo Error", paradigm="search")
    assert experiments.log_query(db, "  monte carlo   error ", paradigm="ask")  # normalizes → same row
    experiments.log_query(db, "bayesian inference")
    assert experiments.log_query(db, "x") is False    # too short, ignored
    qs = {q["query_norm"]: q for q in experiments.list_queries(db)}
    assert qs["monte carlo error"]["count"] == 2       # deduped + counted
    assert qs["monte carlo error"]["paradigm"] == "ask"  # last paradigm wins
    assert "bayesian inference" in qs


@pytest.mark.unit
def test_feedback_roundtrip(tmp_path):
    db = tmp_path / "exp.sqlite"
    fid = experiments.log_feedback(db, {"query": "q", "chosen_profile": "rerank", "rating": "up"})
    assert fid is not None
    rows = experiments.list_feedback(db)
    assert rows[0]["chosen_profile"] == "rerank" and rows[0]["rating"] == "up"


@pytest.mark.unit
def test_run_search_returns_column(appmod, isolated_wiki):
    col = appmod.run_search("entropy", profile="lexical_only", max_results=3, log=False)
    assert col["profile_name"] == "lexical_only"
    assert "coherence" in col["metrics"]
    assert [s["name"] for s in col["trace"]["stages"]][0] == "retrieve:lexical"
    assert col["retrieval_ms"] >= 0
