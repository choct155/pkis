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
- bayesian-inference
- probabilistic-programming
id: pkis:technique:bbvi
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
tags:
- BBVI
- score-function-estimator
- REINFORCE
- control-variates
- black-box-inference
title: Blackbox Variational Inference (BBVI)
understanding: 0
---

## Definition
$$\nabla_\psi \mathcal{L}(\psi) = \mathbb{E}_{q(z|\psi)}\!\Bigl[\tilde{L}(\psi,z)\,\nabla_\psi \log q(z|\psi)\Bigr], \quad \tilde{L} = \log p(x,z)-\log q_\psi(z)$$

BBVI (Ranganath et al., 2014) estimates ELBO gradients using the **score-function (REINFORCE) estimator**, requiring only pointwise evaluation of $\log p(x,z)$ and $\log q_\psi(z)$ — no reparameterization or model-specific derivations are needed. Variance is reduced via control variates; the optimal per-dimension control variate is $c_i = \mathrm{Cov}[g_i(z)\tilde{L},\,g_i(z)] / \mathbb{V}[g_i(z)]$.

### Why it matters
BBVI treats the generative model as a black box, enabling VI for models with discrete latents or non-differentiable likelihoods where reparameterization fails. It is the basis for many automatic inference engines in probabilistic programming languages.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]