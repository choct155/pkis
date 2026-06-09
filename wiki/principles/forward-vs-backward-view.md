---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:principle:forward-vs-backward-view
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch12
tags:
- reinforcement-learning
- temporal-difference
- algorithm-design
title: Forward vs. Backward View
understanding: 0
---

## Definition
A pair of complementary perspectives on learning algorithms, central to understanding eligibility traces. The forward (theoretical) view formulates an update for each state by looking forward to all future rewards and deciding how to combine them (as in Monte Carlo, n-step, and lambda-return targets); it is conceptually clean but not directly implementable, since the target depends on information not yet available. The backward (mechanistic) view instead rides along the stream of states computing the current TD error and 'shouts it back' to recently visited states via an eligibility trace. A recurring and powerful idea in modern RL is that a forward-view algorithm can be transformed into a nearly-equivalent (and sometimes exactly equivalent, e.g. true online methods) incremental backward-view algorithm with O(d) per-step cost. Such transformations rest on rewriting returns as sums of TD errors when the value function is held fixed.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]