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
- economics
id: pkis:concept:repeated-game
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
specializes:
- normal-form-game
tags:
- iterated-game
- stage-game
- finite-state-strategies
- backward-induction
title: Repeated Game
understanding: 0
uses:
- backward-induction
---

## Definition
A multi-move game in which players repeatedly play rounds of a single-move *stage game*; a strategy specifies an action for every possible history of play. With a fixed, finite, mutually known number of rounds, backward induction forces the stage-game Nash equilibrium in every round (e.g., always defect in the finitely repeated prisoner's dilemma). Dropping any of those three conditions breaks the induction: in *infinitely* repeated games, strategies are represented as finite-state machines (e.g., Tit-for-Tat, Grim, Hawk, Dove) and utility is measured by the limit of means of per-round payoffs. Infinite repetition enables cooperative outcomes (e.g., Grim vs. Grim) to be sustained as Nash equilibria that are impossible in the one-shot game, via the threat of perpetual punishment.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[backward-induction]] — uses
- [[normal-form-game]] — specializes
[To be populated during integration]