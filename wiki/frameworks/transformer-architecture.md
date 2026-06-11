---
aliases: []
also_type: []
applies:
- machine-translation
- language-model
- neural-scaling-laws
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- recurrent-neural-network
- long-short-term-memory-lstm
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- nlp
id: pkis:framework:transformer-architecture
instantiates:
- encoder-decoder-architecture
- sequence-to-sequence-model
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
uses:
- multi-headed-attention
- sinusoidal-positional-encoding
- batch-normalization
- residual-network
- multi-head-attention
- layer-normalization
- residual-skip-connection
- language-model
- contextual-word-embeddings
- masked-language-modeling
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
- [[masked-language-modeling]] — uses
- [[contextual-word-embeddings]] — uses
- [[long-short-term-memory-lstm]] — contrasts-with
- [[neural-scaling-laws]] — applies
- [[language-model]] — uses
- [[sequence-to-sequence-model]] — instantiates
- [[residual-skip-connection]] — uses
- [[layer-normalization]] — uses
- [[multi-head-attention]] — uses
- [[residual-network]] — uses
- [[batch-normalization]] — uses: Transformer uses Layer Normalization (a variant)
- [[language-model]] — applies
- [[machine-translation]] — applies
- [[recurrent-neural-network]] — contrasts-with
- [[sinusoidal-positional-encoding]] — uses
- [[multi-headed-attention]] — uses
- [[encoder-decoder-architecture]] — instantiates
[To be populated during integration]