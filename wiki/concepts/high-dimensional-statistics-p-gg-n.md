---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:concept:high-dimensional-statistics-p-gg-n
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch18
tags:
- high-dimensional
- regularization
- genomics
- overfitting
- p-gg-n
title: High-Dimensional Statistics (p ≫ N)
understanding: 0
---

## Definition
The statistical setting in which the number of features p vastly exceeds the number of observations N (p ≫ N), characteristic of genomic, proteomic, and document data. In this regime high variance and overfitting dominate: the p×p feature covariance matrix has rank at most N < p and is therefore singular, ordinary least squares and full linear discriminant analysis are undefined, and any unregularized linear classifier can perfectly separate the training data. The governing empirical principle is that 'less fitting is better' — heavier regularization (shrinking coefficients toward zero) typically yields lower prediction error as p grows, because there is not enough information in N samples to estimate the high-dimensional covariance structure. Methods either modify N>p procedures (diagonal/regularized discriminant analysis, penalized logistic regression) or are purpose-built (nearest shrunken centroids, supervised principal components), and feature selection becomes a primary scientific goal alongside prediction. A key computational fact: any linear model with a quadratic (L2) penalty can be fit in N-dimensional space rather than p via the SVD of the data matrix, since N points in p-space lie in an (N−1)-dimensional affine subspace.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]