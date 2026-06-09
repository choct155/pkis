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
- reinforcement-learning
- statistical-learning
id: pkis:technique:memory-based-function-approximation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- nonparametric
- lazy-learning
- nearest-neighbor
- locally-weighted-regression
title: Memory-based Function Approximation
understanding: 0
---

## Definition
A nonparametric alternative to parametric value approximation: training examples s' ↦ g are simply stored (or a subset retained) without updating any parameters; when a query state's value is needed, relevant examples—usually the nearest neighbors by some distance—are retrieved and combined to produce an estimate, then the local approximation is discarded ('lazy learning'). Variants include nearest neighbor (return the closest example's value), weighted average (distance-weighted mean of neighbors), and locally weighted regression (fit a local surface minimizing a distance-weighted error and evaluate it at the query). Because the functional form is set by the data rather than a fixed class, accuracy improves as examples accumulate. It suits RL well: trajectory sampling concentrates examples where the agent actually goes, experience has immediate local effect, and memory grows only linearly in dimension and example count—addressing the curse of dimensionality. The practical challenge is fast nearest-neighbor retrieval, accelerated with k-d trees or special hardware.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]