---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- generative-modeling
id: pkis:technique:bidirectional-gan
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- inference
- encoder
- GAN
- latent-variable
- BiGAN
title: Bidirectional GAN (BiGAN)
understanding: 0
---

## Definition
BiGAN (bidirectional GAN) / ALI (adversarially learned inference) augments the GAN framework with a learned encoder $E_\zeta: x\mapsto z$ to perform posterior inference. A discriminator $D_\phi$ learns to distinguish joint pairs $(x, E_\zeta(x))$ with $x\sim p^*$ (real) from $(G_\theta(z), z)$ with $z\sim q(z)$ (fake):
$$\min_{\theta,\zeta}\max_\phi\;\mathbb{E}_{p^*(x)}[\log D_\phi(x,E_\zeta(x))]+\mathbb{E}_{q(z)}[\log(1-D_\phi(G_\theta(z),z))]$$
Under global optimality, the encoder and generator are inverses: $E_\zeta(G_\theta(z))=z$ and $G_\theta(E_\zeta(x))=x$.

### Why it matters
BiGAN simultaneously learns a generative model and an inference (encoding) network without requiring a reconstruction loss, providing a GAN-based alternative to VAE inference. It demonstrates that the adversarial principle can match joint distributions, not just marginals.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]