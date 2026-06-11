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
- semi-supervised-learning
id: pkis:technique:pseudo-labeling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- semi-supervised
- self-training
- confirmation-bias
- knowledge-distillation
- low-data
title: Pseudo-Labeling (Self-Training for SSL)
understanding: 0
---

## Definition
Pseudo-labeling (self-training) iteratively uses a model trained on labeled data $D_L$ to generate predicted labels $\hat{y}$ for unlabeled data $D_U$, then retrains on $D_L \cup \{(x,\hat{y})\}$. Two main variants exist:
- **Offline**: relabel all of $D_U$, retrain to convergence, repeat.
- **Online**: continuously label random batches and train immediately.

A confidence threshold (e.g., $\max_c p_\theta(y=c|x) > \tau$) filters pseudo-labels to mitigate *confirmation bias* — the tendency for incorrect predictions to reinforce themselves through subsequent training.

### Why it matters
Pseudo-labeling is model-agnostic and simple to implement, making it one of the most widely applied semi-supervised techniques. It scales to very large unlabeled corpora (offline variant) and is a component in state-of-the-art pipelines such as SimCLRv2. Knowledge distillation (training a student on teacher soft predictions) can be viewed as a generalisation of pseudo-labeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]