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
- deep-learning
- regularization
- robustness
id: pkis:technique:adversarial-training-regularization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
tags:
- adversarial-training
- adversarial-examples
- robustness
- regularization
- FGSM
- local-constancy
title: Adversarial Training
understanding: 0
---

## Definition
A regularization strategy that augments the training set with **adversarial examples** — inputs $\mathbf{x}'$ near training points $\mathbf{x}$ that are found by maximizing the loss:
$$\mathbf{x}' = \mathbf{x} + \epsilon\, \operatorname{sign}(\nabla_{\mathbf{x}} J(\boldsymbol{\theta}, \mathbf{x}, y))$$
(fast gradient sign method), and trains the model to produce consistent outputs on both $\mathbf{x}$ and $\mathbf{x}'$.

Adversarial training explicitly introduces a **local constancy prior**, discouraging the high-sensitivity linear behavior that makes neural networks vulnerable to small perturbations.

### Why it matters
Purely linear models cannot resist adversarial perturbations; deep networks, with their capacity for near-constant local functions, can be trained to be robust. Adversarial training also enables semi-supervised learning via **virtual adversarial examples** (Miyato et al., 2015), where the model's own pseudo-label is used for unlabeled points. It is the non-infinitesimal version of tangent propagation and of double backprop.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]