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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- generative-models
- game-theory
id: pkis:framework:generative-adversarial-network-framework
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
- murphy-pml2-advanced-ch26
tags:
- adversarial-training
- minimax
- implicit-density
- image-synthesis
title: Generative Adversarial Network (GAN)
understanding: 0
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
[To be populated during integration]