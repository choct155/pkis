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
id: pkis:technique:variable-and-value-ordering-heuristics
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch06
tags:
- csp
- backtracking
- heuristics
- domain-independent
- fail-first
- fail-last
title: Variable and Value Ordering Heuristics for CSPs
understanding: 0
---

## Definition
Domain-independent heuristics that exploit the factored representation of a CSP to decide, within backtracking search, which variable to assign next and in what order to try its values -- the SELECT-UNASSIGNED-VARIABLE and ORDER-DOMAIN-VALUES choices. Unlike Chapter-3 uninformed search (improvable only with domain-specific heuristics), backtracking can be sped up by orders of magnitude with these general heuristics.

Variable selection is FAIL-FIRST: the MINIMUM-REMAINING-VALUES (MRV) heuristic (a.k.a. most-constrained-variable / fail-first) picks the variable with the fewest legal values, because if a variable has no legal value the failure is detected immediately, pruning the tree; it usually dominates static or random ordering. The DEGREE HEURISTIC, useful as a tie-breaker (and when MRV is uninformative, e.g. all regions start with three colors), selects the variable involved in the most constraints on other unassigned variables, reducing future branching (SA has degree 5 in the Australia map; choosing it first solves the map with no backtracking).

Value selection is FAIL-LAST: the LEAST-CONSTRAINING-VALUE heuristic prefers the value that rules out the fewest choices for neighboring variables, leaving maximum flexibility downstream. The asymmetry (fail-first for variables, fail-last for values) is principled: every variable must eventually be assigned, so failing fast on variables minimizes successful assignments to backtrack over; but only one consistent value per variable is needed, so trying the most-likely-to-succeed value first finds a solution sooner (value ordering is irrelevant if all solutions are wanted).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]