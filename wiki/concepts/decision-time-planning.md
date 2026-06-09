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
id: pkis:concept:decision-time-planning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
specializes:
- planning-rl
tags:
- reinforcement-learning
- planning
- action-selection
- lookahead
- online
title: Decision-Time Planning
understanding: 0
---

## Definition
Using planning to select a single action for the current state St: planning begins and completes after each new state is encountered, its output being the action choice, and the resulting (state-specific) values and policy are typically discarded afterward. This contrasts with background planning, which gradually improves a global policy or value function regardless of the current state. Decision-time planning can look much deeper than one step, evaluating action choices over many predicted trajectories. It is most useful when fast responses are not required (e.g. chess programs allotted seconds or minutes per move); when low-latency action selection matters, background planning is preferable. Heuristic search, rollout algorithms, and Monte Carlo Tree Search are all decision-time planning methods. The two modes can blend (focus on the current state while storing results for reuse).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[planning-rl]] — specializes: Decision-time planning is planning whose output is the action for the current state, discarded afterward.
[To be populated during integration]