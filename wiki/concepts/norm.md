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
id: pkis:concept:norm
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
title: Norm
understanding: 0
---

## Definition
$$\|\cdot\|: V \to \mathbb{R},\quad x \mapsto \|x\|$$

A norm is a function that assigns each vector a non-negative "length," formalizing the intuitive distance of a vector's tip from the origin.

### What it is
A norm on a vector space $V$ satisfies three axioms for all $\lambda \in \mathbb{R}$ and $x, y \in V$: it is **absolutely homogeneous** ($\|\lambda x\| = |\lambda|\,\|x\|$), obeys the **triangle inequality** ($\|x+y\| \le \|x\| + \|y\|$), and is **positive definite** ($\|x\| \ge 0$, with $\|x\| = 0 \iff x = 0$). The triangle inequality says that no side of a triangle exceeds the sum of the other two.

### Common norms
On $\mathbb{R}^n$ the **Manhattan ($\ell_1$) norm** is $\|x\|_1 = \sum_i |x_i|$, and the **Euclidean ($\ell_2$) norm** is $\|x\|_2 = \sqrt{\sum_i x_i^2} = \sqrt{x^\top x}$. The set $\{x : \|x\| = 1\}$ (the unit ball boundary) has a different shape for each norm: a diamond for $\ell_1$, a circle for $\ell_2$.

### Relation to inner products
Every inner product *induces* a norm via $\|x\| := \sqrt{\langle x, x\rangle}$, but not every norm arises this way (the Manhattan norm does not). Norms induced by inner products inherit the Cauchy-Schwarz inequality.

### Why it matters
Norms are the basic measure of magnitude in ML: $\ell_1$ and $\ell_2$ penalties drive sparse (lasso) and shrinkage (ridge) regularization, norms define loss magnitudes and gradient sizes, and they underpin distances and convergence criteria throughout optimization.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]