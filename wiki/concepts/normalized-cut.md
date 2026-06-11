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
- graph-theory
- combinatorics
id: pkis:concept:normalized-cut
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- graph-partitioning
- spectral-clustering
- np-hard
- combinatorial-optimization
title: Normalized Cut (Graph Partitioning)
understanding: 0
uses:
- spectral-clustering
---

## Definition
For a weighted undirected graph $G=(V,W)$, a $K$-way partition $S_1,\ldots,S_K$ has **cut weight** $\text{cut}(S_k,\bar{S}_k) = \sum_{i\in S_k, j\notin S_k} w_{ij}$ and **volume** $\text{vol}(S_k) = \sum_{i\in S_k} d_i$. The **normalized cut** objective is:
$$\text{Ncut}(S_1,\ldots,S_K) = \frac{1}{2}\sum_{k=1}^K \frac{\text{cut}(S_k,\bar{S}_k)}{\text{vol}(S_k)}$$
Minimizing Ncut is NP-hard in the binary case, but a continuous relaxation via the eigenvectors of the normalized graph Laplacian $L_{\text{sym}}$ provides a tractable approximation (spectral clustering).

### Why it matters
Ncut balances between small inter-cluster edge weight and large intra-cluster connectivity, preventing the degenerate solution of isolating single nodes that plagues the unnormalized min-cut. It is the combinatorial objective that spectral clustering approximately solves.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[spectral-clustering]] — uses
[To be populated during integration]