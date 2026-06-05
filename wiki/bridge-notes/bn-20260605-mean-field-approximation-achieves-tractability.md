---
date_created: '2026-06-05'
id: pkis:bridge-note:bn-20260605-mean-field-approximation-achieves-tractability
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- mean-field-approximation
- transformer-attention-mechanisms
- intensional-grounding
origin: conversation
proposed_edge_type: ''
rationale: 'Mean field approximation achieves tractability by assuming components
  are independent — each unit responds only to the aggregate behavior of others, not
  to specific pairwise dependencies. This is productive in many settings but structurally
  incapable of representing cases where specific inter-unit correlations are the computationally
  relevant information.


  Transformer attention is architecturally designed to do exactly what mean field
  gives up. Scaled dot-product attention computes, for each token, a weighted combination
  over all other tokens where the weights are a learned function of specific query-key
  compatibility. This is not an average field — it is a selective, content-dependent
  aggregation that explicitly preserves and exploits pairwise structure.


  A mean field treatment of a sequence model would have each token''s representation
  updated by the average representation of all others — which is approximately what
  simple pooling or bag-of-words approaches do. The transformer replaces that average
  with a structured, dynamic weighting that can concentrate attention on specific
  tokens based on content.


  Implication for the intensional grounding thesis: the claim that ontological structure
  improves model performance by reshaping attention weights is a claim about the *correlation
  structure* of attention, not its average behavior. Mean field reasoning would be
  blind to exactly this mechanism. The hypothesis is only coherent in a framework
  that assumes attention is doing non-mean-field work.'
source_context: ''
status: unreviewed
title: Attention as deliberate recovery of correlations that mean field discards
---

## Connection
Mean field approximation achieves tractability by assuming components are independent — each unit responds only to the aggregate behavior of others, not to specific pairwise dependencies. This is productive in many settings but structurally incapable of representing cases where specific inter-unit correlations are the computationally relevant information.

Transformer attention is architecturally designed to do exactly what mean field gives up. Scaled dot-product attention computes, for each token, a weighted combination over all other tokens where the weights are a learned function of specific query-key compatibility. This is not an average field — it is a selective, content-dependent aggregation that explicitly preserves and exploits pairwise structure.

A mean field treatment of a sequence model would have each token's representation updated by the average representation of all others — which is approximately what simple pooling or bag-of-words approaches do. The transformer replaces that average with a structured, dynamic weighting that can concentrate attention on specific tokens based on content.

Implication for the intensional grounding thesis: the claim that ontological structure improves model performance by reshaping attention weights is a claim about the *correlation structure* of attention, not its average behavior. Mean field reasoning would be blind to exactly this mechanism. The hypothesis is only coherent in a framework that assumes attention is doing non-mean-field work.

## Nodes Involved
- [[mean-field-approximation]]
- [[transformer-attention-mechanisms]]
- [[intensional-grounding]]

## Integration Notes
Pending review.