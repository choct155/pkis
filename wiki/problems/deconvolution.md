---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:problem:deconvolution
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch46
tags:
- inverse-problem
- deconvolution
- image-reconstruction
- ill-posed
- regularization
- point-spread-function
title: Deconvolution (Linear Inverse Problem)
understanding: 0
uses:
- regularization
---

## Definition
Deconvolution is the task of recovering an unknown signal or image $\mathbf{f}$ from measurements $\mathbf{d}$ that are a *linear* but degraded function of it, corrupted by noise:
$$d_n = \sum_k R_{nk} f_k + n_n,$$
where $\mathbf{R}$ is a known linear operator (for a blurred camera image, a convolution by the *point spread function*) and $\mathbf{n}$ is additive noise. It is the canonical *linear inverse problem*: given the forward map $\mathbf{R}$ and data $\mathbf{d}$, invert to estimate $\mathbf{f}$.

### The ill-posed nature
Though the blur was created by a linear operation, naively undoing it is *ill-posed*. The operator $\mathbf{R}^T\mathbf{R}$ is typically rank-deficient or ill-conditioned: small high-frequency noise components are amplified enormously by the pseudoinverse $[\mathbf{R}^T\mathbf{R}]^{-1}\mathbf{R}^T$, so a direct inversion produces wildly oscillating, useless reconstructions. The information destroyed by blurring (and the modes swamped by noise) cannot be recovered without extra assumptions.

### Role of a prior / regularizer
The cure is to inject prior knowledge about plausible images, which stabilizes the inversion. A Gaussian prior yields the optimal linear filter; a positivity-enforcing entropic prior yields maximum-entropy reconstruction. The data alone underdetermine $\mathbf{f}$; the prior selects among the many images consistent with $\mathbf{d}$.

### Why it matters
Deconvolution is ubiquitous: astronomical imaging, microscopy, medical imaging, audio restoration, and even the early visual system, which must deconvolve the chromatic aberration of the eye's optics. It is the prototype showing that *inference, not algebra*, is required when measurement loses information.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — uses: The ill-posed inversion requires a prior/regularizer to stabilize amplified noise.
[To be populated during integration]