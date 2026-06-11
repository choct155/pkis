---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- natural-language-processing
extends:
- scaled-dot-product-attention
id: pkis:technique:multi-head-attention
instantiates:
- transformer-attention-mechanisms
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch16
tags:
- attention
- transformer
- multi-head
- NLP
title: Multi-Head Attention (MHA)
understanding: 0
---

## Definition
$$\text{MHA}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \text{Concat}(h_1,\ldots,h_H)\mathbf{W}^O, \quad h_i = \text{Attn}(\mathbf{Q}\mathbf{W}_i^Q,\, \mathbf{K}\mathbf{W}_i^K,\, \mathbf{V}\mathbf{W}_i^V)$$

Each head $h_i$ applies scaled dot-product attention in a lower-dimensional subspace via learned projection matrices $\mathbf{W}_i^Q, \mathbf{W}_i^K, \mathbf{W}_i^V$; the $H$ head outputs are concatenated and projected back with $\mathbf{W}^O$.

### Why it matters
Multiple heads allow the model to jointly attend to information from different representation subspaces at different positions. Empirically this improves performance; theoretically each head can specialize in a different type of relationship (syntactic, semantic, positional). After training, redundant heads can often be pruned without loss, suggesting the model discovers a parsimonious set of attention patterns.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[transformer-attention-mechanisms]] — instantiates
- [[scaled-dot-product-attention]] — extends
[To be populated during integration]