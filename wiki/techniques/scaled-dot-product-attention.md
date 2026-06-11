---
aliases: []
also_type: []
analogous-to:
- kernel-regression-rl
- gaussian-process
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
- machine-learning
- deep-learning
- nlp
id: pkis:technique:scaled-dot-product-attention
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- multi-headed-attention
related_concepts: []
sources:
- murphy-pml1-intro-ch15
- murphy-pml2-advanced-ch16
specializes:
- transformer-attention-mechanisms
tags:
- attention
- transformer
- self-attention
- query-key-value
title: Scaled Dot-Product Attention
understanding: 0
uses:
- softmax-action-selection
- inner-product
- layer-normalization
---

## Definition
Given query matrix $\mathbf{Q} \in \mathbb{R}^{n \times d}$, key matrix $\mathbf{K} \in \mathbb{R}^{m \times d}$, and value matrix $\mathbf{V} \in \mathbb{R}^{m \times v}$, the output is

$$\text{Attn}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d}}\right)\mathbf{V} \in \mathbb{R}^{n \times v}$$

Dividing by $\sqrt{d}$ stabilises gradients: if $q$ and $k$ are i.i.d. zero-mean, unit-variance vectors their inner product has variance $d$, so the scaling keeps variance at 1.

### Why it matters
Scaled dot-product attention is the core computational primitive of the Transformer and can be batched over all query-key pairs in a single matrix multiply, making it GPU-friendly. Its $O(n^2 d)$ cost motivates efficient variants (sparse, linear, hashing-based attention) for long sequences.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[layer-normalization]] — uses: LayerNorm stabilizes dot-product magnitudes entering attention
- [[inner-product]] — uses
- [[gaussian-process]] — analogous-to: attention is a parametric, differentiable analogue of kernel-based GP prediction
- [[kernel-regression-rl]] — analogous-to: Non-parametric attention is equivalent to kernel regression with Gaussian kernel
- [[multi-headed-attention]] — prerequisite-of
- [[softmax-action-selection]] — uses
- [[transformer-attention-mechanisms]] — specializes
[To be populated during integration]