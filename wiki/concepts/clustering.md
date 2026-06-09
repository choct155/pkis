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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:concept:clustering
instantiates:
- unsupervised-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch20
tags:
- unsupervised-learning
- density-estimation
- compression
title: Clustering
understanding: 0
uses:
- vector-quantization
- cluster-dissimilarity-measures
---

## Definition
The operation of taking a set of $N$ objects and grouping them into $K$ clusters of mutually similar items, so that a brief cluster label substitutes for a full description of each object. As an inference task, clustering posits latent cluster labels $\{k^{(n)}\}$ that are assumed meaningful and seeks parameters (e.g. cluster centres $\{\mathbf{m}^{(k)}\}$) under which the data are well described.

### Why clustering matters
MacKay identifies four motivations. (1) **Prediction**: a good clustering has predictive power — knowing an object's cluster fills in uncertain-but-useful attribute predictions, with objective the data's information content $\log 1/P(\{x\})$. This framing is *mixture density modelling*. (2) **Lossy compression / communication**: a category name is enough to identify an object, so clusters enable economical description; in image coding this is *vector quantization*, sending template labels $k_1,\dots,k_N$. (3) **Anomaly detection**: objects the cluster model compresses poorly (a green thing that runs away) deserve special attention. (4) **Models of learning**: competitive-learning clustering algorithms model adaptation in neural systems.

### Two stances
Vector quantization supplies the distortion measure as part of the problem and treats centres as mere tools; data modelling instead treats cluster labels as meaningful latent variables and asks what objective function (and hence distance) the data justify.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cluster-dissimilarity-measures]] — uses: the supplied dissimilarity is the central, algorithm-independent input to any clustering method
- [[unsupervised-learning]] — instantiates
- [[vector-quantization]] — uses: Vector quantization is the lossy-compression motivation for clustering; cluster centres are the codebook.
[To be populated during integration]