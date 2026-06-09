---
aliases: []
also_type: []
applies:
- repeated-game
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- decision-theory
- economics
id: pkis:result:folk-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- repeated-games
- cooperation
- security-value
- punishment-strategies
title: Nash Folk Theorem
understanding: 0
uses:
- nash-equilibrium
---

## Definition
A class of results characterizing which outcomes can be sustained by Nash equilibria in infinitely repeated games. Defining a player's *security value* as the best payoff they can guarantee themselves, the rough form is: every outcome in which each player receives at least their security value can be sustained as a Nash equilibrium of the infinitely repeated game. Grim-style strategies are the mechanism — the mutual threat of permanent punishment for any deviation keeps every player in line — but the deterrent works only if each player believes the other has (or might have) adopted such a strategy. The folk theorems explain how rational self-interested agents can rationally achieve cooperative outcomes (e.g., mutual cooperation in the iterated prisoner's dilemma) that are unreachable in the one-shot game.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[nash-equilibrium]] — uses
- [[repeated-game]] — applies
[To be populated during integration]