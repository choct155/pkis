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
- representation-learning
id: pkis:framework:vq-vae
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- discrete-latent
- codebook
- straight-through-estimator
- DALL-E
- image-generation
title: VQ-VAE (Vector-Quantized VAE)
understanding: 0
---

## Definition
VQ-VAE replaces the continuous Gaussian latents of a standard VAE with a discrete codebook $\{e_k\}_{k=1}^K$. The encoder maps input to a continuous vector $z_e(x)$; quantisation selects the nearest codebook entry:

$$q(z_{ij}=k|x) = \mathbf{1}\!\left[k = \arg\min_{k'}\|z_e(x)_{ij} - e_{k'}\|_2\right]$$

The reconstruction loss plus codebook loss and commitment loss are:

$$\mathcal{L} = -\log p(x|z_q(x)) + \|\mathrm{sg}(z_e(x)) - e\|_2^2 + \beta\|z_e(x) - \mathrm{sg}(e)\|_2^2$$

Gradients bypass the non-differentiable quantisation via the straight-through estimator.

### Why it matters
VQ-VAE avoids posterior collapse (KL is constant under a uniform discrete prior) and produces highly compressed discrete representations suitable for downstream autoregressive or transformer priors (enabling high-quality image, audio, and video generation). It is the backbone of DALL-E and many modern image-generation pipelines.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]