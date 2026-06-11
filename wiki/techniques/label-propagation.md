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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- semi-supervised-learning
- graph-methods
id: pkis:technique:label-propagation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- semi-supervised
- graph
- manifold-assumption
- transductive
- low-data
title: Label Propagation on Graphs
understanding: 0
---

## Definition
Label propagation assigns soft labels to unlabeled nodes in a similarity graph by iteratively spreading known labels across edges. Given $M$ labeled and $N$ unlabeled points with similarity weights $w_{i,j}$, define the $(M+N)\times(M+N)$ column-normalised transition matrix
$$T_{i,j} = \frac{w_{i,j}}{\sum_k w_{k,j}}$$
and a label matrix $\mathbf{Y}$ (rows = class distributions). Iterate: (1) $\mathbf{Y}\leftarrow\mathbf{T}\mathbf{Y}$; (2) row-normalise $\mathbf{Y}$; (3) clamp labeled rows to their one-hot vectors. This converges to a unique fixed point obtained by inverting the unlabeled-to-unlabeled block of $\mathbf{T}$.

### Why it matters
Label propagation operationalises the **manifold assumption** — nearby points share labels — without requiring a parametric model. It is a form of *transductive learning* that can initialise or regularise deep classifiers. Its convergence guarantee and closed-form solution make it appealing when graph construction is tractable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]