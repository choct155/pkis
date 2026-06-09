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
id: pkis:concept:deviance-information-criterion
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch07
tags:
- information-criteria
- model-comparison
- predictive-accuracy
- deviance
- posterior-mean
- bias-correction
title: Deviance Information Criterion (DIC)
understanding: 0
---

## Definition
A partially Bayesian information criterion that modifies AIC in two ways: it replaces the maximum likelihood estimate with the posterior mean ω̂_Bayes = E(ω|y), and replaces the raw parameter count k with a data-based effective number of parameters p_DIC = 2(log p(y|ω̂_Bayes) − E_post(log p(y|ω))). The predictive accuracy estimate is elpd_DIC = log p(y|ω̂_Bayes) − p_DIC, reported as DIC = −2 log p(y|ω̂_Bayes) + 2 p_DIC on the deviance scale.

DIC became popular because p_DIC has an easy, stable Monte Carlo estimate from posterior draws and the criterion reduces to k for linear models with uniform priors. Its weaknesses, however, motivate WAIC: because it conditions on the posterior mean rather than averaging over the posterior, it can give nonsensical results when the posterior is poorly summarized by its mean (p_DIC can even go negative when the mean is far from the mode), and it relies on plug-in / regular-model assumptions that fail for singular models. It is asymptotically equal to leave-one-out cross-validation using plug-in predictive densities.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]