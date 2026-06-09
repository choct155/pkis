---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- knowledge-representation
id: pkis:framework:adversarial-search
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch05
tags:
- games
- multi-agent
- game-tree-search
- competitive-environments
title: Adversarial Search
understanding: 0
---

## Definition
The framework for acting optimally in competitive environments where two or more agents have conflicting goals, by explicitly modeling adversarial agents through game-tree search rather than treating them as part of an aggregate economy or as mere environmental nondeterminism. The central insight is that an adversary actively tries to defeat us, so MAX's solution is not a single action sequence but a *contingent strategy* specifying a response to each opponent move (identical in form to a solution of a nondeterministic planning problem via AND-OR search). The canonical setting is deterministic, two-player, turn-taking, perfect-information, zero-sum games, formalized by S0, TO-MOVE, ACTIONS, RESULT, IS-TERMINAL, and UTILITY over a game tree. Because optimal play is generally intractable, all practical algorithms approximate: minimax (and its efficient equivalent alpha-beta pruning) backs up exact values but must cut off search and apply a heuristic evaluation function; Monte Carlo tree search averages over random playouts; expectiminimax handles chance nodes in stochastic games; and belief-state search handles imperfect information. Shared limitations include vulnerability to evaluation-function error, wasted computation when one move is obviously best (motivating metareasoning -- reasoning about which computations to perform), reasoning only at the move level rather than over abstract goals, and the historical reliance on hand-crafted knowledge now being displaced by self-play machine learning (AlphaZero, MuZero). The field has produced superhuman play in chess, checkers (solved -- a draw), Othello, Go, and poker.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]