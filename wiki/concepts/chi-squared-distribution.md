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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability-theory
- statistics
id: pkis:concept:chi-squared-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- chi-squared
- goodness-of-fit
- hypothesis-testing
- sum-of-squares
- gamma-special-case
title: Chi-Squared Distribution
understanding: 0
---

## Definition
The **chi-squared distribution** with $\nu$ degrees of freedom is defined as
$$\chi^2_\nu(x) \triangleq \mathrm{Ga}\!\left(x\,\Big|\,\mathrm{shape}=\tfrac{\nu}{2},\,\mathrm{rate}=\tfrac{1}{2}\right), \quad x > 0.$$
It is the distribution of the sum of squares of $\nu$ independent standard normal variables: if $Z_i \sim \mathcal{N}(0,1)$ then $\sum_{i=1}^\nu Z_i^2 \sim \chi^2_\nu$. Its mean is $\nu$ and variance is $2\nu$.

### Why it matters
The chi-squared distribution underpins classical hypothesis tests (goodness-of-fit, independence tests, likelihood-ratio tests) and is the sampling distribution of the sample variance under normality, making it central to frequentist and Bayesian inference for variance parameters.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]