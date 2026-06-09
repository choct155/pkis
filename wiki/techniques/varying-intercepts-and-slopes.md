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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:varying-intercepts-and-slopes
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch15
tags:
- regression
- multilevel-models
- covariance
title: Varying-Intercept, Varying-Slope Models
understanding: 0
---

## Definition
A multilevel regression in which more than one coefficient varies by group: each group j has its own intercept alpha_j and slope(s) beta_j, modeled jointly as draws from a multivariate normal population distribution, (alpha_j, beta_j) ~ N(mu, Sigma_beta). The group-level covariance matrix Sigma_beta captures both the across-group variance of each coefficient and the correlation between intercepts and slopes, so a non-diagonal Sigma_beta is what distinguishes this from independent varying-intercept and varying-slope models. The key modeling object is the prior on Sigma_beta; the conditionally conjugate choice is inverse-Wishart, but the standard Inv-Wishart_{K+1}(I) over-constrains the variances, motivating the redundant 'scaled inverse-Wishart' parameterization Sigma_beta = Diag(xi) Sigma_eta Diag(xi) that decouples scales (xi) from correlations (Sigma_eta). This technique is essential when group-level data are sparse: separate per-group least-squares fits are impossible (e.g., the business-school GMAT example with 8 coefficients per school and very few black students per school), but partial pooling through Sigma_beta estimates all coefficients simultaneously.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]