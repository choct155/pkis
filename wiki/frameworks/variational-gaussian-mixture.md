---
aliases: []
also_type: []
applies:
- bayesian-model-comparison
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- Bayesian-inference
extends:
- gaussian-mixture-models
id: pkis:framework:variational-gaussian-mixture
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch10
tags:
- mixture-model
- variational-EM
- Dirichlet
- Wishart
- automatic-relevance-determination
- ELBO
title: Variational Bayesian Mixture of Gaussians
understanding: 0
uses:
- variational-em
- dirichlet-distribution
- conjugate-prior
- induced-factorization
- elbo
---

## Definition
A fully Bayesian Gaussian mixture model in which conjugate priors are placed on all parameters: Dirichlet $\text{Dir}(\boldsymbol{\pi}|\alpha_0)$ on mixing weights, Gaussian-Wishart $\mathcal{N}(\boldsymbol{\mu}_k|\mathbf{m}_0,(\beta_0\boldsymbol{\Lambda}_k)^{-1})\mathcal{W}(\boldsymbol{\Lambda}_k|\mathbf{W}_0,\nu_0)$ on component parameters. Inference uses a mean-field factorization $q(\mathbf{Z})q(\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Lambda})$, leading to VB-EM updates:

- **VB-E step:** Compute soft responsibilities $r_{nk}$ from current parameter moments.
- **VB-M step:** Update Dirichlet and Gaussian-Wishart posteriors using weighted statistics $N_k, \bar{\mathbf{x}}_k, \mathbf{S}_k$.

The ELBO (10.70) serves as convergence monitor and model-selection criterion, automatically pruning redundant components (those with $N_k\approx 0$ revert to their priors).

### Why it matters
Resolves the three main pathologies of ML-EM for Gaussians: (1) eliminates likelihood singularities, (2) prevents overfitting with excess components, and (3) enables principled model-order selection without cross-validation — all at essentially the same computational cost as ML-EM.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-model-comparison]] — applies
- [[elbo]] — uses
- [[induced-factorization]] — uses
- [[conjugate-prior]] — uses
- [[dirichlet-distribution]] — uses
- [[gaussian-mixture-models]] — extends
- [[variational-em]] — uses
[To be populated during integration]