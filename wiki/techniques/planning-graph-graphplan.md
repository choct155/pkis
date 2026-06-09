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
contrasts-with:
- partial-order-planning
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- symbolic-subsymbolic
id: pkis:technique:planning-graph-graphplan
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- planning-graph
- graphplan
- mutex
- heuristic-estimation
title: Planning Graphs and Graphplan
understanding: 0
uses:
- classical-planning-pddl
---

## Definition
A planning graph is a specialized leveled data structure that encodes constraints on how actions relate to their preconditions and effects, and which propositions or actions are mutually exclusive (mutex). Graphplan (Blum & Furst, 1997) uses it to extract plans and was orders of magnitude faster than the partial-order planners of its time, revitalizing the field. Beyond direct plan extraction, planning graphs are widely used to compute admissible and informative heuristic estimates: for example, the FF planner estimates the ignore-delete-lists heuristic with the help of a planning graph, and planning graphs can be generalized to produce heuristics for conformant and contingent planning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partial-order-planning]] — contrasts-with: Graphplan outpaced partial-order planners
- [[classical-planning-pddl]] — uses: encodes constraints among PDDL actions, preconditions, effects
[To be populated during integration]