---
aliases: []
also_type: []
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
- generative-models
- probabilistic-models
id: pkis:framework:ddpm
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- diffusion
- generative-model
- image-generation
- latent-variable
- noise-prediction
title: Denoising Diffusion Probabilistic Model (DDPM)
understanding: 0
---

## Definition
$$q(x_t|x_{t-1}) = \mathcal{N}(x_t|\sqrt{1-\beta_t}x_{t-1},\, \beta_t I), \qquad p_\theta(x_{t-1}|x_t) = \mathcal{N}(x_{t-1}|\mu_\theta(x_t,t),\Sigma_\theta(x_t,t))$$

A hierarchical latent-variable generative model in which a **fixed** linear-Gaussian forward (encoder) process progressively corrupts data into isotropic Gaussian noise over $T$ steps, while a **learned** Gaussian reverse (decoder) process reconstructs data from noise; both encoder and decoder share weights across time steps.

The key analytical insight is that the marginal $q(x_t|x_0)=\mathcal{N}(\sqrt{\bar\alpha_t}x_0,(1-\bar\alpha_t)I)$ is available in closed form (where $\bar\alpha_t=\prod_{s=1}^t(1-\beta_s)$), enabling the ELBO to be written as a sum of KL divergences between Gaussian pairs, each reducible to a **noise-prediction** least-squares loss:

$$L_{\text{simple}} = \mathbb{E}_{x_0,\epsilon,t}\left[\|\epsilon - \epsilon_\theta(\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,\, t)\|^2\right]$$

### Why it matters
DDPMs achieve state-of-the-art sample quality on images and other modalities while admitting a simple, stable training objective that avoids posterior collapse and mode-dropping issues common to GANs and VAEs. The noise-prediction reparameterisation connects directly to score-based generative models and continuous-time SDEs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]