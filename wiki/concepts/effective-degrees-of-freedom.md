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
- statistical-learning
id: pkis:concept:effective-degrees-of-freedom
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch03
tags:
- model-complexity
- shrinkage
- regression
- model-selection
- bias-variance
title: Effective Degrees of Freedom
understanding: 0
---

## Definition
A general measure of the complexity of a fitted model, defined for a fitted vector yhat = (yhat_1,...,yhat_N) by df(yhat) = (1/sigma^2) * sum_{i=1}^N Cov(yhat_i, y_i): the harder a procedure fits the training data, the larger the sampling covariance between each prediction and its own outcome, and hence the more degrees of freedom it consumes. The definition generalizes the classical count of linearly independent parameters and applies to adaptively fitted models. For a linear fit yhat = H y it equals tr(H); a k-predictor linear regression with fixed predictors has df = k. For ridge regression it has the closed form df(lambda) = tr[X(X^T X + lambda I)^{-1} X^T] = sum_j d_j^2/(d_j^2 + lambda), a monotone decreasing function of lambda equal to p at lambda = 0 and approaching 0 as lambda -> infinity. For best-subset selection of size k the effective df exceeds k (the search 'uses up' extra freedom) and has no closed form, so it must be estimated by simulation. Strikingly, after the kth step of the LAR algorithm the effective degrees of freedom is exactly k. The notion underlies fair comparison of prediction-error estimates across procedures of differing complexity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]