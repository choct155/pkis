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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- deep-learning
- statistical-learning
id: pkis:concept:single-neuron-classifier
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch39
tags:
- single-neuron
- perceptron
- classification
- sigmoid
- weight-space
- feedforward
title: Single Neuron as a Classifier
understanding: 0
---

## Definition
A single neuron is the atomic feedforward unit of a neural network: given inputs $\mathbf{x}=(x_1,\dots,x_I)$ (with an optional bias input $x_0\equiv 1$) and weights $\mathbf{w}$, it computes a scalar **activation** $a=\sum_i w_i x_i = \mathbf{w}\cdot\mathbf{x}$ and emits an **activity** $y=f(a)$. With the logistic (sigmoid) activation
$$y(\mathbf{x};\mathbf{w}) = \frac{1}{1+e^{-\mathbf{w}\cdot\mathbf{x}}}\in(0,1),$$
the neuron is a binary classifier whose output is read as $P(\text{class }1\mid\mathbf{x})$.

### Input space vs weight space
For a fixed $\mathbf{w}$, the output is constant on hyperplanes perpendicular to $\mathbf{w}$ and varies as a sigmoid ramp along $\mathbf{w}$ — so $\mathbf{w}$ both orients and sharpens the decision boundary $\mathbf{w}\cdot\mathbf{x}=0$. Dually, each point of **weight space** indexes one whole function of $\mathbf{x}$; the sigmoid's gain grows with $\|\mathbf{w}\|$. Learning is search through weight space for a $\mathbf{w}$ minimizing an objective over labelled data.

### Why it matters
The single neuron is the conceptual seed of all of deep learning: networks are built by composing many such units, and backpropagation generalizes its gradient. It also bridges statistics and neural computation — with a logistic activation it *is* logistic regression, exposing that a foundational "learning machine" is an old statistical model in new clothing.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]