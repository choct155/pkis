---
aliases: []
also_type: []
analogous-to:
- adversarial-training-regularization
applies:
- neural-networks
- overfitting-and-underfitting
- restricted-boltzmann-machine
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- weight-decay-as-prior
- batch-normalization
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- regularization
extends:
- bagging
id: pkis:technique:dropout-regularization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
specializes:
- regularization
tags:
- dropout
- ensemble
- bagging
- regularization
- neural-networks
- weight-scaling
title: Dropout Regularization
understanding: 0
uses:
- bias-variance-tradeoff
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
- [[adversarial-training-regularization]] — analogous-to: Both inject noise that forces robust representations
- [[restricted-boltzmann-machine]] — applies
- [[batch-normalization]] — contrasts-with: Batch normalization introduces additive+multiplicative noise and can make dropout unnecessary
- [[weight-decay-as-prior]] — contrasts-with: Wager et al. showed dropout on linear regression equals L2 decay with per-feature coefficients
- [[bias-variance-tradeoff]] — uses
- [[overfitting-and-underfitting]] — applies
- [[neural-networks]] — applies
- [[bagging]] — extends: Dropout approximates bagging over exponentially many sub-networks with shared parameters
- [[regularization]] — specializes
[To be populated during integration]