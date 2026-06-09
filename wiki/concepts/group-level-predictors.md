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
id: pkis:concept:group-level-predictors
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch15
tags:
- regression
- multilevel-models
title: Group-Level Predictors
understanding: 0
---

## Definition
Predictors measured at a higher level of aggregation than the individual unit of analysis (e.g., teacher characteristics for students in a class, regional economic conditions for states in a year), which enter a multilevel model through a regression at the population-distribution level: beta ~ N(X_beta alpha, Sigma_beta) rather than the exchangeable beta ~ N(1 alpha, sigma_beta^2 I). Group-level predictors let the model explain systematic across-group variation instead of treating group effects as purely exchangeable noise. A structural flexibility of the hierarchical formulation is that group-level predictors and the constant term can be placed at any of the levels of the model (likelihood, population, or hyperprior) with equivalent fits, since these are alternate but statistically equivalent parameterizations of the same joint model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]