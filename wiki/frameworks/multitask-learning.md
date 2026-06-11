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
id: pkis:framework:multitask-learning
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- transfer-learning
- shared-representations
- multi-objective
- generalization
title: Multitask Learning
understanding: 0
---

## Definition
$$f^* = \arg\min_f \sum_{j=1}^J \sum_{n=1}^{N_j} \ell_j\!\left(y_n^j,\, f(x_n^j, j)\right)$$

Multitask learning (MTL) trains a single model $f(x, j)$ to perform well on $J \geq 2$ related tasks simultaneously, exploiting shared structure across tasks to improve data efficiency and generalization.

### Why it matters
Shared representations can act as a regularizer, reducing overfitting on individual tasks with small datasets. The most common architecture is a shared trunk (feature extractor) with task-specific output heads. However, MTL can suffer from *negative transfer* or *task interference* when tasks are poorly correlated.

### Relation to domain generalization and meta-learning
MTL differs from domain generalization (DG) in that DG only targets a new unseen distribution, while MTL aims for accuracy on all training distributions. MTL differs from meta-learning in that it does not explicitly optimize for fast adaptation to new tasks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]