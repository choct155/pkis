---
aliases: []
also_type: []
analogous-to:
- kernel-pca
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:spectral-clustering
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
specializes:
- clustering
tags:
- clustering
- unsupervised-learning
- graph-methods
- non-convex-clusters
title: Spectral Clustering
understanding: 0
uses:
- eigendecomposition
- k-means-clustering
- the-kernel-trick
---

## Definition
A clustering generalization that finds non-convex groups (e.g. concentric circles) on which metric methods like K-means fail. From an N×N similarity matrix s_{ii'} ≥ 0 (commonly the radial-kernel gram matrix exp(−d²_{ii'}/c)) one builds a weighted similarity graph — typically a mutual K-nearest-neighbor graph that zeroes non-local similarities to capture local neighborhood structure — with adjacency matrix W, degree matrix G (g_i = Σ_{i'} w_{ii'}), and **graph Laplacian** L = G − W (or a normalized variant ÃL = I − G⁻¹W). One extracts the m eigenvectors Z of the smallest eigenvalues of L (ignoring the trivial constant vector) and runs K-means on the rows of Z. It works because fᵀLf = ½Σ w_{ii'}(f_i−f_{i'})², so low-energy eigenvectors are nearly constant within strongly connected components; a graph with m connected components has exactly m zero eigenvalues whose eigenspace is spanned by component indicator vectors, and in practice weak inter-cluster links turn these into small eigenvalues. With a normalized Laplacian, P = G⁻¹W is a random-walk transition matrix and clusters are groups the walk rarely leaves. Closely related to kernel PCA on the smallest eigenvalues of I−ÃK.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[the-kernel-trick]] — uses: similarity matrix is the radial-kernel gram matrix exp(−d²/c)
- [[kernel-pca]] — analogous-to: Laplacian eigenproblem nearly matches kernel PCA on I−ÃK; both built from a radial-kernel gram matrix
- [[k-means-clustering]] — uses: runs K-means on the rows of the Laplacian eigenvector matrix Z
- [[eigendecomposition]] — uses: clusters the eigenvectors of the smallest eigenvalues of the graph Laplacian
- [[clustering]] — specializes: a graph-partition clustering that handles non-convex groups where metric K-means fails
[To be populated during integration]