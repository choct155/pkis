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
id: pkis:concept:gaussian-scale-mixture
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
- murphy-pml2-advanced-ch28
tags:
- heavy-tails
- sparsity
- hierarchical-model
- Bayesian-lasso
- horseshoe
title: Gaussian Scale Mixture
understanding: 0
---

## Definition
$$p(w) = \int \mathcal{N}(w \mid 0, \tau^2)\, p(\tau^2)\, d\tau^2$$

A distribution obtained by placing a mixing prior on the variance of a zero-mean Gaussian; the resulting marginal is typically heavy-tailed or sparsity-inducing. Examples include the Laplace ($p(\tau^2) = \text{Ga}(1, \gamma^2/2)$), Student-$t$, and horseshoe priors.

### Why it matters
Gaussian scale mixtures (GSMs) enable tractable hierarchical inference: conditional on $\tau^2$, the model remains Gaussian and admits conjugate updates, while the marginal prior encourages sparsity or robustness. They underpin the Bayesian lasso, ARD, horseshoe prior, and robust regression models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]