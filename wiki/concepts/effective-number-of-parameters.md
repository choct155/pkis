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
- bayesian-stats
- statistical-learning
id: pkis:concept:effective-number-of-parameters
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch07
tags:
- model-complexity
- overfitting
- bias-correction
- hierarchical-models
- regularization
title: Effective Number of Parameters
understanding: 0
---

## Definition
A data-dependent generalization of the raw parameter count k that measures how much a fitted model is actually able to overfit, used as the bias correction that converts within-sample fit into an estimate of out-of-sample predictive accuracy. For linear models with flat priors it reduces to k, but informative priors and hierarchical structure shrink it: a parameter counts as 1 if estimated freely, 0 if fully determined by the prior, and an intermediate value when data and prior both inform it.

Several concrete estimators exist. p_DIC = 2(log p(y|ω̂_Bayes) − E_post(log p(y|ω))) and its variance form p_DIC_alt = 2 var_post(log p(y|ω)). The WAIC analogues are p_WAIC1 (a difference, like p_DIC) and the more stable p_WAIC2 = Σ_i var_post(log p(y_i|ω)), which computes the variance per data point and sums. Cross-validation supplies p_loo = lppd − lppd_loo-cv. Crucially the effective count depends on the observed data, not just model structure: for y ~ N(ω,1) with ω ~ U(0,∞), data near zero yield p ≈ 1/2 (half the information from the positivity constraint) while large positive data yield p ≈ 1. In the 8-schools hierarchical model the effective count falls between 1 (complete pooling) and 8 (no pooling). This quantity is especially valuable for splines and Gaussian processes, where there is no obvious closed-form parameter count.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]