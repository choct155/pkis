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
id: pkis:concept:bargaining-theory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- negotiation
- alternating-offers
- discount-factor
- monotonic-concession
- Zeuthen-strategy
title: Bargaining Theory
understanding: 0
---

## Definition
The game-theoretic study of how agents reach agreement on matters of common interest by exchanging offers under a protocol, accepting or rejecting each. In the *alternating offers* model (Rubinstein 1982) agents take turns proposing divisions; with a fixed finite horizon the last mover takes all, and with unbounded rounds there are infinitely many Nash equilibria — resolved by assuming *impatience* via per-agent discount factors γ_i, under which the first mover obtains (1−γ_2)/(1−γ_1 γ_2) of the pie and patience confers bargaining power. For *task-oriented domains* with an initial task allocation and a monotone cost function, the negotiation set is the individually rational and Pareto-optimal deals; the *monotonic concession protocol* with the *Zeuthen strategy* (concede when your willingness to risk conflict is lower, by the smallest amount that shifts the balance, coin-flipping on ties) yields an agreement that is Pareto optimal, individually rational, and in Nash equilibrium.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]