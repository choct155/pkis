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
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
extends:
- semi-gradient-td
id: pkis:technique:semi-gradient-sarsa
instantiates:
- markov-decision-processes
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch10
tags:
- sarsa
- on-policy-control
- function-approximation
- action-value
- epsilon-greedy
- gpi
- mountain-car
title: Episodic Semi-Gradient Sarsa
understanding: 0
uses:
- function-approximation-rl
---

## Definition
Episodic semi-gradient Sarsa is the on-policy control algorithm obtained by extending semi-gradient TD(0) from state values to parameterized action values $\hat{q}(s,a,\mathbf{w}) \approx q_*(s,a)$. The one-step update is

$$\mathbf{w}_{t+1} \doteq \mathbf{w}_t + \alpha\left[R_{t+1} + \gamma\hat{q}(S_{t+1},A_{t+1},\mathbf{w}_t) - \hat{q}(S_t,A_t,\mathbf{w}_t)\right]\nabla\hat{q}(S_t,A_t,\mathbf{w}_t).$$

Control is achieved by interleaving this prediction step with generalized policy iteration: in each next state the agent evaluates $\hat{q}(S_{t+1},a,\mathbf{w}_t)$ for every available action, acts $\epsilon$-greedily with respect to those values, and uses the action it actually takes ($A_{t+1}$) in the bootstrapped target — the defining on-policy character of Sarsa. The approach is practical when the action set is discrete and small enough to maximize over directly.

On the Mountain Car task with tile-coding features, optimistic zero-initialized weights drive early exploration even at $\epsilon=0$, and the learned cost-to-go function recovers the classic "build momentum on the back slope" solution.

### Why it matters
This is the chapter's headline algorithm and the canonical template for value-based approximate control. It also exposes a key limitation: with function approximation the policy-improvement theorem is lost, so $\epsilon$-greedification can chatter rather than converge — motivating both the $n$-step and average-reward refinements that follow.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — instantiates: Semi-gradient Sarsa solves the control problem of an MDP via generalized policy iteration with approximate action values.
- [[function-approximation-rl]] — uses: Sarsa control here represents the action-value function with a weight vector, e.g. linearly via tile-coded features.
- [[semi-gradient-td]] — extends: Episodic semi-gradient Sarsa extends semi-gradient TD(0) from state values to action values and to on-policy control.
[To be populated during integration]