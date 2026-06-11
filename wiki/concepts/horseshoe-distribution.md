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
- bayesian-statistics
- probability-theory
id: pkis:concept:horseshoe-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch28
tags:
- sparsity
- shrinkage
- half-cauchy
- heavy-tails
- robust-prior
title: Horseshoe Distribution
understanding: 0
---

## Definition
$$p(x) = \int_0^\infty \mathcal{N}(x \mid 0, \epsilon^2)\, \mathcal{C}_+(\epsilon \mid 0, 1)\, d\epsilon$$

The horseshoe distribution arises as a Gaussian scale mixture when the scale $\epsilon$ follows a half-Cauchy prior. It has a sharp spike at zero (promoting sparsity) yet has heavy, non-vanishing tails (avoiding over-shrinkage of large signals).

### Why it matters
The horseshoe prior is the gold standard sparsity-promoting prior in Bayesian statistics: it aggressively shrinks near-zero coefficients while leaving large signals almost unregularized, unlike the Laplace/LASSO prior which over-penalizes large effects. It has become the default for sparse Bayesian regression when the true sparsity level is unknown.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]