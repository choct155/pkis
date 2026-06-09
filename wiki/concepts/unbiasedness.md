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
id: pkis:concept:unbiasedness
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch04
tags:
- point-estimation
- bias-variance
- sampling-theory
- frequentist
title: Unbiasedness
understanding: 0
---

## Definition
A point estimate omega-hat(y) is unbiased if its expectation over the sampling distribution equals the true parameter for every parameter value: E(omega-hat(y)|omega) = omega for all omega. Unbiasedness is a central organizing principle of classical sampling-theory estimation, but from a Bayesian standpoint it is reasonable only in the large-sample limit and is otherwise potentially misleading. Three difficulties recur. (1) Estimating many related parameters: requiring each estimate to be unbiased forces relevant cross-parameter information to be discarded, and minimizing bias often inflates variance counterproductively (e.g. unbiased estimates of individual omega_j yield an upwardly biased estimate of their variance; hierarchical shrinkage estimators are biased but have lower mean squared error). (2) Prediction problems: the posterior-mean predictor is biased under repeated sampling of the predictor (regression to the mean), and the unbiased alternative over-extrapolates absurdly, so unbiasedness requires an artificial dichotomy between 'parameters' and 'predictions' with no clear substantive basis. (3) Proper-prior posterior means cannot be unbiased except in degenerate problems. Gelman's position is that unbiasedness is a poor target in itself; the goal is good calibrated inference (low mean squared error, correct coverage), to which a modest bias is often a worthwhile price.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]