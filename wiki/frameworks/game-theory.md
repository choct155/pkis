---
aliases: []
also_type: []
analogous-to:
- decision-theory-foundations
applies:
- expected-utility-theory
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- conjectural-variation
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- decision-theory
- economics
id: pkis:framework:game-theory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- strategic-interaction
- solution-concepts
- rationality
title: Game Theory
understanding: 0
---

## Definition
The mathematical theory of strategic decision making: how rational agents should act when the outcome of their choices depends on the choices of other rational agents who are reasoning about them in turn. Game theory is to multiagent decision making as decision theory is to single-agent decision making; its distinguishing feature is the strategic aspect — each player must reason about how others will act, including how others reason about the player. A game is specified by players, the actions available to each, and a payoff (utility) function over action profiles. The central output is a *solution concept* that characterizes which outcomes count as rational. In AI it is used both for *agent design* (computing a best response and expected return against rational counterparts) and *mechanism design* (defining the rules of an environment so that self-interested play yields a desired collective outcome). A primary division is between cooperative game theory (binding agreements possible) and non-cooperative game theory (no binding agreement; cooperation, if it occurs, must be individually rational).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conjectural-variation]] — contrasts-with
- [[expected-utility-theory]] — applies
- [[decision-theory-foundations]] — analogous-to
[To be populated during integration]