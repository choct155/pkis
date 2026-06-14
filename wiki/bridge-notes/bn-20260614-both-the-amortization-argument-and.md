---
date_created: '2026-06-14'
id: pkis:bridge-note:bn-20260614-both-the-amortization-argument-and
illustrated-by:
- ganter-formal-1999
- giglou-llms4ol-2024
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- concept-typed-nodes-dominate-document-nodes-on-coverage
- coverage-driven-graph-traversal
- bn-20260613-beyond-whether-a-concept-is
- graph-encoded-concept-dependencies-reduce-expected-infe
origin: conversation
proposed_edge_type: extends
rationale: 'Both the amortization argument and the coverage-driven traversal algorithm
  implicitly assume node content quality but neither formalizes it. This assumption
  is load-bearing for both.


  The amortization claim — Eff(q, concept node) > Eff(q, document) — holds because
  I(q; concept node) is high and tokens(concept node) is low. But I(q; concept node)
  is high only if the node is well-instantiated. If a concept node is a shallow stub
  — containing a bare definition without application conditions, implications, or
  formal properties — then H(c | node) is not driven toward zero. The node costs concept-node
  tokens but delivers document-level instantiation quality. The efficiency advantage
  collapses proportionally to how far H(c | node) deviates from zero.


  The traversal algorithm assumes that retrieving c2 via a high-Reliability(τ) edge
  delivers the ΔCoverage predicted by the ranking function. If c2 is shallowly instantiated,
  the traversal decision was correct — τ was a reliable predictor of c2''s relevance
  — but the realized ΔCoverage falls short of the predicted ΔCoverage. The algorithm
  makes the right routing decision and still gets a bad outcome. These two failure
  modes — poor edge reliability and poor node instantiation — produce identical observable
  signals (bad answer quality) but require different interventions (improve edge weighting
  vs. deepen node content).


  This creates a credit assignment problem at a finer grain than the edge attribution
  problem already identified. Separating edge reliability failure from node instantiation
  failure from a scalar outcome signal requires either: (a) ablation — re-running
  the query with a better-instantiated version of c2 to isolate the node contribution,
  or (b) direct assessment of H(c | node) independent of query outcomes, which requires
  an evaluation rubric for node completeness.


  Instantiation depth is therefore the missing quality assumption that both the amortization
  argument and the traversal algorithm rest on without stating. It is not a third
  independent problem — it is the shared precondition that determines whether the
  efficiency and traversal claims hold in practice.


  The separation between Candidate B (edge reliability scoring via Reliability(τ))
  and instantiation depth (node content quality via H(c|node)) is clean: edge reliability
  is a property of the predicate τ estimable from traversal logs; instantiation depth
  is a property of the node content estimable from direct assessment or ablation.
  Both feed into realized retrieval quality but through orthogonal mechanisms.'
source_context: Conversation on edge information content formalization — Candidate
  B reliability scoring and its relationship to instantiation depth and amortization
status: unreviewed
title: Instantiation depth as shared precondition for amortization and traversal efficiency
  claims
---

## Connection
Both the amortization argument and the coverage-driven traversal algorithm implicitly assume node content quality but neither formalizes it. This assumption is load-bearing for both.

The amortization claim — Eff(q, concept node) > Eff(q, document) — holds because I(q; concept node) is high and tokens(concept node) is low. But I(q; concept node) is high only if the node is well-instantiated. If a concept node is a shallow stub — containing a bare definition without application conditions, implications, or formal properties — then H(c | node) is not driven toward zero. The node costs concept-node tokens but delivers document-level instantiation quality. The efficiency advantage collapses proportionally to how far H(c | node) deviates from zero.

The traversal algorithm assumes that retrieving c2 via a high-Reliability(τ) edge delivers the ΔCoverage predicted by the ranking function. If c2 is shallowly instantiated, the traversal decision was correct — τ was a reliable predictor of c2's relevance — but the realized ΔCoverage falls short of the predicted ΔCoverage. The algorithm makes the right routing decision and still gets a bad outcome. These two failure modes — poor edge reliability and poor node instantiation — produce identical observable signals (bad answer quality) but require different interventions (improve edge weighting vs. deepen node content).

This creates a credit assignment problem at a finer grain than the edge attribution problem already identified. Separating edge reliability failure from node instantiation failure from a scalar outcome signal requires either: (a) ablation — re-running the query with a better-instantiated version of c2 to isolate the node contribution, or (b) direct assessment of H(c | node) independent of query outcomes, which requires an evaluation rubric for node completeness.

Instantiation depth is therefore the missing quality assumption that both the amortization argument and the traversal algorithm rest on without stating. It is not a third independent problem — it is the shared precondition that determines whether the efficiency and traversal claims hold in practice.

The separation between Candidate B (edge reliability scoring via Reliability(τ)) and instantiation depth (node content quality via H(c|node)) is clean: edge reliability is a property of the predicate τ estimable from traversal logs; instantiation depth is a property of the node content estimable from direct assessment or ablation. Both feed into realized retrieval quality but through orthogonal mechanisms.

## Nodes Involved
- [[concept-typed-nodes-dominate-document-nodes-on-coverage]]
- [[coverage-driven-graph-traversal]]
- [[bn-20260613-beyond-whether-a-concept-is]]
- [[graph-encoded-concept-dependencies-reduce-expected-infe]]

## Integration Notes
Pending review.

## Connections
- [[giglou-llms4ol-2024]] — illustrated-by: LLMs4OL boundary task failure motivates the instantiation depth precondition — shallow LLM-generated nodes are the failure mode the bridge note describes.
- [[ganter-formal-1999]] — illustrated-by: FCA closure operators provide the formal criterion for concept node completeness — the missing precondition the bridge note identifies.