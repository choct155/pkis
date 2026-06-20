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
date_updated: '2026-06-20'
domain:
- machine-learning
- deep-learning
- bayesian-inference
id: pkis:technique:reparameterized-vi
instantiates:
- reparameterization-trick
- variational-inference-framework
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
- mohamed-monte-2020
tags:
- reparameterization-trick
- gradient-estimator
- VAE
- continuous-latents
title: Reparameterized Variational Inference
understanding: 0
uses:
- cholesky-decomposition
- monte-carlo-estimator
---

## Definition
Express $z\sim q_\phi(z|x)$ as a deterministic transformation of a noise variable $\epsilon\sim p(\epsilon)$ independent of $\phi$:
$$z = g(\phi, x, \epsilon), \qquad \nabla_\phi\,\mathbb{E}_{q_\phi}[f(z)] = \mathbb{E}_{p(\epsilon)}[\nabla_\phi f(g(\phi,x,\epsilon))]$$
For Gaussian $q$: $z=\mu+\sigma\odot\epsilon$, $\epsilon\sim\mathcal{N}(0,I)$ (diagonal covariance) or $z=\mu+L\epsilon$ with Cholesky $\Sigma=LL^T$ (full covariance). The log-density under the reparameterized variable uses the change-of-variables formula: $\log q_\phi(z|x)=\log p(\epsilon)-\log|\det(\partial z/\partial\epsilon)|$.

### Why it matters
Reparameterized VI (Kingma & Welling 2014; Rezende et al. 2014) yields low-variance, unbiased gradient estimates for continuous latents, enabling scalable end-to-end training of deep generative models. It is strictly lower-variance than the score-function estimator when applicable, and is the workhorse of VAE training.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[monte-carlo-estimator]] — uses: A single Monte Carlo sample from p(epsilon) provides an unbiased gradient estimate.
- [[cholesky-decomposition]] — uses: Full-covariance Gaussian VI uses the Cholesky decomposition z = mu + L*epsilon.
- [[variational-inference-framework]] — instantiates
- [[reparameterization-trick]] — instantiates: Reparameterized VI is the application of the reparameterization trick to ELBO gradient estimation.
[To be populated during integration]