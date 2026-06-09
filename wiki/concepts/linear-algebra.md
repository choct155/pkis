---
aliases: []
also_type:
- framework
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-09'
domain:
- statistical-learning
- bayesian-stats
- deep-learning
id: pkis:concept:linear-algebra
knowledge_type: concept
maturity: settled
prerequisite-of:
- principal-component-analysis
related_concepts:
- '[[analytic-geometry]]'
- '[[matrix-decompositions]]'
- '[[vector-calculus]]'
sources:
- '[[deisenroth-mml]]'
- '[[carrell-groups-matrices-vectors]]'
tags:
- mathematical-foundations
title: Linear Algebra
understanding: 0
uses:
- vector-space
- linear-mapping
---

The mathematical study of vector spaces, linear maps, and their structure — the substrate for virtually all computation in machine learning, from data representation (vectors and matrices) through optimization (gradient updates) to model parameterization.

## Reading Path
- [[deisenroth-mml]] (unread) — ML-oriented treatment: systems of linear equations, matrices as linear maps, basis and rank
- [[carrell-groups-matrices-vectors-ch03]] (unread) — matrix algebra from group-theoretic perspective; matrices as linear maps
- [[carrell-groups-matrices-vectors-ch06]] (unread) — abstract vector space axioms, bases, dimension, inner product spaces
- [[carrell-groups-matrices-vectors-ch07]] (unread) — linear mappings, rank-nullity, dual space

## Connections
- [[linear-mapping]] — uses: Linear mappings and their matrix representations are core to linear algebra.
- [[vector-space]] — uses: Vector spaces are the central object of study in linear algebra.
- [[principal-component-analysis]] — prerequisite-of: MML Ch.1: data is represented as vectors/matrices (linear algebra, Ch.2) which is the foundation for the dimensionality-reduction pillar realized as PCA (Ch.10).

## Core algebraic structures
Deisenroth et al. (Ch. 2) build linear algebra as a layered hierarchy of structures, each adding one capability:

- **Group** $(\mathcal{G},\otimes)$ — a set closed under an associative operation with a neutral element and inverses. The invertible $n\times n$ matrices under multiplication form the (non-Abelian) **general linear group** $GL(n,\mathbb{R})$.
- **[[vector-space]]** — an Abelian group under addition plus a compatible scalar multiplication; the closure idea ("what can I reach by adding and scaling?") is the unifying motivation, with **subspaces** as closed subsets.
- **[[linear-independence]]** and **[[basis-and-rank]]** — minimal non-redundant generating sets (bases) fix coordinates and dimension; rank measures effective degrees of freedom.
- **[[linear-mapping]]** — structure-preserving maps between spaces, represented (once bases are chosen) by transformation matrices, with image/kernel and the rank-nullity theorem.
- **[[affine-space]]** — subspaces offset from the origin (lines, planes, hyperplanes), the geometry behind biased/inhomogeneous models.

The computational backbone tying these together is **[[solving-linear-systems]]** (Gaussian elimination), which simultaneously solves $A x = b$, inverts matrices, finds bases, and tests independence.

Deisenroth et al. (Ch. 2) build linear algebra as a layered hierarchy of structures, each adding one capability:

- **Group** $(\mathcal{G},\otimes)$ — a set closed under an associative operation with a neutral element and inverses. The invertible $n\times n$ matrices under multiplication form the (non-Abelian) **general linear group** $GL(n,\mathbb{R})$.
- **[[vector-space]]** — an Abelian group under addition plus a compatible scalar multiplication; the closure idea ("what can I reach by adding and scaling?") is the unifying motivation, with **subspaces** as closed subsets.
- **[[linear-independence]]** and **[[basis-and-rank]]** — minimal non-redundant generating sets (bases) fix coordinates and dimension; rank measures effective degrees of freedom.
- **[[linear-mapping]]** — structure-preserving maps between spaces, represented (once bases are chosen) by transformation matrices, with image/kernel and the rank-nullity theorem.
- **[[affine-space]]** — subspaces offset from the origin (lines, planes, hyperplanes), the geometry behind biased/inhomogeneous models.

The computational backbone tying these together is **[[solving-linear-systems]]** (Gaussian elimination), which simultaneously solves $A x = b$, inverts matrices, finds bases, and tests independence.