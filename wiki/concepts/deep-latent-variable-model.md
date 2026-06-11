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
- probabilistic-modelling
id: pkis:concept:deep-latent-variable-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- latent-variable
- generative-model
- VAE
- DLGM
- intractable-likelihood
title: Deep Latent Variable Model (DLVM)
understanding: 0
---

## Definition
$$z \sim p_\theta(z), \quad x|z \sim \mathrm{Expfam}(x|d_\theta(z))$$

A deep latent variable model (DLVM) is a latent variable model in which the parameters of an exponential-family observation distribution are computed by a deep neural network decoder $d_\theta(z)$ applied to a latent code $z$. When $p(z)$ is Gaussian the model is called a deep latent Gaussian model (DLGM).

### Why it matters
DLVMs are the probabilistic backbone of VAEs and their many extensions. Because the marginal likelihood $p_\theta(x)=\int p_\theta(x|z)p_\theta(z)\,dz$ is intractable, they motivate the entire family of amortised variational inference algorithms. Their flexibility — any architecture for $d_\theta$ — makes them the dominant paradigm for unsupervised representation learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]