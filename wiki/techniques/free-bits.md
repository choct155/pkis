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
id: pkis:technique:free-bits
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- posterior-collapse
- rate-distortion
- hierarchical-VAE
title: Free Bits
understanding: 0
---

## Definition
Free bits replaces the standard per-dimension KL penalty in a VAE with a hinge loss that stops penalising dimensions that are already below a target rate $\lambda$:

$$L'_R = \sum_i \max\!\left(\lambda,\; D_{KL}(q_\phi(z_i|x)\|p_\theta(z_i))\right)$$

Dimensions whose KL is less than $\lambda$ are 'free' — the model is not forced to push them further toward the prior.

### Why it matters
Free bits provides a principled lower bound on the per-latent information rate, preventing posterior collapse without the schedule-tuning burden of KL annealing. It is widely used in hierarchical VAEs and VQ-VAE variants to ensure each latent layer carries meaningful information.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]