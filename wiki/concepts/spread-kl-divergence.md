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
- machine-learning
- generative-models
- information-theory
extends:
- kl-divergence
id: pkis:concept:spread-kl-divergence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- variational-autoencoder
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- KL-divergence
- manifold
- smoothing
- delta-VAE
- generative-models
title: Spread KL Divergence
understanding: 0
uses:
- manifold-hypothesis
---

## Definition
The **spread KL divergence** [Zhang et al. 2020] is a smoothed version of the KL divergence designed to remain finite when the supports of $p$ and $q$ do not overlap:
$$D_{\mathrm{KL}}^\sigma(p \| q) = D_{\mathrm{KL}}(p_\sigma \| q_\sigma),$$
where $p_\sigma = p \circledast \mathcal{N}(\cdot|0, \sigma^2 I_D)$ and $q_\sigma = q \circledast \mathcal{N}(\cdot|0, \sigma^2 I_D)$ are Gaussian-smoothed versions of $p$ and $q$.

Smoothing ensures both distributions have full support over $\mathbb{R}^D$, so the KL is always finite even when $p$ lives on a low-dimensional manifold.

### Why it matters
The spread KL motivates the **delta-VAE**: a latent variable model $q(x) = \mathcal{N}(x|g_\theta(z), \sigma^2 I)$ with $z \sim \mathcal{N}(0, I_d)$. After training with spread KL, the decoder noise $\sigma$ can be set to zero so $q$ recovers the manifold geometry of $p$. This provides a principled alternative to standard VAE training when data lies on a low-dimensional manifold.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[manifold-hypothesis]] — uses
- [[variational-autoencoder]] — prerequisite-of: Motivates delta-VAE variant
- [[kl-divergence]] — extends
[To be populated during integration]