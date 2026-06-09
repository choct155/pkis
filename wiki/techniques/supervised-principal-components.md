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
id: pkis:technique:supervised-principal-components
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch18
tags:
- dimension-reduction
- regression
- survival-analysis
- feature-screening
- latent-variable
- genomics
title: Supervised Principal Components
understanding: 0
---

## Definition
A regression/generalized-regression method for p ≫ N that finds low-dimensional structure correlated with the outcome, rather than merely high-variance. Ordinary PCA can be contaminated by a large number of noise features and need not correlate with the response; supervised principal components first screens features, retaining only those whose univariate association with the outcome exceeds a cross-validated threshold (a least-squares coefficient for regression, a Cox score test for censored survival data), then computes the leading principal component(s) of the retained subset and uses them as predictors in a final regression. It can be motivated by a single-component latent-variable (factor-analysis) model Y = β₀ + β₁U + ε, X_j = α_0j + α_1j U + ε_j for features in a relevant set P, with the latent factor U interpreted as an underlying 'cell type'; the screening step estimates P, the leading PC estimates U, and under p,p1 → ∞ with p1/p small the supervised PC is consistent for U whereas the ordinary leading PC is not. It relates to partial least squares (thresholded PLS is a noisier variant using single-outcome inner products) and can be combined with the lasso via pre-conditioning — lasso the denoised SPC-predicted outcome — to recover a sparse model with low test error.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]