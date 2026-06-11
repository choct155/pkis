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
- graph-learning
- linear-algebra
- spectral-methods
id: pkis:concept:graph-laplacian
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- spectral-graph-theory
- Laplacian
- eigendecomposition
- graph-smoothness
- GCN
title: Graph Laplacian
understanding: 0
---

## Definition
For a weighted graph with adjacency matrix $\mathbf{W}$ and degree matrix $\mathbf{D}$ (diagonal, $D_{ii}=\sum_j W_{ij}$), the (combinatorial) graph Laplacian is
$$\mathbf{L} = \mathbf{D} - \mathbf{W}$$
and the symmetric normalised Laplacian is $\mathbf{L}_{\text{sym}} = \mathbf{D}^{-1/2}\mathbf{L}\mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2}\mathbf{W}\mathbf{D}^{-1/2}$. A key identity is
$$\mathbf{z}^\top \mathbf{L}\mathbf{z} = \frac{1}{2}\sum_{i,j}W_{ij}(z_i - z_j)^2 \geq 0$$
showing $\mathbf{L}$ is positive semi-definite. Its smallest eigenvalue is 0 (eigenvector $\mathbf{1}$) for connected graphs.

The graph Laplacian generalises the discrete Laplace operator to irregular domains and measures the smoothness of a signal defined on graph nodes.

### Why it matters
The Laplacian appears throughout graph learning: Laplacian Eigenmaps use its eigenvectors as low-dimensional embeddings; GCN normalises the adjacency with $\mathbf{D}^{-1/2}(\mathbf{A}+\mathbf{I})\mathbf{D}^{-1/2}$; label propagation uses it as a smoothness regulariser; and spectral graph convolutions are defined via its eigendecomposition. It also provides the theoretical bridge between graph structure and signal processing.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]