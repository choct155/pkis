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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- Bayesian-inference
id: pkis:technique:variational-em
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch10
- murphy-pml2-advanced-ch10
tags:
- EM
- variational-inference
- conjugate-prior
- Bayesian-mixture
- ELBO
title: Variational Bayesian EM (VB-EM)
understanding: 0
---

## Definition
An iterative two-phase algorithm for models with latent variables $\mathbf{Z}$ and parameters $\boldsymbol{\theta}$ that places prior distributions on $\boldsymbol{\theta}$, absorbs them into $\mathbf{Z}$, and alternates:

**VB-E step:** Update $q(\mathbf{Z})$ by evaluating responsibilities using current moments of $q(\boldsymbol{\theta})$:
$$\ln q^*(\mathbf{Z}) = \mathbb{E}_{q(\boldsymbol{\theta})}[\ln p(\mathbf{X},\mathbf{Z},\boldsymbol{\theta})] + \text{const}$$

**VB-M step:** Update $q(\boldsymbol{\theta})$ using expected sufficient statistics from $q(\mathbf{Z})$:
$$\ln q^*(\boldsymbol{\theta}) = \mathbb{E}_{q(\mathbf{Z})}[\ln p(\mathbf{X},\mathbf{Z},\boldsymbol{\theta})] + \text{const}$$

Each step increases the ELBO; convergence is guaranteed. With conjugate-exponential models the updates are closed-form.

### Why it matters
Generalizes maximum-likelihood EM to a fully Bayesian treatment, automatically regularizing against overfitting and allowing model-order selection (e.g., number of mixture components) without cross-validation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]