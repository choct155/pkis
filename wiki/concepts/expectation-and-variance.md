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
id: pkis:concept:expectation-and-variance
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch06
tags: []
title: Expectation and Variance
understanding: 0
---

## Definition
$$\mathbb{E}_X[g(x)] = \int_{\mathcal{X}} g(x)\,p(x)\,dx \;\;(\text{or } \textstyle\sum_x g(x)p(x)), \qquad \mathbb{V}_X[x] = \mathbb{E}_X[(x-\mu)^2] = \mathbb{E}_X[x^2] - (\mathbb{E}_X[x])^2$$

The expected value is the probability-weighted average of a function of a random variable; the variance is the expected squared deviation from the mean, measuring spread.

### Mean, median, mode
The **mean** $\mathbb{E}_X[x]$ is the expectation of the identity function. Two other notions of "average" are the **median** (the value where the cdf is $0.5$, robust to outliers and long tails) and the **mode** (the most frequent value / a density peak; distributions may be multimodal). In high dimensions the mean generalizes element-wise but the median has no canonical extension since points cannot be totally ordered.

### Linearity and key identities
Expectation is a **linear operator**: $\mathbb{E}[af+bg]=a\mathbb{E}[f]+b\mathbb{E}[g]$, and $\mathbb{E}[x\pm y]=\mathbb{E}[x]\pm\mathbb{E}[y]$. Variance is *not* linear: $\mathbb{V}[x+y]=\mathbb{V}[x]+\mathbb{V}[y]+2\,\mathrm{Cov}[x,y]$. Under affine maps $y=Ax+b$: $\mathbb{E}[y]=A\mu+b$ and $\mathbb{V}[y]=A\Sigma A^\top$. The **law of total variance** decomposes $\mathbb{V}_X[x]=\mathbb{E}_Y[\mathbb{V}_X[x\mid y]]+\mathbb{V}_Y[\mathbb{E}_X[x\mid y]]$.

### Why it matters
Expectations are the workhorse of ML: losses are expected risks, the marginal likelihood is an expectation, and gradient estimators (e.g. score-function and reparameterization) are Monte Carlo expectations. Variance quantifies estimator uncertainty and underlies the bias–variance decomposition.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]