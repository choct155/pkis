---
aliases: []
also_type: []
applies:
- vanishing-gradient-problem
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
- machine-learning
- deep-learning
- optimization
extends:
- generative-adversarial-network-framework
id: pkis:concept:non-saturating-gan-loss
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- GAN
- loss-function
- gradient-flow
- training-stability
title: Non-Saturating GAN Loss
understanding: 0
---

## Definition
In the original (saturating) GAN, the generator minimises $\mathbb{E}_{q(z)}[\log(1-D_\phi(G_\theta(z)))]$, which saturates (near-zero gradient) when the discriminator easily rejects generated samples ($D_\phi(G_\theta(z))\approx 0$). The non-saturating loss replaces this with:
$$L_G^{\text{NS}}=-\mathbb{E}_{q(z)}[\log D_\phi(G_\theta(z))]$$
This objective provides a larger gradient when the generator is weak, since $-\log D_\phi(G_\theta(z))$ grows as $D_\phi(G_\theta(z))\to 0$.

### Why it matters
The non-saturating loss was introduced in the original GAN paper as a practical fix to vanishing gradients in early training. It breaks the zero-sum structure but is the most widely used generator loss in practice, illustrating that the game-theoretic formulation is best viewed as motivation rather than a strict constraint.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[vanishing-gradient-problem]] — applies: Designed to avoid vanishing generator gradients when the discriminator is strong.
- [[generative-adversarial-network-framework]] — extends
[To be populated during integration]