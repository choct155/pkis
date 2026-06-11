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
- geometry
- deep-learning
generalizes:
- graph-neural-networks
- convolutional-neural-networks
id: pkis:concept:geometric-deep-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- non-Euclidean
- graph-neural-networks
- manifold-learning
- equivariance
- GDL
title: Geometric Deep Learning
understanding: 0
uses:
- graph-convolutional-network
- hyperbolic-graph-embeddings
---

## Definition
Geometric Deep Learning (GDL) is the research programme of extending deep neural networks to data defined on non-Euclidean domains — graphs, manifolds, point clouds, and meshes — where standard Euclidean operations (e.g. shift-invariant convolution) do not apply.

The central challenge is that non-Euclidean domains lack a canonical notion of translation, fixed neighbourhood structure, or global coordinate system, making it impossible to directly reuse Euclidean convolutional filters across locations.

### Why it matters
GDL encompasses spectral graph convolutions (GCN), spatial methods (GraphSAGE, GAT, MoNet), hyperbolic embeddings, and equivariant networks. It provides the theoretical grounding — via group equivariance and the geometric priors framework (Bronstein et al. 2021) — for understanding why certain architectures are appropriate for certain data types. Applications span molecular design, social-network analysis, 3-D shape analysis, and physics simulations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hyperbolic-graph-embeddings]] — uses
- [[graph-convolutional-network]] — uses
- [[convolutional-neural-networks]] — generalizes
- [[graph-neural-networks]] — generalizes
[To be populated during integration]