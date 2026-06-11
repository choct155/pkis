---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- convex-optimization
id: pkis:technique:svm-dual-formulation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
tags:
- duality
- kernel-methods
- quadratic-programming
- KKT
- svm
title: SVM Dual Formulation
understanding: 0
---

## Definition
Applying Lagrangian duality to the primal SVM problem converts it into maximisation of
$$\tilde{L}(\mathbf{a}) = \sum_{n=1}^{N}a_n - \frac{1}{2}\sum_{n,m}a_n a_m t_n t_m k(\mathbf{x}_n,\mathbf{x}_m)$$
over dual variables $\mathbf{a} = (a_1,\ldots,a_N)^T \geq 0$ subject to $\sum_n a_n t_n = 0$ (and additionally $a_n \leq C$ in the soft-margin case). The primal weight vector is recovered as $\mathbf{w} = \sum_n a_n t_n \phi(\mathbf{x}_n)$, and predictions use $y(\mathbf{x}) = \sum_n a_n t_n k(\mathbf{x},\mathbf{x}_n) + b$.

The dual expresses the entire optimisation in terms of the kernel matrix, enabling implicit, potentially infinite-dimensional feature spaces.

### Why it matters
The dual formulation is what allows SVMs to exploit the kernel trick: neither the feature map $\phi$ nor its dimension $M$ need to be specified explicitly. The Karush–Kuhn–Tucker conditions reveal that only support vectors ($a_n > 0$) appear in predictions. The positive-definiteness of the kernel guarantees the dual QP is bounded below and well-posed.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]