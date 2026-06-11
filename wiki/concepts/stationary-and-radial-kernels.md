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
- kernel-methods
- gaussian-processes
id: pkis:concept:stationary-and-radial-kernels
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch06
tags:
- stationary-kernel
- RBF
- Gaussian-kernel
- Ornstein-Uhlenbeck
- translation-invariance
title: Stationary and Radial Basis Kernels
understanding: 0
---

## Definition
A kernel $k(\mathbf{x},\mathbf{x}')$ is **stationary** if it depends only on the difference $\mathbf{x}-\mathbf{x}'$, making it translation-invariant. It is **radial** (homogeneous, or an RBF kernel) if it depends only on the Euclidean distance $\|\mathbf{x}-\mathbf{x}'\|$:

$$k(\mathbf{x},\mathbf{x}') = k(\|\mathbf{x}-\mathbf{x}'\|).$$

Canonical examples:
- **Gaussian (squared-exponential):** $k(\mathbf{x},\mathbf{x}') = \exp\!\left(-\|\mathbf{x}-\mathbf{x}'\|^2/2\sigma^2\right)$ — corresponds to an infinite-dimensional feature space.
- **Ornstein–Uhlenbeck / exponential:** $k(x,x') = \exp(-\theta|x-x'|)$ — generates continuous but non-differentiable sample paths.

### Why it matters
Stationarity is a key modelling assumption: it implies the correlation between function values depends only on how far apart the inputs are, not where they are. Radial kernels are widely used defaults in Gaussian process regression and SVMs, and their Fourier structure (Bochner's theorem) underpins random-feature approximations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]