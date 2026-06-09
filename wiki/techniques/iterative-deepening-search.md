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
- optimization
- knowledge-representation
id: pkis:technique:iterative-deepening-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch03
tags:
- search
- depth-first
- depth-limited
- memory-efficient
title: Iterative Deepening Search
understanding: 0
---

## Definition
An uninformed search that solves the problem of choosing a depth limit by repeatedly calling depth-limited search with limits l = 0, 1, 2, ... until a solution is found (the depth-limited call returns failure rather than cutoff). It combines the modest memory of depth-first search, O(bd) space when a solution exists, with the completeness and unit-cost optimality of breadth-first search. Although shallow nodes are regenerated many times (those at depth d once, their parents twice, ... the root's children d times), most nodes lie in the bottom level, so the total node count N(IDS) = d*b + (d-1)*b^2 + ... + b^d is O(b^d) -- asymptotically the same as breadth-first search. It is the preferred uninformed method when the state space is larger than memory and the solution depth is unknown. Its informed analogue is iterative-deepening A* (IDA*), which uses an f = g+h cost cutoff instead of a depth cutoff.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]