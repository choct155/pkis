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
generalizes:
- dominant-strategy
id: pkis:concept:nash-equilibrium
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- solution-concept
- best-response
- stability
title: Nash Equilibrium
understanding: 0
uses:
- game-theory
- mixed-strategy
---

## Definition
A strategy profile in which no player can unilaterally change their strategy and obtain a higher payoff, assuming the others keep their strategies fixed; equivalently, every player is simultaneously playing a best response to the others. A Nash equilibrium is a *locally* stable point — there may be multiple equilibria (a coordination problem). Every dominant-strategy equilibrium is also a Nash equilibrium. Nash's theorem (1950) establishes that every finite game has at least one Nash equilibrium in mixed strategies, which is why it is the central solution concept of non-cooperative game theory: unlike dominant-strategy equilibrium, it is guaranteed to exist. Refinements such as Bayes–Nash equilibrium (equilibrium with respect to priors over others' strategies) and subgame-perfect equilibrium address its limitations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[dominant-strategy]] — generalizes
- [[mixed-strategy]] — uses
- [[game-theory]] — uses
[To be populated during integration]