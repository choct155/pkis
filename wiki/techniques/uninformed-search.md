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
id: pkis:technique:uninformed-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch03
tags:
- search
- blind-search
- bfs
- dfs
- uniform-cost
title: Uninformed Search
understanding: 0
---

## Definition
The family of search strategies that have access only to the problem definition and no estimate of how close a state is to a goal. The members differ only in which frontier node they expand first. **Breadth-first search (BFS)** expands the shallowest node first (FIFO queue, early goal test); it is complete and cost-optimal for unit action costs, with O(b^d) time and space. **Uniform-cost search** (Dijkstra's algorithm) expands the lowest path-cost g(n) node first (priority queue); it is complete and cost-optimal for general positive costs, with O(b^{1+floor(C*/eps)}) time and space. **Depth-first search (DFS)** expands the deepest node first (LIFO stack/recursion); usually run as tree-like search with O(bm) space but is neither complete (can loop or follow infinite paths) nor optimal. **Depth-limited search** treats nodes at depth l as leaves (O(b^l) time, O(bl) space) but is incomplete if l is too small. **Iterative deepening search** runs depth-limited search with increasing limits. **Bidirectional search** runs two frontiers (forward from the start, backward from the goal) that meet in the middle, giving O(b^{d/2}). **Backtracking search** is a DFS variant generating one successor at a time and mutating the state in place, using only O(m) memory. Performance is judged on completeness, cost optimality, time complexity, and space complexity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]