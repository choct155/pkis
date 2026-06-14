---
date_created: '2026-06-13'
date_updated: '2026-06-14'
id: pkis:bridge-note:bn-20260613-the-existing-coveragepertoken-efficiency-formali
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- concept-typed-nodes-dominate-document-nodes-on-coverage
- graph-encoded-concept-dependencies-reduce-expected-infe
- mutual-information
- conditional-entropy
origin: conversation
proposed_edge_type: extends
rationale: "The existing coverage-per-token efficiency formalism captures node information
  content but not edge information content. Typed directed edges carry two forms of
  information not representable in set-membership metadata: (1) directionality — a
  prerequisite-of edge from c1 to c2 encodes an asymmetric dependency that constrains
  retrieval order; set logic has no representation for this asymmetry. (2) edge type
  — the predicate τ (prerequisite-of, instantiates, contrasts-with, etc.) carries
  information about the nature of the relationship that shapes which node to fetch
  next given the current retrieved set S.\n\nTwo candidate formalizations identified
  but neither fully tight: \n\nCandidate A (decision-theoretic): information content
  of edge e = reduction in expected search cost it provides — how much it narrows
  the traversal space given S. Frames edge value as a routing signal rather than a
  coverage signal.\n\nCandidate B (probabilistic lift): edge type τ induces a conditional
  distribution P(c2 | c1, τ). Edge information content = I(q; c2 | c1, τ) − I(q; c2)
  — the lift in relevance probability for c2 provided by knowing both the source node
  c1 and the edge type τ. High-τ-lift edges are those where knowing the relationship
  type substantially increases the probability that the target concept is in C(q).\n\nEnriched
  document metadata (concept tags without graph structure) partially addresses coverage
  but loses both directionality and typed edge information entirely. This is the formal
  basis for why concept-tagged document indexes are an incomplete substitute for graph
  structure even when concept vocabulary is shared.\n\nOpen formalization: how to
  integrate edge information content into the Efficiency(q,n) metric, and how to measure
  the empirical lift of typed edges over untyped co-occurrence."
source_context: Conversation on retrieval efficiency explainer — edge value formalization
  as open problem
status: partially-resolved
title: Edge information content — directionality, typed predicates, and traversal
  ranking
---

## Connection
The existing coverage-per-token efficiency formalism captures node information content but not edge information content. Typed directed edges carry two forms of information not representable in set-membership metadata: (1) directionality — a prerequisite-of edge from c1 to c2 encodes an asymmetric dependency that constrains retrieval order; set logic has no representation for this asymmetry. (2) edge type — the predicate τ (prerequisite-of, instantiates, contrasts-with, etc.) carries information about the nature of the relationship that shapes which node to fetch next given the current retrieved set S.

Two candidate formalizations identified but neither fully tight: 

Candidate A (decision-theoretic): information content of edge e = reduction in expected search cost it provides — how much it narrows the traversal space given S. Frames edge value as a routing signal rather than a coverage signal.

Candidate B (probabilistic lift): edge type τ induces a conditional distribution P(c2 | c1, τ). Edge information content = I(q; c2 | c1, τ) − I(q; c2) — the lift in relevance probability for c2 provided by knowing both the source node c1 and the edge type τ. High-τ-lift edges are those where knowing the relationship type substantially increases the probability that the target concept is in C(q).

Enriched document metadata (concept tags without graph structure) partially addresses coverage but loses both directionality and typed edge information entirely. This is the formal basis for why concept-tagged document indexes are an incomplete substitute for graph structure even when concept vocabulary is shared.

Open formalization: how to integrate edge information content into the Efficiency(q,n) metric, and how to measure the empirical lift of typed edges over untyped co-occurrence.

## Nodes Involved
- [[concept-typed-nodes-dominate-document-nodes-on-coverage]]
- [[graph-encoded-concept-dependencies-reduce-expected-infe]]
- [[mutual-information]]
- [[conditional-entropy]]

## Integration Notes
Pending review.