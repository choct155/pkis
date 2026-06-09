---
aliases: []
also_type: []
analogous-to:
- principal-curves-surfaces
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
id: pkis:technique:self-organizing-map
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
specializes:
- k-means-clustering
tags:
- unsupervised-learning
- dimension-reduction
- clustering
- manifold-learning
title: Self-Organizing Map
understanding: 0
uses:
- principal-component-analysis
---

## Definition
A clustering/visualization technique (Kohonen) that places K prototypes m_j ∈ ℝ^p on a fixed low-dimensional (usually 2D rectangular) integer grid and fits them to data such that prototypes adjacent on the grid stay close in feature space — a *constrained* version of K-means in which centers are tied to a smooth manifold. In the online algorithm, observations are processed one at a time: the closest prototype m_j to x_i is found, and m_j together with its grid-neighbors m_k (within topological radius r) are moved toward x_i via m_k ← m_k + α(x_i−m_k), optionally weighted by a neighborhood function h(‖ℓ_j−ℓ_k‖). The learning rate α and radius r are decreased to zero over many passes; prototypes are typically initialized in the data's principal-component plane. As r shrinks so each neighborhood holds one point, the SOM reduces exactly to online K-means. Reasonableness of the manifold constraint is checked by comparing SOM reconstruction error Σ‖x−m_j‖² to that of unconstrained K-means. A batch version updates m_j as a weighted mean of points mapping to its neighbors, making it a discrete analog of principal surfaces.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[principal-curves-surfaces]] — analogous-to: both constrain prototypes to a smooth manifold; the batch SOM is a discrete version of a principal surface
- [[principal-component-analysis]] — uses: prototypes are initialized in the two-dimensional principal-component plane of the data
- [[k-means-clustering]] — specializes: K-means with prototypes constrained to a fixed low-dimensional grid; reduces to online K-means as the neighborhood shrinks
[To be populated during integration]