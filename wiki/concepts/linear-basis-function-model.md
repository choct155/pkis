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
- machine-learning
- statistics
id: pkis:concept:linear-basis-function-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
tags:
- regression
- basis-functions
- supervised-learning
- linear-models
title: Linear Basis Function Model
understanding: 0
---

## Definition
$$y(\mathbf{x}, \mathbf{w}) = \sum_{j=0}^{M-1} w_j \phi_j(\mathbf{x}) = \mathbf{w}^T \boldsymbol{\phi}(\mathbf{x})$$

where $\{\phi_j(\mathbf{x})\}$ are fixed (possibly nonlinear) basis functions and $\mathbf{w}$ are adaptive parameters. The model is *linear in the parameters* even when the basis functions are highly nonlinear functions of $\mathbf{x}$.

### Why it matters
Linearity in $\mathbf{w}$ yields closed-form maximum-likelihood and MAP solutions, a tractable Bayesian posterior, and a clean bias-variance analysis, making these models the natural pedagogical and practical precursor to kernel methods, Gaussian processes, and neural networks. Common basis choices include polynomial, Gaussian radial, sigmoidal, and Fourier/wavelet families.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]