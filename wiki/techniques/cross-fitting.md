---
aliases: []
also_type: []
analogous-to:
- cross-validation
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
- causal-inference
- statistics
- machine-learning
id: pkis:technique:cross-fitting
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- aiptw-double-ml
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- sample-splitting
- double-ml
- nuisance
- semiparametric
- causal-estimation
title: Cross-Fitting for Causal Estimation
understanding: 0
---

## Definition
**Cross-fitting** is a sample-splitting procedure for double machine learning estimators that eliminates the "empirical process" bias term arising from reusing data for both nuisance function estimation and estimand computation.

**Procedure** (K-fold):
1. Partition the dataset into $K$ folds $\{\mathcal{D}_1,\ldots,\mathcal{D}_K\}$.
2. For each fold $k$, fit nuisance functions $\hat{Q}^{-k}$, $\hat{g}^{-k}$ on $\mathcal{D} \setminus \mathcal{D}_k$.
3. For each unit $i \in \mathcal{D}_k$, set $\hat{Q}(a_i,x_i) = \hat{Q}^{-k}(a_i,x_i)$ and $\hat{g}(x_i) = \hat{g}^{-k}(x_i)$.
4. Plug all out-of-fold predictions into the AIPTW formula.

The guarantee is that, under the product-rate condition on nuisance errors, the cross-fitted estimator satisfies the same $\sqrt{n}$-CLT as the oracle estimator that knows the true nuisance functions.

### Why it matters
Without sample splitting, empirical process terms can dominate and destroy the $\sqrt{n}$ rate for flexible (e.g., high-dimensional) nuisance estimators. Cross-fitting recovers the optimal rate while using all data for both steps (unlike a simple 50/50 split), balancing statistical efficiency with theoretical validity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[aiptw-double-ml]] — prerequisite-of
- [[cross-validation]] — analogous-to: Both use K-fold data splitting but for different purposes (inference vs. model selection)
[To be populated during integration]