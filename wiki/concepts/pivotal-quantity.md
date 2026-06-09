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
contrasts-with:
- confidence-interval
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:pivotal-quantity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch03
tags:
- inference
- sampling-theory
- interval-estimation
title: Pivotal Quantity
understanding: 0
---

## Definition
A pivotal quantity for an estimand is a nontrivial function of the data and the estimand whose sampling distribution is free of all unknown parameters (and of the data). The canonical example is the t statistic for a normal mean,

$$\frac{\bar{y}-\mu}{s/\sqrt{n}} \;\Big|\; \mu, \sigma^2 \sim t_{n-1},$$

whose distribution depends on neither mu nor the nuisance parameter sigma^2. Pivots are the classical engine for constructing confidence intervals, since a probability statement about the pivot can be inverted into one about the estimand without needing the nuisance parameters.

## Bayesian mirror
Gelman highlights a striking duality for the normal model: the same quantity is pivotal in two senses. Its **sampling** distribution (given mu, sigma^2) does not depend on the nuisance parameter sigma^2; its **posterior** distribution (given y) does not depend on the data. Under the noninformative prior the posterior of (mu - \bar{y})/(s/sqrt(n)) is exactly t_{n-1}, matching the sampling distribution of (\bar{y} - mu)/(s/sqrt(n)). This coincidence is why Bayesian and frequentist interval estimates agree numerically for the normal-mean problem despite differing in interpretation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-distribution]] — applies
- [[confidence-interval]] — contrasts-with
[To be populated during integration]