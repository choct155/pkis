---
aliases: []
also_type: []
applies:
- gaussian-distribution
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
date_updated: '2026-06-20'
domain:
- probability-theory
- statistics
generalizes:
- probability-mass-function
id: pkis:concept:cumulative-distribution-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- quantile-function
related_concepts: []
sources:
- murphy-pml1-intro-ch02
- kroese-statistical-modeling-ch02
tags:
- cdf
- continuous
- distribution
- quantile
- fundamentals
title: Cumulative Distribution Function (CDF)
understanding: 0
uses:
- random-variable
---

## Definition
$$P(x) \triangleq \Pr(X \leq x), \qquad \Pr(a < X \leq b) = P(b) - P(a)$$

The **cumulative distribution function** of a random variable $X$ gives the probability that $X$ takes a value less than or equal to $x$. It is monotonically non-decreasing, right-continuous, with $P(-\infty)=0$ and $P(\infty)=1$. The probability density function is its derivative: $p(x) = dP/dx$ wherever this exists.

### Why it matters
The CDF provides a unified representation for both discrete and continuous distributions and enables computation of interval probabilities without integration: $\Pr(a < X \leq b) = P(b)-P(a)$. Quantiles and confidence/credible intervals are defined directly through the inverse CDF (quantile function), making it central to statistical inference, hypothesis testing, and calibration.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[quantile-function]] — prerequisite-of
- [[gaussian-distribution]] — applies
- [[probability-mass-function]] — generalizes
- [[random-variable]] — uses
[To be populated during integration]