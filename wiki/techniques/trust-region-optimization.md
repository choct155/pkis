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
- optimization
id: pkis:technique:trust-region-optimization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- second-order
- non-convex
- Tikhonov-damping
- Newton
- regularization
title: Trust-Region Optimization
understanding: 0
---

## Definition
**Trust-region methods** restrict each iterate to a ball $\mathcal{R}_t = \{\delta : \|\delta\|_2 \leq r\}$ within which a quadratic model $M_t$ is trusted:

$$\delta^* = \arg\min_{\delta \in \mathcal{R}_t} M_t(\delta), \quad M_t(\delta) = L(\theta_t) + g_t^T\delta + \tfrac{1}{2}\delta^T H_t \delta$$

Converting via a Lagrange multiplier $\lambda > 0$ (Tikhonov damping) gives:

$$\delta^* = -(H_t + \lambda I)^{-1} g_t$$

Choosing $\lambda$ large enough makes $H_t + \lambda I$ positive-definite even when $H_t$ has negative eigenvalues. As $\lambda \to 0$ the method reduces to Newton's method; large $\lambda$ gives gradient descent with small step.

### Why it matters
Trust-region methods handle non-convex objectives (where Newton's method may ascend) by automatically damping ill-conditioned or indefinite Hessians. Tikhonov damping is also directly connected to $\ell_2$ regularization, bridging optimization and statistics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]