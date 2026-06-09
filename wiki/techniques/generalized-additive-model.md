---
aliases: []
also_type: []
applies:
- basis-function-models
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
generalizes:
- generalized-linear-models
id: pkis:technique:generalized-additive-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch09
specializes:
- supervised-learning
tags:
- nonparametric-regression
- interpretability
- smoothing
title: Generalized Additive Model (GAM)
understanding: 0
uses:
- backfitting-algorithm
- generalized-linear-models
---

## Definition
A generalized additive model relates the conditional mean of a response to an additive sum of unspecified smooth functions of the individual predictors through a link function g: g[E(Y|X)] = alpha + f_1(X_1) + ... + f_p(X_p). It generalizes the generalized linear model by replacing each linear term beta_j X_j with a flexible nonparametric function f_j (e.g. a cubic smoothing spline or kernel smoother), retaining additivity so the marginal effect of each predictor remains interpretable while finessing the curse of dimensionality. The link function g (identity for Gaussian, logit/probit for binomial, log for Poisson) carries over from the exponential-family GLM family. Each f_j is identified up to a constant, so the standard convention is sum_i f_j(x_ij)=0 for all j with alpha=ave(y_i). The penalized residual sum of squares PRSS = sum_i (y_i - alpha - sum_j f_j(x_ij))^2 + sum_j lambda_j integral f_j''(t)^2 dt is minimized by an additive cubic-spline model; the smoothness of each term is controlled by lambda_j (equivalently a target degrees of freedom df_j = trace[S_j]-1, with df_j=1 recovering a linear term). Functions are estimated by the backfitting algorithm; for non-Gaussian responses backfitting is nested inside a local-scoring / IRLS Newton-Raphson loop maximizing a penalized log-likelihood. Limitations for large data mining: backfitting fits all predictors (no built-in selection; cf. BRUTO, COSSO, SpAM, or boosting), and interactions must be added manually or via MARS.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[basis-function-models]] — applies
- [[supervised-learning]] — specializes
- [[generalized-linear-models]] — uses
- [[backfitting-algorithm]] — uses
- [[generalized-linear-models]] — generalizes
[To be populated during integration]