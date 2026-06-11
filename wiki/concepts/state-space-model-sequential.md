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
- probabilistic-graphical-models
- time-series
generalizes:
- hidden-markov-model
- linear-dynamical-system
id: pkis:concept:state-space-model-sequential
instantiates:
- probabilistic-graphical-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
specializes:
- latent-variable-models
tags:
- sequential-data
- latent-variables
- markov-chain
- graphical-model
- state-space
title: State Space Model (Sequential Latent Variable)
understanding: 0
uses:
- markov-chains
- sum-product-algorithm
---

## Definition
$$p(x_1,\ldots,x_N, z_1,\ldots,z_N) = p(z_1)\prod_{n=2}^{N}p(z_n|z_{n-1})\prod_{n=1}^{N}p(x_n|z_n)$$

A directed graphical model for sequential data in which a Markov chain of latent variables $\{z_n\}$ drives observed variables $\{x_n\}$; the latent chain enforces the key conditional independence $z_{n+1}\perp z_{n-1}\mid z_n$ while the observed sequence can exhibit arbitrary long-range dependence mediated through the latents.

### Why it matters
Unifying framework that subsumes both the Hidden Markov Model (discrete latents) and the Linear Dynamical System (Gaussian latents) as special cases, enabling efficient O(K²N) or O(L²N) inference via the sum-product algorithm on a tree-structured graph. It escapes the parameter-explosion of high-order Markov models by compressing history into a fixed-dimensional hidden state.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sum-product-algorithm]] — uses
- [[latent-variable-models]] — specializes
- [[probabilistic-graphical-models]] — instantiates
- [[markov-chains]] — uses
- [[linear-dynamical-system]] — generalizes
- [[hidden-markov-model]] — generalizes
[To be populated during integration]