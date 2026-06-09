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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- deep-learning
id: pkis:technique:perceptron-learning-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch04
tags:
- classification
- separating-hyperplane
- stochastic-gradient
- online-learning
- linear-classifier
title: Perceptron Learning Algorithm
understanding: 0
---

## Definition
Rosenblatt's (1958) algorithm for finding a separating hyperplane between two classes by minimizing the total distance of misclassified points to the decision boundary. A perceptron classifies via the sign of a linear function sign(beta^T x + beta_0). The objective D(beta, beta_0) = - sum_{i in M} y_i (x_i^T beta + beta_0), summing only over the misclassified set M, is nonnegative and piecewise linear. The algorithm minimizes it by STOCHASTIC gradient descent: it visits misclassified observations in sequence and, after each, updates (beta, beta_0) <- (beta, beta_0) + rho (y_i x_i, y_i), where the learning rate rho can be set to 1 without loss of generality. If the classes are linearly separable, convergence to SOME separating hyperplane in a finite number of steps is guaranteed. Known problems: the solution found depends on the starting values (many solutions exist when separable); the finite step count can be very large when the margin (gap) is small; and when the data are NOT separable the algorithm fails to converge and cycles. Perceptrons set the foundation for the neural-network models of the 1980s-90s, and the non-uniqueness problem motivates the optimal separating hyperplane.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]