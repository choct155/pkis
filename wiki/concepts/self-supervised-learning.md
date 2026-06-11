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
- representation-learning
- nlp
id: pkis:concept:self-supervised-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch01
- murphy-pml1-intro-ch19
tags:
- pretext-task
- representation-learning
- unsupervised
- large-language-models
title: Self-Supervised Learning
understanding: 0
---

## Definition
An unsupervised representation-learning paradigm in which supervision signals are generated automatically from the unlabeled data itself via *pretext tasks*. Formally, for observed input $x$ split into two views $(x_1, x_2)$, the model learns $\hat{x}_1 = f(x_2; \theta)$ to predict one view from the other:
$$\hat{\theta} = \arg\min_\theta \mathbb{E}[\ell(x_1, f(x_2; \theta))]$$
Examples: masked language modeling (predict masked tokens), colorization (predict color from grayscale), contrastive prediction.

### Why it matters
Self-supervised learning has driven major breakthroughs in NLP (BERT, GPT) and vision (SimCLR, MAE). By leveraging vast amounts of unlabeled data, it produces rich representations that substantially reduce labeled-data requirements for downstream tasks, bridging the gap between unsupervised and supervised learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]