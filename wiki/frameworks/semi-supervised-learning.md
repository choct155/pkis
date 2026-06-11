---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
extends:
- unsupervised-learning
- supervised-learning
id: pkis:framework:semi-supervised-learning
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- low-data
- cluster-assumption
- unlabeled-data
- representation-learning
title: Semi-Supervised Learning
understanding: 0
uses:
- variational-autoencoder
- generative-adversarial-network
---

## Definition
Semi-supervised learning (SSL) exploits a small labeled set $D_L = \{(x_i,y_i)\}$ together with a large unlabeled set $D_U=\{x_j\}$ to learn a predictive model better than could be obtained from $D_L$ alone. The central assumptions are:
- **Cluster assumption**: decision boundaries lie in low-density regions.
- **Manifold assumption**: nearby points share labels.
- **Smoothness assumption**: the model output varies slowly in high-density regions.

Key algorithmic families include: self-training / pseudo-labeling (Section 19.3.1), entropy minimization (19.3.2), co-training (19.3.3), label propagation (19.3.4), consistency regularization (19.3.5), and deep generative model approaches (VAE-M2, semi-supervised GANs, normalizing flows — Section 19.3.6).

### Why it matters
Labeled data is expensive; unlabeled data is often abundant. SSL bridges the gap, underpinning modern speech recognition, medical AI, and large-scale vision systems where full annotation is infeasible.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-adversarial-network]] — uses: Semi-supervised GANs extend the critic to output class labels plus fake class.
- [[variational-autoencoder]] — uses: VAE M1/M2 models use the ELBO on unlabeled data for semi-supervised learning.
- [[supervised-learning]] — extends
- [[unsupervised-learning]] — extends
[To be populated during integration]