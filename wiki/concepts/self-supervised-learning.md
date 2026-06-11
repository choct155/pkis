---
aliases: []
also_type: []
analogous-to:
- contrastive-divergence
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
generalizes:
- word-embeddings
- masked-language-modeling
id: pkis:concept:self-supervised-learning
instantiates:
- masked-language-modeling
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- pretraining-and-fine-tuning
- transfer-learning-fine-tuning
related_concepts: []
sources:
- murphy-pml1-intro-ch01
- murphy-pml1-intro-ch19
specializes:
- unsupervised-learning
tags:
- pretext-task
- representation-learning
- unsupervised
- large-language-models
title: Self-Supervised Learning
understanding: 0
uses:
- supervised-learning
- transfer-learning
- mutual-information
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
- [[mutual-information]] — uses: Maximising I(x1;x2) between views motivates contrastive objectives.
- [[contrastive-divergence]] — analogous-to: Contrastive SSL objectives can be viewed as approximate MLE of energy-based models.
- [[masked-language-modeling]] — generalizes: MLM is an imputation/cloze SSL task.
- [[transfer-learning-fine-tuning]] — prerequisite-of: SSL pre-trains representations on unlabeled data; fine-tuning adapts them to downstream tasks.
- [[pretraining-and-fine-tuning]] — prerequisite-of
- [[word-embeddings]] — generalizes
- [[transfer-learning]] — uses
- [[masked-language-modeling]] — instantiates
- [[supervised-learning]] — uses
- [[unsupervised-learning]] — specializes
[To be populated during integration]