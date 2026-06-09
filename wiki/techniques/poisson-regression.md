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
id: pkis:technique:poisson-regression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch16
specializes:
- generalized-linear-models
tags:
- poisson-regression
- glm
- count-data
- log-link
- offset
- loglinear
title: Poisson Regression
understanding: 0
uses:
- link-function
- poisson-process
---

## Definition
**Poisson regression** is the generalized linear model for count outcomes. The response is modeled as Poisson with mean $\mu$ (and hence variance $\mu$), and the canonical log link relates the mean to the linear predictor:

$$\log\mu_i = \eta_i = X_i\beta, \qquad p(y\mid\beta)=\prod_{i=1}^n \frac{1}{y_i!}\,e^{-\exp(\eta_i)}\,(\exp(\eta_i))^{y_i}.$$

In the Bayesian posterior the $1/y_i!$ factors are constants and can be absorbed. A key modeling device is the **offset**: a predictor with known coefficient fixed at 1. When the rate is $\mu$ per unit exposure $T$, the expected count is $\mu T$, so adding a column $\log T$ to $X$ encodes exposure exactly (e.g. previous-year arrests as the offset in the NYPD stop-and-frisk study).

Intuition: model the log-rate linearly so multiplicative effects on counts become additive on coefficients, while respecting that counts are non-negative integers.

### Why it matters
Poisson regression is the default tool for events-per-exposure data — disease incidence, accidents, police stops — wherever a normal model would be illogical (counts cannot be negative, variance grows with the mean). Because the Poisson fixes variance equal to mean, applied work almost always pairs it with an overdispersion term, and its log-link/offset structure also underlies loglinear models for contingency tables and the Poisson trick for fitting multinomial responses.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[poisson-process]] — uses
- [[link-function]] — uses
- [[generalized-linear-models]] — specializes
[To be populated during integration]