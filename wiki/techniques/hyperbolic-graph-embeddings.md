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
- graph-learning
- geometry
id: pkis:technique:hyperbolic-graph-embeddings
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- hyperbolic-geometry
- Poincaré-embedding
- Lorentz-model
- hierarchical-graphs
- Riemannian-optimization
title: Hyperbolic Graph Embeddings (Poincaré / Lorentz)
understanding: 0
---

## Definition
Embeddings are placed in hyperbolic space — either the Poincaré ball model or the Lorentz (hyperboloid) model — where the distance between two points $\mathbf{Z}_i, \mathbf{Z}_j$ in the Poincaré ball is
$$d_{\text{Poincaré}}(\mathbf{Z}_i, \mathbf{Z}_j) = \text{arcosh}\!\left(1 + 2\frac{\|\mathbf{Z}_i - \mathbf{Z}_j\|_2^2}{(1-\|\mathbf{Z}_i\|_2^2)(1-\|\mathbf{Z}_j\|_2^2)}\right)$$
and optimised using Riemannian gradient descent to keep embeddings on the manifold.

Hyperbolic space grows exponentially with radius, mirroring the combinatorial growth of trees, so hierarchical graphs embed with far less distortion than in Euclidean space of the same dimension.

### Why it matters
Nickel & Kiela (2017, 2018) showed that even two-dimensional Poincaré embeddings rival high-dimensional Euclidean embeddings for WordNet noun hierarchies. Extensions include mixed-curvature product spaces (for graphs combining tree-like and cyclic structure) and Hyperbolic GCNs (HGCN), which apply graph convolutions in hyperbolic space via the Euclidean tangent-space map.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]