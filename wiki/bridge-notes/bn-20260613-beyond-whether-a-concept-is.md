---
date_created: '2026-06-13'
id: pkis:bridge-note:bn-20260613-beyond-whether-a-concept-is
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- retrieval-inference-tradeoff
- compositional-query-grounding
- conditional-entropy
- ontological-coverage-planning
origin: conversation
proposed_edge_type: extends
rationale: 'Beyond whether a concept is referenced in retrieved content (coverage,
  first-order), there is a second dimension: instantiation depth — how completely
  a knowledge unit is explained given that it appears. Formalized as conditional entropy
  H(c|d): after reading document d, how much residual uncertainty remains about concept
  c? A concept node drives H(c|d) toward zero by design. A document leaves H(c|d)
  positive and variable — the concept may appear as a bare reference (contango in
  a commodity blog), as partial intuition, or as a full explanation. This gradient
  matters for synthesis quality: a response assembled from shallow instantiations
  will be accurate at the assertion level but incomplete at the implication level.
  First-order problem (coverage/availability) is the priority to formalize. Instantiation
  depth is the second-order open question to return to after coverage is tightened.'
source_context: Conversation on mutual information framing of query-node scope matching
  — organizational knowledge architecture pitch
status: unreviewed
title: Instantiation depth as second-order retrieval quality dimension
---

## Connection
Beyond whether a concept is referenced in retrieved content (coverage, first-order), there is a second dimension: instantiation depth — how completely a knowledge unit is explained given that it appears. Formalized as conditional entropy H(c|d): after reading document d, how much residual uncertainty remains about concept c? A concept node drives H(c|d) toward zero by design. A document leaves H(c|d) positive and variable — the concept may appear as a bare reference (contango in a commodity blog), as partial intuition, or as a full explanation. This gradient matters for synthesis quality: a response assembled from shallow instantiations will be accurate at the assertion level but incomplete at the implication level. First-order problem (coverage/availability) is the priority to formalize. Instantiation depth is the second-order open question to return to after coverage is tightened.

## Nodes Involved
- [[retrieval-inference-tradeoff]]
- [[compositional-query-grounding]]
- [[conditional-entropy]]
- [[ontological-coverage-planning]]

## Integration Notes
Pending review.