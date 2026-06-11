---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- optimization
- machine-learning
id: pkis:framework:kkt-conditions
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
tags:
- Lagrangian
- constrained-optimization
- complementary-slackness
- duality
- SVM
title: Karush–Kuhn–Tucker (KKT) Conditions
understanding: 0
---

## Definition
The **KKT conditions** are necessary (and, for convex problems, sufficient) first-order optimality conditions for the constrained problem

$$\min_{\mathbf{x}} f(\mathbf{x}) \quad \text{s.t.} \quad g^{(i)}(\mathbf{x})=0,\; h^{(j)}(\mathbf{x})\leq 0.$$

The **generalised Lagrangian** is

$$L(\mathbf{x},\boldsymbol{\lambda},\boldsymbol{\alpha}) = f(\mathbf{x}) + \sum_i \lambda_i g^{(i)}(\mathbf{x}) + \sum_j \alpha_j h^{(j)}(\mathbf{x}).$$

At an optimal feasible point $\mathbf{x}^*$ the KKT conditions require:
1. **Stationarity**: $\nabla_{\mathbf{x}} L = \mathbf{0}$.
2. **Primal feasibility**: all $g^{(i)}(\mathbf{x}^*)=0$, $h^{(j)}(\mathbf{x}^*)\leq 0$.
3. **Dual feasibility**: $\alpha_j \geq 0$.
4. **Complementary slackness**: $\alpha_j h^{(j)}(\mathbf{x}^*) = 0$ for all $j$.

### Why it matters
KKT unifies equality and inequality constrained optimisation under a single framework. In ML it underlies the dual formulation of SVMs (the support vectors are exactly the active constraints), regularised regression (norm-ball constraints), and portfolio optimisation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]