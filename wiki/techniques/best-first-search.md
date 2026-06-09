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
id: pkis:technique:best-first-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch03
tags:
- search
- frontier
- evaluation-function
- priority-queue
title: Best-First Search
understanding: 0
uses:
- state-space-search
---

## Definition
A general search template that, on each iteration, removes from the frontier the node n with the minimum value of an **evaluation function** f(n), returns it if its state is a goal, and otherwise expands it, adding each child to the frontier (or re-adding it with a cheaper path). The frontier is a **priority queue** ordered by f, and reached states are stored in a lookup table (e.g. a hash table) so that redundant paths can be detected and only the best path to each state retained (graph search). By choosing different f functions, best-first search instantiates a whole family of concrete algorithms: f = depth gives breadth-first search, f = g(n) (path cost) gives uniform-cost search, f = h(n) gives greedy best-first search, and f = g(n)+h(n) gives A* search. Because it tests for the goal when a node is *popped* (late goal test) rather than when generated, best-first search can guarantee optimality whenever f is a suitable lower bound on solution cost.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[state-space-search]] — uses: operates over the search tree and frontier defined by the state-space-search framework
[To be populated during integration]