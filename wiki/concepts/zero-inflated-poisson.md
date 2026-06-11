---
aliases: []
also_type: []
applies:
- overdispersion
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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
extends:
- poisson-regression
id: pkis:concept:zero-inflated-poisson
instantiates:
- mixture-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
tags:
- count-data
- overdispersion
- mixture-model
- biostatistics
- genomics
title: Zero-Inflated Poisson (ZIP) Model
understanding: 0
---

## Definition
$$\text{ZIP}(y \mid \rho, \lambda) = \begin{cases} \rho + (1-\rho)e^{-\lambda} & y=0 \\ (1-\rho)\frac{\lambda^y e^{-\lambda}}{y!} & y>0 \end{cases}$$

A mixture of a point mass at zero (with probability $\rho$) and a Poisson distribution (with rate $\lambda$ and mixing weight $1-\rho$), designed for count data exhibiting excess zeros.

### Why it matters
Excess zeros are ubiquitous in biostatistics (disease counts), genomics (read counts), and sales data. The ZIP model distinguishes between a *structural* zero-generating mechanism and a *sampling* zero from a low-rate Poisson, enabling more accurate inference and better-calibrated predictions than standard Poisson regression.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[overdispersion]] — applies
- [[mixture-models]] — instantiates
- [[poisson-regression]] — extends
[To be populated during integration]