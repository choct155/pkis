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
date_updated: '2026-06-20'
domain:
- statistical-learning
id: pkis:concept:linear-mapping
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch02
- carrell-groups-matrices-vectors-ch07
- carrell-groups-matrices-vectors-ch10
specializes:
- affine-space
tags:
- mathematical-foundations
- linear-algebra
title: Linear Mapping
understanding: 0
uses:
- solving-linear-systems
---

## Definition
$$\Phi(\lambda x + \psi y) = \lambda\,\Phi(x) + \psi\,\Phi(y)\quad \forall x,y\in V,\ \lambda,\psi\in\mathbb{R}$$

A linear mapping (homomorphism) is a function between vector spaces that respects addition and scaling — and once bases are fixed, every such mapping is just a matrix.

### Definition
$\Phi:V\to W$ is linear if it preserves linear combinations as above. Given ordered bases $B$ of $V$ and $C$ of $W$, the **transformation matrix** $A_\Phi$ has as its $j$-th column the coordinates of $\Phi(b_j)$ with respect to $C$, so coordinate vectors transform by $\hat{y}=A_\Phi\hat{x}$.

### Special cases
$\Phi$ can be injective, surjective, or bijective; a linear bijection is an **isomorphism** (and finite-dimensional spaces are isomorphic iff they have equal dimension). $V\to V$ maps are **endomorphisms**, bijective ones **automorphisms**.

### Image, kernel, basis change
The **image** $\mathrm{Im}(\Phi)=\mathrm{span}$ of the columns (the column space) and the **kernel** $\ker(\Phi)=\{v:\Phi(v)=\mathbf{0}\}$ (the null space, = solutions of $A x=\mathbf{0}$) are subspaces linked by the **rank-nullity theorem** $\dim\ker(\Phi)+\dim\mathrm{Im}(\Phi)=\dim V$. Under a basis change the matrix becomes $\tilde{A}_\Phi = T^{-1}A_\Phi S$ (an *equivalent*, or if $V=W$ and $S=T$, *similar*, matrix).

### Why it matters
Neural network layers, projections, rotations, and coordinate transforms are all linear mappings; the matrix view turns abstract structure-preservation into concrete, composable arithmetic ($A_{\Psi\circ\Phi}=A_\Psi A_\Phi$).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[solving-linear-systems]] — uses: The kernel (null space) of a linear map is the general solution of the homogeneous system Ax=0, found by elimination.
- [[affine-space]] — specializes: An affine mapping is a linear mapping composed with a translation.
[To be populated during integration]