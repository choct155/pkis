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
- kernel-methods
extends:
- the-kernel-trick
id: pkis:concept:kernel-construction-rules
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- gaussian-process-regression
related_concepts: []
sources:
- bishop-prml-ch06
tags:
- kernel-validity
- positive-semidefinite
- kernel-engineering
- closure
title: Kernel Construction Rules (Closure Properties)
understanding: 0
uses:
- gram-matrix
---

## Definition
Given valid kernels $k_1, k_2$ on the same input space, the following operations preserve validity (i.e., the resulting Gram matrix is PSD for all data sets):

$$k = c\,k_1,\quad k = f(\mathbf{x})k_1(\mathbf{x},\mathbf{x}')f(\mathbf{x}'),\quad k = q(k_1),\quad k = \exp(k_1)$$
$$k = k_1+k_2,\quad k = k_1\cdot k_2,\quad k(\mathbf{x},\mathbf{x}') = k_3(\varphi(\mathbf{x}),\varphi(\mathbf{x}'))$$
$$k(\mathbf{x},\mathbf{x}') = \mathbf{x}^T\mathbf{A}\mathbf{x}' \text{ (}\mathbf{A}\text{ PSD)},\quad k = k_a(\mathbf{x}_a,\mathbf{x}_a')+k_b(\mathbf{x}_b,\mathbf{x}_b'),\quad k = k_a k_b$$

where $c>0$, $f$ is any function, $q$ is a polynomial with non-negative coefficients.

These closure rules allow complex kernels to be assembled from primitive building blocks (linear, polynomial, Gaussian) without separately verifying the PSD condition.

### Why it matters
The rules systematise 'kernel engineering': practitioners can compose stationary, non-stationary, or symbolic kernels by straightforward algebraic manipulation, and the resulting kernel is guaranteed valid.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-process-regression]] — prerequisite-of
- [[the-kernel-trick]] — extends
- [[gram-matrix]] — uses
[To be populated during integration]