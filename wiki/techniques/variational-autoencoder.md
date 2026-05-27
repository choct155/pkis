---
id: "pkis:technique:variational-autoencoder"
aliases: ["VAE"]
title: "Variational Autoencoder (VAE)"
knowledge_type: technique
also_type: [framework]
domain: [bayesian-stats, deep-learning]
tags: [variational-methods, generative-models, approximate-inference, deep-learning]
related_concepts: ["[[variational-inference]]", "[[elbo]]", "[[amortized-inference]]", "[[reparameterization-trick]]", "[[neural-networks]]"]
sources: ["[[ganguly-intro-vi]]", "[[sjolund-parametric-vi]]", "[[yellapragada-variational-bayes]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

A deep generative model (Kingma & Welling, 2013) that combines amortized variational inference with a neural network decoder: an encoder network q_φ(z|x) approximates the posterior over latent codes, a decoder p_θ(x|z) models the generative process, and both are trained jointly by maximizing the ELBO via the reparameterization trick; the ELBO objective decomposes into a reconstruction term E_q[log p(x|z)] minus a KL regularization term KL(q_φ(z|x)‖p(z)).

Classification note: assigned as technique but also qualifies as framework because it provides an architecture paradigm (encoder-decoder with latent code) that organizes many derivative models (β-VAE, VAE-GAN, VQ-VAE, hierarchical VAEs).

## Connections

- [[variational-inference]] — specializes: VAE is an amortized parametric VI algorithm; the encoder implements approximate posterior inference
- [[amortized-inference]] — uses: encoder network Λ_θ(x) predicts local variational parameters ϕ_i = Λ_θ(x_i), amortizing inference over data
- [[reparameterization-trick]] — uses: z = μ + σ·ε, ε~N(0,I) enables backpropagation through the stochastic latent variable sampling
- [[neural-networks]] — uses: both encoder and decoder are neural networks trained jointly by gradient descent on the ELBO
- [[elbo]] — uses: ELBO = E_q[log p(x|z)] − KL(q_φ(z|x)‖p(z)) is the VAE training objective; reconstruction quality versus posterior regularization trade-off

## Reading Path

- [[ganguly-intro-vi]] (unread) — Section 6.1; derives VAE objective from VI; explains reparameterization trick; discusses VAE-GAN extension
- [[sjolund-parametric-vi]] (unread) — Section on amortized VI; shows VAE encoder as the canonical amortized inference network; worked gradient computation examples
- [[yellapragada-variational-bayes]] (unread) — Section 3.2; reviews AEVB/VAE in the context of Bayesian neural networks; SGVB estimator derivation
