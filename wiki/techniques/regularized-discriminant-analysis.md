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
id: pkis:technique:regularized-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch18
tags:
- classification
- lda
- covariance-shrinkage
- regularization
- p-gg-n
title: Regularized Discriminant Analysis (RDA)
understanding: 0
---

## Definition
A modification of linear discriminant analysis for high-dimensional problems where the p×p within-class covariance estimate Σ̂ has rank at most N < p and is singular. RDA regularizes by shrinking Σ̂ toward its diagonal: Σ̂(γ) = γΣ̂ + (1−γ) diag(Σ̂), γ ∈ [0,1], so that γ=1 is full LDA and γ=0 is diagonal LDA (the 'no shrinkage' limit of nearest shrunken centroids). The shrinkage parameter γ is chosen by cross-validation. The construction parallels ridge regression — which shrinks the feature covariance toward a scalar matrix — and via the optimal-scoring view of LDA as linear regression the equivalence is exact; extensions also shrink the centroids in addition to the covariance. The expensive inversion of the large p×p matrix is avoided by the SVD-based reduction that works in N-dimensional space.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]