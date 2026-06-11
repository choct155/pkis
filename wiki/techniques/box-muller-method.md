---
aliases: []
also_type: []
applies:
- gaussian-distribution
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- inverse-cdf-sampling
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- probability
- simulation
id: pkis:technique:box-muller-method
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch11
tags:
- gaussian-sampling
- change-of-variables
- cholesky
- exact-sampling
title: Box-Muller Method
understanding: 0
uses:
- change-of-variables-for-densities
- cholesky-decomposition
---

## Definition
$$x_i = z_i\left(\frac{-2\ln r^2}{r^2}\right)^{1/2}, \quad r^2 = z_1^2+z_2^2, \quad (z_1,z_2)\text{ uniform in unit disk}$$

Produces two independent standard-normal samples from two uniform samples inside the unit circle by a polar change of variables.

### Why it matters
A simple, exact method for Gaussian sampling that avoids the inverse-CDF (which has no closed form for the normal). Extended to multivariate Gaussians via Cholesky decomposition: $y = Lx + \mu$ where $\Sigma = LL^T$ and $x\sim N(0,I)$.

### Extension to multivariate Gaussian
Because $\text{Cov}[Lx]=L\,\text{Cov}[x]\,L^T=\Sigma$, the Cholesky transform maps i.i.d. standard normals to the target $N(\mu,\Sigma)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inverse-cdf-sampling]] — contrasts-with: Box-Muller avoids the intractable Gaussian inverse CDF
- [[cholesky-decomposition]] — uses
- [[change-of-variables-for-densities]] — uses
- [[gaussian-distribution]] — applies
[To be populated during integration]