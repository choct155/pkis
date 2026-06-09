---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
id: pkis:problem:multi-armed-bandit
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- decision-making
- exploration
- evaluative-feedback
- nonassociative
title: k-armed Bandit Problem
understanding: 0
---

## Definition
$$q_*(a) \doteq \mathbb{E}[R_t \mid A_t = a]$$

The canonical nonassociative reinforcement-learning problem: repeatedly choose one of $k$ actions, each of which returns a reward drawn from a fixed (stationary) distribution whose mean $q_*(a)$ is the unknown *value* of that action; the goal is to maximize expected cumulative reward.

### Setup
Named by analogy to a slot machine ("one-armed bandit") with $k$ levers. On step $t$ the learner selects $A_t$ and observes reward $R_t$. The action values $q_*(a)$ are unknown but can be *estimated* by $Q_t(a)$; if they were known the problem would be trivial (always pick the argmax). The setting is *nonassociative*: there is a single situation, so the learner seeks one best action rather than a state-to-action mapping.

### Why it matters
The bandit strips reinforcement learning down to its defining feature — *evaluative* rather than *instructive* feedback — isolating the exploration–exploitation tension without the complications of delayed reward or multiple states. It is the pedagogical entry point from which $\varepsilon$-greedy, UCB, and gradient methods are introduced and later lifted to the full RL problem.

### Variants
The *stationary* case has fixed $q_*(a)$; the *nonstationary* case lets them drift over time, which is the norm in full RL. Adding a context signal yields the *associative* (contextual) bandit; allowing actions to affect the next situation yields the full reinforcement-learning problem.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]