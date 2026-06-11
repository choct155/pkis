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
id: pkis:technique:line-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- step-size
- Armijo
- Wolfe
- backtracking
- gradient-descent
title: Line Search (Exact and Armijo Backtracking)
understanding: 0
---

## Definition
**Line search** selects a step size $\eta_t$ by (approximately) solving the one-dimensional sub-problem along a descent direction $d_t$:

$$\eta_t = \arg\min_{\eta > 0} \mathcal{L}(\theta_t + \eta\, d_t)$$

**Exact line search** solves this precisely; for a quadratic objective it gives the closed form $\eta = -d^T(A\theta + b)/(d^T A d)$. **Armijo (backtracking) line search** starts from a candidate step and repeatedly shrinks it by factor $c \in (0,1)$ until the sufficient-decrease (Armijo-Goldstein) condition is met:

$$\mathcal{L}(\theta_t + \eta\, d_t) \leq \mathcal{L}(\theta_t) + c\,\eta\, d_t^T \nabla\mathcal{L}(\theta_t)$$

typically with $c = 10^{-4}$. The **Wolfe conditions** additionally require a curvature condition to keep the Hessian approximation positive-definite in quasi-Newton methods.

### Why it matters
Line search converts the free hyper-parameter of step size into an automatic, locally optimal choice. Combined with Newton or quasi-Newton directions it provides robust, globally-convergent algorithms without manual learning-rate tuning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]