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
- multi-agent-systems
- decision-theory
- optimization
id: pkis:technique:backward-induction
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- dynamic-programming
- game-tree
- minimax
- equilibrium-computation
title: Backward Induction
understanding: 0
---

## Definition
A dynamic-programming technique for solving sequential games, generalizing the minimax algorithm to multiplayer payoff profiles. Working backwards from terminal states to the initial state, each non-terminal node is labeled with the payoff profile of the child that maximizes the payoff of the player to move there (using expected utility at chance nodes, arbitrary tie-breaking). The strategies it traces out are Nash-equilibrium strategies — in fact subgame-perfect equilibria — and it runs in time polynomial in the size of the game tree. The same reasoning, applied informally, shows why finitely repeated games with a known horizon collapse to repeating the stage-game equilibrium. Backward induction does not work for games of imperfect information.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]