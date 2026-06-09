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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- statistical-learning
id: pkis:concept:convex-conjugate
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch07
tags: []
title: Convex Conjugate (Legendre-Fenchel Transform)
understanding: 0
---

## Definition
$$f^*(s) = \sup_{x \in \mathbb{R}^D} \big(\langle s, x\rangle - f(x)\big)$$

The convex conjugate re-describes a function in terms of the slopes $s = \nabla_x f(x)$ of its supporting hyperplanes (tangents) rather than its input $x$.

### Geometric meaning
A convex set is fully described by its supporting hyperplanes; filling a convex function gives the convex epigraph, so a convex function is equally describable by its tangents. For each slope $s$, $f^*(s)$ records (the negative of) the $y$-intercept of the supporting line of that slope. The definition needs neither convexity nor differentiability of $f$, because the supremum picks out the tightest supporting hyperplane.

### Properties
For a convex differentiable $f$ the supremum is attained uniquely and the transform is involutive: $f^{**} = f$. Slopes are exchanged with arguments (the slope of $f^*$ at $s$ is the $x$ achieving the sup). The conjugate of a separable sum is the sum of conjugates: $L(t) = \sum_i \ell_i(t_i) \Rightarrow L^*(z) = \sum_i \ell_i^*(z_i)$.

### Duality via conjugates
The transform yields dual problems directly. For convex $f, g$ with $Ax = y$, $\min_x f(Ax) + g(x) = \max_u -f^*(u) - g^*(-A^\top u)$, a second route to duality alongside Lagrangian duality.

### Why it matters
Conjugate losses give a convenient, modular way to derive dual problems for ML objectives that are convex sums over examples (e.g. smoothing the SVM hinge loss for L-BFGS), and the transform is the same duality that appears in maximum-entropy / exponential-family estimation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]