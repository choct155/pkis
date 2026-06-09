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
id: pkis:technique:backward-regression-planning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- regression
- backward-search
- relevant-actions
title: Backward Regression Planning
understanding: 0
---

## Definition
Backward (regression) planning searches from the goal toward the initial state, considering only *relevant* actions — those whose effect unifies with a goal literal and whose effects do not negate any part of the goal. Regressing a goal g over an action a yields a predecessor goal description g' in which the action's preconditions must have held while the literals it added/deleted need not have: POS(g') = (POS(g) - ADD(a)) ∪ POS(Precond(a)) and NEG(g') = (NEG(g) - DEL(a)) ∪ NEG(Precond(a)). Because it works backward from a small set of goal literals using states-with-variables, regression keeps the branching factor far lower than forward search (the classic ISBN example: one regressed action vs. enumerating a trillion ground Buy actions), but the variable-laden states make good heuristics harder to obtain.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]