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
instantiates:
- variational-inference
- latent-variable-models
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
uses:
- elbo
- reparameterization-trick
- differentiable-generator-network
- kl-divergence
- amortized-inference
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
- [[amortized-inference]] — uses: A parametric encoder replaces per-datapoint optimisation of q.
- [[latent-variable-models]] — instantiates
- [[kl-divergence]] — uses: KL(q||p_model(z)) acts as a regulariser in the ELBO.
- [[differentiable-generator-network]] — uses
- [[variational-inference]] — instantiates
- [[reparameterization-trick]] — uses: Gradients through the Gaussian sampling step use the reparameterisation trick.
- [[elbo]] — uses: VAE training objective is the ELBO / variational lower bound.
[To be populated during integration]