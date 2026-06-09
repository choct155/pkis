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
id: pkis:concept:lagrangian-duality
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch07
tags: []
title: Lagrangian Duality
understanding: 0
---

## Definition
$$\min_{x} \max_{\lambda \ge 0} \mathcal{L}(x,\lambda) \;\ge\; \max_{\lambda \ge 0} \underbrace{\min_{x} \mathcal{L}(x,\lambda)}_{\mathcal{D}(\lambda)}$$

Duality converts an optimization in the primal variables $x$ into one in dual variables $\lambda$ (the Lagrange multipliers), exchanging a constrained problem for an unconstrained inner minimization.

### Primal and dual problems
The primal is $\min_x f(x)$ s.t. $g_i(x) \le 0$. Its Lagrangian dual is $\max_{\lambda \ge 0} \mathcal{D}(\lambda)$ with dual function $\mathcal{D}(\lambda) = \min_x \mathcal{L}(x,\lambda)$. Crucially, $\mathcal{D}(\lambda)$ is **concave** (a pointwise min of functions affine in $\lambda$) even when $f$ and the $g_i$ are nonconvex, so the outer maximization is always tractable.

### Weak vs. strong duality
The minimax inequality $\max_y \min_x \varphi \le \min_x \max_y \varphi$ gives **weak duality**: the dual optimum lower-bounds the primal optimum (the duality gap is $\ge 0$). When the problem is convex (convex $f$, $g_i$; convex feasible set), **strong duality** holds and the gap closes: dual and primal optima coincide.

### Why it matters
Duality lets us solve whichever of the primal ($d$ variables) or dual ($m$ variables, one per constraint) is smaller, and the dual is often unconstrained-per-$\lambda$ and concave. It underpins the SVM dual, kernel methods, and constrained statistical estimation, and connects to the Legendre-Fenchel (convex-conjugate) route to duality.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]