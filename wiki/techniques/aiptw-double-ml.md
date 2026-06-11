---
aliases: []
also_type: []
applies:
- average-treatment-effect
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
- causal-inference
- statistics
- machine-learning
extends:
- iptw-estimator
- g-computation
id: pkis:technique:aiptw-double-ml
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- doubly-robust
- semiparametric-efficiency
- influence-function
- nuisance
- causal-estimation
title: Augmented IPTW / Double Machine Learning Estimator (AIPTW)
understanding: 0
uses:
- cross-fitting
---

## Definition
The **AIPTW** (augmented inverse probability of treatment weighted) estimator combines an outcome model $\hat{Q}(a,x)$ and a propensity model $\hat{g}(x)$ via the **influence function**
$$\phi(X_i,A_i,Y_i;Q,g,\tau) \triangleq Q(1,X_i)-Q(0,X_i) + \frac{A_i(Y_i-Q(1,X_i))}{g(X_i)} - \frac{(1-A_i)(Y_i-Q(0,X_i))}{1-g(X_i)} - \tau,$$
yielding
$$\hat{\tau}^{\text{AIPTW}} = \frac{1}{n}\sum_i \phi(X_i;\hat{Q},\hat{g},0) + \tau.$$

Key properties:
1. **Doubly robust**: consistent if *either* $\hat{Q}$ or $\hat{g}$ is consistent.
2. **Semi-parametrically efficient**: achieves the non-parametric Cramér–Rao lower bound $\mathrm{Var}[\phi]$.
3. **Double robustness rate**: achieves $\sqrt{n}$-consistent inference for $\tau$ as long as $\|\hat{Q}-Q\|_2 \cdot \|\hat{g}-g\|_2 = o(n^{-1/2})$, permitting each nuisance function to converge at the slower $n^{-1/4}$ rate.

### Why it matters
IPTW and outcome regression each require one nuisance function to be accurately estimated. AIPTW requires only their *product* of errors to be small, enabling the use of flexible ML models (neural nets, forests) for nuisance estimation while still achieving $\sqrt{n}$ convergence and valid confidence intervals for the low-dimensional causal parameter $\tau$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cross-fitting]] — uses: Cross-fitting eliminates the empirical-process bias term in AIPTW
- [[average-treatment-effect]] — applies
- [[g-computation]] — extends: AIPTW adds a propensity-score stabilisation to outcome regression
- [[iptw-estimator]] — extends: AIPTW augments IPTW with an outcome model correction term
[To be populated during integration]