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
- statistics
- bayesian-inference
id: pkis:concept:normal-inverse-gamma-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
tags:
- conjugate-prior
- linear-regression
- inverse-gamma
- closed-form-posterior
title: Normal-Inverse-Gamma (NIG) Prior
understanding: 0
---

## Definition
$$\text{NIG}(w, \sigma^2 \mid \bar{w}, \bar{\Sigma}, \bar{a}, \bar{b}) \triangleq \mathcal{N}(w \mid \bar{w}, \sigma^2\bar{\Sigma})\,\text{IG}(\sigma^2 \mid \bar{a}, \bar{b})$$

The conjugate joint prior for the regression weights $w$ and noise variance $\sigma^2$ in a linear regression model, combining a conditionally Gaussian prior on $w$ (whose scale depends on $\sigma^2$) with an inverse-gamma prior on $\sigma^2$.

### Why it matters
With this prior the posterior is also NIG and can be computed in closed form; the marginal posterior over $w$ is a multivariate Student-$t$ distribution with analytically tractable predictive distributions. It is the building block for conjugate Bayesian linear regression and multivariate linear regression (matrix normal inverse-Wishart).

### Posterior update
Given $N$ observations: $\hat{w}=(\bar{\Sigma}^{-1}+X^TX)^{-1}(\bar{\Sigma}^{-1}\bar{w}+X^Ty)$, $\hat{a}=\bar{a}+N/2$, and $\hat{b}$ absorbs prior and empirical sums of squares.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]