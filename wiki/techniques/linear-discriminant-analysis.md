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
id: pkis:technique:linear-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch04
- hastie-esl-ch12
tags:
- classification
- generative-classifier
- gaussian
- discriminant-function
- dimension-reduction
title: Linear Discriminant Analysis
understanding: 0
---

## Definition
A generative classifier that models each class-conditional density f_k(x) as a multivariate Gaussian with a class-specific mean mu_k but a COMMON covariance matrix Sigma shared across all classes, then classifies via Bayes' theorem. The shared covariance causes the quadratic terms in the log-density ratio to cancel, so the log-posterior odds log[Pr(G=k|x)/Pr(G=l|x)] are linear in x — hence linear decision boundaries (in p dimensions, hyperplanes). Equivalently, classification reduces to the linear discriminant functions delta_k(x) = x^T Sigma^{-1} mu_k - (1/2) mu_k^T Sigma^{-1} mu_k + log pi_k, classifying to argmax_k delta_k(x). Parameters are estimated from training data: pi_k = N_k/N, mu_k as class sample means, and Sigma as the pooled within-class covariance with N-K denominator. Implementation: sphere the data with respect to Sigma (X* <- D^{-1/2} U^T X via eigendecomposition Sigma = UDU^T) and classify to the nearest class centroid in the sphered space, modulo the log pi_k prior correction. In the two-class case the LDA direction coincides (up to scale) with the least-squares regression coefficient on +/-1 coded targets, though the intercept differs unless N_1 = N_2. LDA has fewer parameters and lower variance than QDA — a bias-variance argument explains its robust empirical performance even when the Gaussian assumptions are violated.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]