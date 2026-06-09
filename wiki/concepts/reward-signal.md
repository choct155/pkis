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
- reinforcement-learning
id: pkis:concept:reward-signal
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch01
- sutton-reinforcement-2018-ch14
tags:
- reward
- goal
- objective
- scalar-feedback
title: Reward Signal
understanding: 0
---

## Definition
A reward signal defines the goal of a reinforcement learning problem. On each time step the environment sends the agent a single number, the **reward**, and the agent's sole objective is to maximize the *total* reward accumulated over the long run. The reward signal thereby defines which events are good or bad for the agent—analogous to pleasure and pain in a biological system—and is the primary basis for changing the policy: an action followed by low reward makes the policy less likely to choose it again.

The **reward hypothesis** holds that all of what we mean by goals and purposes can be cast as the maximization of expected cumulative scalar reward. Rewards may be stochastic functions of state and action.

### Reward vs. value
Rewards are *primary*: they are given directly by the environment and define immediate desirability. **Values** are *secondary*—predictions of long-run reward derived from them. Without rewards there are no values; the only purpose of estimating values is to obtain more reward.

### Why it matters
The scalar-reward formulation is what makes RL a single, well-posed optimization problem and is what separates it from supervised learning, where the feedback is the correct label rather than an evaluation of the chosen action.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]