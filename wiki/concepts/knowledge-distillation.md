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
- deep-learning
- model-compression
id: pkis:concept:knowledge-distillation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- model-compression
- label-smoothing
- semi-supervised
- soft-targets
- temperature
title: Knowledge Distillation
understanding: 0
---

## Definition
Knowledge distillation trains a *student* model $S$ to mimic the *soft* output distribution of a larger pretrained *teacher* model $T$ by minimising
$$\mathcal{L}(T) = -\sum_{x_i\in D}\sum_y p^T(y|x_i;\tau)\log p^S(y|x_i;\tau)$$
where $\tau>0$ is a temperature parameter that softens the teacher's softmax, spreading probability mass to non-argmax classes and conveying richer inter-class similarity information than hard labels.

### Why it matters
Distillation enables **model compression**: a compact student can approach teacher accuracy because soft targets encode structured information about class relationships. It generalises pseudo-labeling (when $S=T$ it reduces to self-training) and label smoothing (uniform soft target). It is widely used to deploy large language/vision models on resource-constrained devices.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]