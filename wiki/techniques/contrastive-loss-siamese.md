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
id: pkis:technique:contrastive-loss-siamese
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- triplet-loss
- n-pairs-loss
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- siamese
- pairwise-loss
- margin
- self-supervised
- metric-learning
title: Contrastive Loss and Siamese Networks
understanding: 0
uses:
- hinge-loss
---

## Definition
$$\mathcal{L}(\theta;x_i,x_j) = \mathbb{I}(y_i=y_j)\,d(x_i,x_j)^2 + \mathbb{I}(y_i\neq y_j)\,[m - d(x_i,x_j)]_+^2$$

where $d$ is a distance in embedding space and $m>0$ is a safety margin. Both inputs are processed by the *same* weight-shared encoder $f(\cdot;\theta)$ (hence *Siamese*), pulling positive pairs together and pushing negative pairs beyond margin $m$.

### Why it matters
Contrastive loss is among the earliest and most influential losses for learning similarity metrics from labeled pairs. It is the precursor to triplet loss, N-pairs loss, and InfoNCE, and remains the conceptual basis of modern self-supervised contrastive learning. The Siamese architecture enforces representation symmetry without requiring class labels at inference time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hinge-loss]] — uses
- [[n-pairs-loss]] — prerequisite-of
- [[triplet-loss]] — prerequisite-of: contrastive/pairwise loss is the conceptual predecessor to triplet loss
[To be populated during integration]