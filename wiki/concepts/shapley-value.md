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
- economics
id: pkis:concept:shapley-value
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- cooperative-game
- fair-division
- marginal-contribution
- axiomatic
title: Shapley Value
understanding: 0
---

## Definition
Lloyd Shapley's (1953) proposal for fairly dividing a grand coalition's value v(N) among its members, paying each player their *average marginal contribution* over all n! orderings in which the coalition could form: φ_i(G) = (1/n!) Σ_p mc_i(p_i), where mc_i(C) = v(C∪{i}) − v(C) and p_i is the set of players preceding i in ordering p. Its remarkable property is uniqueness: the Shapley value is the *only* payoff division satisfying four fairness axioms — Efficiency (all value distributed), Dummy Player (zero-contribution players get nothing), Symmetry (equal contributors get equal pay), and Additivity (value is additive across games). Though the naive computation is exponential, it can be computed in polynomial time under compact representations such as marginal contribution networks (MC-nets), where each rule defines a symmetric sub-game.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]