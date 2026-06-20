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
date_updated: '2026-06-20'
domain:
- reinforcement-learning
id: pkis:concept:agent-environment-interface
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- reinforcement-learning
related_concepts: []
sources:
- sutton-reinforcement-2018-ch01
- gulli-agentic-design-patterns-ch10
- gulli-agentic-design-patterns-ch23
tags:
- agent
- environment
- state
- action
- interaction
title: Agent–Environment Interface
understanding: 0
---

## Definition
The agent–environment interface is the basic structure of every reinforcement learning problem: a goal-directed **agent** interacts over time with an **environment** it cannot fully control or predict. At each step the agent senses the **state** of the environment, selects an **action** that influences the next state, and receives a scalar reward. Correct behavior must account for indirect, delayed consequences of actions and operate despite uncertainty about the environment.

The boundary is drawn by control, not physics: the agent is everything it can change directly, and the environment is everything else—so an agent can be a whole robot or merely a component of a larger system (e.g., a battery monitor whose environment is the rest of the robot plus the world).

### State as the interface
State is the signal conveying "how the environment is" at a given time; it is the input to policy and value function. Sutton & Barto treat the state signal as given by preprocessing, focusing on *what action to take* given whatever state is available rather than on constructing the state.

### Whole-problem stance
RL deliberately starts from a complete, interactive, goal-seeking agent rather than studying isolated subproblems, so that planning, perception, and learning are addressed in their proper relationship.

### Why it matters
This loop—state, action, reward, repeat—is the common skeleton onto which MDPs, policies, value functions, and every RL algorithm are built.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reinforcement-learning]] — prerequisite-of: The agent/environment/state/action/reward loop is the structure RL operates over.
[To be populated during integration]