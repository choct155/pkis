---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- bayesian-statistics
id: pkis:result:bayesian-linear-regression-predictive
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
tags:
- predictive-distribution
- uncertainty-quantification
- gaussian
- bayesian-regression
title: Bayesian Linear Regression Predictive Distribution
understanding: 0
---

## Definition
After integrating out the weight vector $\mathbf{w}$, the predictive distribution for a new input $x$ in a Bayesian linear basis function model is Gaussian:

$$p(t|x,\mathbf{t},\alpha,\beta) = \mathcal{N}(t|\mathbf{m}_N^T\boldsymbol{\phi}(x),\,\sigma_N^2(x))$$

$$\sigma_N^2(x) = \frac{1}{\beta} + \boldsymbol{\phi}(x)^T \mathbf{S}_N \boldsymbol{\phi}(x)$$

The first term is aleatoric (irreducible noise), the second is epistemic (parameter uncertainty). The predictive variance satisfies $\sigma_{N+1}^2(x) \le \sigma_N^2(x)$, so uncertainty monotonically decreases as data accumulate.

### Why it matters
Provides principled, input-dependent uncertainty estimates without held-out data or Monte Carlo sampling. Serves as the template for Gaussian process regression and motivates the *equivalent kernel* interpretation of linear smoothers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]