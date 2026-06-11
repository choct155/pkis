---
aliases: []
also_type: []
analogous-to:
- spike-and-slab-prior
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- lasso
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- bayesian-inference
id: pkis:concept:horseshoe-prior
instantiates:
- gaussian-scale-mixture
- shrinkage-priors
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
tags:
- sparsity
- shrinkage
- half-Cauchy
- continuous-prior
- scale-mixture
title: Horseshoe Prior
understanding: 0
---

## Definition
$$w_j \sim \mathcal{N}(0, \gamma_j^2 \tau^2), \quad \gamma_j \sim C_+(0,1), \quad \tau \sim C_+(0,1)$$

A continuous, hierarchical Gaussian-scale-mixture prior with half-Cauchy hyper-priors on both local shrinkage factors $\gamma_j$ and a global shrinkage factor $\tau$, whose marginal density has a horseshoe shape with a sharp spike at zero and heavy tails.

### Why it matters
The horseshoe prior achieves near-spike-and-slab sparsity without discrete latent variables, making it computationally tractable via gradient-based samplers (HMC). The fat tails allow large signals to pass through unattenuated while near-zero coefficients are strongly shrunk, outperforming the Laplace prior in sparse recovery.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[shrinkage-priors]] — instantiates
- [[lasso]] — contrasts-with
- [[spike-and-slab-prior]] — analogous-to
- [[gaussian-scale-mixture]] — instantiates
[To be populated during integration]