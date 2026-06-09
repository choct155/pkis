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
id: pkis:technique:minimax-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch05
tags:
- adversarial-search
- games
- game-tree
- depth-first-search
- optimal-play
title: Minimax Algorithm
understanding: 0
---

## Definition
An algorithm that computes the optimal move for MAX in a deterministic, two-player, turn-taking, zero-sum, perfect-information game by recursively backing up minimax values through the game tree. The minimax value MINIMAX(s) is the utility (for MAX) of state s assuming both players play optimally to the end: it equals UTILITY(s,MAX) at terminal states, max over actions of the children's minimax values at MAX nodes, and min over actions at MIN nodes. The algorithm performs a complete depth-first exploration: it recurses to the leaves, applies UTILITY there, and backs the values up as the recursion unwinds, choosing at the root the action leading to the highest-value child. Time complexity is O(b^m) and space O(bm) (or O(m) generating actions one at a time), for branching factor b and maximum depth m; this exponential cost makes it impractical for nontrivial games (chess: b~=35, depth~=80 ply, 35^80~=10^123 states) but it remains the formal basis for the analysis of games and a generalization of AND-OR search. It assumes the opponent also plays optimally; against a suboptimal opponent MAX does at least as well, though the minimax move is not always the highest-expected-value choice. Minimax extends to >2 players by backing up a *vector* of utilities (one component per player), each interior node taking the successor vector that maximizes the value for the player to move there; this framing reveals that alliances can emerge as a consequence of selfish optimal play.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]