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
- recommender-systems
id: pkis:technique:autorec
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch22
tags:
- autoencoder
- collaborative-filtering
- nonlinear
- neural-recommender
title: 'AutoRec: Autoencoder-Based Recommender'
understanding: 0
---

## Definition
$$f(\mathbf{y}_{:,i};\theta) = \mathbf{W}^\top \varphi(\mathbf{V}\mathbf{y}_{:,i} + \boldsymbol{\mu}) + \mathbf{b}$$

where $\mathbf{y}_{:,i} \in \mathbb{R}^M$ is the (zero-imputed) rating column for item $i$, $\mathbf{V} \in \mathbb{R}^{K \times M}$ encodes it into a $K$-dimensional latent space, and $\mathbf{W} \in \mathbb{R}^{K \times M}$ decodes it back to a predicted rating vector. Training updates only parameters associated with observed ratings. A symmetric user-based variant exists.

### Why it matters
AutoRec shows that a single-hidden-layer autoencoder outperforms more complex models (RBMs, local low-rank methods) on standard benchmarks with far fewer parameters. It bridges matrix factorisation and deep learning for recommendation, motivating variational and deeper autoencoder extensions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]