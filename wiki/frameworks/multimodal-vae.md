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
- machine-learning
- multimodal-learning
extends:
- variational-autoencoder
id: pkis:framework:multimodal-vae
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- product-of-experts
- multimodal
- missing-data
- semi-supervised
title: Multimodal VAE (MVAE)
understanding: 0
uses:
- missing-data-mechanisms
---

## Definition
A multimodal VAE models $M$ conditionally independent modalities given a shared latent $z$:

$$p_\theta(x_1,\ldots,x_M,z) = p(z)\prod_{m=1}^M p_\theta(x_m|z)$$

The key inference challenge is computing $q_\phi(z|X)$ for arbitrary subsets of observed modalities. Under the Gaussian product-of-experts (PoE) formula, the joint posterior precision is the sum of individual expert precisions:

$$\Sigma^{-1} = \sum_{m=0}^M \Lambda_m, \quad \mu = \Sigma\sum_{m=0}^M \Lambda_m\mu_m$$

Training uses a sum of ELBOs over the fully observed joint, all marginals, and random subsets (Equation 21.48).

### Why it matters
MVAEs enable learning across heterogeneous data types (e.g., images and text) with limited paired data by leveraging the much larger sets of unpaired unimodal data. The PoE aggregation rule makes inference modular and handles arbitrary missingness patterns at test time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[missing-data-mechanisms]] — uses
- [[variational-autoencoder]] — extends
[To be populated during integration]