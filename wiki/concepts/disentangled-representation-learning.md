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
- representation-learning
- generative-models
id: pkis:concept:disentangled-representation-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- beta-VAE
- identifiability
- latent-factors
- ICA
- causal-representation-learning
title: Disentangled Representation Learning
understanding: 0
---

## Definition
A representation $h = f_\theta(x)$ is **disentangled** if each dimension $h_i$ corresponds to a single ground-truth factor of variation $z_i$, up to permutation and element-wise reparameterisation: $h_i = \psi_i(z_i)$. Formally, a disentangled representation satisfies

$$p(h) = \prod_i p_i(h_i)$$

and there exists a matching between the indices of $h$ and $z$ such that each $h_i$ is a function only of $z_i$. Prominent methods include $\beta$-VAE, FactorVAE, and weakly-supervised approaches using paired data.

### Why it matters
Disentanglement is a key desideratum for representations that support systematic generalisation, interpretability, and sample-efficient downstream learning. The impossibility result of Locatello et al. shows that without additional assumptions or supervision, unsupervised disentanglement is provably unidentifiable, shifting the field toward weakly-supervised and causal approaches.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]