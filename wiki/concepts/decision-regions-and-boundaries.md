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
- machine-learning
- statistics
- pattern-recognition
id: pkis:concept:decision-regions-and-boundaries
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- classification
- decision-boundary
- posterior-probability
- reject-option
title: Decision Regions and Decision Boundaries
understanding: 0
---

## Definition
A classification rule partitions the input space $\mathcal{X}$ into $K$ **decision regions** $\{\mathcal{R}_k\}$ such that every $\mathbf{x}\in\mathcal{R}_k$ is assigned to class $C_k$. The surfaces separating adjacent regions are **decision boundaries** (or decision surfaces).

Optimal assignment to minimise misclassification probability requires:
$$\mathbf{x}\in\mathcal{R}_k \iff p(C_k|\mathbf{x}) \geq p(C_j|\mathbf{x}) \;\forall j,$$
i.e., assign to the class with the highest posterior probability.

### Why it matters
Decision regions provide the geometric vocabulary for all classifiers. Whether one uses generative models, discriminative models, or direct discriminant functions, the output is always a partition of $\mathcal{X}$. The reject option is obtained by leaving a region unassigned when $\max_k p(C_k|\mathbf{x})\leq\theta$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]