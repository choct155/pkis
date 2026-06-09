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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:shrinkage-priors
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch20
tags:
- sparsity
- regularization
- scale-mixture-of-normals
- global-local-priors
- heavy-tails
- gibbs-sampling
title: Shrinkage Priors (Continuous / Global-Local)
understanding: 0
---

## Definition
A class of continuous prior distributions for regression coefficients that concentrate mass near zero while retaining heavy tails, providing a *continuous analogue* to discrete (spike-and-slab) variable selection: unimportant coefficients are shrunk toward — but not exactly to — zero, while heavy tails avoid over-shrinking the few large, important coefficients. They sidestep the combinatorial 2^H model space of formal variable selection and so scale to high-dimensional problems.

## Scale-Mixture-of-Normals Representation
Most useful shrinkage priors are expressible as β_h ~ N(0, σ_h²), σ_h² ~ G, where the mixing distribution G over the local variances determines the marginal shape. This representation is the source of their computational convenience: conditional on the latent variances, the model is Gaussian and admits block Gibbs updates of β.

Special cases:
- **Student-t prior**: G = Inv-gamma(ν/2, ν/2). As ν → 0 one recovers the **normal-Jeffreys** prior — improper posterior, but the posterior *mode* can put σ_h = 0, inducing empirical-Bayes basis selection. A small ν (e.g., 10⁻⁶) restores propriety while keeping strong shrinkage; ν = 1 (Cauchy) is a common, well-performing default.
- **Laplace / double-exponential prior** (Bayesian lasso): induces sparsity in the posterior *mode* (β_h can be exactly 0) and is the heaviest-tailed prior keeping a unimodal posterior under a log-concave likelihood — but posterior *draws* are never exactly zero, and its tails are often too light, over-shrinking large coefficients.
- **Generalized double Pareto (GDP)**: resembles the double-exponential near the origin but has arbitrarily heavy (polynomial) tails: gdP(β|ξ,α) ∝ (1 + |β|/(αξ))^{−(α+1)}. Admits a scale-mixture representation (β ~ N(0,σ²), σ² ~ Expon(λ²/2), λ ~ Gamma(α,η)), so a clean block Gibbs sampler follows; defaults α = η = 1 give Cauchy-like tails.

## When To Use
Preferred over spike-and-slab when H (the number of candidate predictors/basis functions) is large enough that MCMC cannot realistically explore the discrete model space, or when nonconjugate components make discrete model search expensive. The trade-off: no exact zeros and no explicit posterior model probabilities, but far better mixing and scalability.

## Reading Path
- [[gelman-bda3-ch20]] — shrinkage priors as the continuous alternative to basis-function variable selection: scale-mixture-of-normals representation, t / normal-Jeffreys / Laplace / generalized-double-Pareto priors, and the GDP block Gibbs sampler.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]