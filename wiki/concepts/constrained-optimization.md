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
- optimization
- machine-learning
id: pkis:concept:constrained-optimization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
tags:
- feasible-set
- projected-gradient
- Lagrangian
- KKT
- active-constraint
title: Constrained Optimization
understanding: 0
---

## Definition
**Constrained optimization** seeks

$$\mathbf{x}^* = \arg\min_{\mathbf{x} \in \mathbb{S}} f(\mathbf{x})$$

where $\mathbb{S}$ is a feasible set defined by equality constraints $g^{(i)}(\mathbf{x})=0$ and/or inequality constraints $h^{(j)}(\mathbf{x})\leq 0$. Points inside $\mathbb{S}$ are **feasible**; constraints with $h^{(j)}(\mathbf{x}^*)=0$ at optimum are **active**.

Approaches include: (1) projected gradient descent — step then project back into $\mathbb{S}$; (2) re-parameterisation — convert to an unconstrained problem; (3) KKT / Lagrangian methods — add penalty terms for constraint violations.

### Why it matters
Constrained optimisation appears throughout ML: training SVMs (margin constraints), weight-norm regularisation ($\|\mathbf{x}\|\leq 1$), fairness constraints, and resource-limited deployment. The KKT framework converts constrained problems into unconstrained saddle-point problems solvable by standard gradient methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]