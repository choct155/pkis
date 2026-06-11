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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability-theory
- statistics
- machine-learning
id: pkis:concept:laplace-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
- murphy-pml2-advanced-ch02
tags:
- heavy-tails
- L1
- sparsity
- regularization
title: Laplace Distribution
understanding: 0
---

## Definition
The **Laplace distribution** with location $\mu$ and scale $\gamma > 0$ has PDF
$$\text{Laplace}(x;\mu,\gamma) = \frac{1}{2\gamma}\exp\!\left(-\frac{|x-\mu|}{\gamma}\right).$$
It places a sharp, tent-shaped peak at $\mu$ and has heavier tails than the Gaussian, with variance $2\gamma^2$.

### Why it matters
Using the Laplace distribution as a likelihood is equivalent to optimizing the mean absolute error, while using it as a prior over weights corresponds to $L_1$ (lasso) regularization. This sparsity-inducing property makes it a key tool for sparse modelling in machine learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]