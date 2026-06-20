---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- prioritized-sweeping
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- optimization
- deep-learning
id: pkis:technique:trajectory-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
- gulli-agentic-design-patterns-ch19
tags:
- reinforcement-learning
- planning
- on-policy
- update-distribution
- simulation
title: Trajectory Sampling
understanding: 0
---

## Definition
A way of distributing planning updates by simulating individual trajectories under the current policy (using the model for transitions and rewards) and updating the state or state-action pairs encountered along the way. It generates updates according to the on-policy distribution, contrasting with classical dynamic-programming sweeps that update every state once per pass and thereby waste effort on rarely visited or irrelevant states. Trajectory sampling is the only practical way to follow the on-policy distribution, which would otherwise require explicit knowledge of a distribution that changes with every policy update. Empirically, on-policy focusing yields faster planning initially (by concentrating on near-descendants of start states, whose values matter most for improving start-state behavior) but slower planning in the long run, because eventually all states must be evaluated and uniform allocation becomes more efficient; the early advantage is larger for smaller branching factors and larger state spaces.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[prioritized-sweeping]] — contrasts-with: Forward focusing (on-policy trajectory sampling) vs. backward focusing (prioritized sweeping) as update-distribution strategies.
[To be populated during integration]