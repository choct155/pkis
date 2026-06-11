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
[To be populated during integration]