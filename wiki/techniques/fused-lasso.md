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
id: pkis:technique:fused-lasso
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch18
tags:
- regularization
- structured-sparsity
- ordered-features
- total-variation
- feature-selection
title: Fused Lasso
understanding: 0
---

## Definition
A lasso variant that exploits a natural ordering of the features by penalizing both their magnitude and their successive differences: minimize Σ_i (y_i − β₀ − Σ_j x_ijβ_j)² + λ₁ Σ_j |β_j| + λ₂ Σ_j |β_{j+1} − β_j|. The first (L1) penalty encourages sparsity; the second (total-variation / fusion) penalty encourages the coefficient profile to be piecewise-constant and smooth in the index j, appropriate when features are ordered by some index variable t (e.g., mass-to-charge ratio in mass spectrometry, chromosomal location in CGH arrays). The criterion is strictly convex, so the solution is unique. For nonuniform spacing the difference penalty is replaced by divided differences |β_{j+1}−β_j|/|t_{j+1}−t_j|. A useful special case with X = I_N, the fused lasso signal approximator, smooths a sequence {y_i} into piecewise-constant segments — used to detect contiguous regions of gene amplification or deletion in tumors. A two-dimensional version penalizes first differences to neighboring pixels for image denoising/classification, and fast generalized coordinate-descent algorithms solve both forms.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]