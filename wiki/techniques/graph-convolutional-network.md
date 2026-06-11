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
contrasts-with:
- graph-sage
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- graph-learning
- deep-learning
id: pkis:technique:graph-convolutional-network
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- variational-graph-auto-encoder
related_concepts: []
sources:
- murphy-pml1-intro-ch23
specializes:
- message-passing-neural-networks
tags:
- spectral-graph-convolution
- GCN
- semi-supervised
- Laplacian
- Kipf-Welling
title: Graph Convolutional Network (GCN)
understanding: 0
uses:
- graph-laplacian
- eigendecomposition
---

## Definition
A GCN (Kipf & Welling, 2017) is a spectrum-free spectral graph convolution method. For a two-layer network the propagation rule is
$$\mathbf{Z} = \text{softmax}\!\left(\tilde{\mathbf{A}}\, \text{ReLU}(\tilde{\mathbf{A}}\mathbf{X}\Theta^{(0)})\,\Theta^{(1)}\right)$$
where $\tilde{\mathbf{A}} = \hat{\mathbf{D}}^{-1/2}(\mathbf{A}+\mathbf{I})\hat{\mathbf{D}}^{-1/2}$ is the symmetrically normalised adjacency with added self-loops. Each layer computes a weighted average of neighbour features followed by a linear transform and nonlinearity.

GCNs approximate spectral convolutions with a first-order Chebyshev polynomial, avoiding an explicit eigendecomposition while still leveraging the graph Laplacian structure.

### Why it matters
GCN achieved state-of-the-art semi-supervised node classification on citation networks and became the default baseline for graph learning. It is the encoder in variational graph auto-encoders (VGAE) and many downstream architectures. Its limitation — requiring the full adjacency matrix at training time — motivates inductive methods like GraphSAGE and GAT.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[graph-sage]] — contrasts-with
- [[variational-graph-auto-encoder]] — prerequisite-of
- [[eigendecomposition]] — uses
- [[graph-laplacian]] — uses
- [[message-passing-neural-networks]] — specializes
[To be populated during integration]