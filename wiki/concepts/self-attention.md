---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- nlp
id: pkis:concept:self-attention
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch15
tags:
- transformer
- attention
- contextual-embeddings
- sequence
title: Self-Attention
understanding: 0
---

## Definition
Self-attention is attention applied to a single sequence where queries, keys, and values are all derived from the same input $x_1, \ldots, x_n$:

$$y_i = \text{Attn}(x_i,\ (x_1, x_1), \ldots, (x_n, x_n))$$

This allows each position to attend to every other position in the sequence, producing contextualised representations in $O(1)$ maximum path length between any two tokens.

### Why it matters
Self-attention replaces recurrence as the primary mechanism for capturing intra-sequence dependencies in Transformers. Because it is permutation-equivariant (the attention weights depend only on content, not position), positional encodings must be added explicitly. Self-attention enables parallelism across the sequence at training time, eliminating the sequential bottleneck of RNNs, while achieving superior long-range dependency modeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]