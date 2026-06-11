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
- computer-vision
- machine-learning
- signal-processing
id: pkis:technique:expected-patch-log-likelihood
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch28
tags:
- image-restoration
- patch-prior
- gmm
- inverse-problems
- regularization
- half-quadratic-splitting
title: Expected Patch Log Likelihood (EPLL)
understanding: 0
---

## Definition
$$\text{EPLL}(x) = \sum_i \log p(\mathbf{P}_i x)$$

The Expected Patch Log Likelihood is an image-level regularisation objective that sums the log probability of every overlapping patch $x_i = \mathbf{P}_i x$ under a patch prior $p(\cdot)$ (typically a $K$-component GMM fit to millions of natural-image patches). The full inverse-problem objective is:
$$E(x \mid y) = \frac{1}{2\sigma^2}\|Wx - y\|^2 - \text{EPLL}(x)$$
minimised via half-quadratic splitting.

### Why it matters
EPLL bridges classical patch-based image restoration and probabilistic modelling: by using a learned GMM patch prior one obtains a single framework for denoising, deblurring, inpainting, and super-resolution, all differing only in the forward operator $W$. It also motivates amortised inference networks that learn to invert the operator directly.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]