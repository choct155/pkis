---
aliases: []
also_type: []
applies:
- logistic-regression
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
- machine-learning
extends:
- newtons-method-optimization
id: pkis:technique:bfgs-lbfgs
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- quasi-Newton
- second-order
- large-scale
- inverse-Hessian
- L-BFGS
title: BFGS and L-BFGS (Quasi-Newton Methods)
understanding: 0
uses:
- line-search
- low-rank-approximation
---

## Definition
**BFGS** (Broyden-Fletcher-Goldfarb-Shanno) is a quasi-Newton method that iteratively builds a rank-2 positive-definite approximation $B_t \approx H_t$ (or its inverse $C_t \approx H_t^{-1}$) using gradient-difference information:

$$B_{t+1} = B_t + \frac{y_t y_t^T}{y_t^T s_t} - \frac{(B_t s_t)(B_t s_t)^T}{s_t^T B_t s_t}$$

where $s_t = \theta_t - \theta_{t-1}$ and $y_t = g_t - g_{t-1}$. The Wolfe conditions on the step size preserve positive-definiteness of $B_t$. **L-BFGS** (limited-memory BFGS) stores only the $M$ most recent $(s_t, y_t)$ pairs ($M = 5$–$20$), reducing storage from $O(D^2)$ to $O(MD)$ and making it practical for large-scale problems.

### Why it matters
L-BFGS is the de-facto standard second-order optimizer for batch ML problems (e.g., the default solver in scikit-learn's logistic regression). It achieves super-linear convergence near optima without requiring explicit Hessian computation or storage.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logistic-regression]] — applies
- [[low-rank-approximation]] — uses
- [[line-search]] — uses
- [[newtons-method-optimization]] — extends
[To be populated during integration]