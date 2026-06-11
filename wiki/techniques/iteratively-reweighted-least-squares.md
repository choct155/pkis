---
aliases: []
also_type: []
applies:
- logistic-regression
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
- optimization
- bayesian-stats
generalizes:
- linear-regression
id: pkis:technique:iteratively-reweighted-least-squares
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch04
tags:
- maximum-likelihood
- newton-raphson
- logistic-regression
- glm
- weighted-least-squares
title: Iteratively Reweighted Least Squares
understanding: 0
uses:
- maximum-likelihood-estimation
- hessian-matrix
- glm-gradient-hessian
- convex-optimization
---

## Definition
An algorithm for maximum-likelihood fitting of logistic regression (and GLMs generally) that re-expresses each Newton-Raphson step as a weighted least squares solve. For logistic regression the score equations sum_i x_i (y_i - p(x_i; beta)) = 0 are nonlinear in beta; the Newton step uses the Hessian -X^T W X, where W is the diagonal matrix of weights p_i(1-p_i). The update beta_new = (X^T W X)^{-1} X^T W z, with adjusted (working) response z = X beta_old + W^{-1}(y - p), is exactly the solution of the weighted least squares problem beta_new <- argmin_beta (z - X beta)^T W (z - X beta). Because p, W, and z all depend on the current beta, the weighted regression is solved repeatedly until convergence — hence 'iteratively reweighted.' Starting at beta = 0 usually works; since the log-likelihood is concave the procedure typically converges, with step-size halving guaranteeing convergence in the rare cases it decreases. The MLE thus satisfies a self-consistency relation as the fixed point of the weighted regression, connecting logistic-regression inference (Pearson chi-square, asymptotic normality N(beta, (X^T W X)^{-1}), Rao score and Wald tests) directly to ordinary least-squares machinery.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[convex-optimization]] — uses
- [[linear-regression]] — generalizes
- [[glm-gradient-hessian]] — uses
- [[generalized-linear-models]] — applies: IRLS is the general fitting procedure for the GLM family, of which logistic regression is a member
- [[hessian-matrix]] — uses: Newton step uses the log-likelihood Hessian -X^T W X
- [[maximum-likelihood-estimation]] — uses: solves the ML score equations via repeated Newton steps
- [[logistic-regression]] — applies: IRLS is the standard maximum-likelihood fitting algorithm for logistic regression
[To be populated during integration]