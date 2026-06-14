---
date_created: '2026-06-14'
id: pkis:bridge-note:bn-20260614-edge-traversal-frequency-and-node
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- bn-20260613-the-existing-coveragepertoken-efficiency-formali
- retrieval-inference-tradeoff
- concept-typed-nodes-dominate-document-nodes-on-coverage
origin: conversation
proposed_edge_type: extends
rationale: 'Edge traversal frequency and node contribution to answer quality are distinct
  quantities that require different measurement strategies.


  Traversal frequency P(edge traversed | query class) is cheaply observable from logs
  — which edges were crossed on the path to a satisfactory answer. This is the hardening
  signal: high traversal frequency under a given edge type indicates that edge is
  doing routing work. Does not require user feedback.


  Contribution attribution E[ΔCoverage | node retrieved] is not recoverable from traversal
  alone. Users evaluate the composed payload, not individual nodes. This is structurally
  a credit assignment problem — response quality is a function of many retrieved nodes,
  and the user signal is a scalar over the composition. Attribution requires either
  ablation (expensive: what would quality have been without this node?), Shapley-style
  decomposition, or counterfactual testing. At organizational query volumes this is
  not feasible per-query.


  Two-tier measurement strategy: (1) System level — use traversal frequency as the
  hardening signal continuously. Cheap, always available, gives routing quality of
  edges. (2) Evaluation level — periodic sampling framework with ground truth and
  attribution analysis. Expensive but provides contribution weights unrecoverable
  from traversal alone.


  The relationship between signals: traversal frequency estimates P(edge relevant
  | q). Contribution attribution estimates E[ΔCoverage | edge traversed]. The product
  is expected marginal contribution weighted by relevance probability — the quantity
  actually needed to rank edge value. Estimate the first cheaply from logs, the second
  expensively on samples, use samples to calibrate the cheap signal.'
source_context: Conversation on edge information content formalization — measurement
  architecture for contribution attribution
status: unreviewed
title: Edge contribution attribution — two-tier measurement strategy
---

## Connection
Edge traversal frequency and node contribution to answer quality are distinct quantities that require different measurement strategies.

Traversal frequency P(edge traversed | query class) is cheaply observable from logs — which edges were crossed on the path to a satisfactory answer. This is the hardening signal: high traversal frequency under a given edge type indicates that edge is doing routing work. Does not require user feedback.

Contribution attribution E[ΔCoverage | node retrieved] is not recoverable from traversal alone. Users evaluate the composed payload, not individual nodes. This is structurally a credit assignment problem — response quality is a function of many retrieved nodes, and the user signal is a scalar over the composition. Attribution requires either ablation (expensive: what would quality have been without this node?), Shapley-style decomposition, or counterfactual testing. At organizational query volumes this is not feasible per-query.

Two-tier measurement strategy: (1) System level — use traversal frequency as the hardening signal continuously. Cheap, always available, gives routing quality of edges. (2) Evaluation level — periodic sampling framework with ground truth and attribution analysis. Expensive but provides contribution weights unrecoverable from traversal alone.

The relationship between signals: traversal frequency estimates P(edge relevant | q). Contribution attribution estimates E[ΔCoverage | edge traversed]. The product is expected marginal contribution weighted by relevance probability — the quantity actually needed to rank edge value. Estimate the first cheaply from logs, the second expensively on samples, use samples to calibrate the cheap signal.

## Nodes Involved
- [[bn-20260613-the-existing-coveragepertoken-efficiency-formali]]
- [[retrieval-inference-tradeoff]]
- [[concept-typed-nodes-dominate-document-nodes-on-coverage]]

## Integration Notes
Pending review.