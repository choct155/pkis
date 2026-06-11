---
aliases: []
also_type: []
analogous-to:
- transfer-learning
- partial-pooling-shrinkage
applies:
- neural-networks
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
- deep-learning
- regularization
id: pkis:technique:multi-task-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
specializes:
- regularization
tags:
- multi-task-learning
- shared-representation
- regularization
- transfer-learning
- generalization
title: Multi-Task Learning
understanding: 0
uses:
- inductive-bias
---

## Definition
A training paradigm in which a shared representation $\mathbf{h}^{\text{shared}}$ is learned jointly across $T$ related tasks $\{(\mathbf{x}, y^{(t)})\}_{t=1}^T$, with shared lower-layer parameters and task-specific upper-layer parameters:
$$\min_{\boldsymbol{\theta}_{\text{shared}},\, \{\boldsymbol{\theta}_t\}} \sum_{t=1}^T \mathcal{L}_t\bigl(f_t(\mathbf{h}(\mathbf{x};\boldsymbol{\theta}_{\text{shared}});\boldsymbol{\theta}_t),\, y^{(t)}\bigr)$$

Shared parameters receive gradient signal from all tasks, effectively increasing their sample size and acting as a soft regularizer that pushes them toward values that generalize across tasks.

### Why it matters
Multi-task learning improves generalization when tasks share latent factors; the shared representation pools statistical strength across tasks just as additional training data would. It is widely used in NLP (joint POS/NER/parsing), computer vision (joint detection/segmentation), and robotics. Improved generalization bounds (Baxter, 1995) formalize the benefit in terms of reduced sample complexity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partial-pooling-shrinkage]] — analogous-to: Both pool statistical strength across tasks/groups
- [[neural-networks]] — applies
- [[inductive-bias]] — uses
- [[transfer-learning]] — analogous-to
- [[regularization]] — specializes
[To be populated during integration]