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
- knowledge-representation
- optimization
- symbolic-subsymbolic
id: pkis:technique:dpll-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch07
tags:
- dpll
- sat-solver
- backtracking
- unit-propagation
- model-checking
title: DPLL Algorithm
understanding: 0
---

## Definition
A complete, recursive, depth-first backtracking search over truth assignments that decides the satisfiability of a CNF sentence. DPLL (Davis, Logemann, Loveland 1962, refining Davis-Putnam 1960) improves on naive model enumeration (TT-ENTAILS?) with three devices: early termination (a clause is true once any literal is true, and the sentence false once any clause is false, so whole subtrees are pruned before the model is complete); the pure-symbol heuristic (a symbol appearing with only one sign across all not-yet-satisfied clauses can safely be set to make its literal true); and the unit-clause heuristic (a clause with all but one literal already falsified forces that literal, and such forced assignments cascade — unit propagation). DPLL is the foundation of modern SAT solvers, which add component analysis, variable/value ordering, conflict-driven clause learning, intelligent backtracking, random restarts, and fast indexing.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]