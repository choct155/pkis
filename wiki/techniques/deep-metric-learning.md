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
- metric-learning
id: pkis:technique:deep-metric-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- embedding
- hypersphere
- contrastive
- triplet
- siamese
- deep-learning
title: Deep Metric Learning (DML)
understanding: 0
---

## Definition
Given an embedding function $f(x;\theta)\in\mathbb{R}^L$ with $\ell_2$-normalized outputs $\hat{e}=e/\|e\|_2$, deep metric learning trains $\theta$ so that semantically similar pairs satisfy $\|\hat{e}_i - \hat{e}_j\|_2 \ll \|\hat{e}_i - \hat{e}_k\|_2$ whenever $y_i=y_j\neq y_k$. Distances are measured either by normalized Euclidean distance $\|\hat{e}_i-\hat{e}_j\|_2^2 = 2-2\hat{e}_i^T\hat{e}_j$ or cosine similarity $\hat{e}_i^T\hat{e}_j$.

### Why it matters
DML decouples representation learning from classification, enabling retrieval, verification, and few-shot recognition without retraining when new classes appear. Using a DNN as $f$ sidesteps the curse of dimensionality by mapping raw inputs to a compact hyperspherical manifold where Euclidean geometry is semantically meaningful.

### Key loss functions
Common objectives include contrastive loss (pairwise), triplet loss (anchor–positive–negative triples), N-pairs / InfoNCE loss (one positive vs. $N{-}1$ negatives), and proxy-based losses that reduce $O(N^3)$ mining cost to $O(NC)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]