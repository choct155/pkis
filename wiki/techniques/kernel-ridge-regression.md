---
aliases: []
also_type: []
analogous-to:
- gp-posterior-inference
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
extends:
- ridge-regression
generalizes:
- ridge-regression
id: pkis:technique:kernel-ridge-regression
instantiates:
- representer-theorem
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch17
- murphy-pml2-advanced-ch18
tags:
- kernel ridge
- dual
- representer theorem
- regularisation
- nonparametric
title: Kernel Ridge Regression
understanding: 0
uses:
- mercer-kernel
- the-kernel-trick
- gram-matrix
- reproducing-kernel-hilbert-space
- representer-theorem
- regularization
---

## Definition
Kernel ridge regression applies the kernel trick to ridge regression. Using the matrix inversion lemma, the primal ridge solution $\hat{w}=(X^TX+\lambda I_D)^{-1}X^T y$ can be re-expressed via **dual variables** $\alpha=(K+\lambda I_N)^{-1}y$ as
$$f(x) = w^Tx = \sum_{n=1}^N \alpha_n K(x_n,x) = k^T(K+\lambda I_N)^{-1}y,$$
where $k=[K(x,x_1),\dots,K(x,x_N)]^T$ and $K_{ij}=K(x_i,x_j)$. Predictions are a weighted sum over all $N$ training points with weights $\alpha$ satisfying a Gaussian linear system.

### Why it matters
Kernel ridge regression unifies nonparametric regression with regularised linear regression and equals the **posterior mean** of a GP (Section 17.2.2). Its $\alpha$ vector is dense (no sparsity), distinguishing it from SVM regression where the epsilon-insensitive loss induces sparsity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — uses
- [[gp-posterior-inference]] — analogous-to
- [[ridge-regression]] — generalizes
- [[representer-theorem]] — uses
- [[reproducing-kernel-hilbert-space]] — uses
- [[gram-matrix]] — uses
- [[representer-theorem]] — instantiates
- [[ridge-regression]] — extends
- [[the-kernel-trick]] — uses
- [[mercer-kernel]] — uses
[To be populated during integration]