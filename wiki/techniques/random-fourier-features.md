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
- approximation-theory
id: pkis:technique:random-fourier-features
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch17
- murphy-pml2-advanced-ch18
tags:
- random features
- RFF
- kernel approximation
- Fourier
- scalable
- fastfood
title: Random Fourier Features
understanding: 0
---

## Definition
For a **shift-invariant** kernel $K(x,x')=K(x-x')$, Bochner's theorem guarantees a spectral representation. Drawing $T$ frequencies $\omega_t \sim p(\omega)$ (the spectral density), the approximation
$$K(x,x') \approx \phi(x)^T\phi(x'), \quad \phi(x) = \tfrac{1}{\sqrt{T}}[\sin(\Omega x),\cos(\Omega x)]$$
where $\Omega\in\mathbb{R}^{T\times D}$ has iid rows from $\mathcal{N}(0,1/\sigma^2)$ for the RBF kernel, is called **random Fourier features (RFF)**. This reduces kernel method cost from $O(N^3)$ to $O(NM+M^3)$.

### Why it matters
RFF enables large-scale kernel machine learning by converting a kernel method into a linear model in an $M$-dimensional explicit feature space. Variants include **orthogonal random features** (lower variance, obtained via Gram-Schmidt) and **positive random features** (preferred for attention kernels). The **Fastfood** trick further reduces memory from $O(MD)$ to $O(M)$ using structured Hadamard transforms.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]