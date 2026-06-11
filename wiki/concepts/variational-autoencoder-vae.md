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
- generative-models
- variational-inference
id: pkis:concept:variational-autoencoder-vae
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- generative-model
- latent-variable
- encoder-decoder
- reparameterisation
title: Variational Autoencoder (VAE)
understanding: 0
---

## Definition
A directed latent-variable generative model trained by maximising a variational lower bound (ELBO) on the marginal log-likelihood:
$$\mathcal{L}(q)=\mathbb{E}_{z\sim q(z|x)}\log p_{\theta}(x|z)-D_{\mathrm{KL}}\!\left(q_{\phi}(z|x)\,\|\,p(z)\right)\leq\log p_{\theta}(x).$$
A parametric encoder $q_{\phi}(z|x)$ (inference network) and decoder $p_{\theta}(x|z)$ (generator network) are trained jointly with gradient descent using the reparameterisation trick to differentiate through the sampling of $z$. Intuitively, the encoder compresses data into a structured latent space and the decoder reconstructs from it, with the KL term regularising the latent code towards a prior.

### Why it matters
VAEs are end-to-end differentiable, do not require MCMC, and learn interpretable disentangled representations. They serve as a principled framework for density estimation, manifold learning, semi-supervised learning, and conditional generation. Key extensions include DRAW (recurrent attention), variational RNNs, and the importance-weighted autoencoder (IWAE) objective $L_k$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]