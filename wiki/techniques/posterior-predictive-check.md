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
contrasts-with:
- cross-validation
- likelihood-principle
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
generalizes:
- hypothesis-testing
id: pkis:technique:posterior-predictive-check
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-linear-regression
related_concepts: []
sources:
- gelman-bda3-ch06
- gelman-bda3-ch14
tags:
- posterior-predictive
- model-checking
- goodness-of-fit
- simulation
- self-consistency
- bayesian-stats
title: Posterior Predictive Check
understanding: 0
uses:
- posterior-predictive-distribution
- test-quantity-discrepancy
- bayesian-p-value
- monte-carlo-estimator
---

## Definition
A model check that draws simulated datasets from the posterior predictive distribution and compares them to the observed data; any systematic difference between simulations and data signals a potential model failure. It is fundamentally a self-consistency check: if the model fits, the observed data should look plausible among replications, so an observed discrepancy is due either to model misfit or to chance. The procedure: choose a test quantity T(y) or T(y,θ) and a replication scheme y_rep (deciding which aspects of the data, if any, to condition on), then for each posterior draw θ^s compute realized T(y,θ^s) and predictive T(y_rep^s, θ^s); the estimated Bayesian p-value is the proportion of draws with T(y_rep^s,θ^s) ≥ T(y,θ^s). Unlike classical testing it needs no special handling of nuisance parameters — averaging over the posterior implicitly integrates them out — and requires no pivotal quantities or asymptotics. A poorly chosen test quantity (e.g. a sufficient statistic like the sample variance under a noninformative prior) yields a p-value near ½ by construction and detects nothing; good test quantities target features not directly fitted by the model. Marginal and cross-validation variants compare each p(y_rep_i | y) (or p(y_rep_i | y_−i)) separately to find outliers and check calibration.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-linear-regression]] — prerequisite-of
- [[likelihood-principle]] — contrasts-with: inference obeys the likelihood principle but checking depends on the sampling/stopping rule
- [[cross-validation]] — contrasts-with: cross-validation predictive checks compare each point to inference from all others
- [[monte-carlo-estimator]] — uses: p_B estimated as the proportion of joint draws with T(y_rep)>=T(y)
- [[hypothesis-testing]] — generalizes: averages over the posterior of theta instead of fixing it at an estimate
- [[bayesian-p-value]] — uses: summarizes the discrepancy as a posterior predictive p-value
- [[test-quantity-discrepancy]] — uses: compares realized vs replicated test quantities
- [[posterior-predictive-distribution]] — uses: draws replicated data from p(y_rep|y)
[To be populated during integration]