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
- deep-learning
- generative-models
id: pkis:framework:hierarchical-vae
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- hierarchical
- top-down-inference
- generative-model
- VD-VAE
- NVAE
title: Hierarchical VAE (HVAE)
understanding: 0
---

## Definition
A hierarchical VAE with $L$ stochastic layers defines the generative model:

$$p_\theta(x, z_{1:L}) = p_\theta(z_L)\left[\prod_{l=L-1}^{1} p_\theta(z_l|z_{l+1:L})\right]p_\theta(x|z_{1:L})$$

and uses a top-down inference model:

$$q_\phi(z|x) = q_\phi(z_L|x)\prod_{l=L-1}^{1}q_\phi(z_l|x, z_{l+1:L})$$

where each layer's posterior combines bottom-up information from $x$ with top-down context from higher layers $z_{>l}$.

### Why it matters
Hierarchical VAEs can represent any autoregressive model as a special case (with $L\geq D$), and in practice achieve state-of-the-art likelihoods and sample quality with fewer parameters and faster generation than autoregressive models. Multi-scale architectures exploit the hierarchy for both global (high-level semantics) and local (fine texture) structure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]