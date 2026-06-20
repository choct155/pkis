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
date_updated: '2026-06-20'
domain:
- machine-learning
- statistics
- probability
id: pkis:concept:gaussian-process-gp
instantiates:
- bayesian-inference
- latent-variable-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch18
- kroese-statistical-modeling-ch11
specializes:
- gaussian-process
tags:
- nonparametric
- Bayesian
- regression
- function-space
- uncertainty-quantification
title: Gaussian Process (GP)
understanding: 0
uses:
- mercer-kernel
- covariance-function
- reproducing-kernel-hilbert-space
---

## Definition
$$f(x) \sim \mathcal{GP}(m(x), K(x, x'))$$

where $m(x) = \mathbb{E}[f(x)]$ and $K(x, x') = \mathbb{E}[(f(x)-m(x))(f(x')-m(x'))^T]$, such that for any finite set $\mathbf{X} = \{x_1,\ldots,x_N\}$, $p(\mathbf{f}_X|\mathbf{X}) = \mathcal{N}(\mathbf{f}_X | \boldsymbol{\mu}_X, \mathbf{K}_{X,X})$.

A GP is a prior distribution over functions: every finite collection of function values is jointly Gaussian, enabling exact Bayesian inference for regression and approximate inference for non-Gaussian likelihoods.

### Why it matters
GPs are the canonical Bayesian nonparametric model for supervised learning. They provide well-calibrated predictive uncertainty, scale to millions of points with modern approximations, and yield closed-form posteriors under Gaussian likelihoods. Capacity adapts automatically to data size, avoiding over- and underfitting of fixed-capacity parametric models. Key applications include spatial interpolation (kriging), Bayesian optimization, robust regression, and representation learning through kernel learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reproducing-kernel-hilbert-space]] — uses
- [[latent-variable-models]] — instantiates
- [[bayesian-inference]] — instantiates
- [[covariance-function]] — uses
- [[mercer-kernel]] — uses: GP covariance function must be a Mercer kernel.
- [[gaussian-process]] — specializes: Chapter 18 develops GP as a prior over functions; existing node covers the concept broadly.
[To be populated during integration]