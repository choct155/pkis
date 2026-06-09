---
aliases: []
also_type: []
applies:
- curse-of-dimensionality
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
- robotics
- optimization
id: pkis:technique:cell-decomposition-motion-planning
instantiates:
- motion-planning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- motion-planning
- grid
- graph-search
title: Cell Decomposition Motion Planning
understanding: 0
uses:
- value-iteration
---

## Definition
A family of motion-planning methods that partition the free space into a finite number of contiguous cells (e.g., a regular grid) within which the local path problem is trivial, then solve the global problem by discrete graph search (e.g., A* or value iteration) over the cells. Limitations: cell count grows exponentially with dimension (curse of dimensionality), paths through a grid are jagged/non-smooth, and 'mixed' cells (partly free, partly occupied) force a soundness/completeness tradeoff that recursive subdivision can resolve. Hybrid A* stores, per cell, the exact continuous state attained on arrival and propagates using the robot motion model, yielding smooth, dynamically-feasible trajectories. Obstacle space need not be represented explicitly—a collision checker γ(q) suffices.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[curse-of-dimensionality]] — applies: limited to low-dimensional C-spaces because cell count grows exponentially in d
- [[value-iteration]] — uses: grid cell costs (shortest path to goal) computed by a deterministic value-iteration
- [[motion-planning]] — instantiates: a concrete grid/cell-based method for solving the motion-planning problem
[To be populated during integration]