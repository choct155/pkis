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
id: pkis:concept:covariance-and-correlation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch06
tags: []
title: Covariance and Correlation
understanding: 0
---

## Definition
$$\mathrm{Cov}[x,y] = \mathbb{E}\big[(x-\mathbb{E}[x])(y-\mathbb{E}[y])^\top\big] = \mathbb{E}[xy^\top] - \mathbb{E}[x]\mathbb{E}[y]^\top, \qquad \mathrm{corr}[x,y] = \frac{\mathrm{Cov}[x,y]}{\sqrt{\mathbb{V}[x]\mathbb{V}[y]}} \in [-1,1]$$

Covariance measures the joint linear variability of two random variables; correlation is its scale-normalized version bounded in $[-1,1]$.

### Covariance matrix
Applying the definition to a multivariate $X$ with itself gives the **covariance matrix** $\mathbb{V}_X[x]=\mathbb{E}[(x-\mu)(x-\mu)^\top]$, a symmetric positive-semidefinite $D\times D$ matrix with marginal variances on the diagonal and cross-covariances off-diagonal. The correlation matrix is the covariance matrix of standardized variables $x/\sigma(x)$.

### Covariance vs. independence
Independence ($p(x,y)=p(x)p(y)$) implies zero covariance, **but not conversely**: covariance captures only *linear* dependence, so a variable and its square can have zero covariance while being fully dependent (e.g. $X$ symmetric about $0$, $Y=X^2$). There is also a geometric reading: treating zero-mean random variables as vectors with inner product $\langle X,Y\rangle=\mathrm{Cov}[x,y]$, the correlation is the cosine of the angle between them and uncorrelated means orthogonal.

### Why it matters
The covariance matrix is the second moment that parameterizes the Gaussian, drives PCA (its eigenvectors are principal directions), and encodes the kernel structure of Gaussian processes. Distinguishing correlation from independence is essential for correct probabilistic modeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]