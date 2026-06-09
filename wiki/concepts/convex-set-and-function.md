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
id: pkis:concept:convex-set-and-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch07
tags: []
title: Convex Sets and Convex Functions
understanding: 0
---

## Definition
$$\theta x + (1-\theta)y \in C, \qquad f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y), \quad \theta \in [0,1]$$

A set is convex if the straight line between any two of its points lies inside it; a function is convex if the chord between any two points on its graph lies above the graph.

### Geometric intuition
Convex sets contain every segment joining their members. A convex function is a "bowl": pouring water in fills its **epigraph**, which is itself a convex set. This bridge between convex functions and convex sets underlies duality theory (supporting hyperplanes describe both).

### Differentiable characterizations
If $f$ is differentiable, it is convex iff its graph lies above every tangent: $f(y) \ge f(x) + \nabla_x f(x)^\top (y - x)$. If $f$ is twice differentiable, it is convex iff its Hessian $\nabla_x^2 f(x)$ is positive semidefinite everywhere on its (convex) domain. A concave function is the negative of a convex one.

### Convexity-preserving operations
Rather than verify the definition from scratch, one checks convexity via closure operations: a nonnegative scalar multiple $\alpha f$ ($\alpha \ge 0$) is convex, and a sum $f_1 + f_2$ of convex functions is convex; hence any nonnegative weighted sum $\sum_i \alpha_i f_i$ is convex. (The defining chord inequality is itself a form of Jensen's inequality.)

### Why it matters
Convexity is the property that makes optimization tractable and reliable: for a convex objective over a convex feasible set, every local minimum is global. Recognizing or engineering convexity in an ML objective guarantees that an optimizer reaches the true optimum.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]