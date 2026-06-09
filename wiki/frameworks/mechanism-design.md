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
id: pkis:framework:mechanism-design
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- reverse-game-theory
- incentive-compatibility
- strategy-proof
- center
title: Mechanism Design
understanding: 0
---

## Definition
The problem of *designing the rules of a game* so that self-interested agents, each maximizing their own utility, collectively produce a desired outcome — sometimes called reverse game theory. Formally a mechanism comprises a language of allowable strategies, a distinguished *center* (e.g., an auctioneer) that collects agents' strategy reports, and an *outcome rule*, known to all, that maps reports to payoffs. Key desiderata include *strategy-proofness* (each agent has a dominant strategy, so no costly reasoning about others is needed), *incentive compatibility / truthfulness* (the dominant strategy is to report one's true value), and efficiency (goods go to those who value them most). The *revelation principle* says any mechanism can be transformed into an equivalent truth-revealing one. Concrete mechanisms include auctions, the VCG mechanism, contract nets, voting procedures, and bargaining protocols.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]