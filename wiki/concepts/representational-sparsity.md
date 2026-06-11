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
- representation-learning
- regularization
id: pkis:concept:representational-sparsity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
tags:
- sparse-coding
- representational-sparsity
- L1-penalty
- activations
- dictionary-learning
title: Representational Sparsity
understanding: 0
---

## Definition
A property of a learned representation $\mathbf{h} = f(\mathbf{x})$ in which most elements are zero (or near zero) for any given input. Distinct from **parameter sparsity** (many weights being zero), representational sparsity concerns the activation values rather than the model parameters.

Formally, an $L^1$ penalty on activations, $\Omega(\mathbf{h}) = \|\mathbf{h}\|_1 = \sum_i |h_i|$, is added to the loss to encourage representational sparsity.

A sparse code uses a small active subset of features per input, leading to more interpretable and efficient representations.

### Why it matters
Representational sparsity is motivated by neuroscience (sparse coding in primary visual cortex, Olshausen & Field 1996) and information theory (efficient coding). It differs fundamentally from parameter sparsity: a densely parametrized model (full weight matrix) can still produce sparse activations. Applications include sparse autoencoders, dictionary learning, and OMP-based feature extractors for deep architectures.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]