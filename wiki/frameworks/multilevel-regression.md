---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
extends:
- linear-regression
id: pkis:framework:multilevel-regression
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch15
specializes:
- hierarchical-bayesian-models
tags:
- regression
- multilevel-models
- shrinkage
title: Multilevel Regression
understanding: 0
uses:
- partial-pooling-shrinkage
- bayesian-linear-regression
---

## Definition
A regression framework for data with predictors and structure at multiple levels of variation (e.g., students within classes within schools), in which groups of regression coefficients are modeled as draws from population (group-level) distributions rather than as free parameters or a single shared value. The simplest form is the varying-coefficients / random-effects model in which all coefficients in a batch are exchangeable, beta ~ N(1*alpha, sigma_beta^2 I); classical no-pooling (sigma_beta = infinity) and complete-pooling (sigma_beta = 0) regressions are recovered as the two extremes, and the favored hierarchical model interpolates between them. Because the hierarchical prior is conjugate to the normal regression likelihood, the whole model can be re-expressed as a single augmented (weighted) linear regression whose 'observations' include rows contributed by the population and hyperprior distributions. Multilevel regression breaks down the lowest-level exchangeability assumption by conditioning on group-indicator variables, inducing intraclass correlation among units in the same group. In the social sciences this is usually called multilevel modeling; an equivalent name is the hierarchical linear model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-linear-regression]] — uses: conjugacy recasts the multilevel model as a single augmented weighted normal regression
- [[partial-pooling-shrinkage]] — uses: estimation interpolates between no pooling and complete pooling
- [[linear-regression]] — extends: adds group-level population distributions over batches of coefficients
- [[hierarchical-bayesian-models]] — specializes: the hierarchical linear model is the normal-likelihood specialization of the general hierarchical Bayesian framework
[To be populated during integration]