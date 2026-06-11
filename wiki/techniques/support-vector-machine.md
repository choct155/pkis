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
- statistical-learning-theory
id: pkis:technique:support-vector-machine
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
- murphy-pml1-intro-ch17
tags:
- classification
- kernel-methods
- sparse-models
- convex-optimization
- quadratic-programming
title: Support Vector Machine (SVM)
understanding: 0
---

## Definition
Given training data $\{(\mathbf{x}_n, t_n)\}$ with $t_n \in \{-1,+1\}$, the SVM finds the decision boundary $y(\mathbf{x}) = \mathbf{w}^T\phi(\mathbf{x}) + b = 0$ by solving
$$\min_{\mathbf{w},b} \frac{1}{2}\|\mathbf{w}\|^2 \quad \text{subject to} \quad t_n(\mathbf{w}^T\phi(\mathbf{x}_n)+b) \geq 1, \; \forall n,$$
which maximises the geometric margin $\rho = 2/\|\mathbf{w}\|$ between the two classes. Via Lagrangian duality the primal is converted to a quadratic programme over dual variables $\{a_n\}$, and predictions for new inputs are made through $y(\mathbf{x}) = \sum_n a_n t_n k(\mathbf{x},\mathbf{x}_n) + b$, depending only on the subset of training points (support vectors) for which $a_n > 0$.

The SVM is a sparse, maximum-margin, kernel-based classifier whose solution is always a global optimum (convex QP).

### Why it matters
SVMs offer strong generalisation guarantees via VC theory, handle high- and infinite-dimensional feature spaces implicitly through kernels, and produce sparse models whose prediction cost scales with the number of support vectors rather than the full training set. The soft-margin variant (C-SVM) extends to overlapping class distributions via slack variables.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]