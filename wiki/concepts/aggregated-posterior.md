---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- variational-inference
id: pkis:concept:aggregated-posterior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- latent-variable
- marginal-posterior
- InfoVAE
title: Aggregated Posterior (Inference Marginal)
understanding: 0
---

## Definition
$$q_{D,\phi}(z) = \int_x p_D(x)\,q_\phi(z|x)\,dx$$

The aggregated posterior is the marginal distribution over the latent code $z$ obtained by averaging the per-datapoint variational posteriors $q_\phi(z|x)$ over the empirical data distribution $p_D(x)$. It represents what the encoder collectively 'assigns' to the latent space across all training examples.

### Why it matters
The gap $D_{KL}(q_{D,\phi}(z)\|p_\theta(z))$ between the aggregated posterior and the prior is one of two terms that govern the VAE ELBO (Equation 21.22). Minimising this term encourages the encoded latents to match the generative prior globally, and is central to the InfoVAE and MMD-VAE objectives, as well as to understanding posterior collapse and disentanglement.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]