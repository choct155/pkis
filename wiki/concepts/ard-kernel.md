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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- Bayesian-statistics
id: pkis:concept:ard-kernel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch17
specializes:
- mercer-kernel
tags:
- ARD
- automatic relevance determination
- feature selection
- GP
- kernel
- length scale
title: ARD Kernel (Automatic Relevance Determination Kernel)
understanding: 0
uses:
- gaussian-process-regression
---

## Definition
The ARD kernel generalises the squared-exponential kernel by replacing isotropic Euclidean distance with a **per-dimension Mahalanobis distance**:
$$K(x,x';\boldsymbol{\ell},\sigma^2) = \sigma^2\exp\!\left(-\tfrac{1}{2}\sum_{d=1}^D \frac{(x_d-x'_d)^2}{\ell_d^2}\right),$$
assigning a separate length scale $\ell_d$ to each input dimension $d$. Setting $\ell_d\to\infty$ effectively ignores dimension $d$.

### Why it matters
When the length scales $\{\ell_d\}$ are learned by marginal likelihood maximisation, irrelevant features are automatically suppressed (their $\ell_d$ grows large), performing implicit feature selection — the Bayesian analogue of LASSO. This is the kernel version of the ARD prior used in sparse Bayesian learning and neural networks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[lasso]] — analogous-to: Both perform implicit feature selection; ARD via length-scale marginalisation
- [[gaussian-process-regression]] — uses
- [[mercer-kernel]] — specializes
[To be populated during integration]