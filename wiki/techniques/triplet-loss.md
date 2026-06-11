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
- representation-learning
id: pkis:technique:triplet-loss
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- n-pairs-loss
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- ranking-loss
- hard-negatives
- face-recognition
- metric-learning
- anchor-positive-negative
title: Triplet Loss
understanding: 0
uses:
- hinge-loss
- hard-negative-mining
---

## Definition
$$\mathcal{L}(\theta;x_i,x_i^+,x_i^-) = \bigl[d_\theta(x_i,x_i^+)^2 - d_\theta(x_i,x_i^-)^2 + m\bigr]_+$$

For each anchor $x_i$, a positive example $x_i^+$ (same class) and a negative example $x_i^-$ (different class) are selected. The loss pushes the anchor–positive distance below the anchor–negative distance by at least margin $m$.

### Why it matters
Triplet loss ties positive and negative pair optimization into a single objective, making their magnitudes directly comparable—a key improvement over pairwise contrastive loss. It is used in FaceNet for face verification and in many image retrieval systems. Hard-negative mining within minibatches is essential: naïve enumeration costs $O(N^3)$, but filtering to *semi-hard negatives* ($d(a,p)<d(a,n)<d(a,p)+m$) dramatically reduces this cost.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[n-pairs-loss]] — prerequisite-of
- [[hard-negative-mining]] — uses
- [[hinge-loss]] — uses
[To be populated during integration]