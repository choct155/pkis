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
id: pkis:concept:average-reward-setting
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch10
tags:
- average-reward
- continuing-tasks
- ergodicity
- steady-state-distribution
- reward-rate
- undiscounted
title: Average-Reward Setting
understanding: 0
---

## Definition
The average-reward setting is a third formulation of the MDP objective, alongside the episodic and discounted settings, for continuing problems that never terminate. There is no discounting; the quality of a policy $\pi$ is its long-run reward rate

$$r(\pi) \doteq \lim_{h\to\infty}\frac{1}{h}\sum_{t=1}^{h}\mathbb{E}[R_t\mid S_0, A_{0:t-1}\sim\pi] = \sum_s \mu_\pi(s)\sum_a \pi(a\mid s)\sum_{s',r} p(s',r\mid s,a)\,r,$$

where $\mu_\pi$ is the steady-state distribution satisfying $\sum_s \mu_\pi(s)\sum_a \pi(a\mid s)p(s'\mid s,a) = \mu_\pi(s')$. The second and third equalities hold when the MDP is ergodic, so the long-run state distribution is independent of the start state. Policies are then ranked simply by $r(\pi)$, and any policy attaining the maximal $r(\pi)$ is optimal.

The intuition: in a never-ending stream of experience with no special start or end, the only meaningful summary of performance is the average reward per step.

### Why it matters
This chapter argues the discounted control objective is futile under function approximation — the average of discounted returns is always $r(\pi)/(1-\gamma)$, so $\gamma$ does not change the policy ordering. The average-reward setting is the replacement, and it underpins the differential value functions and the differential semi-gradient Sarsa algorithms used for approximate continuing control.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]