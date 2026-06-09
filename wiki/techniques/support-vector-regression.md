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
- optimization
id: pkis:technique:support-vector-regression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch12
tags:
- regression
- kernel-methods
- robust
title: Support Vector Regression (SVR)
understanding: 0
---

## Definition
An adaptation of the support vector machine to quantitative-response regression that inherits the SVM's sparsity (support-vector) and kernel properties. It minimizes H(beta, beta_0) = sum_i V_epsilon(y_i - f(x_i)) + (lambda/2)||beta||^2 with f(x) = x^T beta + beta_0, where V_epsilon is the epsilon-insensitive loss: zero for residuals smaller than epsilon, linear beyond. Only observations whose residuals fall outside the epsilon-tube enter the solution as support vectors, giving a sparse representation f_hat(x) = sum_i (alpha*_i - alpha_i) <x, x_i> + beta_0 that depends on the inputs only through inner products and therefore generalizes to nonlinear fits via kernels (12.22).

## Operational Mechanism
Solve the dual QP min over alpha_i, alpha*_i of epsilon sum (alpha*_i + alpha_i) - sum y_i(alpha*_i - alpha_i) + (1/2) sum_{i,i'} (alpha*_i - alpha_i)(alpha*_{i'} - alpha_{i'}) <x_i, x_{i'}> subject to 0 <= alpha_i, alpha*_i <= 1/lambda, sum (alpha*_i - alpha_i) = 0, and alpha_i alpha*_i = 0. Replace inner products by a kernel K for nonlinear regression. Two tuning parameters: epsilon (loss-function width, analogous to Huber's c) and lambda (regularization, set by cross-validation); both depend on the scale of y.

## Connections
- Specializes / adapts [[support-vector-machines]] to regression
- Uses [[epsilon-insensitive-loss]] and [[the-kernel-trick]]
- Contrasts with Huber robust regression: both have linear tails, but SVR additionally flattens small residuals

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]