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
id: pkis:technique:alpha-beta-pruning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch05
specializes:
- minimax-algorithm
tags:
- adversarial-search
- games
- pruning
- move-ordering
- transposition-table
title: Alpha-Beta Pruning
understanding: 0
---

## Definition
A pruning technique that computes exactly the same optimal move as minimax while avoiding examination of subtrees that provably cannot affect the root decision. Because minimax search is depth-first, only nodes along a single root-to-leaf path are active at once; alpha-beta carries two bounds along that path: alpha = the best (highest) value found so far for MAX ('at least'), beta = the best (lowest) value found so far for MIN ('at most'). A node's recursive evaluation is terminated (its remaining children pruned) as soon as its backed-up value is known to be no better than alpha (for a MIN node) or no worse than beta (for a MAX node) -- i.e., the player who could route here already has a better alternative at this level or higher. Effectiveness depends critically on move ordering: with perfect ordering alpha-beta examines only O(b^(m/2)) nodes (effective branching factor sqrt(b), ~6 instead of 35 for chess, roughly doubling reachable depth), versus O(b^(3m/4)) with random ordering. Practical ordering heuristics include trying captures/threats first, dynamic schemes such as the *killer move heuristic* (try moves that caused cutoffs earlier), and ranking from iterative-deepening searches; *transposition tables* cache backed-up values of states reachable by different move permutations (transpositions), roughly doubling reachable depth in chess. *Singular extensions* (extending search on a move clearly better than all alternatives) help mitigate the horizon effect. Conceived by McCarthy (1956); proven correct and analyzed by Knuth & Moore (1975); shown asymptotically optimal among fixed-depth game-tree algorithms by Pearl (1982). Distinguished from *forward pruning* (e.g. beam search, PROBCUT, late move reduction), which prunes moves that merely *appear* poor and may discard the best move.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[minimax-algorithm]] — specializes: Alpha-beta computes the identical optimal move as minimax while pruning provably irrelevant subtrees.
[To be populated during integration]