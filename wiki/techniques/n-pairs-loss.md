---
aliases: []
also_type: []
analogous-to:
- mutual-information
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
- self-supervised-learning
id: pkis:technique:n-pairs-loss
instantiates:
- cross-entropy-loss
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- InfoNCE
- NT-Xent
- contrastive
- temperature
- self-supervised
- CPC
title: N-Pairs Loss (InfoNCE / NT-Xent)
understanding: 0
---

## Definition
$$\mathcal{L}(\theta;x,x^+,\{x_k^-\}_{k=1}^{N-1}) = -\log\frac{\exp(\hat{e}(x)^T\hat{e}(x^+))}{\exp(\hat{e}(x)^T\hat{e}(x^+))+\sum_{k=1}^{N-1}\exp(\hat{e}(x)^T\hat{e}(x_k^-))}$$

This is a softmax cross-entropy over one positive and $N{-}1$ negatives for each anchor; also called **InfoNCE** (used in CPC) or **NT-Xent** when inner products are scaled by a temperature $\tau$.

### Why it matters
N-pairs loss provides a stronger learning signal than triplet loss by contrasting one positive against many negatives simultaneously. When $N=2$ it reduces to the logistic loss, connecting metric learning to binary classification. The temperature parameter controls the geometry of the embedding hypersphere, and the loss forms the backbone of modern self-supervised contrastive methods (SimCLR, MoCo).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mutual-information]] — analogous-to: InfoNCE is a lower bound on mutual information between views
- [[cross-entropy-loss]] — instantiates: N-pairs loss is a softmax cross-entropy over positive vs. negative embeddings
[To be populated during integration]