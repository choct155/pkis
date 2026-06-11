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
- optimization
id: pkis:technique:minibatch-sgd
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
- goodfellow-deeplearning-ch08
tags:
- SGD
- gradient-descent
- minibatch
- scalability
- optimization
- deep-learning
title: Minibatch Stochastic Gradient Descent
understanding: 0
---

## Definition
**Minibatch SGD** approximates the full gradient of an additive loss $J(\boldsymbol{\theta})=\frac{1}{m}\sum_i L(\mathbf{x}^{(i)},y^{(i)},\boldsymbol{\theta})$ using a randomly sampled subset (minibatch) $\mathcal{B}$ of size $m'\ll m$:

$$\mathbf{g} = \frac{1}{m'}\sum_{i\in\mathcal{B}}\nabla_{\boldsymbol{\theta}}L(\mathbf{x}^{(i)},y^{(i)},\boldsymbol{\theta}), \qquad \boldsymbol{\theta}\leftarrow \boldsymbol{\theta}-\epsilon\,\mathbf{g}.$$

The key insight: the gradient is an expectation, so a small sample provides an unbiased (noisy) estimate. Per-update cost is $O(m')$ regardless of $m$, giving asymptotically $O(1)$ training cost.

### Why it matters
Minibatch SGD is the engine of virtually all modern deep learning. It scales to datasets with billions of examples where full-batch gradient descent is computationally infeasible, and its inherent noise can help escape sharp local minima. Practical choices of $m'$ (32–512) balance gradient variance against hardware parallelism.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]