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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
id: pkis:concept:sufficient-statistics
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch22
- mackay-itila-ch24
tags:
- likelihood
- sufficiency
- sample-mean
- gaussian
- data-summary
title: Sufficient Statistics
understanding: 0
---

## Definition
A **sufficient statistic** is a function $T(\{x_n\})$ of the data that captures *everything the data say about the parameters*: once $T$ is known, the raw data are irrelevant to inference. Formally, the likelihood depends on the data only through $T$, so $P(\{x_n\}\mid\theta) = g(T,\theta)\,h(\{x_n\})$ (the Fisher–Neyman factorization).

MacKay's worked example is the Gaussian. The log likelihood of $N$ i.i.d. points $\{x_n\}$ under $\mathcal N(\mu,\sigma^2)$ is
$$\ln P = -N\ln(\sqrt{2\pi}\,\sigma) - \frac{N(\mu-\bar x)^2 + S}{2\sigma^2},$$
where the **sample mean** $\bar x \equiv \frac1N\sum_n x_n$ and the **sum of squared deviations** $S \equiv \sum_n (x_n-\bar x)^2$ are the two sufficient statistics. Two data sets sharing the same $(\bar x, S)$ yield *identical* likelihoods and therefore identical inferences about $(\mu,\sigma)$, regardless of the individual values.

### Why it matters
Sufficiency is the formal reason that a model can be fit — and predictions made — from a handful of summaries rather than the full data set, which underlies both compact data storage and the closed-form maximum-likelihood estimators $\hat\mu = \bar x$, $\hat\sigma^2 = S/N$. The notion is sharpest, and statistics are finite-dimensional, precisely for exponential-family models, linking it directly to that class.

### Connection to the exponential family
In an exponential-family model $P(x\mid\mathbf w)\propto\exp(\sum_k w_k f_k(x))$, the data-averages $\langle f_k\rangle_{\text{Data}}$ are the sufficient statistics, and they are exactly the quantities the maximum-likelihood fit must match.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]