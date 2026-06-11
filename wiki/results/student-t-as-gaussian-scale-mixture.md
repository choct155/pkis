---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability-theory
- statistics
id: pkis:result:student-t-as-gaussian-scale-mixture
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch28
tags:
- student-t
- scale-mixture
- inverse-gamma
- heavy-tails
- robust-regression
title: Student-t as a Gaussian Scale Mixture
understanding: 0
---

## Definition
$$\mathcal{T}(x \mid 0, \sigma^2, \nu) = \int_0^\infty \mathcal{N}(x \mid 0,\, z\sigma^2)\, \text{IG}\!\left(z \,\Big|\, \frac{\nu}{2}, \frac{\nu}{2}\right) dz$$

The Student-$t$ distribution with $\nu$ degrees of freedom arises exactly as a scale mixture of Gaussians where the variance $z$ follows an inverse-Gamma (or equivalently a scaled inverse-$\chi^2$) distribution. In the limit $\nu \to \infty$, $\text{IG}(\nu/2, \nu/2) \to \delta_1(z)$, recovering the Gaussian.

### Why it matters
This representation (i) provides an interpretable derivation of the Student's heavy tails as arising from variance uncertainty, (ii) enables efficient EM or Gibbs inference by working with the conditionally Gaussian expanded parameterisation, and (iii) directly motivates robust regression and robust Bayesian models by replacing Gaussian observation noise with Student noise.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]