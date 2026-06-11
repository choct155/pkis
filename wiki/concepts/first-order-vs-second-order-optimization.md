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
- optimization
- machine-learning
generalizes:
- gradient-descent
- newtons-method-optimization
id: pkis:concept:first-order-vs-second-order-optimization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
tags:
- gradient-descent
- Newton
- curvature
- SGD
- adaptive-learning-rate
title: First-Order vs Second-Order Optimization
understanding: 0
uses:
- hessian-matrix
---

## Definition
Optimization algorithms are classified by the order of derivative information they use:

- **First-order methods** use only the gradient $\nabla f$; examples: gradient descent, SGD, Adam.
- **Second-order methods** additionally use (or approximate) the Hessian $\mathbf{H}$; examples: Newton's method, L-BFGS, natural gradient.

For a gradient descent step $\mathbf{x}' = \mathbf{x} - \epsilon\mathbf{g}$, the second-order Taylor approximation of the cost change is

$$\Delta f \approx -\epsilon\,\mathbf{g}^\top\mathbf{g} + \tfrac{1}{2}\epsilon^2\,\mathbf{g}^\top\mathbf{H}\mathbf{g},$$

showing how curvature ($\mathbf{g}^\top\mathbf{H}\mathbf{g}$) degrades first-order steps.

### Why it matters
Most large-scale deep learning uses first-order methods because Hessian storage and inversion are $O(n^2)$/$O(n^3)$. Understanding the divide motivates quasi-Newton approximations, adaptive learning-rate methods (which implicitly approximate curvature), and analysis of convergence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hessian-matrix]] — uses
- [[newtons-method-optimization]] — generalizes
- [[gradient-descent]] — generalizes
[To be populated during integration]