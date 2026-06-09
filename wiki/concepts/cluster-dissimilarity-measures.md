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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:concept:cluster-dissimilarity-measures
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
tags:
- clustering
- unsupervised-learning
- metric-choice
title: Cluster Dissimilarity Measures
understanding: 0
---

## Definition
The specification of how unalike two objects are, supplied as input to a clustering algorithm — the choice that matters more for clustering success than the algorithm itself. Data arrive either directly as an N×N proximity matrix D (often subjective judgments, which must be symmetrized via (D+Dᵀ)/2 and need not satisfy the triangle inequality, so are not true distances) or as attribute vectors from which pairwise dissimilarities are built. The overall object dissimilarity is a weighted average over attributes D(x_i,x_{i'}) = Σ_j w_j d_j(x_{ij},x_{i'j}), Σ w_j = 1, with per-attribute measures depending on type: squared or absolute error for quantitative variables, rank-scaled treatment for ordinal, and an explicit M×M loss matrix for categorical/nominal. A key subtlety: equal weights w_j do NOT give equal influence — the relative influence of attribute j is w_j·d̄_j where d̄_j is its average dissimilarity (proportional to var_j under squared error), so setting w_j∝1/d̄_j equalizes influence, though this is often counterproductive when only some attributes carry the grouping signal.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]