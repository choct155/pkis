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
id: pkis:concept:negative-binomial-distribution
instantiates:
- overdispersion
- mixture-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch17
tags:
- count-data
- overdispersion
- mixture
- poisson
title: Negative Binomial Distribution
understanding: 0
uses:
- gamma-distribution
---

## Definition
A two-parameter distribution for overdispersed count data, $\text{Neg-bin}(\alpha,\beta)$, that lets the mean and variance be fit separately with the variance always at least as large as the mean. It arises as a **gamma mixture of Poissons**: data are Poisson with means $\lambda_i$ that themselves follow a $\text{Gamma}(\alpha,\beta)$ distribution. Its mean is $\alpha/\beta$ and its variance is $\frac{\beta+1}{\beta}\cdot\frac{\alpha}{\beta}$, strictly exceeding the mean (in contrast to the Poisson, whose variance equals its mean). As $\beta\to\infty$ with $\alpha/\beta$ held fixed, the gamma collapses to a spike and the negative binomial converges to the Poisson, making it the canonical Poisson generalization for overdispersed counts (used e.g. by Mosteller and Wallace for word-frequency data in the Federalist papers).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gamma-distribution]] — uses: Poisson means follow a Gamma(alpha,beta)
- [[mixture-models]] — instantiates: gamma mixture of Poissons
- [[overdispersion]] — instantiates: canonical overdispersed alternative to the Poisson
[To be populated during integration]