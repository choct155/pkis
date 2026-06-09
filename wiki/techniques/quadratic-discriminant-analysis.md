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
id: pkis:technique:quadratic-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch04
tags:
- classification
- generative-classifier
- gaussian
- discriminant-function
title: Quadratic Discriminant Analysis
understanding: 0
---

## Definition
A generative classifier that, like LDA, models each class-conditional density as a multivariate Gaussian, but allows a SEPARATE covariance matrix Sigma_k per class. Because the covariances differ, the quadratic terms in the log-density no longer cancel, yielding quadratic discriminant functions delta_k(x) = -(1/2) log|Sigma_k| - (1/2)(x - mu_k)^T Sigma_k^{-1} (x - mu_k) + log pi_k; the decision boundary between any pair of classes {x : delta_k(x) = delta_l(x)} is a quadratic surface. Estimation mirrors LDA but a full covariance is fit per class, so the parameter count grows to (K-1){p(p+3)/2 + 1}, a dramatic increase when p is large. QDA can also be approximated by running LDA in the enlarged space of original features augmented with their squares and cross-products. Computations are simplified by eigendecomposing each Sigma_k. QDA is more flexible than LDA but higher-variance; Friedman's regularized discriminant analysis (RDA) shrinks each Sigma_k toward the pooled Sigma via Sigma_k(alpha) = alpha Sigma_k + (1-alpha) Sigma, giving a tunable continuum between QDA (alpha=1) and LDA (alpha=0).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]