---
aliases: []
also_type: []
applies:
- imitation-learning
- distribution-shift
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
extends:
- generative-adversarial-network-framework
id: pkis:technique:conditional-gan
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- conditional-generation
- image-translation
- pix2pix
- CycleGAN
- GAN
title: Conditional GAN
understanding: 0
---

## Definition
A conditional GAN (cGAN) learns an implicit conditional distribution $q_\theta(x|y)$ by providing conditioning information $y$ to both the generator and discriminator:
$$\min_\theta\max_\phi\;\tfrac{1}{2}\mathbb{E}_{p(y)}\mathbb{E}_{p^*(x|y)}[\log D_\phi(x,y)]+\tfrac{1}{2}\mathbb{E}_{p(y)}\mathbb{E}_{q(z)}[\log(1-D_\phi(G_\theta(z,y),y))]$$
For discrete labels, an auxiliary classification loss $L_c$ trains the critic to classify both real and generated samples into $K$ classes, yielding a combined objective. Key variants include pix2pix (paired image translation with a U-net generator and patchGAN discriminator) and CycleGAN (unpaired translation with a cycle-consistency loss $L_{\text{cycle}}=\mathbb{E}_{p(x)}\|F(G(x))-x\|_1+\mathbb{E}_{p(y)}\|G(F(y))-y\|_1$).

### Why it matters
Conditional GANs enable fine-grained control over generated outputs, supporting applications from class-conditional image synthesis to image-to-image translation, text-to-speech, and domain adaptation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[distribution-shift]] — applies: Domain adaptation via CycleGAN addresses distribution shift between source and target domains.
- [[imitation-learning]] — applies
- [[generative-adversarial-network-framework]] — extends
[To be populated during integration]