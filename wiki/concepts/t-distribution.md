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
generalizes:
- gaussian-distribution
id: pkis:concept:t-distribution
instantiates:
- mixture-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch17
tags:
- heavy-tailed
- robustness
- scale-mixture
- cauchy
title: Student t Distribution
understanding: 0
uses:
- em-algorithm
---

## Definition
A symmetric, longer-tailed family $t_\nu(\mu,\sigma^2)$ parameterized by a center $\mu$, scale $\sigma$, and a degrees-of-freedom parameter $\nu \in (0,\infty)$ controlling tail weight. At $\nu=1$ it is the Cauchy distribution, so long-tailed that its mean and variance are infinite; as $\nu\to\infty$ it converges to the normal. The t is the workhorse of robust modeling, accommodating either occasional unusual observations in a data distribution or occasional extreme parameters in a prior/hierarchical model. Its key tractable property is the **scale-mixture-of-normals representation**: $y\sim t_\nu(\mu,\sigma^2)$ is equivalent to $y\mid V\sim N(\mu,V)$ with $V\sim \text{Inv-}\chi^2(\nu,\sigma^2)$, so observations assigned a large latent variance $V_i$ act as the outliers. This representation enables the EM algorithm and Gibbs sampling via auxiliary variances treated as missing data. When the t is used purely as a robust alternative, $\nu$ is fixed at a small value (e.g. 4); when it is used to genuinely fit a long-tailed population from ample data, $\nu$ is estimated. Parameterizing sensitivity analyses in $1/\nu \in [0,1]$ neatly spans the entire range from normal ($1/\nu=0$) to Cauchy ($1/\nu=1$). Because the variance is infinite for $\nu\le 2$, the t cannot be parameterized by its variance, and $\mu,\sigma$ describe the median and curvature at the median rather than mean and variance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[em-algorithm]] — uses: EM via the normal scale-mixture treats latent variances as missing data
- [[mixture-models]] — instantiates: t is a scale mixture of normals with Inv-chi^2 variances
- [[gaussian-distribution]] — generalizes: normal is the nu->infinity limit of the t
[To be populated during integration]