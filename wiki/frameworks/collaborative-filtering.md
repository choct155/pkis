---
aliases: []
also_type: []
analogous-to:
- word-embeddings
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
- recommender-systems
id: pkis:framework:collaborative-filtering
instantiates:
- low-rank-matrix-approximation
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- matrix-factorization-recommender
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
- murphy-pml1-intro-ch22
tags:
- matrix-factorisation
- recommender
- embeddings
- SVD
- Netflix
title: Collaborative Filtering with Latent Factor Models
understanding: 0
uses:
- matrix-decompositions
- singular-value-decomposition
- restricted-boltzmann-machine
---

## Definition
Collaborative filtering predicts the preference of user $u$ for item $i$ from observed rating matrix $R$ by learning low-dimensional user embeddings $\mathbf{a}_u \in \mathbb{R}^d$ and item embeddings $\mathbf{b}_i \in \mathbb{R}^d$. The bilinear (matrix factorisation) model predicts
$$\hat{R}_{u,i} = \mu_u + \nu_i + \mathbf{a}_u^\top \mathbf{b}_i,$$
where $\mu_u$ and $\nu_i$ are user and item bias terms. Parameters are estimated by minimising squared error on observed entries:
$$\min_{\{\mathbf{a}_u\},\{\mathbf{b}_i\}} \sum_{(u,i)\in\Omega}(R_{u,i} - \hat{R}_{u,i})^2 + \text{regularisation}.$$
Missing entries are ignored (not set to zero), avoiding the biased imputation of plain SVD.

### Why it matters
The dominant paradigm for recommender systems; matrix factorisation won the Netflix Prize and forms the backbone of most modern recommendation engines; naturally extends to deep architectures (RBMs, neural CF) and to content-based systems via learned item/user embeddings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[matrix-factorization-recommender]] — prerequisite-of
- [[low-rank-matrix-approximation]] — instantiates
- [[restricted-boltzmann-machine]] — uses
- [[word-embeddings]] — analogous-to
- [[singular-value-decomposition]] — uses
- [[matrix-decompositions]] — uses
[To be populated during integration]