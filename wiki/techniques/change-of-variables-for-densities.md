---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:change-of-variables-for-densities
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch06
tags: []
title: Change of Variables for Densities
understanding: 0
---

## Definition
$$y = f(x), \quad p_Y(y) = p_X\big(f^{-1}(y)\big)\,\left|\det \frac{\partial f^{-1}(y)}{\partial y}\right|$$

The rule for finding the density of a transformed random variable: push the source density through the inverse map and rescale by the Jacobian determinant that accounts for how the transformation stretches volume.

### Affine and Gaussian case
For an affine map $y=Ax+b$ of a random variable with mean $\mu$ and covariance $\Sigma$, the moments transform as $\mathbb{E}[y]=A\mu+b$ and $\mathbb{V}[y]=A\Sigma A^\top$ regardless of the underlying law. For a Gaussian this is especially clean: **any affine transformation of a Gaussian is Gaussian**, so $y\sim\mathcal{N}(A\mu+b,\ A\Sigma A^\top)$ — no Jacobian bookkeeping is needed because the family is closed under linear maps.

### Sampling application
The rule powers sampling from a general multivariate Gaussian $\mathcal{N}(\mu,\Sigma)$: draw $z\sim\mathcal{N}(0,I)$ and set $y=Az+\mu$ with $AA^\top=\Sigma$, conveniently via the Cholesky factor of $\Sigma$. For non-invertible $A$, a pseudo-inverse construction recovers the reverse transformation.

### Why it matters
Change of variables is the mechanism behind reparameterization-based gradient estimation and is the literal engine of normalizing flows, which compose invertible maps and track log-Jacobians to build expressive densities. It also explains why Gaussian modeling so often avoids explicit density transformation — the closure properties do the work.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]