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
id: pkis:technique:nearest-shrunken-centroids
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch18
tags:
- classification
- feature-selection
- shrinkage
- soft-thresholding
- genomics
- diagonal-lda
title: Nearest Shrunken Centroids (NSC)
understanding: 0
---

## Definition
A regularized nearest-centroid classifier for the p ≫ N setting that performs automatic feature selection. It starts from diagonal-covariance LDA — the 'independence rule' that assumes features are independent within each class (a special case of naive Bayes), giving the discriminant score δ_k(x*) = −Σ_j (x*_j − x̄_kj)²/s_j² + 2 log π_k, equivalent to nearest-centroid classification after standardization. NSC then shrinks each class centroid toward the overall centroid feature-by-feature: standardize the contrast d_kj = (x̄_kj − x̄_j)/[m_k(s_j+s₀)], apply soft thresholding d'_kj = sign(d_kj)(|d_kj| − Δ)_+, and back-transform. Genes whose d'_kj is zero for every class drop out of the rule entirely, so the vast majority of features are discarded, yielding an interpretable signature; the shrinkage Δ is chosen by cross-validation. The soft-thresholding step is a lasso-style estimator for the class means, and the small constant s₀ (median of the s_j) guards against inflated d_kj from near-zero expression. Because it standardizes each feature individually, NSC requires the raw feature matrix and cannot be run from an inner-product kernel alone.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]