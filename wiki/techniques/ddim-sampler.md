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
- generative-models
extends:
- ddpm
id: pkis:technique:ddim-sampler
instantiates:
- diffusion-sde-framework
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- diffusion
- fast-sampling
- deterministic-generation
- inference
title: DDIM Sampler (Denoising Diffusion Implicit Model)
understanding: 0
---

## Definition
A deterministic (or low-stochasticity) reverse sampler for diffusion models that replaces the standard Markovian reverse process with a **non-Markovian** process conditioned on both $x_t$ and the predicted clean image $\hat x_0$:

$$p_\theta(x_{t-1}|x_t) = \mathcal{N}\!\left(\sqrt{\alpha_{t-1}}\hat x_0 + \sqrt{1-\alpha_{t-1}-\tilde\sigma_t^2}\cdot\frac{x_t-\sqrt{\alpha_t}\hat x_0}{\sqrt{1-\alpha_t}},\; \tilde\sigma_t^2 I\right)$$

Setting $\tilde\sigma_t^2=0$ makes generation fully deterministic; the DDIM sampler uses the **same trained weights** as DDPM (same $L_{\text{simple}}$ objective) but can produce high-quality samples in 20–50 steps instead of 1000.

### Why it matters
DDIM dramatically reduces the inference cost of diffusion models without retraining. The deterministic mapping also provides a consistent latent encoding: each image encodes to a unique $x_T$, enabling semantic interpolation and image editing. It is a special case of the probability flow ODE.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[diffusion-sde-framework]] — instantiates: DDIM is a discretisation of the probability flow ODE
- [[ddpm]] — extends: Uses the same trained weights but a non-Markovian deterministic reverse process for faster sampling
[To be populated during integration]