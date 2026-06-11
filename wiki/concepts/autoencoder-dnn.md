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
- deep-learning
- representation-learning
- unsupervised-learning
generalizes:
- variational-autoencoder
- principal-component-analysis
- low-rank-approximation
id: pkis:concept:autoencoder-dnn
instantiates:
- unsupervised-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch16
specializes:
- latent-variable-models
tags:
- autoencoder
- latent-space
- representation-learning
- reconstruction
title: Autoencoder
understanding: 0
---

## Definition
$$\mathcal{L}(\theta) = \|f_d(f_e(x)) - x\|_2^2$$

An autoencoder (AE) is a neural network trained to reconstruct its input through a low-dimensional bottleneck: an encoder $z = f_e(x)$ maps input to a latent code $z$, and a decoder $\hat{x} = f_d(z)$ reconstructs the input. The bottleneck forces the model to learn a compressed, informative representation.

### Why it matters
Autoencoders provide a general unsupervised technique for dimensionality reduction, feature learning, and anomaly detection. Unlike PCA, they can capture nonlinear structure. They are also the deterministic precursor to variational autoencoders (VAEs), which add a probabilistic prior over the latent space to enable principled generation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[low-rank-approximation]] — generalizes
- [[principal-component-analysis]] — generalizes: autoencoder with linear activations and MSE loss recovers PCA subspace
- [[latent-variable-models]] — specializes
- [[variational-autoencoder]] — generalizes: VAE adds a probabilistic prior over the latent space
- [[unsupervised-learning]] — instantiates
[To be populated during integration]