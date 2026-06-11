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
generalizes:
- relu
id: pkis:concept:maxout-unit
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
specializes:
- activation-functions
tags:
- activation-function
- piecewise-linear
- learnable-activation
- regularization
title: Maxout Unit
understanding: 0
uses:
- depth-efficiency-rectifier-networks
---

## Definition
A maxout unit divides its pre-activation vector $\mathbf{z}$ into groups of $k$ values and outputs the maximum within each group: $$g(\mathbf{z})_i = \max_{j \in G^{(i)}} z_j,$$ where $G^{(i)} = \{(i-1)k+1,\ldots,ik\}$. Each maxout unit is parametrized by $k$ weight vectors, making it a learnable piecewise-linear convex function with up to $k$ pieces.

Maxout units learn the activation function itself rather than fixing it a priori.

### Why it matters
A single maxout unit can implement ReLU, leaky ReLU, or absolute-value rectification as special cases, or discover a completely different piecewise-linear response. The redundancy across $k$ filters provides robustness to catastrophic forgetting. The cost is $k$-fold parameter increase, requiring stronger regularization or large datasets. Maxout networks also achieve the exponential-in-depth linear region count proven by Montufar et al. (2014).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[depth-efficiency-rectifier-networks]] — uses
- [[activation-functions]] — specializes
- [[relu]] — generalizes
[To be populated during integration]