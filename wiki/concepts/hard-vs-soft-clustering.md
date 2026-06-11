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
- unsupervised-learning
id: pkis:concept:hard-vs-soft-clustering
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch28
tags:
- clustering
- mixture-model
- k-means
- responsibility
- posterior
title: Hard vs. Soft Clustering
understanding: 0
---

## Definition
Given responsibilities $r_{nk} = p(z_n = k \mid x_n, \theta)$ from a mixture model:
- **Hard clustering** assigns $\hat{z}_n = \arg\max_k r_{nk}$ — each point belongs to exactly one cluster.
- **Soft clustering** retains the full responsibility vector $r_{n\cdot}$ — each point is fractionally assigned to every cluster.

Hard clustering is a special case that recovers K-means when the GMM uses uniform weights and spherical covariances: $\hat{z}_n = \arg\min_k \|x_n - \mu_k\|_2^2$.

### Why it matters
The hard/soft distinction reflects the trade-off between interpretability (crisp assignments) and probabilistic completeness (uncertainty in cluster identity). Soft assignments are essential for downstream inference (e.g., semi-supervised learning), while hard assignments reduce memory and enable faster nearest-centroid operations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]