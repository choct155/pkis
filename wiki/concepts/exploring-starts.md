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
- optimization
- deep-learning
id: pkis:concept:exploring-starts
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch05
tags:
- reinforcement-learning
- monte-carlo
- exploration
- action-values
- coverage
title: Exploring Starts
understanding: 0
---

## Definition
Exploring starts is an assumption used to guarantee sufficient exploration in Monte Carlo control: every episode begins in a randomly chosen state-action pair $(S_0, A_0)$ such that *every* pair has nonzero probability of being the start,
$$\Pr\{S_0 = s, A_0 = a\} > 0 \quad \text{for all } s, a.$$
This ensures that, in the limit of infinitely many episodes, every state-action pair is visited infinitely often, so the Monte Carlo estimate $Q(s,a)$ improves for *all* actions — not just the action a deterministic policy currently favors. Without it, a deterministic policy followed greedily would only ever generate returns for one action per state, leaving the other action values frozen at their initial values and breaking policy improvement.

### Why it matters
It isolates the *maintaining-exploration* problem at the heart of model-free control: to learn which actions are best you must try actions that currently look suboptimal. Exploring starts solves this cleanly and is sometimes arrangeable in simulation (e.g., randomizing the dealt cards in blackjack), but it is unrealistic when learning from actual online interaction, where you cannot dictate the starting situation. That limitation is exactly what motivates the two general alternatives — on-policy soft policies (e.g., $\varepsilon$-greedy) and off-policy learning with a separate exploratory behavior policy — making exploring starts the conceptual pivot of the chapter.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]