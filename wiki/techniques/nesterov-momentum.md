---
aliases: []
also_type: []
applies:
- convex-optimization
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
- optimization
extends:
- sgd-momentum
id: pkis:technique:nesterov-momentum
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
tags:
- momentum
- accelerated-gradient
- convex-optimization
- deep-learning
title: Nesterov Momentum
understanding: 0
---

## Definition
Nesterov momentum (Sutskever et al., 2013, adapting Nesterov 1983) evaluates the gradient at a *lookahead* point:
$$\mathbf{v} \leftarrow \alpha\mathbf{v} - \epsilon\nabla_{\theta}\hat{J}(\theta + \alpha\mathbf{v}), \qquad \theta \leftarrow \theta + \mathbf{v}.$$
In the convex batch setting this reduces excess error from $O(1/k)$ to $O(1/k^2)$; in the stochastic setting the improvement in rate does not hold but practical benefits are often observed.

Intuition: rather than computing the gradient where the particle currently is, compute it where it *will be* after the momentum step — a correction factor that anticipates overshooting.

### Why it matters
Nesterov momentum is theoretically optimal among first-order methods for smooth convex functions. Although the rate improvement vanishes in the stochastic regime, it often gives better empirical performance than standard momentum and is widely used as the momentum component inside adaptive optimizers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[convex-optimization]] — applies: achieves optimal O(1/k^2) rate for smooth convex functions
- [[sgd-momentum]] — extends
[To be populated during integration]