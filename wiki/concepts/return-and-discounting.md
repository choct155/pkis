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
- optimization
id: pkis:concept:return-and-discounting
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- state-value-function
- action-value-function
related_concepts: []
sources:
- sutton-reinforcement-2018-ch03
tags: []
title: Return and Discounting
understanding: 0
---

## Definition
$$G_t \doteq \sum_{k=0}^{\infty} \gamma^k R_{t+k+1} = R_{t+1} + \gamma G_{t+1}, \qquad 0 \le \gamma \le 1$$

The **return** $G_t$ is the cumulative future reward an agent seeks to maximize; **discounting** by $\gamma$ makes it finite and trades off immediate against delayed reward.

### Intuition
The agent's goal is not to maximize the next reward but the long-run sum of rewards. The discount rate $\gamma$ sets the present value of future rewards: a reward $k$ steps away is worth $\gamma^{k-1}$ times an immediate one. With $\gamma=0$ the agent is myopic; as $\gamma\to 1$ it becomes farsighted.

### Episodic vs. continuing tasks
When interaction breaks into episodes ending in a terminal state, the return is a finite sum up to $T$ (undiscounted is fine). When interaction continues without limit ($T=\infty$), an undiscounted sum can diverge, so discounting with $\gamma<1$ is used. Treating termination as an absorbing zero-reward state unifies both under $G_t = \sum_{k=t+1}^{T} \gamma^{k-t-1} R_k$ (allowing $T=\infty$ or $\gamma=1$, not both).

### Recursive structure
The identity $G_t = R_{t+1} + \gamma G_{t+1}$ (with $G_T=0$) is the engine behind value-function recursions and bootstrapping. For a constant reward $+1$, the discounted return is the geometric sum $\tfrac{1}{1-\gamma}$.

### Why it matters
The return is the precise object value functions estimate; its recursive form is what makes the Bellman equations possible and underlies essentially every RL algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[action-value-function]] — prerequisite-of: Action values are expected returns conditioned on a state-action pair.
- [[state-value-function]] — prerequisite-of: Value functions are defined as the expected return.
[To be populated during integration]