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
- robotics
- signal-processing
- statistics
id: pkis:concept:sensor-fusion
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch03
tags:
- gaussian
- bayesian-inference
- estimation
- robotics
title: Sensor Fusion
understanding: 0
---

## Definition
**Sensor fusion** is the problem of combining observations $y_1, \ldots, y_M$ from $M$ sensors with different noise characteristics to form a single posterior estimate of an unknown quantity $z$:
$$p(z, \mathbf{y}) = p(z)\prod_{m=1}^{M}\prod_{n=1}^{N_m}\mathcal{N}(y_{n,m}|z, \Sigma_m)$$

When each sensor has a Gaussian noise model, the posterior $p(z|\mathbf{y})$ is obtained via Bayes rule for Gaussians and places more weight on more reliable sensors.

### Why it matters
Sensor fusion is foundational in robotics, navigation, medical imaging, and signal processing. The Gaussian case yields closed-form posteriors in which the posterior precision is the sum of per-sensor precisions, making the approach both principled and computationally efficient.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]