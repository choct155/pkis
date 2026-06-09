---
aliases: []
also_type: []
applies:
- multilevel-regression
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- non-centered-parameterization
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- optimization
id: pkis:technique:parameter-expansion-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch15
tags:
- mcmc
- gibbs-sampling
- multilevel-models
- sampling
title: Parameter Expansion for Hierarchical Sampling
understanding: 0
uses:
- gibbs-sampler
---

## Definition
A technique to accelerate Gibbs/EM sampling of hierarchical variance parameters by introducing a redundant, non-identified multiplicative factor for each batch of coefficients. Writing beta_j^(m) = zeta_m * gamma_j^(m) and sigma_m = |zeta_m| * tau_m adds the auxiliary parameters zeta (given uniform priors and unidentified in the posterior) whose role is to break the strong dependence between a batch of coefficients and its variance parameter. Without expansion the ordinary Gibbs sampler can get trapped near sigma_m = 0: a small variance draw shrinks the coefficients toward zero, which in turn re-estimates the variance near zero. The expanded sampler alternately updates the coefficients (linear regression), the variances (inverse-chi^2), and the zeta factors (a small linear regression of residuals on the current coefficients), then recovers the original parameters by multiplying through by zeta. It is closely related to, but distinct from, the non-centered parameterization used for HMC.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[non-centered-parameterization]] — contrasts-with: related reparameterizations: redundant multiplicative (PX) vs decoupling for HMC
- [[gibbs-sampler]] — uses: parameter-expanded Gibbs sampler updates coefficients, variances, and zeta factors
- [[multilevel-regression]] — applies: redundant multiplicative factors decouple coefficients from variance parameters
[To be populated during integration]