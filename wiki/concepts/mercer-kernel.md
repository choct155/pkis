---
aliases: []
also_type: []
analogous-to:
- covariance-function
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
generalizes:
- inner-product
id: pkis:concept:mercer-kernel
instantiates:
- reproducing-kernel-hilbert-space
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- the-kernel-trick
related_concepts: []
sources:
- murphy-pml1-intro-ch17
- murphy-pml2-advanced-ch18
tags:
- kernel
- positive-definite
- Mercer
- similarity
- RKHS
- nonparametric
title: Mercer Kernel (Positive Definite Kernel)
understanding: 0
uses:
- gram-matrix
- the-kernel-trick
- mercers-theorem
- reproducing-kernel-hilbert-space
- inner-product
---

## Definition
A Mercer kernel is any symmetric function $K : \mathcal{X} \times \mathcal{X} \to \mathbb{R}^+$ satisfying
$$\sum_{i=1}^{N}\sum_{j=1}^{N} K(x_i, x_j)\, c_i c_j \geq 0$$
for all $N$, all distinct points $x_i \in \mathcal{X}$, and all $c_i \in \mathbb{R}$. Equivalently, the **Gram matrix** $\mathbf{K}_{ij} = K(x_i, x_j)$ must be positive semi-definite for any finite set of inputs. Intuitively, a Mercer kernel is a generalized inner product that encodes prior knowledge about the similarity of two inputs.

### Why it matters
By Mercer's theorem, every such kernel admits an implicit feature map $\phi$ such that $K(x, x') = \phi(x)^T\phi(x')$, possibly in an infinite-dimensional space. This means algorithms that rely only on inner products (e.g., SVM, GP, kernel ridge regression) can operate in very rich — even infinite-dimensional — feature spaces at the cost of $O(N^2)$ kernel evaluations rather than $O(D)$ dot products.

### Key examples
- **Squared-exponential (RBF):** $K(x,x')=\exp\!\left(-\|x-x'\|^2/2\ell^2\right)$
- **Polynomial:** $K(x,x')=(x^Tx'+c)^M$
- **Matérn:** parameterized by smoothness order $\nu$
- **Periodic:** $K(r)=\exp\!\left(-\frac{2}{\ell^2}\sin^2(\pi r/p)\right)$
- **ARD:** replaces Euclidean distance with per-dimension Mahalanobis distance

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inner-product]] — uses
- [[reproducing-kernel-hilbert-space]] — uses
- [[mercers-theorem]] — uses
- [[the-kernel-trick]] — uses
- [[covariance-function]] — analogous-to
- [[inner-product]] — generalizes
- [[reproducing-kernel-hilbert-space]] — instantiates
- [[gram-matrix]] — uses
- [[the-kernel-trick]] — prerequisite-of
[To be populated during integration]