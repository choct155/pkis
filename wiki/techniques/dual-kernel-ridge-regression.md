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
- kernel-methods
- regression
extends:
- linear-regression
id: pkis:technique:dual-kernel-ridge-regression
instantiates:
- the-kernel-trick
- representer-theorem
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- support-vector-machines
related_concepts: []
sources:
- bishop-prml-ch06
tags:
- kernel-ridge-regression
- dual-formulation
- representer-theorem
- kernel-trick
title: Dual Representation of Kernel Ridge Regression
understanding: 0
uses:
- gram-matrix
- regularization
---

## Definition
$$\mathbf{a} = (\mathbf{K} + \lambda I_N)^{-1}\mathbf{t}, \qquad y(\mathbf{x}) = \mathbf{k}(\mathbf{x})^T(\mathbf{K}+\lambda I_N)^{-1}\mathbf{t}$$

where $\mathbf{K}$ is the $N\times N$ Gram matrix, $\mathbf{k}(\mathbf{x})$ is the vector of kernel evaluations between the test point and all training points, and $\lambda$ is the regularisation coefficient. Minimising the regularised sum-of-squares objective $J(\mathbf{w}) = \tfrac{1}{2}\sum_n(\mathbf{w}^T\varphi(\mathbf{x}_n)-t_n)^2 + \tfrac{\lambda}{2}\|\mathbf{w}\|^2$ shows $\mathbf{w} = \boldsymbol{\Phi}^T\mathbf{a}$; substituting back yields a purely kernel-based predictor.

### Why it matters
The dual formulation replaces the $M\times M$ inversion in weight space with an $N\times N$ inversion in data space, enabling the kernel trick: any valid kernel $k(\mathbf{x},\mathbf{x}')$ can be substituted without ever computing the (possibly infinite-dimensional) feature map $\varphi$. This is the algebraic foundation on which support vector machines and Gaussian process regression are built.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[support-vector-machines]] — prerequisite-of
- [[regularization]] — uses
- [[linear-regression]] — extends
- [[representer-theorem]] — instantiates
- [[the-kernel-trick]] — instantiates
- [[gram-matrix]] — uses
[To be populated during integration]