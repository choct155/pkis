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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:multidimensional-scaling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
tags:
- unsupervised-learning
- dimension-reduction
- visualization
- embedding
title: Multidimensional Scaling
understanding: 0
---

## Definition
A dimension-reduction/visualization technique that embeds N objects into a low-dimensional (usually 2D) Euclidean space from a matrix of pairwise dissimilarities d_{ii'}, placing points so that interpoint distances reproduce the input dissimilarities as closely as possible. Unlike PCA it operates directly on a proximity/dissimilarity matrix rather than on raw attribute coordinates, so it can be applied whenever only distances are available (e.g. subjective dissimilarity judgments). In ESL it is used to display clustering results geometrically — e.g. plotting the K-medoid country clusters in 2D, where the MDS layout reveals that Egypt sits halfway between two clusters — and as an alternative rule for ordering dendrogram leaves. It connects to spectral methods via local MDS variants that, like spectral clustering, encode local neighborhood structure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]