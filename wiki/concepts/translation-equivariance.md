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
- deep-learning
- mathematics
id: pkis:concept:translation-equivariance
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- equivariance
- invariance
- CNN
- symmetry
- group theory
title: Translation Equivariance
understanding: 0
---

## Definition
A function $f$ is **equivariant** to a transformation $g$ if $f(g(x)) = g(f(x))$. For convolution, equivariance to translation means: if the input is shifted by $(\delta_i, \delta_j)$, the feature map shifts by the same amount.

Formally, let $T_\delta$ denote a translation operator; then $(T_\delta I * K) = T_\delta(I * K)$.

### Why it matters
Equivariance preserves spatial structure through the network, enabling each layer to detect where a feature occurs rather than merely whether it occurs. Pooling converts this equivariance into approximate *invariance*, discarding fine-grained position information when that is beneficial.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]