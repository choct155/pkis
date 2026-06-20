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
date_updated: '2026-06-20'
domain:
- probability-theory
- statistics
id: pkis:concept:probability-density-change-of-variables
instantiates:
- change-of-variables-for-densities
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- reparameterization-trick
- normalizing-flows
related_concepts: []
sources:
- bishop-prml-ch01
- kroese-statistical-modeling-ch03
specializes:
- probability-theory
tags:
- jacobian
- change-of-variables
- probability-density
- cumulative-distribution
title: Probability Density Function and Change of Variables
understanding: 0
---

## Definition
For a continuous variable $x$ with density $p_x(x)$, a smooth invertible change of variable $x = g(y)$ yields
$$p_y(y) = p_x(g(y))\left|g'(y)\right|$$
due to the Jacobian factor $|dx/dy|$.

The cumulative distribution function is $P(z)=\int_{-\infty}^{z}p(x)\,dx$, satisfying $P'(x)=p(x)$.

### Why it matters
The Jacobian correction is essential when reparameterising models (e.g., log-normal, normalising flows). A direct corollary is that the *mode* of a density is not preserved under nonlinear transformations — a common source of confusion in Bayesian inference and importance sampling.

### Subsection: Multivariate extension
For $\mathbf{x}\in\mathbb{R}^D$ the joint density satisfies $p(\mathbf{x})\geq 0$ and $\int p(\mathbf{x})\,d\mathbf{x}=1$; sum and product rules extend by replacing sums with integrals.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[normalizing-flows]] — prerequisite-of
- [[reparameterization-trick]] — prerequisite-of
- [[change-of-variables-for-densities]] — instantiates
- [[probability-theory]] — specializes
[To be populated during integration]