---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- knowledge-representation
id: pkis:concept:game-tree
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- minimax-algorithm
related_concepts: []
sources:
- russell-norvig-aima-ch05
tags:
- adversarial-search
- games
- search-tree
- ply
title: Game Tree
understanding: 0
---

## Definition
A search tree superimposed over the state-space graph of a game, in which vertices are game states (positions), edges are legal moves, and paths follow sequences of moves. A *complete* game tree follows every move sequence all the way to a terminal state. Games are formally specified by S0 (initial state), TO-MOVE(s), ACTIONS(s), RESULT(s,a) (transition model), IS-TERMINAL(s) (terminal test), and UTILITY(s,p) (payoff to player p at a terminal state). The canonical AI setting is deterministic, two-player, turn-taking, perfect-information, zero-sum games (e.g. chess, Go), where the two players are conventionally MAX (moves first, maximizes utility) and MIN (minimizes it); 'perfect information' is synonymous with 'fully observable', and 'zero-sum' means one player's gain is exactly the other's loss. A *ply* is one move by one player (one level deeper in the tree), disambiguating the word 'move' which sometimes denotes a turn by each side. Game trees are typically intractably large (tic-tac-toe has <9!=362,880 leaves and 5,478 distinct states; chess exceeds 10^40 nodes), and may be infinite if the state space is unbounded or positions can repeat indefinitely, so the complete tree is a theoretical construct rather than a realizable object. The tree may include MAX nodes, MIN nodes, and (in stochastic games) chance nodes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[minimax-algorithm]] — prerequisite-of: The game-tree formalism (S0, ACTIONS, RESULT, UTILITY, MAX/MIN) must be understood before minimax.
[To be populated during integration]