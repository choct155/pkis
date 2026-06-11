---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- gaussian-processes
- bayesian-statistics
id: pkis:result:nn-gp-infinite-width-limit
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch06
tags:
- infinite-width
- neural-tangent-kernel
- Gaussian-process-limit
- Neal-1996
- Bayesian-neural-network
title: Neural Network to Gaussian Process in the Infinite-Width Limit
understanding: 0
---

## Definition
For a two-layer neural network with $M$ hidden units and i.i.d. zero-mean priors on all weights, as $M\to\infty$ the distribution over network functions $y(\mathbf{x})$ converges to a **Gaussian process** whose covariance (kernel) function depends on the prior variance and the hidden-unit activation function:

$$\lim_{M\to\infty} y(\mathbf{x}) \sim \mathcal{GP}\bigl(0,\, k(\mathbf{x},\mathbf{x}')\bigr).$$

For probit activations Williams (1998) derives a closed-form non-stationary kernel; for Gaussian activations another closed form exists. The resulting kernel is generally **non-stationary** because the zero-centred weight prior breaks translation invariance in weight space.

### Why it matters
This result (Neal, 1996) provides a rigorous limit connecting neural networks and Gaussian processes, justifying the Bayesian use of GPs as infinite-parameter neural network surrogates. It also explains why deep networks with large width can behave like kernel machines, underpinning the modern neural tangent kernel (NTK) programme.

### Caveat
In the GP limit the multiple outputs become independent, losing the 'weight sharing' statistical benefit of finite networks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]