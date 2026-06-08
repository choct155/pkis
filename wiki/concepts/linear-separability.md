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
id: pkis:concept:linear-separability
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- cover-function-counting-theorem
- support-vector-machines
related_concepts: []
sources:
- mackay-itila-ch40
tags:
- perceptron
- hyperplane
- dichotomy
- xor
- general-position
title: Linear Separability
understanding: 0
---

## Definition
A binary labelling $\{t_n\}$ of points $\{\mathbf{x}_n\}$ is **linearly separable** if some hyperplane assigns every positively-labelled point to one side and every negatively-labelled point to the other — equivalently, a weight vector $\mathbf{w}$ (with optional bias) exists such that $\operatorname{sign}(\mathbf{w}\cdot\mathbf{x}_n)$ matches $t_n$ for all $n$.

A single linear threshold neuron can realise exactly the linearly separable dichotomies; the count of these is Cover's $T(N,K)$.

### General position
The count is clean only when the points are in **general position**: any subset of size $\le K$ is linearly independent, and no $K+1$ points lie in a $(K-1)$-dimensional plane. Intuitively, points behave like random points with no accidental alignments.

### The XOR obstruction
Not every labelling is separable: the XOR function on $(\pm1,\pm1)$ in $K=2$ is the canonical non-separable example, and remains non-separable under small perturbations into general position. For $N\ge 3$ in $K=2$, some of the $2^N$ labellings are already unrealisable.

### Why it matters
Linear separability is the dividing line between what a perceptron can and cannot fit. Its failure on XOR motivated multilayer networks and nonlinear feature maps (the kernel trick), and it underlies margin-based classifiers such as support vector machines.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[support-vector-machines]] — prerequisite-of: Margin-based classifiers build directly on the separability of dichotomies by hyperplanes.
- [[cover-function-counting-theorem]] — prerequisite-of: T(N,K) counts exactly the linearly separable dichotomies.
[To be populated during integration]