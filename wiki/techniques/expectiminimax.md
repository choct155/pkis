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
generalizes:
- minimax-algorithm
id: pkis:technique:expectiminimax
instantiates:
- adversarial-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch05
tags:
- adversarial-search
- games-of-chance
- chance-nodes
- expected-value
- backgammon
title: Expectiminimax
understanding: 0
---

## Definition
A generalization of minimax to stochastic games -- games with a random element such as dice rolls or card shuffles (e.g. backgammon) -- by introducing *chance nodes* into the game tree alongside MAX and MIN nodes. Because the random outcome is not known in advance, positions have no definite minimax value; instead one computes the *expected value*. EXPECTIMINIMAX(s) equals UTILITY(s,MAX) at terminal states, max over actions at MAX nodes, min over actions at MIN nodes, and at a CHANCE node the probability-weighted sum sum_r P(r) * EXPECTIMINIMAX(RESULT(s,r)) over the possible chance outcomes r (e.g. the 21 distinct two-dice rolls, doubles at 1/36 and others at 1/18). Two consequences distinguish it from deterministic minimax: (1) the evaluation function must return values that are a *positive linear transformation* of the probability of winning -- unlike deterministic minimax, the chosen move can change even when only the magnitudes (not the order) of leaf evaluations change; and (2) complexity rises to O(b^m n^m) for n distinct chance outcomes per node, making deep lookahead infeasible (backgammon: n=21, b~=20, often only ~3 ply). Alpha-beta-style pruning can still be applied to chance nodes if utility values are bounded, since bounds on the children then bound their average; high-fan-out chance nodes (e.g. Yahtzee) motivate forward pruning by sampling chance branches or switching to Monte Carlo tree search. Proposed by Michie (1966); chance-node pruning by Ballard (1983).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[adversarial-search]] — instantiates: Expectiminimax is the adversarial-search method for stochastic games.
- [[minimax-algorithm]] — generalizes: Expectiminimax extends minimax to stochastic games by adding chance nodes evaluated as expected values.
[To be populated during integration]