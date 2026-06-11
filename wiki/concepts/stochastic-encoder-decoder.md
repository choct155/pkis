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
- probabilistic-modelling
- generative-models
id: pkis:concept:stochastic-encoder-decoder
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
tags:
- stochastic
- latent-variable
- encoder
- decoder
- VAE
title: Stochastic Encoder-Decoder
understanding: 0
---

## Definition
A stochastic encoder-decoder generalises deterministic encoder/decoder functions to conditional distributions:
$$p_{\text{encoder}}(h \mid x) = p_{\text{model}}(h \mid x), \qquad p_{\text{decoder}}(x \mid h) = p_{\text{model}}(x \mid h)$$
Any latent-variable model $p_{\text{model}}(x,h)$ defines a compatible stochastic encoder-decoder pair. Training minimises the expected negative log-likelihood under the joint corruption-and-encoding distribution.

### Why it matters
The stochastic encoder-decoder view unifies autoencoders with probabilistic latent-variable models. It is the conceptual stepping stone from deterministic autoencoders to the variational autoencoder (VAE), where the encoder becomes a learned approximate posterior $q_\phi(h|x) \approx p(h|x)$ and training maximises the ELBO. It also clarifies how denoising autoencoders implicitly define a stochastic generative model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]