---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- deep-learning
- statistical-learning
id: pkis:result:cover-function-counting-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch40
tags:
- dichotomies
- counting
- recurrence
- pascals-triangle
- vc-dimension
- perceptron
title: Cover's Function-Counting Theorem
understanding: 0
---

## Definition
The number $T(N,K)$ of distinct linear-threshold dichotomies (homogeneous, through the origin) of $N$ points **in general position** in $K$ dimensions is
$$T(N,K)=2\sum_{k=0}^{K-1}\binom{N-1}{k},\qquad T(N,K)=2^N\ \text{for }K\ge N.$$
This is **Cover's function-counting theorem** (Cover, 1965).

### Derivation by recurrence
Work in weight space: each datapoint $\mathbf{x}^{(n)}$ contributes a hyperplane $\mathbf{x}^{(n)}\cdot\mathbf{w}=0$, and dichotomies correspond to the regions these hyperplanes carve. Adding the $N$th hyperplane bisects exactly $T(N-1,K-1)$ of the existing regions, giving
$$T(N,K)=T(N-1,K)+T(N-1,K-1),$$
the **Pascal's-triangle recurrence**, with boundary conditions $T(N,1)=2$ and $T(1,K)=2$. Solving it yields the boxed formula. Worked small cases: $T(N,2)=2N$, $T(4,3)=14$.

### Why it matters
It gives an exact combinatorial count of the expressive power of a linear classifier and pins the **VC dimension** of homogeneous threshold functions at $K$ (the largest $N$ for which $T=2^N$). It is the engine behind the two-bits-per-weight neuron capacity, and explains geometric facts such as the $7/8$ probability that four random points on a sphere share a hemisphere ($T(4,3)/2^4$).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]