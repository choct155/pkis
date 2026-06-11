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
contrasts-with:
- variational-autoencoder-vae
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- generative-models
- game-theory
id: pkis:framework:generative-adversarial-network-framework
instantiates:
- game-theory
- implicit-generative-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
- murphy-pml2-advanced-ch26
specializes:
- generative-adversarial-network
tags:
- adversarial-training
- minimax
- implicit-density
- image-synthesis
title: Generative Adversarial Network (GAN)
understanding: 0
uses:
- differentiable-generator-network
- nash-equilibrium
- jensen-shannon-divergence
- minimax-algorithm
- reparameterization-trick
- stochastic-gradient-descent
- mode-collapse
- non-saturating-gan-loss
- density-ratio-estimation
- convolutional-neural-networks
- batch-normalization
- transformer-attention-mechanisms
---

## Definition
A framework for training generative models via a minimax game between two networks:
$$g^*=\arg\min_g\max_d\;v(g,d),\quad v=\mathbb{E}_{x\sim p_{\mathrm{data}}}\log d(x)+\mathbb{E}_{x\sim p_{\mathrm{model}}}\log(1-d(x)).$$
The **generator** $g(z;\theta^{(g)})$ maps noise $z$ to samples; the **discriminator** $d(x;\theta^{(d)})$ tries to distinguish real from generated samples. At the Nash equilibrium the generator distribution matches the data distribution and $d(x)=\frac{1}{2}$ everywhere. Intuitively, training proceeds by alternating gradient ascent on the discriminator and gradient descent on the generator.

### Why it matters
GANs require neither approximate inference nor partition-function estimation, producing sharp, high-quality samples (notably images). Challenges include training instability, mode collapse, and the lack of a tractable likelihood. The DCGAN and subsequent architectures demonstrated high-fidelity image synthesis; GAN training remains an active research area.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[transformer-attention-mechanisms]] — uses: SAGAN uses self-attention in both generator and discriminator for global context.
- [[batch-normalization]] — uses
- [[convolutional-neural-networks]] — uses: DCGAN and subsequent architectures use convolutional nets for both generator and discriminator.
- [[density-ratio-estimation]] — uses
- [[non-saturating-gan-loss]] — uses
- [[mode-collapse]] — uses: Mode collapse is the primary failure mode of GAN training.
- [[stochastic-gradient-descent]] — uses
- [[reparameterization-trick]] — uses: Used to compute generator gradients through the sampling path.
- [[minimax-algorithm]] — uses
- [[implicit-generative-model]] — instantiates
- [[jensen-shannon-divergence]] — uses: The original GAN minimax objective is equivalent to minimising JSD at discriminator optimality.
- [[variational-autoencoder-vae]] — contrasts-with: GANs use no approximate inference/partition function; VAEs use ELBO.
- [[generative-adversarial-network]] — specializes: The framework chapter entry extends the earlier node with training details.
- [[game-theory]] — instantiates
- [[nash-equilibrium]] — uses: Convergence corresponds to a Nash equilibrium of the minimax game.
- [[differentiable-generator-network]] — uses
[To be populated during integration]