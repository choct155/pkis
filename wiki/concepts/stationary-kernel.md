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
- functional-analysis
id: pkis:concept:stationary-kernel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch18
specializes:
- mercer-kernel
tags:
- GP
- kernel
- Bochner
- spectral-density
- translation-invariance
title: Stationary (Shift-Invariant) Kernel
understanding: 0
uses:
- mutual-information
---

## Definition
A kernel $K: \mathbb{R}^D \times \mathbb{R}^D \to \mathbb{R}$ is **stationary** (shift-invariant) if it depends only on the difference $r = x - x'$:
$$K(x, x') = K(r), \quad r = x - x'$$
It is **isotropic** if it further depends only on the magnitude $r = \|x - x'\|_2$. Common examples include the squared-exponential (RBF), Matérn, rational quadratic, and periodic kernels.

By Bochner's theorem, every continuous positive-definite stationary kernel is the Fourier transform of a non-negative spectral measure $p(\omega)$:
$$K(r) = \int p(\omega) e^{i\omega^T r}\, d\omega$$

### Why it matters
Stationarity is the most common structural assumption for GP kernels: it implies translation-invariant similarity and connects kernel design to spectral analysis. The spectral density $p(\omega)$ governs frequency content of GP samples — RBF kernels have Gaussian spectral densities (smooth, low-frequency), while Matérn kernels have heavy-tailed Student-$t$ spectral densities (rougher, higher-frequency).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mutual-information]] — uses: Spectral density via Bochner's theorem connects to Fourier analysis.
- [[mercer-kernel]] — specializes
[To be populated during integration]