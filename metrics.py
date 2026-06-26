"""Reference-free retrieval-quality metrics.

The cheap, annotation-free subset of the Multidimensional Retrieval Quality
Framework (`framework:multidimensional-retrieval-quality-framework`) — computable
on every query with no C(q) estimate and no LLM call:

- structural_coherence — does the retrieved set hang together as a connected
  subgraph over typed edges? (framework dim 6)
- redundancy / diversity — how much do results repeat each other? a cheap proxy
  for Concision before C(q) is available (framework dim 2).
- groundedness — how well is generated text supported by retrieved node text?
  embedding-alignment proxy for the LLM-entailment version (framework dim 3).

The C(q)-dependent dimensions (Coverage, the exact Concision = Coverage/tokens,
Structural Relevance) live in a later phase behind the `deep_metrics` toggle.

Pure functions: numpy + networkx in, plain dicts out. Callers (store/app/ask)
own embedding and graph construction so this module stays dependency-light and
unit-testable.
"""

import networkx as nx
import numpy as np

_EPS = 1e-9


def _unit_rows(mat):
    m = np.asarray(mat, dtype=np.float32)
    if m.ndim != 2 or m.shape[0] == 0:
        return None
    return m / (np.linalg.norm(m, axis=1, keepdims=True) + _EPS)


def structural_coherence(iris, graph, typed_only=True):
    """Fraction of the retrieved set in its largest connected component over the
    induced subgraph. 1.0 = every retrieved node links to the rest; low = a bag
    of disconnected hits. `typed_only` drops weak wikilink ("related") edges so
    only deliberate typed predicates count (matches _cluster_proximity_map)."""
    nodes = [i for i in iris if graph.has_node(i)]
    n = len(nodes)
    if n <= 1:
        return {"coherence": 1.0, "n_components": 1 if n else 0, "n_in_graph": n}
    sub = graph.subgraph(nodes)
    if typed_only:
        H = nx.Graph()
        H.add_nodes_from(nodes)
        H.add_edges_from(
            (u, v) for u, v, d in sub.edges(data=True) if d.get("edge_type") != "related"
        )
    else:
        H = sub.to_undirected()
    comps = list(nx.connected_components(H))
    largest = max((len(c) for c in comps), default=0)
    return {"coherence": largest / n, "n_components": len(comps), "n_in_graph": n}


def redundancy(vectors):
    """Mean pairwise cosine among result embeddings. High redundancy = the set
    repeats itself (low concision); diversity = 1 - redundancy."""
    Vn = _unit_rows(vectors)
    if Vn is None or Vn.shape[0] < 2:
        return {"redundancy": 0.0, "diversity": 1.0}
    sim = Vn @ Vn.T
    n = sim.shape[0]
    off = (float(sim.sum()) - float(np.trace(sim))) / (n * (n - 1))
    off = float(np.clip(off, -1.0, 1.0))
    return {"redundancy": off, "diversity": 1.0 - off}


def groundedness(answer_vecs, evidence_vecs):
    """For each answer unit (sentence/claim), max cosine to any evidence vector;
    return the mean. Embedding-alignment proxy for entailment-based groundedness.
    Pass per-sentence answer vectors and per-node evidence vectors."""
    A = _unit_rows(answer_vecs)
    E = _unit_rows(evidence_vecs)
    if A is None or E is None:
        return {"groundedness": None}
    per_unit = (A @ E.T).max(axis=1)
    return {"groundedness": float(per_unit.mean()), "per_unit": [float(x) for x in per_unit]}


def deep_metrics(cq_iris, result_iris, graph, result_tokens, depth=2):
    """The C(q)-dependent framework dims (1 Coverage, 2 Concision, 7 Structural
    Relevance), given an estimated concept set C(q) for the query.

    - Coverage = fraction of C(q) concepts present in S or directly referenced by it
      (a concept counts as covered if it's in the retrieved set or a graph neighbour
      of one). Σ_c 𝟙[c ∈ S ∪ N(S)] / |C(q)|.
    - Concision = Coverage / tokens(S), reported per 1k tokens. (tokens(S) is the
      caller's token estimate; with capped excerpts this is approximate and mostly
      tracks coverage — refine with full node content later.)
    - Structural relevance = fraction of S reachable from any C(q) anchor within
      `depth` typed-edge hops.
    """
    if not cq_iris:
        return {}
    s_set = set(result_iris)
    neigh = set()
    for s in result_iris:
        if graph.has_node(s):
            neigh.update(graph.successors(s))
            neigh.update(graph.predecessors(s))
    covered = sum(1 for c in cq_iris if c in s_set or c in neigh)
    coverage = covered / len(cq_iris)
    concision = coverage / (max(float(result_tokens), 1.0) / 1000.0)
    UG = graph.to_undirected()
    reach = set()
    for a in cq_iris:
        if UG.has_node(a):
            reach.update(nx.single_source_shortest_path_length(UG, a, cutoff=depth).keys())
    rel = (sum(1 for s in result_iris if s in reach) / len(result_iris)) if result_iris else 0.0
    return {"coverage": round(coverage, 3), "concision_per_1k": round(concision, 3),
            "structural_relevance": round(rel, 3), "cq_size": len(cq_iris)}


def cheap_metrics(result_iris, result_vecs, graph):
    """Convenience bundle for the search paradigm: structural coherence over the
    graph + redundancy/diversity over result embeddings. (Groundedness applies to
    the ask paradigm, where there's generated text to ground.)"""
    out = {}
    if graph is not None:
        out.update(structural_coherence(result_iris, graph))
    if result_vecs is not None:
        out.update(redundancy(result_vecs))
    return out
