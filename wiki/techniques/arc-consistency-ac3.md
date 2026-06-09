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
id: pkis:technique:arc-consistency-ac3
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch06
tags:
- csp
- constraint-propagation
- arc-consistency
- path-consistency
- node-consistency
- inference
title: Arc Consistency and the AC-3 Algorithm
understanding: 0
---

## Definition
A family of local-consistency conditions for CSPs, and the standard algorithm (AC-3, Mackworth 1977) for enforcing arc consistency, used as preprocessing or interleaved with search to shrink variable domains before/while branching.

The consistency hierarchy: a variable is NODE-CONSISTENT if every value in its domain satisfies its unary constraints (trivially enforced by domain reduction). X_i is ARC-CONSISTENT with respect to X_j if for every value in D_i there is some value in D_j satisfying the binary constraint on the arc (X_i, X_j); a graph is arc-consistent if every variable is arc-consistent with every other. PATH CONSISTENCY tightens binary constraints by reasoning over triples: {X_i, X_j} is path-consistent w.r.t. X_m if every consistent assignment to {X_i,X_j} can be extended to X_m satisfying the constraints on {X_i,X_m} and {X_m,X_j}. These generalize to k-CONSISTENCY: any consistent assignment to k-1 variables can be extended to any k-th variable (1-consistency = node, 2 = arc, 3 = path for binary graphs). A CSP is strongly k-consistent if it is k-, (k-1)-, ... 1-consistent; strong n-consistency lets a CSP be solved backtrack-free in O(n^2 d), but establishing it costs time and space exponential in n in the worst case.

AC-3 mechanism: maintain a queue initially containing all arcs (each binary constraint becomes two directed arcs). Pop an arc (X_i, X_j), REVISE D_i by deleting any value with no supporting value in D_j. If D_i is unchanged, continue; if revised, re-enqueue all arcs (X_k, X_i) for neighbors X_k (since D_i shrank, X_k may now lose values). If any domain empties, the CSP is unsolvable and AC-3 returns failure. Termination yields an arc-consistent CSP with the same solution set but smaller domains (sometimes solving the problem outright, e.g. easy Sudoku, or proving infeasibility). Complexity: with n variables, max domain size d, and c arcs, each arc enters the queue at most d times and a revision costs O(d^2), giving O(c d^3) worst-case time.

Limits: arc consistency alone cannot detect that the three-colorable Australia map needs three colors (2-coloring fails only at a triple); stronger consistency (path / k-consistency) is needed. Determining the right consistency level is empirical; 2-consistency is common, 3-consistency less so.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]