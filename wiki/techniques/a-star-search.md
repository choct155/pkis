---
aliases: []
also_type: []
analogous-to:
- min-sum-algorithm
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- greedy-best-first-search
- uninformed-search
- heuristic-search-rl
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- knowledge-representation
- deep-learning
id: pkis:technique:a-star-search
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
- optimal
- best-first
title: A* Search
understanding: 0
uses:
- heuristic-function
- admissible-and-consistent-heuristics
---

## Definition
The most common informed search algorithm: a best-first search using the evaluation function f(n) = g(n) + h(n), where g(n) is the path cost from the initial state to n and h(n) is the heuristic estimate of the cheapest path from n to a goal -- so f(n) estimates the cost of the best solution through n. A* is **complete**; it is **cost-optimal** when h is admissible, and additionally never re-expands states when h is consistent. With a consistent heuristic A* is **optimally efficient**: any algorithm using the same heuristic must expand all the *surely expanded* nodes (those with f(n) < C*). A* prunes nodes with f(n) > C*, but for many problems the number expanded is still exponential in solution length, and its memory use (storing all reached states) is the main limitation. Numerous variants trade optimality or memory: **weighted A*** uses f = g + W*h (W>1) for bounded-suboptimal, faster search; **IDA*** is iterative-deepening A* using an f-cost cutoff; **RBFS** (recursive best-first search) and **SMA*** (simplified memory-bounded A*) achieve (near-)optimality in linear or bounded memory by backing up forgotten-subtree f-values; **beam search** caps the frontier size; and **bidirectional A*** searches from both ends. Uniform-cost search (W=0), A* (W=1), and greedy best-first search (W=infinity) are all special cases of weighted A*.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[heuristic-search-rl]] — contrasts-with: classical heuristic graph search vs decision-time tree search with learned value backups in RL
- [[min-sum-algorithm]] — analogous-to: both find lowest-cost paths over a weighted graph by expanding/relaxing nodes in cost order
- [[uninformed-search]] — contrasts-with: informed vs uninformed: A* uses a goal-distance estimate, uninformed search does not
- [[greedy-best-first-search]] — contrasts-with: A* trades the speed of greedy search for cost-optimality by adding g(n)
- [[admissible-and-consistent-heuristics]] — uses: cost-optimality and non-re-expansion guarantees rest on admissibility and consistency
- [[heuristic-function]] — uses: combines the heuristic h(n) with path cost g(n)
- [[best-first-search]] — specializes: best-first search with f(n) = g(n) + h(n)
[To be populated during integration]