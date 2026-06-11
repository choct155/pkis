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
id: pkis:technique:matrix-factorization-recommender
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch22
tags:
- collaborative-filtering
- matrix-completion
- low-rank
- embedding
- netflix-prize
title: Matrix Factorization for Recommendation
understanding: 0
---

## Definition
$$\hat{y}_{ui} = \mu + b_u + c_i + \mathbf{u}_u^\top \mathbf{v}_i$$

where $\mathbf{U} \in \mathbb{R}^{M \times K}$ and $\mathbf{V} \in \mathbb{R}^{N \times K}$ are learned user and item embedding matrices, $b_u$ and $c_i$ are bias terms, and $K \ll \min(M,N)$ is the latent rank. The observed-entry loss with $\ell_2$ regularisation is

$$\mathcal{L}(\theta) = \sum_{(u,i): Y_{ui} \neq ?} (y_{ui} - \hat{y}_{ui})^2 + \lambda\bigl(b_u^2 + c_i^2 + \|\mathbf{u}_u\|^2 + \|\mathbf{v}_i\|^2\bigr)$$

The low-rank assumption encodes the belief that user preferences are governed by a small number of latent factors; proximity of a user vector and an item vector in the latent space indicates preference.

### Why it matters
Matrix factorisation (popularised by Simon Funk and the BellKor team during the Netflix Prize) remains the foundational baseline for collaborative filtering. It is optimised via ALS or SGD and generalises naturally to the probabilistic PMF formulation, exponential-family variants, and neural extensions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]