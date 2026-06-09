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
id: pkis:concept:affine-space
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch02
tags:
- mathematical-foundations
- linear-algebra
- geometry
title: Affine Space
understanding: 0
---

## Definition
$$L = x_0 + U = \{x_0 + u : u \in U\},\quad U\subseteq V\ \text{a subspace}$$

An affine subspace is a vector subspace shifted off the origin by a support point — the lines, planes, and hyperplanes that need not pass through $\mathbf{0}$.

### Definition
For a vector space $V$, a support point $x_0\in V$, and a subspace $U$ (the **direction space**), the set $L=x_0+U$ is an **affine subspace** (or linear manifold). If $x_0\notin U$ then $\mathbf{0}\notin L$, so $L$ is *not* a vector subspace. With an ordered basis $(b_1,\ldots,b_k)$ of $U$, every $x\in L$ is uniquely $x = x_0 + \sum_{i=1}^{k}\lambda_i b_i$ — the **parametric equation**.

### Examples
Lines ($k=1$), planes ($k=2$), and **hyperplanes** ($k=n-1$ in $\mathbb{R}^n$). The solution set of an *inhomogeneous* system $A x = b$ ($b\neq\mathbf{0}$) is an affine subspace of dimension $n-\mathrm{rk}(A)$ — a particular solution ($x_0$) plus the homogeneous null space ($U$).

### Affine mappings
An **affine mapping** $x\mapsto a + \Phi(x)$ is a linear map $\Phi$ followed by a translation $a$; it preserves dimension and parallelism but not the origin.

### Why it matters
The "linear" layers of ML models are usually affine (a weight matrix plus a bias), decision boundaries of linear classifiers are hyperplanes, and the particular-plus-homogeneous structure of $A x = b$ is exactly an affine space — making this the geometric language for regression and classification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]