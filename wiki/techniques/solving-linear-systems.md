---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:solving-linear-systems
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch02
tags:
- mathematical-foundations
- linear-algebra
- algorithm
title: Solving Linear Systems (Gaussian Elimination)
understanding: 0
---

## Definition
$$A x = b,\quad A\in\mathbb{R}^{m\times n}\;\xrightarrow{\text{elementary row ops}}\; \text{(reduced) row-echelon form}$$

Gaussian elimination is the constructive algorithm that applies solution-preserving row operations to bring a system $A x = b$ into echelon form, from which all solutions can be read off.

### Elementary transformations
Three operations leave the solution set unchanged: swapping two rows, scaling a row by $\lambda\neq 0$, and adding one row to another. Applied to the **augmented matrix** $[A\,|\,b]$, they drive it toward **row-echelon form** (REF): zero rows at the bottom, each pivot strictly right of the one above, giving a staircase structure. **Reduced REF** additionally makes every pivot $1$ and the only non-zero entry in its column.

### Reading off solutions
Pivot variables are **basic**; the rest are **free**. The full solution is a **particular solution** (from expressing $b$ via pivot columns) plus the **general solution** of $A x=\mathbf{0}$ (the kernel), recoverable via the "Minus-1 Trick" on the RREF. A system has no, one, or infinitely many solutions, decided by $\mathrm{rk}(A)$ vs. $\mathrm{rk}([A|b])$.

### Related computations
The same machinery inverts a matrix — reduce $[A\,|\,I_n]$ to $[I_n\,|\,A^{-1}]$ — and tests linear independence and finds bases. When no exact solution exists, the least-squares normal equations $x=(A^\top A)^{-1}A^\top b$ give the best approximation.

### Why it matters
It is the workhorse for inversion, rank, and least squares; understanding it clarifies why linear regression, conditioning, and identifiability behave as they do.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]