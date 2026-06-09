---
aliases: []
also_type: []
applies:
- constraint-satisfaction-problem
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
id: pkis:technique:backtracking-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch06
tags:
- csp
- depth-first-search
- commutativity
- backjumping
- conflict-set
- no-good
- constraint-learning
title: Backtracking Search for CSPs
understanding: 0
uses:
- forward-checking
- variable-and-value-ordering-heuristics
---

## Definition
The standard complete solver for CSPs: a depth-first search over partial assignments that exploits the commutativity of variable assignment. Because the order of assigning values does not matter in a CSP, the search need consider only a single variable at each node (collapsing the naive n! * d^n leaf count to d^n). BACKTRACKING-SEARCH repeatedly selects an unassigned variable, tries each domain value in turn extending the partial assignment via recursion, and on failure restores the previous state and tries the next value; it mutates a single state representation rather than copying. It is improved by domain-independent heuristics (variable/value ordering), by interleaved inference (forward checking, MAC), and by smarter failure handling.

When a branch fails, naive CHRONOLOGICAL BACKTRACKING simply undoes the most recent assignment, which can be wasteful (e.g. re-coloring Tasmania to fix an unrelated South Australia conflict). BACKJUMPING instead records a conflict set for the failing variable (the assigned variables in conflict with all its values) and jumps back to the most recent variable in that set. Simple backjumping is provably redundant under forward checking. CONFLICT-DIRECTED BACKJUMPING uses a deeper conflict set -- the preceding variables that, together with subsequent variables, made the assignment unsolvable -- propagating conflict sets backward via conf(X_i) <- conf(X_i) U conf(X_j) - {X_i}, so it can jump even when the immediate variable still had legal values.

CONSTRAINT LEARNING (no-good learning) extracts a minimal subset of the conflict set responsible for failure -- a NO-GOOD -- and records it (as a new constraint or in a cache) to avoid re-encountering the same dead end elsewhere in the search tree. This is one of the most important techniques in modern CSP/SAT solvers; it descends from dependency-directed backtracking (Stallman & Sussman 1977) and underlies truth-maintenance systems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variable-and-value-ordering-heuristics]] — uses: MRV, degree, and LCV heuristics guide backtracking choices
- [[forward-checking]] — uses: backtracking interleaves forward checking / MAC inference
- [[constraint-satisfaction-problem]] — applies: backtracking search is the standard complete solver for CSPs
[To be populated during integration]