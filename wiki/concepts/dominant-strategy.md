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
contrasts-with:
- pareto-optimality
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- decision-theory
id: pkis:concept:dominant-strategy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- solution-concept
- domination
- best-response
title: Dominant Strategy
understanding: 0
uses:
- game-theory
---

## Definition
A strategy s for player p *strongly dominates* s' if s yields a strictly better outcome for p than s' for every choice of strategies by the other players; it *weakly dominates* s' if it is at least as good against every profile and strictly better against at least one. A dominant strategy dominates all others, so a rational player can adopt it without reasoning about what opponents will do. When every player has and plays a dominant strategy, the resulting outcome is a *dominant strategy equilibrium* — a very strong solution concept (no player can do better by deviating regardless of others), but one that rarely exists. In the prisoner's dilemma, 'testify' is the dominant strategy for both players, producing a dominant strategy equilibrium that is nonetheless Pareto-dominated.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[pareto-optimality]] — contrasts-with
- [[game-theory]] — uses
[To be populated during integration]