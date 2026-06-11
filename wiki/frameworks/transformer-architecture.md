---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- nlp
id: pkis:framework:transformer-architecture
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch15
- murphy-pml2-advanced-ch16
tags:
- architecture
- attention
- language-model
- seq2seq
title: Transformer (Seq2Seq Attention Architecture)
understanding: 0
---

## Definition
The Transformer [Vaswani et al., 2017] is a seq2seq architecture that replaces recurrence with stacked multi-headed self-attention and position-wise feedforward layers:

**Encoder block:**
$$Z = \text{LayerNorm}(\text{MHA}(X,X,X) + X), \quad E = \text{LayerNorm}(\text{FF}(Z) + Z)$$

**Decoder block:**
$$Z = \text{LN}(\text{MaskedMHA}(Y,Y,Y)+Y)$$
$$Z' = \text{LN}(\text{MHA}(Z,E,E)+Z)$$
$$D = \text{LN}(\text{FF}(Z')+Z')$$

The full model stacks $N$ encoder and $N$ decoder blocks on top of positional-encoded embeddings.

### Why it matters
Transformers achieve $O(1)$ maximum path length between any two tokens (vs. $O(n)$ for RNNs), enabling parallel training on long sequences and superior long-range dependency modeling. They are the architectural backbone of essentially all modern large language models, vision transformers (ViT), and multimodal systems. Their $O(n^2 d)$ attention cost motivates a large family of efficient variants.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]