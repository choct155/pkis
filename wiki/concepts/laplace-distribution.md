---
aliases: []
also_type: []
analogous-to:
- lasso
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- gaussian-distribution
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability-theory
- statistics
- machine-learning
id: pkis:concept:laplace-distribution
instantiates:
- kurtosis-and-tail-behavior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
- murphy-pml2-advanced-ch02
specializes:
- exponential-family
tags:
- heavy-tails
- L1
- sparsity
- regularization
title: Laplace Distribution
understanding: 0
uses:
- probability-density-function
- pmf-and-pdf
- lasso
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
- [[exponential-family]] — specializes
- [[lasso]] — uses
- [[kurtosis-and-tail-behavior]] — instantiates
- [[pmf-and-pdf]] — uses
- [[probability-density-function]] — uses
- [[lasso]] — analogous-to: Laplace prior over weights yields lasso regularization
- [[gaussian-distribution]] — contrasts-with: sharper peak, heavier tails; L1 vs L2 regularization analogy
[To be populated during integration]