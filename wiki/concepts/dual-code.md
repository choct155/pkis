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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:dual-code
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch13
tags:
- coding-theory
- linear-codes
- parity-check-matrix
- generator-matrix
- mod-2-arithmetic
- self-dual
title: Dual of a Linear Code
understanding: 0
---

## Definition
The **dual** $C^{\perp}$ of a linear $(N,K)$ code $C$ is the set of all length-$N$ binary vectors orthogonal (mod 2) to every codeword of $C$:
$$C^{\perp} = \{\mathbf{u} : \mathbf{u}\cdot\mathbf{x} = 0 \ (\mathrm{mod}\ 2)\ \forall \mathbf{x}\in C\}.$$
Operationally, the dual is obtained by **swapping the roles of the generator and parity-check matrices**: $C$ is the row span of $\mathbf{G}$ and the null space of $\mathbf{H}$; $C^{\perp}$ is the row span of $\mathbf{H}$ and the null space of $\mathbf{G}$. If $\mathbf{G}=[\mathbf{I}_K\,|\,\mathbf{P}^{\mathsf T}]$ then $\mathbf{H}=[\mathbf{P}\,|\,\mathbf{I}_M]$, and $C^{\perp}$ is an $(N, N-K)$ code.

### Self-orthogonality and self-duality
In mod-2 arithmetic a non-zero vector can be orthogonal to itself (precisely when it has even weight). A code is **self-orthogonal** if $C\subseteq C^{\perp}$, and **self-dual** if $C=C^{\perp}$ (forcing rate $1/2$, all-even weights, and $\mathbf{G}$ doubling as a parity-check matrix). The (7,4) Hamming code contains its dual: $H_{(7,4)}^{\perp}\subset H_{(7,4)}$.

### Why it matters
Good codes need not have good duals -- the classic example being LDPC codes, whose duals are bad low-density generator-matrix codes. Duals also let functions over a code (e.g. posteriors over codewords) be transformed via a finite-group Fourier transform, and self-dual / self-orthogonal codes underpin quantum error-correction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]