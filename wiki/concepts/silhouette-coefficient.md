---
aliases: []
also_type: []
analogous-to:
- rand-index
applies:
- k-means-clustering
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
- statistics
id: pkis:concept:silhouette-coefficient
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- model-selection
- clustering-evaluation
- k-means
- heuristic
title: Silhouette Coefficient
understanding: 0
---

## Definition
For a data point $i$ assigned to cluster $k_i$, define $a_i$ as the mean intra-cluster distance (to all other points in $k_i$) and $b_i$ as the mean distance to the nearest rival cluster $k'_i \neq k_i$. The **silhouette coefficient** is:
$$\text{sc}(i) = \frac{b_i - a_i}{\max(a_i, b_i)} \in [-1, +1]$$
Values near $+1$ indicate a compact, well-separated cluster membership; values near $0$ indicate a boundary point; values near $-1$ suggest misassignment. The **silhouette score** of a clustering is the mean $\text{sc}(i)$ over all $i$.

### Why it matters
Unlike reconstruction error (distortion), the silhouette score typically peaks at a genuine cluster structure and can therefore be used as a heuristic for selecting $K$. A **silhouette diagram** — a sorted bar chart of individual coefficients by cluster — simultaneously reveals cluster quality and cluster size without requiring 2D data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[rand-index]] — analogous-to: both are external or internal cluster quality measures
- [[k-means-clustering]] — applies
[To be populated during integration]