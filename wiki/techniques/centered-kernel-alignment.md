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
- representation-learning
- linear-algebra
id: pkis:technique:centered-kernel-alignment
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
specializes:
- representational-similarity-analysis
tags:
- representational-similarity
- neural-networks
- kernel-methods
- CKA
- RV-coefficient
title: Centered Kernel Alignment (CKA)
understanding: 0
uses:
- the-kernel-trick
- reproducing-kernel-hilbert-space
- inner-product
- principal-component-analysis
---

## Definition
$$\text{CKA}(\mathbf{K}, \mathbf{K}') = \frac{\langle H\mathbf{K}H,\, H\mathbf{K}'H \rangle_F}{\|H\mathbf{K}H\|_F\,\|H\mathbf{K}'H\|_F}$$

where $H = I - \frac{1}{n}\mathbf{1}\mathbf{1}^\top$ is the centering matrix and $\langle \cdot,\cdot\rangle_F$ is the Frobenius inner product. When linear kernels are used ($K = \tilde{X}\tilde{X}^\top$, $K' = \tilde{Y}\tilde{Y}^\top$), linear CKA reduces to the squared Frobenius norm of cross-covariance divided by individual Frobenius norms, and is equivalent to the RV coefficient between centered features. CKA measures the geometric similarity between two sets of neural network representations for the same examples, invariant to orthogonal transformations.

### Why it matters
CKA provides a principled, invariant way to compare representations across layers or architectures without requiring the representations to share the same dimensionality, making it the standard tool for representational geometry analysis in deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[principal-component-analysis]] — uses: Linear CKA has a closed-form expression in terms of PCA singular vectors and variances
- [[inner-product]] — uses
- [[reproducing-kernel-hilbert-space]] — uses
- [[the-kernel-trick]] — uses
- [[representational-similarity-analysis]] — specializes: CKA is a specific instantiation of RSA with PSD kernels and cosine matrix similarity
[To be populated during integration]