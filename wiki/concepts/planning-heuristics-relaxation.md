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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- symbolic-subsymbolic
id: pkis:concept:planning-heuristics-relaxation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- heuristics
- admissible-heuristic
- relaxation
- abstraction
- ignore-delete-lists
title: Planning Heuristics via Relaxation and Abstraction
understanding: 0
---

## Definition
Because PDDL uses a factored representation of states and actions, admissible domain-independent heuristics can be derived automatically by relaxing the action schemas. The two master relaxations are: adding edges to the state-space graph (making paths easier to find) and grouping nodes (state abstraction, a many-to-one mapping that shrinks the state space). Edge-adding relaxations include the *ignore-preconditions* heuristic (drop all preconditions, reducing to an NP-hard set-cover whose greedy approximation is within log n of optimum but loses admissibility), selective precondition dropping (recovering misplaced-tiles and Manhattan-distance heuristics for the sliding-tile puzzle from a single Slide schema), and the *ignore-delete-lists* heuristic (remove negative effects so progress is monotonic; solvable approximately by hill climbing). State abstraction (e.g. ignoring fluents, pattern databases) and the subgoal-independence assumption supply further estimates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]