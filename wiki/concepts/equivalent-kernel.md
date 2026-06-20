---
aliases: []
also_type: []
analogous-to:
- gaussian-process
- the-kernel-trick
- reproducing-kernel-hilbert-space
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
date_updated: '2026-06-20'
domain:
- machine-learning
- statistics
id: pkis:concept:equivalent-kernel
instantiates:
- covariance-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
- kroese-statistical-modeling-ch11
tags:
- kernel-methods
- linear-smoother
- gaussian-process
- bayesian-regression
title: Equivalent Kernel (Smoother Matrix)
understanding: 0
uses:
- bayesian-linear-regression-predictive
---

## Definition
The predictive mean of Bayesian linear regression can be written as a linear combination of training targets:

$$y(x,\mathbf{m}_N) = \sum_{n=1}^N k(x,x_n)\,t_n, \quad k(x,x') = \beta\,\boldsymbol{\phi}(x)^T \mathbf{S}_N \boldsymbol{\phi}(x')$$

The function $k(x,x')$ is called the **equivalent kernel** or **smoother matrix**. It satisfies: (i) $\sum_n k(x,x_n)=1$; (ii) $\text{cov}[y(x),y(x')] = \beta^{-1}k(x,x')$; (iii) $k(x,x') = \boldsymbol{\psi}(x)^T\boldsymbol{\psi}(x')$ with $\boldsymbol{\psi}(x)=\beta^{1/2}\mathbf{S}_N^{1/2}\boldsymbol{\phi}(x)$, making it a valid Mercer kernel.

### Why it matters
Bridges parametric linear models and nonparametric kernel/Gaussian-process methods: the same predictive mean can be viewed as a *kernel smoother* that directly weights training targets. This duality motivates replacing the basis function set with a directly specified kernel—the key step toward Gaussian processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reproducing-kernel-hilbert-space]] — analogous-to
- [[covariance-function]] — instantiates
- [[the-kernel-trick]] — analogous-to
- [[gaussian-process]] — analogous-to
- [[bayesian-linear-regression-predictive]] — uses
[To be populated during integration]