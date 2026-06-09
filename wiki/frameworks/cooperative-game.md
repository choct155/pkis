---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- economics
- decision-theory
id: pkis:framework:cooperative-game
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- coalition
- characteristic-function
- transferable-utility
- superadditivity
title: Cooperative Game
understanding: 0
---

## Definition
A model of strategic settings in which agents can form *binding* agreements to cooperate and thereby capture surplus value. Formally a transferable-utility game G = (N, v) is a player set N and a characteristic function v assigning to every coalition C ⊆ N the value it could obtain by working together (with v({}) = 0 and v ≥ 0). Players partition into a *coalition structure*; the grand coalition is all of N. An *outcome* pairs a coalition structure with a *payoff vector* that splits each coalition's value among its members. A game is *superadditive* if merging coalitions never lowers value (v(C∪D) ≥ v(C)+v(D)), favoring the grand coalition. Cooperative game theory asks which coalitions are stable (the core) and how to divide value fairly (the Shapley value); it abstracts away the specific actions agents take.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]