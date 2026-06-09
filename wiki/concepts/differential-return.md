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
id: pkis:concept:differential-return
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch10
tags:
- differential-return
- average-reward
- differential-value-function
- bellman-equation
- td-error
- relative-value
title: Differential Return and Differential Value Functions
understanding: 0
---

## Definition
In the average-reward setting, the return is defined not by discounting future rewards but by summing how much each reward exceeds the long-run average reward $r(\pi)$. This is the differential return:

$$G_t \doteq (R_{t+1}-r(\pi)) + (R_{t+2}-r(\pi)) + (R_{t+3}-r(\pi)) + \cdots .$$

The corresponding differential value functions reuse the usual definitions, $v_\pi(s) \doteq \mathbb{E}_\pi[G_t\mid S_t=s]$ and $q_\pi(s,a) \doteq \mathbb{E}_\pi[G_t\mid S_t=s, A_t=a]$. They satisfy differential Bellman equations formed from the ordinary ones by dropping all $\gamma$ and replacing each reward $r$ with $r - r(\pi)$. The differential TD error is likewise

$$\delta_t \doteq R_{t+1} - \bar{R}_t + \hat{q}(S_{t+1},A_{t+1},\mathbf{w}_t) - \hat{q}(S_t,A_t,\mathbf{w}_t),$$

where $\bar{R}_t$ estimates $r(\pi)$. Intuitively, differential values measure how good a state (or action) is *relative* to the average steady-state experience — hence the name relative values.

### Why it matters
Differential values are what make undiscounted continuing control learnable: nearly every discounted algorithm carries over by swapping in the differential TD error. A subtlety is that solutions are determined only up to an additive offset (the Bellman equations are invariant to shifting all values), so methods like differential semi-gradient Sarsa converge to the true values plus an arbitrary constant — usually harmless in practice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]