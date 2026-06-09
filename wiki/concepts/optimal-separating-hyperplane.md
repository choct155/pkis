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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- optimization
extends:
- perceptron-learning-algorithm
id: pkis:concept:optimal-separating-hyperplane
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch04
tags:
- classification
- margin
- convex-optimization
- support-points
- duality
title: Optimal Separating Hyperplane
understanding: 0
uses:
- margin-maximum-margin-classifier
- convex-optimization
- lagrangian-duality
---

## Definition
The unique hyperplane (Vapnik, 1996) that separates two linearly separable classes while maximizing the margin — the distance to the closest training point of either class. It resolves the perceptron's non-uniqueness by adding the maximal-margin constraint, and maximizing the training margin tends to improve test-set classification. The problem max_{beta, beta_0, ||beta||=1} M subject to y_i (x_i^T beta + beta_0) >= M is reparameterized (setting ||beta|| = 1/M) into the convex quadratic program min (1/2)||beta||^2 subject to y_i (x_i^T beta + beta_0) >= 1, which defines an empty slab/margin of thickness 1/||beta|| around the boundary. The Lagrangian primal yields the Wolfe dual L_D = sum alpha_i - (1/2) sum_i sum_k alpha_i alpha_k y_i y_k x_i^T x_k subject to alpha_i >= 0 and sum alpha_i y_i = 0. By the Karush-Kuhn-Tucker conditions, the solution beta = sum alpha_i y_i x_i is a linear combination only of the SUPPORT POINTS — those on the boundary of the slab (alpha_i > 0). Unlike LDA, which depends on all the data, the optimal hyperplane focuses on the boundary points; it is the basis for the support vector classifier, and the non-separable case is handled by the support vector machine.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[lagrangian-duality]] — uses: Wolfe dual and KKT conditions identify the support points
- [[convex-optimization]] — uses: solved as a convex quadratic program with linear inequality constraints
- [[margin-maximum-margin-classifier]] — uses: maximizes the margin to the closest training point of either class
- [[perceptron-learning-algorithm]] — extends: adds a maximal-margin constraint to resolve the perceptron's non-unique solution
[To be populated during integration]