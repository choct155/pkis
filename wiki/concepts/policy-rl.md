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
id: pkis:concept:policy-rl
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
title: Policy (Reinforcement Learning)
understanding: 0
---

## Definition
$$\pi(a \mid s) = \Pr\{A_t = a \mid S_t = s\}$$

A **policy** is a (possibly stochastic) mapping from states to probabilities over actions: the rule by which an agent selects what to do in each state.

### Intuition
The policy *is* the agent's behavior. Learning in RL means changing the policy as a result of experience so that it accumulates more reward. For each state $s$, $\pi(\cdot\mid s)$ is a probability distribution over the available actions $\mathcal{A}(s)$; a deterministic policy is the special case that puts all mass on one action.

### Role in the problem
Value functions are always defined *with respect to* a policy, because the future rewards an agent can expect depend on how it acts. The policy thus sits at the center of the RL loop: it generates the trajectory $S_0, A_0, R_1, S_1, \ldots$, the trajectory is evaluated by value functions, and the evaluation is used to improve the policy.

### Greedy and optimal policies
A policy that, in each state, selects an action maximizing an action-value (or one-step lookahead on a state-value) is *greedy* with respect to that value function. A policy that is greedy with respect to the optimal value function is itself optimal.

### Why it matters
The policy is the deliverable of reinforcement learning. Solving an RL task means finding a policy that earns high return; all value functions and Bellman machinery exist to support policy evaluation and improvement.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[action-value-function]] — prerequisite-of: q_pi is defined with respect to a policy pi.
- [[state-value-function]] — prerequisite-of: v_pi is defined with respect to a policy pi.
[To be populated during integration]