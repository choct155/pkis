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
id: pkis:technique:greedy-best-first-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch03
specializes:
- best-first-search
tags:
- search
- informed-search
- heuristic
- greedy
title: Greedy Best-First Search
understanding: 0
uses:
- heuristic-function
---

## Definition
A form of best-first search whose evaluation function is the heuristic alone, f(n) = h(n): it always expands the node that appears closest to the goal. This tends to find a solution quickly while expanding few nodes, but it is **not cost-optimal** -- being greedy on the heuristic can commit to a cheaper-looking first step that leads to a costlier overall path (e.g. Arad to Sibiu to Fagaras to Bucharest, 32 miles longer than the optimal route). As a graph search it is complete in finite state spaces but not in infinite ones; worst-case time and space are O(|V|), reducible toward O(bm) with a good heuristic. It is the W = infinity limit of weighted A*. The variant **speedy search** uses as its heuristic the estimated *number of actions* to a goal regardless of their cost, finding a solution quickly even if its cost is high.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[heuristic-function]] — uses: evaluates nodes purely by h(n)
- [[best-first-search]] — specializes: best-first search with f(n) = h(n)
[To be populated during integration]