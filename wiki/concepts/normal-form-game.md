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
id: pkis:concept:normal-form-game
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- simultaneous-move
- payoff-matrix
- strategy-profile
title: Normal-Form Game
understanding: 0
---

## Definition
A game in which all players act simultaneously (or, equivalently, with no knowledge of the others' choices) and the outcome depends only on the resulting profile of actions. It is defined by three components: a set of players, a set of actions for each player, and a payoff function giving each player's utility for every combination of actions. For two players the payoff function is conventionally written as a single matrix whose cells list both players' payoffs. A *pure strategy* is a deterministic choice of action; a *mixed strategy* randomizes over actions; a *strategy profile* assigns a strategy to each player. Canonical examples include two-finger Morra, matching pennies, and the prisoner's dilemma.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]