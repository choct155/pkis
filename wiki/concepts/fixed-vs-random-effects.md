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
id: pkis:concept:fixed-vs-random-effects
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch15
specializes:
- multilevel-regression
tags:
- multilevel-models
- variance-components
title: Fixed vs. Random Effects
understanding: 0
uses:
- finite-vs-superpopulation-variance
---

## Definition
In the hierarchical-modeling view, 'random effects' are batches of coefficients given an estimated finite-variance population distribution (enabling partial pooling), while 'fixed effects' are coefficients given noninformative, effectively infinite-variance priors (no pooling). A mixed-effects model combines both: some coefficients get independent improper priors (fixed) and others are exchangeable with a common mean and estimated variance (random). Gelman's reframing dissolves much of the classical fixed-vs-random debate: the distinction is not one of inference or computation but of intended use, mapped onto whether the finite-population or the superpopulation standard deviation is the relevant summary. Relabeling a factor from fixed to random changes neither the coefficient estimates nor their finite/superpopulation variances; it only assigns the superpopulation variance a new interpretive role.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[multilevel-regression]] — specializes: fixed = infinite-variance prior (no pooling), random = estimated finite-variance population distribution
- [[finite-vs-superpopulation-variance]] — uses: Gelman recasts the fixed/random distinction via which variance is of interest
[To be populated during integration]