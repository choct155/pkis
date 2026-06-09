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
id: pkis:technique:forward-checking
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch06
tags:
- csp
- inference
- arc-consistency
- backtracking
- constraint-propagation
title: Forward Checking and Maintaining Arc Consistency (MAC)
understanding: 0
uses:
- arc-consistency-ac3
---

## Definition
Inference performed during backtracking search: each new variable assignment is an opportunity to prune the domains of neighboring unassigned variables, detecting dead ends earlier than search alone.

FORWARD CHECKING: whenever variable X is assigned, establish arc consistency for it by deleting from each unassigned neighbor Y's domain every value inconsistent with X's chosen value. If a domain empties, the partial assignment is inconsistent and the search backtracks immediately. Forward checking also supplies conflict sets for backjumping at no extra cost (record X=x in Y's conflict set whenever it deletes a value from Y). It synergizes with the minimum-remaining-values heuristic -- forward checking is an efficient way to incrementally compute the domain sizes MRV needs -- but it is incomplete: it only establishes consistency on the arcs into the just-assigned variable and does not propagate further, so it can leave two neighbors both reduced to the same single value without noticing the resulting conflict.

MAINTAINING ARC CONSISTENCY (MAC): after assigning X_i, call AC-3 but seed its queue only with the arcs (X_j, X_i) from unassigned neighbors X_j, then let propagation cascade as usual; empty a domain and backtrack. MAC is strictly more powerful than forward checking (it does forward checking's work on the initial arcs, then recursively propagates), and on harder CSPs the extra arc-consistency enforcement after each assignment pays off (Sabin & Freuder 1994).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[arc-consistency-ac3]] — uses: forward checking and MAC enforce arc consistency during search
[To be populated during integration]