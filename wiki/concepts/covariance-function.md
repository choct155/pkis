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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:concept:covariance-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch45
tags:
- covariance-function
- kernel
- gaussian-process
- hyperparameters
- stationary-process
title: Covariance Function (Kernel)
understanding: 0
---

## Definition
The **covariance function** (or **kernel**) $C(\mathbf{x},\mathbf{x}';\boldsymbol{\theta})$ of a Gaussian process specifies the prior covariance between the function values $y(\mathbf{x})$ and $y(\mathbf{x}')$, and thereby *summarizes the entire prior over functions* — replacing the choice of basis functions and parameter priors. The only constraint on a valid kernel is that it must produce a non-negative-definite covariance matrix $Q_{nn'}=C(\mathbf{x}^{(n)},\mathbf{x}^{(n')})$ for every finite set of points.

### Stationary kernels
A kernel is *stationary* if it depends only on the separation, $C(\mathbf{x},\mathbf{x}')=D(\mathbf{x}-\mathbf{x}')$, and *homogeneous* if only on the distance. The canonical squared-exponential form is
$$C(\mathbf{x},\mathbf{x}';\boldsymbol{\theta})=\theta_1\exp\!\Big[-\tfrac{1}{2}\sum_{i=1}^I \tfrac{(x_i-x_i')^2}{r_i^2}\Big]+\theta_2,$$
where $r_i$ is a lengthscale per input dimension, $\theta_1$ the vertical variation scale, and $\theta_2$ a constant offset. A stationary kernel's Fourier transform is its (necessarily positive) *power spectrum*; inverting any positive spectrum yields a valid kernel.

### Why it matters
The continuity and differentiability of typical sample functions are dictated entirely by the kernel: $\exp(-|x-x'|^\nu)$ gives smooth functions for $\nu=2$ and rough ones for $\nu\le 1$. Large per-input lengthscales render an input nearly irrelevant — the basis of **automatic relevance determination**. Periodic and linear-trend kernels encode further structure, and predictions depend *entirely* on the resulting covariance matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]