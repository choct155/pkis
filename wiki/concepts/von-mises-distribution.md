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
- probability
- statistics
id: pkis:concept:von-mises-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
tags:
- circular-statistics
- periodic-variable
- directional-data
- gaussian-limit
title: Von Mises Distribution
understanding: 0
---

## Definition
$$p(\theta|\theta_0, m) = \frac{1}{2\pi I_0(m)}\exp\{m\cos(\theta-\theta_0)\}, \quad \theta\in[0,2\pi)$$

where $I_0(m)=\frac{1}{2\pi}\int_0^{2\pi}\exp\{m\cos\theta\}\,d\theta$ is the zeroth-order modified Bessel function of the first kind. Also called the **circular normal**, it is derived by conditioning a bivariate isotropic Gaussian on the unit circle; $\theta_0$ is the mean direction and $m$ (concentration) plays the role of precision.

### Why it matters
The von Mises distribution is the canonical model for periodic/circular data such as wind directions, calendar phases, or neural tuning curves. Its maximum likelihood estimator for $\theta_0$ is the argument of the vector mean of unit observations, $\bar{\theta}=\text{atan2}(\bar{s},\bar{c})$, which is coordinate-invariant. For large $m$ it approximates a Gaussian, while $m=0$ gives the uniform distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]