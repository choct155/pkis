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
- numerical-methods
generalizes:
- backpropagation
id: pkis:concept:autodiff
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- gradient-descent
related_concepts: []
sources:
- murphy-pml1-intro-ch13
tags:
- gradient
- computation-graph
- differentiable-programming
- chain-rule
title: Automatic Differentiation (Autodiff)
understanding: 0
---

## Definition
Automatic differentiation (autodiff) is a family of techniques for computing exact derivatives of programs by systematically applying the chain rule to elementary operations recorded in a **computation graph** — a directed acyclic graph (DAG) in which each node is a differentiable primitive. Unlike symbolic differentiation it avoids expression swell, and unlike numerical differentiation it is exact up to floating-point precision.
$$\frac{\partial o}{\partial x_j} = \sum_{k \in \text{Ch}(j)} \frac{\partial o}{\partial x_k}\frac{\partial x_k}{\partial x_j}$$
Two modes exist: **forward mode** (Jacobian-vector products) and **reverse mode** (vector-Jacobian products, equivalent to backpropagation when the output is a scalar loss).

### Why it matters
Autodiff enables *differentiable programming*: any differentiable DAG can be trained end-to-end with gradient-based optimization. Libraries such as JAX, PyTorch and TensorFlow implement autodiff, making it trivial to define novel architectures without hand-deriving gradients.

### Static vs dynamic graphs
- **Static graph**: computation graph compiled ahead of time (TF1 style); enables global optimizations.
- **Dynamic graph / tracing**: graph materializes at runtime (JAX, PyTorch eager); easier to express data-dependent control flow.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[backpropagation]] — generalizes
- [[gradient-descent]] — prerequisite-of
[To be populated during integration]