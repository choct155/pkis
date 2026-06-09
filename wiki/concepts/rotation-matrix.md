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
id: pkis:concept:rotation-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch03
specializes:
- orthogonality
tags:
- mathematical-foundations
- linear-algebra
- analytic-geometry
title: Rotation Matrix
understanding: 0
---

## Definition
$$R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}$$

A rotation matrix is an orthogonal transformation that rotates a vector space about a fixed origin while preserving lengths and angles.

### Definition and 2D form
A **rotation** is a length- and angle-preserving automorphism of a Euclidean space fixing the origin; for $\theta > 0$ it rotates counterclockwise. In $\mathbb{R}^2$ it sends the standard basis to $\Phi(e_1) = [\cos\theta, \sin\theta]^\top$, $\Phi(e_2) = [-\sin\theta, \cos\theta]^\top$, giving $R(\theta)$ above, a special orthogonal matrix ($R^\top R = I$, $\det R = 1$).

### Higher dimensions
In $\mathbb{R}^3$ there are three elementary rotations about $e_1, e_2, e_3$, each fixing one axis and rotating the complementary plane. In $\mathbb{R}^n$, a **Givens rotation** $R_{ij}(\theta)$ is the identity with a $2\times2$ rotation block in rows/columns $i,j$ ($r_{ii} = r_{jj} = \cos\theta$, $r_{ij} = -\sin\theta$, $r_{ji} = \sin\theta$), rotating one plane while fixing the other $n-2$ dimensions.

### Properties
Rotations preserve distances and angles, compose by matrix multiplication, and are **non-commutative in 3D and higher**; only 2D rotations about the same point commute, forming an Abelian group.

### Why it matters
Rotations are central to computer graphics and robotics (orienting robot joints, camera transforms) and to numerical linear algebra: Givens rotations selectively zero matrix entries in QR decomposition and eigenvalue algorithms, and orthogonal transformations preserve the geometry that ML methods rely on.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[orthogonality]] — specializes
[To be populated during integration]