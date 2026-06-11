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
- probabilistic-graphical-models
- deep-learning
id: pkis:concept:sigmoid-belief-net
instantiates:
- latent-variable-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- variational-autoencoder
related_concepts: []
sources:
- murphy-pml2-advanced-ch04
specializes:
- bayesian-networks
tags:
- deep-generative-model
- variational-inference
- binary-latent
- logistic-regression
title: Sigmoid Belief Net
understanding: 0
uses:
- elbo
- activation-functions
- explaining-away
---

## Definition
A directed deep generative model with binary latent variables where each CPD is a logistic regression:
$$p(z_{\ell,k} \mid z_{\ell+1}) = \text{Ber}\!\left(\sigma(w_{\ell,k}^T z_{\ell+1})\right), \quad \sigma(u)=\frac{1}{1+e^{-u}}$$
stacked across $L$ layers, giving a hierarchical model $p(x,z) = p(z_L)\prod_{\ell} p(z_\ell\mid z_{\ell+1})\, p(x\mid z_1)$.

A neural-network generative model whose posterior is intractable (explaining-away couples all latents), motivating variational and amortized inference.

### Why it matters
Sigmoid belief nets were the first trainable deep latent variable models and directly inspired the Helmholtz machine and variational autoencoders. Their intractable posterior (due to explaining away across layers) was the key motivation for the wake-sleep algorithm and later ELBO-based training.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[explaining-away]] — uses: Explaining away in the posterior motivates amortized variational inference
- [[activation-functions]] — uses
- [[elbo]] — uses
- [[variational-autoencoder]] — prerequisite-of
- [[latent-variable-models]] — instantiates
- [[bayesian-networks]] — specializes
[To be populated during integration]