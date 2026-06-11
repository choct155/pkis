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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- linear-algebra
- machine-learning
id: pkis:concept:range-and-nullspace
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- orthogonal-projection
related_concepts: []
sources:
- murphy-pml1-intro-ch07
specializes:
- linear-algebra
tags:
- column-space
- kernel
- rank-nullity
- linear-maps
- SVD
title: Range and Nullspace of a Matrix
understanding: 0
uses:
- basis-and-rank
- linear-mapping
- singular-value-decomposition
- linear-independence
---

## Definition
For $\mathbf{A} \in \mathbb{R}^{m \times n}$, the **range** (column space) is
$$\text{range}(\mathbf{A}) \triangleq \{\mathbf{v} \in \mathbb{R}^m : \mathbf{v} = \mathbf{A}\mathbf{x},\ \mathbf{x} \in \mathbb{R}^n\}$$
and the **nullspace** (kernel) is
$$\text{null}(\mathbf{A}) \triangleq \{\mathbf{x} \in \mathbb{R}^n : \mathbf{A}\mathbf{x} = \mathbf{0}\}.$$
The range is the set of all output vectors reachable by $\mathbf{A}$; the nullspace is the set of inputs that collapse to zero — together they characterise exactly what information $\mathbf{A}$ transmits vs. destroys.

### Why it matters
The dimension of the range equals $\text{rank}(\mathbf{A})$; the dimension of the nullspace equals $n - \text{rank}(\mathbf{A})$ (rank–nullity theorem). These spaces govern the existence and uniqueness of solutions to $\mathbf{A}\mathbf{x} = \mathbf{b}$: a solution exists iff $\mathbf{b} \in \text{range}(\mathbf{A})$, and the solution is unique iff $\text{null}(\mathbf{A}) = \{\mathbf{0}\}$. Both are computed numerically via the SVD.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-independence]] — uses
- [[singular-value-decomposition]] — uses
- [[orthogonal-projection]] — prerequisite-of
- [[linear-mapping]] — uses
- [[basis-and-rank]] — uses
- [[linear-algebra]] — specializes
[To be populated during integration]