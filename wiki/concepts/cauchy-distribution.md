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
- probability-theory
- statistics
- bayesian-inference
id: pkis:concept:cauchy-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- cauchy
- heavy-tails
- half-cauchy
- scale-prior
- undefined-mean
title: Cauchy Distribution
understanding: 0
---

## Definition
The **Cauchy (Lorentz) distribution** is the Student-$t$ distribution with $\nu = 1$ degree of freedom:
$$C(x \mid \mu, \gamma) = \frac{1}{\pi\gamma}\left[1 + \left(\frac{x-\mu}{\gamma}\right)^2\right]^{-1}, \quad x \in \mathbb{R}.$$
Its tails are so heavy that the mean, variance, and all higher moments are undefined. The **half-Cauchy** $C_+(x\mid\gamma) = \frac{2}{\pi\gamma}[1+(x/\gamma)^2]^{-1}$ for $x \geq 0$ is widely used as a weakly-informative prior for scale parameters in Bayesian hierarchical models.

### Why it matters
The Cauchy is the canonical example of a distribution with undefined moments; it arises as the ratio of two independent standard Gaussians. The half-Cauchy prior is recommended by Gelman for scale/variance hyperparameters because it is diffuse on large scales yet proper.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]