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
- transformers
id: pkis:technique:layer-normalization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch16
tags:
- normalization
- transformers
- training-stability
- geometry
title: Layer Normalization
understanding: 0
---

## Definition
$$\text{LayerNorm}(x) = \gamma \cdot \frac{x - \mathbb{E}[x]}{\sqrt{\mathbb{V}[x] + \epsilon}} + \beta$$

Geometrically, this equals $\sqrt{d}\,\Pi_S(\Pi_1(x))$: first project $x$ onto the hyperplane orthogonal to $\mathbf{1}$ (remove the mean), then normalize to unit sphere, then apply learned affine parameters $\gamma, \beta$. Unlike batch normalization, statistics are computed over the *feature* dimension of a single example, requiring no batch dimension.

### Why it matters
Layer normalization is the standard normalization choice in transformer architectures because it is independent of batch size and sequence length. The unit-sphere interpretation explains why attention dot-products remain well-scaled: after LayerNorm, inner products are proportional to Euclidean distances, stabilizing softmax attention weights.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]