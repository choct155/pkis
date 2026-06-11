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
- optimisation
id: pkis:technique:kl-annealing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- posterior-collapse
- training-trick
- KL-regularisation
title: KL Annealing
understanding: 0
---

## Definition
KL annealing gradually increases the weight $\beta$ on the KL regulariser in the VAE objective from 0 to 1 over the course of training:

$$\mathcal{L}^{(t)} = -\mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] + \beta^{(t)}\,D_{KL}(q_\phi(z|x)\|p_\theta(z)), \quad \beta^{(t)} \nearrow 1$$

At $\beta=0$ the model is a plain autoencoder; as $\beta$ increases the model is gradually encouraged to match the prior. A popular variant is **cyclical annealing**, which repeats the 0→1 schedule multiple times so that each cycle warm-starts from the previous one.

### Why it matters
KL annealing is the most common practical solution to posterior collapse in VAEs with expressive decoders (e.g., RNN-VAE for text). Cyclical annealing improves over monotone scheduling by progressively refining the latent representation across cycles, leading to better disentanglement and more informative codes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]