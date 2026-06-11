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
contrasts-with:
- reparameterization-trick
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- bayesian-inference
- probabilistic-programming
id: pkis:technique:bbvi
instantiates:
- variational-inference-framework
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
uses:
- reinforce
---

## Definition
$$\nabla_\psi \mathcal{L}(\psi) = \mathbb{E}_{q(z|\psi)}\!\Bigl[\tilde{L}(\psi,z)\,\nabla_\psi \log q(z|\psi)\Bigr], \quad \tilde{L} = \log p(x,z)-\log q_\psi(z)$$

BBVI (Ranganath et al., 2014) estimates ELBO gradients using the **score-function (REINFORCE) estimator**, requiring only pointwise evaluation of $\log p(x,z)$ and $\log q_\psi(z)$ — no reparameterization or model-specific derivations are needed. Variance is reduced via control variates; the optimal per-dimension control variate is $c_i = \mathrm{Cov}[g_i(z)\tilde{L},\,g_i(z)] / \mathbb{V}[g_i(z)]$.

### Why it matters
BBVI treats the generative model as a black box, enabling VI for models with discrete latents or non-differentiable likelihoods where reparameterization fails. It is the basis for many automatic inference engines in probabilistic programming languages.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reparameterization-trick]] — contrasts-with: BBVI uses score-function gradients (higher variance, works for discrete z) vs. reparameterization (lower variance, continuous z only).
- [[variational-inference-framework]] — instantiates: BBVI is a black-box instantiation of the general VI framework requiring only model log-joint evaluations.
- [[reinforce]] — uses: BBVI uses the REINFORCE/score-function gradient estimator to estimate ELBO gradients.
[To be populated during integration]