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
id: pkis:concept:missing-data-mechanisms
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch08
specializes:
- data-collection-mechanism
tags:
- missing-data
- nonresponse
- imputation
- data-collection
title: Missing-Data Mechanisms (MCAR / MAR / MNAR)
understanding: 0
---

## Definition
A taxonomy (Rubin 1976) classifying *why* data are missing, in terms of how the observation indicator I depends on the complete data y = (y_obs, y_mis). **Missing completely at random (MCAR):** missingness is independent of both observed and missing values, p(I | y, phi) = p(I | phi) — e.g. a scale that drops a reading with fixed probability 0.1; here the realized sample size, though random, carries no information about the estimand (given distinct parameters). **Missing at random (MAR):** given fully observed covariates x and the observed responses, missingness does not further depend on the missing values, p(I | x, y, phi) = p(I | x, y_obs, phi) — e.g. auditing all tax returns declaring income over $1M, a deterministic rule depending only on an observed covariate. **Missing not at random (MNAR) / nonignorable:** missingness depends on the unobserved values themselves, e.g. censoring at an unknown threshold, where the proportion observed informs the threshold and induces posterior dependence between omega and phi. The Gelman example weighs an object N times and observes 91 values under each mechanism, showing the *same* observed numbers yield *different* posteriors depending on the mechanism: MCAR/MAR give p(omega) proportional to N(omega | ybar_obs, 1/91), while censoring multiplies by [Phi(omega - phi)]^9 and is nonignorable. MAR plus distinct parameters implies ignorability, so the missing-data mechanism need not be modeled; MNAR forces an explicit model for p(I | y, phi) in the likelihood. The framework subsumes survey nonresponse, experimental dropout, noncompliance, censoring, truncation, and rounding as instances of partially observed data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[data-collection-mechanism]] — specializes: MCAR/MAR/MNAR classify the inclusion model in missing-data settings
[To be populated during integration]