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
- multi-agent-systems
- decision-theory
id: pkis:concept:maximin-equilibrium
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
specializes:
- nash-equilibrium
tags:
- zero-sum-games
- von-neumann
- minimax
- linear-programming
title: Maximin Equilibrium
understanding: 0
---

## Definition
For two-player zero-sum games, the maximin (mixed) strategy maximizes a player's guaranteed expected payoff against a best-responding opponent. Von Neumann (1928) proved that every two-player zero-sum game has a maximin equilibrium in mixed strategies with a well-defined value: the upper bound obtained when one player must reveal their strategy first equals the lower bound obtained when the other reveals first. A maximin strategy gives two guarantees — no strategy does better against a well-playing opponent, and the player does just as well even if the strategy is revealed. Every Nash equilibrium of a zero-sum game is a maximin for both players. Computing it reduces to a linear program, solvable in time polynomial in the number of actions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[nash-equilibrium]] — specializes
[To be populated during integration]