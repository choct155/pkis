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
id: pkis:concept:deep-feedforward-network
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
tags:
- feedforward
- MLP
- neural-network
- architecture
- representation-learning
title: Deep Feedforward Network (MLP)
understanding: 0
---

## Definition
A deep feedforward network defines a parametric mapping $$y = f(x;\theta) = f^{(L)}(\cdots f^{(2)}(f^{(1)}(x))\cdots)$$ as a directed acyclic composition of $L$ layer functions, with no feedback connections. Each intermediate layer $f^{(k)}$ is called a hidden layer because training data does not directly supervise its outputs; the final layer is the output layer. The depth of the network is $L$ and the width at layer $k$ is the dimensionality of $h^{(k)}$.

Intuitively, the network learns a hierarchy of increasingly abstract representations of the input that make the desired mapping linearly separable at the top.

### Why it matters
MLPs are the canonical architecture from which convolutional, recurrent, and attention-based networks are all derived. Understanding their training dynamics—non-convex loss landscape, gradient flow, activation saturation—is prerequisite to understanding virtually all of modern deep learning. The XOR example concretely shows why at least one hidden layer with a nonlinearity is necessary to represent non-linearly-separable functions.

### Key design axes
Depth (number of layers), width (units per layer), activation functions, output unit type, and cost function.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]