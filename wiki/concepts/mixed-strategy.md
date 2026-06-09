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
id: pkis:concept:mixed-strategy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- randomized-policy
- solution-concept
title: Mixed Strategy
understanding: 0
uses:
- game-theory
---

## Definition
A randomized policy that selects actions according to a probability distribution, written e.g. [p:a; (1-p):b]. Mixed strategies generalize pure (deterministic) strategies and are essential because some games (e.g., matching pennies) have no pure-strategy Nash equilibrium yet always have a Nash equilibrium in mixed strategies. A key property at equilibrium is that every action played with positive probability yields the same expected utility as the mixed strategy itself, so the player is indifferent among them. Against a player who has revealed a mixed strategy, the opponent can always achieve their best response with a pure strategy, since expected utility is a linear combination of the pure-strategy payoffs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[game-theory]] — uses
[To be populated during integration]