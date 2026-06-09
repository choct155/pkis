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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
id: pkis:framework:generative-adversarial-network
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch21
- russell-norvig-aima-ch25
tags:
- generative-model
- implicit-model
- game-theory
- image-synthesis
title: Generative Adversarial Network (GAN)
understanding: 0
---

## Definition
A pair of networks (Goodfellow et al., 2014) that together form a generative system. The generator maps a latent z (typically sampled from a unit Gaussian) through a deep network h_w to produce samples x from the modeled distribution P_w(x); it is closely related to the decoder of a variational autoencoder. The discriminator is a classifier trained to label inputs as real (from the training set) or fake (from the generator). The two are trained simultaneously in a competition describable in the language of game theory: the generator learns to fool the discriminator while the discriminator learns to separate real from fake. At the game's equilibrium, the generator reproduces the training distribution perfectly and the discriminator can do no better than random guessing. GANs are implicit models — samples can be generated but their probabilities are not readily available — and the core challenge is designing a loss trainable from samples rather than by likelihood maximization. They excel at image generation (e.g. photorealistic faces of people who never existed) and underpin unsupervised translation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]