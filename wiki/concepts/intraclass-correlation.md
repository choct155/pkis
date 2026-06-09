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
id: pkis:concept:intraclass-correlation
instantiates:
- multilevel-regression
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch15
tags:
- multilevel-models
- covariance
title: Intraclass Correlation
understanding: 0
---

## Definition
The correlation between outcomes on two units belonging to the same group, induced by a shared group-level random effect. For a varying-coefficients model in which group means have population variance sigma_beta^2 on top of within-group variance sigma^2, marginalizing over the group effects gives total variance eta^2 = sigma^2 + sigma_beta^2 and intraclass correlation rho = sigma_beta^2 / (sigma^2 + sigma_beta^2). Thus any positive within-group (intraclass) correlation in a linear regression can be subsumed into a varying-coefficients model by adding group-indicator variables whose coefficients share an exchangeable population distribution. Intraclass correlation is the formal reason the lowest-level exchangeability assumption fails when data are grouped, and why ignoring grouping (as a pooled OLS fit does) yields falsely precise inferences.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[multilevel-regression]] — instantiates: within-group correlation is induced by a shared group-level random effect
[To be populated during integration]