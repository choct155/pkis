---
aliases: []
also_type: []
analogous-to:
- phase-transition
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- vanishing-exploding-gradients
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- optimization
- non-convex-optimization
id: pkis:concept:saddle-points-nn-optimization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
tags:
- critical-points
- non-convex
- deep-learning
- hessian
title: Saddle Points in Neural Network Optimization
understanding: 0
uses:
- hessian-matrix
---

## Definition
A saddle point $\theta^*$ satisfies $\nabla J(\theta^*)=0$ but has a Hessian with both positive and negative eigenvalues. For high-dimensional random functions of the type encountered in deep learning, the fraction of critical points that are saddle points (rather than local minima) grows exponentially with dimensionality. Moreover, critical points at *high* cost are almost all saddle points; local minima concentrate near the global minimum.

Formally, for a function $f:\mathbb{R}^n\to\mathbb{R}$, the expected ratio of saddle points to local minima scales as $e^{\Omega(n)}$ (Dauphin et al., 2014).

Intuition: flipping a coin $n$ times and requiring all heads (all positive Hessian eigenvalues) becomes exponentially unlikely as $n$ grows.

### Why it matters
Saddle points explain why second-order methods like Newton's method often fail for deep networks — they jump toward saddle points rather than minima. First-order methods (SGD) empirically escape saddle points because continuous-time gradient descent is repelled from them. The saddle-free Newton method (Dauphin et al., 2014) modifies Newton's update to step away from saddle points by using $|\mathbf{H}|^{-1}\mathbf{g}$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[phase-transition]] — analogous-to: ratio of saddle points to minima undergoes sharp transition with dimension
- [[hessian-matrix]] — uses
- [[vanishing-exploding-gradients]] — contrasts-with: saddle points have zero gradient but non-zero curvature; vanishing gradient is a separate phenomenon
[To be populated during integration]