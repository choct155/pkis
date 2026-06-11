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
- deep-learning
- ensemble-methods
- efficiency
extends:
- deep-ensembles
id: pkis:technique:batch-ensemble
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- fast-weights
- slow-weights
- memory-efficiency
- rank-one
- ensembles
title: Batch Ensemble
understanding: 0
uses:
- low-rank-approximation
---

## Definition
Each ensemble member $m$ is defined by a rank-one perturbation of a shared weight matrix:
$$\mathbf{W}_m = \mathbf{W} \odot s_m r_m^T, \qquad g_m(x) = \varphi\!\left(\mathbf{W}^T(x \odot s_m) \odot r_m\right)$$
where $\mathbf{W}$ are *slow weights* shared across all $M$ members, and $s_m, r_m$ are *fast weights* (per-member vectors).

### Why it matters
Naïve deep ensembles require $M\times$ memory and compute. Batch ensemble reduces the memory overhead to $O(M \cdot d)$ (two vectors per layer per member) while retaining diversity. Mini-batch inputs can be processed in parallel across ensemble members by replicating per-member vectors, enabling near-constant inference time overhead. Performance is competitive with deep ensembles and can be combined with MC dropout for further gains.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[low-rank-approximation]] — uses: Per-member perturbation is a rank-one matrix
- [[deep-ensembles]] — extends: Achieves ensemble diversity at a fraction of the memory cost via rank-one fast weights
[To be populated during integration]