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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:concept:inner-product
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch03
tags:
- mathematical-foundations
- linear-algebra
- analytic-geometry
title: Inner Product
understanding: 0
---

## Definition
$$\langle x, y\rangle = \hat{x}^\top A \hat{y},\quad A \text{ symmetric positive definite}$$

An inner product is a symmetric, positive-definite bilinear map $\langle \cdot, \cdot\rangle : V \times V \to \mathbb{R}$ that equips a vector space with geometry: lengths, angles, distances, and orthogonality.

### Definition
A bilinear map $\Omega$ is linear in each argument. It is an **inner product** if it is additionally **symmetric** ($\langle x,y\rangle = \langle y,x\rangle$) and **positive definite** ($\langle x,x\rangle > 0$ for $x \neq 0$). The pair $(V, \langle\cdot,\cdot\rangle)$ is an *inner product space*. The familiar **dot product** $x^\top y = \sum_i x_i y_i$ is one instance, yielding a *Euclidean vector space*; with a general SPD matrix $A$, $\langle x,y\rangle = x^\top A y$ defines a different geometry.

### Theorem (matrix characterization)
For a finite-dimensional $V$ with ordered basis $B$, $\langle\cdot,\cdot\rangle$ is an inner product **iff** there exists a symmetric positive definite matrix $A$ with $\langle x,y\rangle = \hat{x}^\top A \hat{y}$, where $A_{ij} = \langle b_i, b_j\rangle$ and $\hat{x}, \hat{y}$ are coordinates in $B$.

### Induced structure
An inner product induces a norm $\|x\| = \sqrt{\langle x,x\rangle}$, a distance $d(x,y) = \|x-y\|$, and angles via $\cos\omega = \langle x,y\rangle / (\|x\|\|y\|)$, valid because of the Cauchy-Schwarz inequality $|\langle x,y\rangle| \le \|x\|\|y\|$. The concept generalizes to functions, $\langle u,v\rangle = \int_a^b u(x)v(x)\,dx$, leading to Hilbert spaces.

### Why it matters
The inner product is the single object from which all of analytic geometry flows, and it is the computational primitive of kernel methods: the kernel trick computes inner products in high- (even infinite-) dimensional feature spaces implicitly, powering SVMs, kernel PCA, and Gaussian processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]