---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- functional-analysis
- machine-learning
- mathematics
id: pkis:result:mercers-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch18
tags:
- kernel-trick
- eigenfunction
- RKHS
- positive-definite
- GP
title: Mercer's Theorem
understanding: 0
uses:
- mercer-kernel
- reproducing-kernel-hilbert-space
- eigendecomposition
- the-kernel-trick
---

## Definition
Let $K: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ be a continuous positive-definite (Mercer) kernel and $\mu$ a finite measure on $\mathcal{X}$. Then there exist eigenfunctions $\{\phi_m\}$ orthonormal in $L^2(\mathcal{X},\mu)$ and non-negative eigenvalues $\lambda_1 \geq \lambda_2 \geq \cdots \geq 0$ such that
$$K(x, x') = \sum_{m=1}^{\infty} \lambda_m \phi_m(x)\phi_m(x')$$
where convergence is absolute and uniform. This makes precise the **kernel trick**: $K(x,x') = \langle\phi(x),\phi(x')\rangle_\mathcal{H}$ for an implicit (possibly infinite-dimensional) feature map $\phi(x) = (\sqrt{\lambda_1}\phi_1(x), \sqrt{\lambda_2}\phi_2(x),\ldots)$.

### Why it matters
Mercer's theorem is the mathematical foundation of the kernel trick, RKHS theory, and GP covariance functions. It shows that every valid Mercer kernel corresponds to an inner product in some Hilbert space, justifying the replacement of explicit feature computation with kernel evaluations — enabling infinite-dimensional feature spaces at finite computational cost.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[the-kernel-trick]] — uses
- [[eigendecomposition]] — uses
- [[reproducing-kernel-hilbert-space]] — uses
- [[mercer-kernel]] — uses
[To be populated during integration]