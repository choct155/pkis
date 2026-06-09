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
- symbolic-subsymbolic
- knowledge-representation
id: pkis:technique:forward-state-space-planning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- progression
- heuristic-search
- forward-search
title: Forward State-Space Planning (Progression)
understanding: 0
---

## Definition
Forward (progression) planning searches the space of ground world-states from the initial state toward a goal state, applying any of the heuristic search algorithms (A*, greedy best-first, hill climbing) to a graph whose nodes are states and whose edges are applicable ground actions. Applicable actions in a state are obtained by unifying the state against each schema's preconditions and applying the resulting substitutions. Although the naive branching factor can be enormous (e.g. an air-cargo problem with hundreds of packages and tens of planes can yield thousands of applicable actions per state), forward search dominates modern practical planning because it operates on ground states, which makes accurate domain-independent heuristics easy to compute.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]