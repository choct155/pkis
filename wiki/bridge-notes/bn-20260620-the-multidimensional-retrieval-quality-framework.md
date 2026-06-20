---
date_created: '2026-06-20'
id: pkis:bridge-note:bn-20260620-the-multidimensional-retrieval-quality-framework
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- multidimensional-retrieval-quality-framework
- graph-retrieval-dominates-vector-search-concept-specifi
- continuous-hardening-mixture-framework
origin: conversation
proposed_edge_type: constrains
rationale: 'The multidimensional retrieval quality framework depends on C(q) — the
  distribution over concept dependencies induced by a query — as its foundational
  measurement primitive. Computing C(q) from graph traversal patterns creates an apparent
  circularity: using the graph as both the retrieval mechanism under evaluation and
  the basis for the evaluation criterion.


  This is structurally analogous to Gödel''s incompleteness result: any sufficiently
  expressive measurement framework will contain evaluation criteria that cannot be
  grounded entirely within the framework itself. A purely external reference — human
  annotation of C(q) for every query — would resolve the circularity but is too expensive
  to be operationally viable.


  The resolution adopted here is a pragmatic strategy, not a methodological proof.
  The argument: the graph is itself constructed from subject matter expert judgment
  — boundary arbitration, edge type validation, source selection, node instantiation.
  Every concept node and typed edge encodes a prior human decision about conceptual
  necessity and relational structure. C(q) derived from graph traversal is therefore
  not circular in a vicious sense — it is a pre-compiled representation of SME knowledge
  that predates any specific query. It is the closest available proxy to an external
  reference at operational scale.


  The incompleteness is not eliminated. It appears as specific failure modes: concepts
  the graph does not yet contain, boundary decisions that were wrong, edge types that
  are miscalibrated. These are detectable through periodic human annotation on a sample
  and task-based ground truth evaluation — not to replace graph-derived C(q) wholesale,
  but to estimate the gap between the proxy and the true external reference and flag
  where it exceeds acceptable tolerance.


  Operational architecture: graph-derived C(q) as the primary continuous measurement
  instrument; human annotation periodically on a sample to measure and track the proxy
  gap; gap magnitude feeds back into the hardening framework as a signal that ontologist
  intervention is needed.


  Key principle governing all measurement decisions in this research program: the
  objective function is engineering optimization and decision support — efficient
  application and yield — not methodological purity. Whatever reduces the cost of
  continuous improvement and improves resource allocation is valuable. A measurement
  framework that is imperfect but cheap, continuous, and actionable is strictly preferable
  to one that is theoretically pure but operationally infeasible. The Gödelian incompleteness
  is a parameter to be estimated and tracked, not a problem to be solved before proceeding.'
source_context: Conversation on C(q) estimation and the epistemological status of
  graph-derived quality metrics — Gödel analogy and pragmatic resolution
status: unreviewed
title: C(q) estimation — Gödelian incompleteness as a tracked parameter, not a blocker
---

## Connection
The multidimensional retrieval quality framework depends on C(q) — the distribution over concept dependencies induced by a query — as its foundational measurement primitive. Computing C(q) from graph traversal patterns creates an apparent circularity: using the graph as both the retrieval mechanism under evaluation and the basis for the evaluation criterion.

This is structurally analogous to Gödel's incompleteness result: any sufficiently expressive measurement framework will contain evaluation criteria that cannot be grounded entirely within the framework itself. A purely external reference — human annotation of C(q) for every query — would resolve the circularity but is too expensive to be operationally viable.

The resolution adopted here is a pragmatic strategy, not a methodological proof. The argument: the graph is itself constructed from subject matter expert judgment — boundary arbitration, edge type validation, source selection, node instantiation. Every concept node and typed edge encodes a prior human decision about conceptual necessity and relational structure. C(q) derived from graph traversal is therefore not circular in a vicious sense — it is a pre-compiled representation of SME knowledge that predates any specific query. It is the closest available proxy to an external reference at operational scale.

The incompleteness is not eliminated. It appears as specific failure modes: concepts the graph does not yet contain, boundary decisions that were wrong, edge types that are miscalibrated. These are detectable through periodic human annotation on a sample and task-based ground truth evaluation — not to replace graph-derived C(q) wholesale, but to estimate the gap between the proxy and the true external reference and flag where it exceeds acceptable tolerance.

Operational architecture: graph-derived C(q) as the primary continuous measurement instrument; human annotation periodically on a sample to measure and track the proxy gap; gap magnitude feeds back into the hardening framework as a signal that ontologist intervention is needed.

Key principle governing all measurement decisions in this research program: the objective function is engineering optimization and decision support — efficient application and yield — not methodological purity. Whatever reduces the cost of continuous improvement and improves resource allocation is valuable. A measurement framework that is imperfect but cheap, continuous, and actionable is strictly preferable to one that is theoretically pure but operationally infeasible. The Gödelian incompleteness is a parameter to be estimated and tracked, not a problem to be solved before proceeding.

## Nodes Involved
- [[multidimensional-retrieval-quality-framework]]
- [[graph-retrieval-dominates-vector-search-concept-specifi]]
- [[continuous-hardening-mixture-framework]]

## Integration Notes
Pending review.