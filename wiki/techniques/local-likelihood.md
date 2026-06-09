---
aliases: []
also_type: []
applies:
- generalized-linear-models
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
extends:
- local-regression-loess
id: pkis:technique:local-likelihood
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch06
specializes:
- logistic-regression
tags:
- nonparametric
- local-likelihood
- varying-coefficient
- generalized-linear-models
- local-logistic-regression
title: Local Likelihood and Varying-Coefficient Models
understanding: 0
uses:
- maximum-likelihood-estimation
---

## Definition
A general principle for localizing any parametric model whose fitting accommodates observation weights: replace the global log-likelihood l(beta) = sum_i l(y_i, x_i^T beta) by a kernel-weighted LOCAL log-likelihood centered at x_0, l(beta(x_0)) = sum_i K_lambda(x_0,x_i) l(y_i, x_i^T beta(x_0)) (ESL 6.16), so a globally linear model becomes locally linear. Applied to generalized linear models (logistic, log-linear) it yields local logistic / local GLM fits; e.g. the local multiclass logistic model centers the regression at x_0 so fitted posterior probabilities read directly off the local intercepts. A key special case is the VARYING-COEFFICIENT MODEL: split predictors into (X_1..X_q) entering linearly and Z entering the coefficients, f(X) = alpha(Z) + sum_j beta_j(Z) X_j, fit by locally weighted least squares K_lambda(z_0, z_i); the coefficients themselves vary smoothly with the conditioning variables Z. The same device localizes autoregressive time-series models (coefficients vary with recent history rather than by windowing time). Because it inherits local regression's first-order bias correction, operating on the unrestricted (e.g. logit) scale gives better bias behavior than directly smoothing a binary response (which is merely a locally-constant logit fit). Provides pointwise standard-error bands. Closely related to generalized additive models, which avoid the dimensionality penalty by imposing additive structure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logistic-regression]] — specializes
- [[generalized-linear-models]] — applies
- [[maximum-likelihood-estimation]] — uses
- [[local-regression-loess]] — extends
[To be populated during integration]