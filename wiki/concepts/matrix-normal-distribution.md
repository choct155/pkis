---
aliases: []
also_type: []
analogous-to:
- gaussian-process
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
generalizes:
- gaussian-distribution
id: pkis:concept:matrix-normal-distribution
instantiates:
- conjugate-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
specializes:
- multivariate-normal-model
tags:
- matrix-normal
- kronecker
- multi-output
- conjugate
- structured-covariance
title: Matrix Normal Distribution
understanding: 0
uses:
- wishart-distribution
---

## Definition
The **matrix normal distribution** over $\mathbf{X} \in \mathbb{R}^{n \times p}$ is parameterized by mean $\mathbf{M} \in \mathbb{R}^{n\times p}$, row-covariance $\mathbf{U} \in \mathbb{S}^n_{++}$, and column-precision $\mathbf{V} \in \mathbb{S}^p_{++}$:
$$\mathcal{MN}(\mathbf{X}\mid\mathbf{M},\mathbf{U},\mathbf{V}) \propto \exp\!\left\{-\tfrac{1}{2}\mathrm{tr}[(\mathbf{X}-\mathbf{M})^\top \mathbf{U}^{-1}(\mathbf{X}-\mathbf{M})\mathbf{V}]\right\},$$
equivalently $\mathrm{vec}(\mathbf{X}) \sim \mathcal{N}(\mathrm{vec}(\mathbf{M}), \mathbf{V}^{-1} \otimes \mathbf{U})$.

### Why it matters
The matrix normal provides a compact, interpretable parameterization of structured multivariate Gaussian distributions where row and column dependencies are separable. It is the conjugate likelihood for Bayesian multi-output regression and appears in Gaussian process models for matrix-valued data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-process]] — analogous-to
- [[conjugate-prior]] — instantiates
- [[wishart-distribution]] — uses
- [[multivariate-normal-model]] — specializes
- [[gaussian-distribution]] — generalizes
[To be populated during integration]