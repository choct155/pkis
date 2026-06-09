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
id: pkis:technique:penalized-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch12
tags:
- classification
- regularization
- signal-image
title: Penalized Discriminant Analysis (PDA)
understanding: 0
---

## Definition
A regularized form of LDA designed for problems with many highly correlated predictors (digitized analog signals, image pixels), where ordinary LDA uses too many parameters and suffers high variance. PDA fits an LDA model but penalizes the discriminant coefficients to be smooth (or otherwise coherent) over the spatial domain. Equivalently it performs (penalized) LDA in a basis-expanded space using a penalized Mahalanobis distance D(x,mu) = (h(x)-h(mu))^T (Sigma_W + lambda Omega)^{-1} (h(x)-h(mu)), where Omega encodes the roughness penalty. The subspace decomposition maximizes u^T Sigma_B u subject to u^T (Sigma_W + lambda Omega) u = 1.

## Why regularization helps
Positively correlated predictors (e.g., neighboring image pixels) lead to noisy, negatively correlated LDA coefficient estimates that cancel under similar inputs, inflating sampling variance. Penalizing coefficients to be smooth over the spatial domain produces interpretable, smooth discriminant images (vs. LDA's salt-and-pepper images) and improved test-set accuracy (roughly 25% in Hastie et al.'s digit-classification trials).

## Connections
- Specializes / regularizes [[linear-discriminant-analysis]]
- Shares the FDA computational machinery (penalized regression in place of plain regression); [[flexible-discriminant-analysis]] with a quadratic penalty *is* PDA in the enlarged space
- Uses [[optimal-scoring]]

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]