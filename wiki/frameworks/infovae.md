---
aliases: []
also_type: []
analogous-to:
- generative-adversarial-network
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
- machine-learning
- variational-inference
- information-theory
generalizes:
- variational-autoencoder
id: pkis:framework:infovae
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- MMD
- mutual-information
- generative-model
title: InfoVAE
understanding: 0
uses:
- aggregated-posterior
- mutual-information
- kl-divergence
---

## Definition
$$\mathcal{L}(\theta,\phi|x) = -\lambda D_{KL}(q_\phi(z)\|p_\theta(z)) - \mathbb{E}_{q_\phi(z)}[D_{KL}(q_\phi(x|z)\|p_\theta(x|z))] + \alpha\,I_q(x;z)$$

InfoVAE generalises the standard ELBO by separately weighting the KL between the aggregated posterior and the prior ($\lambda$) and adding an explicit mutual-information term ($\alpha$). By choosing $\alpha=0,\lambda=1$ one recovers the standard ELBO; $\alpha=1$ yields the MMD-VAE; $\alpha=1-\lambda$ yields the β-VAE.

### Why it matters
The InfoVAE objective addresses two known deficiencies of the standard ELBO: tendency to ignore the latent code (posterior collapse) and tendency to learn a poor posterior approximation due to the mismatch between KL terms in data space and latent space. It unifies β-VAE, MMD-VAE, and adversarial autoencoders under one framework and comes with a global optimality guarantee (Theorem 1 in the chapter).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-adversarial-network]] — analogous-to: MMD-VAE special case uses implicit density matching as in GANs
- [[kl-divergence]] — uses
- [[mutual-information]] — uses
- [[aggregated-posterior]] — uses
- [[variational-autoencoder]] — generalizes
[To be populated during integration]