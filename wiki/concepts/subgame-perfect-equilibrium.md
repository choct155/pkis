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
id: pkis:concept:subgame-perfect-equilibrium
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- equilibrium-refinement
- credible-threat
- backward-induction
- extensive-form
title: Subgame-Perfect Equilibrium
understanding: 0
---

## Definition
A refinement of Nash equilibrium for extensive-form games that eliminates equilibria supported by non-credible threats. Every decision node (including the root) defines a *subgame*; a strategy profile is subgame perfect if it is a Nash equilibrium in *every* subgame. This rules out equilibria where a player threatens an action they would never actually rationally take if the relevant subgame were reached. The strategies computed by backward induction are exactly the subgame-perfect equilibria, so every finite extensive-form game of perfect information has a subgame-perfect equilibrium computable in time polynomial in the size of the game tree.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]