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
id: pkis:technique:reduced-rank-lda
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch04
specializes:
- linear-discriminant-analysis
tags:
- classification
- dimension-reduction
- lda
- generalized-eigenvalue-problem
- canonical-variates
title: Reduced-Rank Linear Discriminant Analysis
understanding: 0
uses:
- principal-component-analysis
- eigendecomposition
---

## Definition
A dimension-reduction refinement of LDA exploiting that the K class centroids span an affine subspace of dimension at most K-1; distances orthogonal to this subspace contribute equally to every class and can be ignored, so LDA classification loses no information when restricted to it. For viewing or further reduction one seeks an L < K-1 dimensional subspace optimal in Fisher's sense: the projected centroids are spread out maximally in variance, i.e. the principal-component subspace of the (sphered) centroids. Fisher's equivalent formulation finds the linear combination Z = a^T X maximizing the BETWEEN-class variance a^T B a relative to the WITHIN-class variance a^T W a — the Rayleigh quotient max_a (a^T B a)/(a^T W a), with B + W = T (total covariance). This is a generalized eigenvalue problem: the optimal a_1 is the leading eigenvector of W^{-1} B, with successive directions a_2, a_3, ... (orthogonal in W) giving the discriminant coordinates / canonical variates Z_l = v_l^T X. The procedure: compute centroid matrix M and within-class W; sphere via M* = M W^{-1/2}; eigendecompose the between-centroid covariance B* = V* D_B V*^T. Notably Fisher's derivation makes no Gaussian assumption, yet the reduced-rank solution coincides with constrained-rank Gaussian ML classification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[eigendecomposition]] — uses: solves the generalized eigenvalue problem of W^{-1}B for discriminant coordinates
- [[principal-component-analysis]] — uses: optimal subspace is the principal-component subspace of the sphered class centroids
- [[linear-discriminant-analysis]] — specializes: reduced-rank restriction confines LDA to the optimal centroid-spanning subspace
[To be populated during integration]