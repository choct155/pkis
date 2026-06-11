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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:scree-plot
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch20
tags:
- model-selection
- pca
- dimensionality-reduction
- eigenvalues
- elbow-method
title: Scree Plot and Fraction of Variance Explained
understanding: 0
---

## Definition
$$\mathcal{L}_L = \sum_{j=L+1}^{D} \lambda_j, \qquad F_L = \frac{\sum_{j=1}^{L}\lambda_j}{\sum_{j'=1}^{D}\lambda_{j'}}$$

A scree plot graphs the ordered eigenvalues $\lambda_1 \geq \lambda_2 \geq \cdots$ of the covariance matrix against their index $j$; the reconstruction error $\mathcal{L}_L$ equals the sum of the discarded eigenvalues, and the fraction of variance explained $F_L$ rises monotonically with $L$. A 'knee' or 'elbow' in the scree plot suggests the intrinsic dimensionality $L^*$.

### Why it matters
Scree plots are the standard diagnostic for choosing $L$ in PCA. When the knee is ambiguous, the **profile likelihood** method (fitting a two-regime Gaussian change-point model to the eigenvalues) automates the detection of $L^*$ by maximising $\ell(L) = \sum_k \log \mathcal{N}(\lambda_k|\mu_{r(k)}, \sigma^2)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]