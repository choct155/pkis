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
- statistics
id: pkis:concept:dendrogram
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- visualization
- hierarchical-clustering
- tree
- unsupervised-learning
title: Dendrogram
understanding: 0
---

## Definition
A dendrogram is a rooted binary tree produced by hierarchical agglomerative clustering (HAC) in which each leaf is a data point, each internal node records the height (dissimilarity) at which two sub-clusters were merged, and the full tree encodes a complete nested hierarchy of partitions. Cutting the tree at height $h$ yields all clusters whose inter-cluster dissimilarity is $\leq h$.

The horizontal axis labels data points and the vertical axis represents the dissimilarity scale, so the visual shape immediately reveals cluster structure and separation.

### Why it matters
Dendrograms let a practitioner defer the choice of the number of clusters $K$ until after fitting: different cuts produce different $K$ without re-running the algorithm. They are a standard visualization tool in bioinformatics (e.g., gene expression analysis) and document clustering.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]