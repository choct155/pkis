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
id: pkis:concept:feedforward-neural-network
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch13
tags:
- neural-networks
- deep-learning
- function-approximation
- tabular-data
title: Feedforward Neural Network (MLP)
understanding: 0
---

## Definition
A feedforward neural network (also called a multilayer perceptron, MLP) is a function defined by composing $L$ differentiable layer functions:
$$f(x;\theta) = f_L(f_{L-1}(\cdots(f_1(x))\cdots)), \quad f_l(z_{l-1}) = \varphi_l(b_l + W_l z_{l-1})$$
where $z_l \in \mathbb{R}^{K_l}$ are the hidden activations, $W_l$ and $b_l$ are weight matrices and bias vectors, and $\varphi_l$ is a differentiable activation function applied elementwise. The computation flows strictly from input to output (no cycles), forming a chain-structured directed acyclic graph.

### Why it matters
MLPs are the canonical universal function approximator for fixed-dimensional (tabular) input, forming the backbone of deep learning. Every other DNN architecture (CNNs, RNNs, Transformers, GNNs) is a specialization that adds inductive bias on top of this basic composition principle.

### Key properties
- **Universal approximation**: a single hidden layer with enough units can approximate any smooth function to arbitrary accuracy.
- **Depth advantage**: deeper networks exploit compositional/hierarchical structure and empirically outperform shallow ones at the same parameter budget.
- **Linear activation collapse**: if all $\varphi_l$ are linear, the whole model reduces to a single linear map $W'x$, so nonlinearity is essential.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]