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
id: pkis:technique:dropout-regularization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
tags:
- dropout
- ensemble
- bagging
- regularization
- neural-networks
- weight-scaling
title: Dropout Regularization
understanding: 0
---

## Definition
$$\tilde{J}(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\mu}}[J(\boldsymbol{\theta}, \boldsymbol{\mu})]$$

where $\boldsymbol{\mu}$ is a binary mask vector sampled independently per training step, with each unit included with probability $p$ (typically 0.5 for hidden units, 0.8 for inputs). At inference time the **weight scaling inference rule** multiplies weights by $p$, approximating the geometric mean over the exponentially large ensemble of sub-networks.

Dropout trains an implicit ensemble of $2^n$ sub-networks that share parameters, providing powerful regularization at $O(n)$ extra cost per step.

### Why it matters
Dropout is the most widely used implicit ensemble regularizer for deep networks. It forces each hidden unit to be useful in many contexts (not co-adapted), analogous to biological sexual recombination creating individually fit genes. It subsumes bagging with parameter sharing and connects to noise-robustness, semi-supervised learning via virtual adversarial examples, and approximate Bayesian inference over weights.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]