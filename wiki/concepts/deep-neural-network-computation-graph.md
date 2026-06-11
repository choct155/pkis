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
id: pkis:concept:deep-neural-network-computation-graph
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch16
tags:
- neural-networks
- computation-graph
- differentiable-programming
- deep-learning
title: Deep Neural Network (DNN) as Differentiable Computation Graph
understanding: 0
---

## Definition
$$f(x;\theta) = f_L \circ f_{L-1} \circ \cdots \circ f_1(x)$$

A deep neural network (DNN) is any differentiable function expressible as a directed computation graph whose nodes are primitive operations (matrix multiplications, elementwise nonlinearities, etc.) and whose edges carry numeric tensors; "deep" refers to models with many such layers stacked in sequence or in more complex topologies.

### Why it matters
This graph-based view unifies MLPs, CNNs, RNNs, and transformers under a single abstraction: any differentiable graph can be trained end-to-end via backpropagation through automatic differentiation, enabling gradient-based fitting of extremely expressive models. The computation-graph perspective also clarifies how probabilistic models and neural networks interact — DNNs can parametrize CPDs inside generative models, or serve as amortized inference networks that approximate posteriors.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]