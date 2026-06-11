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
contrasts-with:
- curse-of-dimensionality
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
generalizes:
- linear-regression
id: pkis:concept:linear-basis-function-model
instantiates:
- supervised-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
specializes:
- basis-function-models
tags:
- regression
- basis-functions
- supervised-learning
- linear-models
title: Linear Basis Function Model
understanding: 0
uses:
- activation-functions
---

## Definition
$$y(\mathbf{x}, \mathbf{w}) = \sum_{j=0}^{M-1} w_j \phi_j(\mathbf{x}) = \mathbf{w}^T \boldsymbol{\phi}(\mathbf{x})$$

where $\{\phi_j(\mathbf{x})\}$ are fixed (possibly nonlinear) basis functions and $\mathbf{w}$ are adaptive parameters. The model is *linear in the parameters* even when the basis functions are highly nonlinear functions of $\mathbf{x}$.

### Why it matters
Linearity in $\mathbf{w}$ yields closed-form maximum-likelihood and MAP solutions, a tractable Bayesian posterior, and a clean bias-variance analysis, making these models the natural pedagogical and practical precursor to kernel methods, Gaussian processes, and neural networks. Common basis choices include polynomial, Gaussian radial, sigmoidal, and Fourier/wavelet families.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[activation-functions]] — uses: Sigmoidal and Gaussian basis functions are specific choices analogous to activation functions
- [[curse-of-dimensionality]] — contrasts-with: Fixed basis functions suffer from exponential growth of required basis functions with input dimensionality
- [[linear-regression]] — generalizes
- [[basis-function-models]] — specializes
- [[supervised-learning]] — instantiates
[To be populated during integration]