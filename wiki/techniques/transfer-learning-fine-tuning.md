---
aliases: []
also_type: []
applies:
- distribution-shift
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
- nlp
- computer-vision
id: pkis:technique:transfer-learning-fine-tuning
instantiates:
- pretraining-and-fine-tuning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- pre-training
- fine-tuning
- representation-learning
- low-data
- domain-shift
title: Transfer Learning and Fine-Tuning
understanding: 0
uses:
- regularization
- data-augmentation
---

## Definition
Transfer learning trains a model on a large source dataset $D_p$, then adapts its parameters to a smaller target dataset $D_q$ via *fine-tuning*. Concretely, given a pretrained model $p(y|x,\theta_p)$ with shared feature extractor $h(x;\theta_1)$ and source head $(\mathbf{W}_2,\mathbf{b}_2)$, fine-tuning replaces the head with $q(y|x,\theta_q) = \text{softmax}(\mathbf{W}_3 h(x;\theta_1)+\mathbf{b}_3)$ and optimises $\theta_q = (\theta_1,\mathbf{W}_3,\mathbf{b}_3)$, optionally freezing $\theta_1$ or updating it with a reduced learning rate.

### Why it matters
Pretrained representations encode general domain structure (edges, textures, grammar) that is expensive to learn from scratch. Fine-tuning transfers this structure to data-scarce target tasks, often yielding large accuracy gains and faster convergence. Frozen-$\theta_1$ fine-tuning reduces the problem to convex optimisation, critical for long-tail and medical settings.

### Variants
Supervised pre-training (ImageNet → CNNs), self-supervised pre-training (masked language modelling → transformers), and *adapters* (Section 19.2.2) that keep the backbone frozen and introduce small trainable bottleneck modules.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[data-augmentation]] — uses: Pre-training benefits greatly from data augmentation for producing diverse views.
- [[regularization]] — uses: Frozen or low-lr backbone prevents divergence from pretrained features.
- [[distribution-shift]] — applies: Domain gap between p(x,y) and q(x,y) motivates the need for fine-tuning.
- [[pretraining-and-fine-tuning]] — instantiates: Chapter provides formal two-phase framework: source pre-training then target fine-tuning.
[To be populated during integration]