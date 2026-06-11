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
- machine-learning
- deep-learning
id: pkis:technique:straight-through-estimator
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
tags:
- quantization
- gradient-approximation
- discrete
- binary-networks
title: Straight-Through Estimator
understanding: 0
---

## Definition
The straight-through estimator (STE) approximates the gradient of a non-differentiable (typically quantization or thresholding) function $f$ during backpropagation by replacing the zero or undefined derivative with the identity (or a clipped identity):
$$\hat{f}'(x) = \mathbf{1}[|x| \leq 1] \quad \text{(hard-tanh variant)}$$
Concretely, the forward pass uses the true discontinuous function $f(x)$ (e.g., $\text{sign}(x)$ or $\text{round}(x)$), while the backward pass propagates gradients **as if** $f$ were the identity (or hard-tanh).

### Why it matters
STE is the standard training recipe for binary/quantized neural networks and discrete autoencoders (VQ-VAE). It is simple, widely applicable, and empirically effective despite lacking rigorous theoretical justification. Alternatives include the Gumbel-softmax and continuous relaxations, but STE avoids the need for an explicit relaxation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]