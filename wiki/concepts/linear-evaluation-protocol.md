---
aliases: []
also_type: []
applies:
- contrastive-representation-learning
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- pretraining-and-fine-tuning
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- representation-learning
id: pkis:concept:linear-evaluation-protocol
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- self-supervised
- transfer-learning
- benchmark
- probing
- fine-tuning
title: Linear Evaluation Protocol
understanding: 0
uses:
- transfer-learning
- logistic-regression
- linear-separability
---

## Definition
A standard benchmark for self-supervised and transfer representations in which the pretrained encoder is **frozen** and only a linear classifier (typically $L_2$-regularised logistic regression) is trained on top of the extracted features:

$$\hat{y} = \text{softmax}(Wf_\theta(x) + b), \quad W, b \text{ only trained}.$$

Accuracy on a held-out set is used as a proxy for the quality of the representation. When features fit in memory, full-batch methods such as L-BFGS are preferred for accurate optimisation; otherwise SGD with careful learning-rate tuning is used.

### Why it matters
Linear evaluation tests whether task-relevant information is **linearly accessible** in the representation, isolating representation quality from the ability of a nonlinear head to compensate for a poor representation. It is the canonical comparison point in the self-supervised learning literature, complementing full fine-tuning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[pretraining-and-fine-tuning]] — contrasts-with
- [[contrastive-representation-learning]] — applies
- [[linear-separability]] — uses
- [[logistic-regression]] — uses
- [[transfer-learning]] — uses
[To be populated during integration]