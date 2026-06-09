---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
- deep-learning
id: pkis:framework:policy-gradient-methods
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-policy-2018
tags:
- policy-gradient
- stochastic-gradient-ascent
- parameterized-policy
- reinforcement-learning
title: Policy Gradient Methods
understanding: 0
---

## Definition
A family of reinforcement-learning methods that learn a parameterized policy $\pi(a\mid s,\theta)$ directly, selecting actions without consulting an action-value function (a value function may still be learned to aid policy learning, but is not required for action selection). The policy parameter $\theta\in\mathbb{R}^{d'}$ is updated by approximate stochastic gradient ascent on a scalar performance measure $J(\theta)$:
$$\theta_{t+1}=\theta_t+\alpha\,\widehat{\nabla J(\theta_t)},$$
where the estimate's expectation approximates $\nabla J$. The only structural requirement is that $\pi(a\mid s,\theta)$ be differentiable in $\theta$ and, in practice, never deterministic (so $\pi(a\mid s,\theta)\in(0,1)$) to preserve exploration.

## Why It Matters
Compared to action-value methods (Q-learning, Sarsa, epsilon-greedy), policy-gradient methods: (1) can represent arbitrary action probabilities, including genuinely stochastic optimal policies (e.g. bluffing in imperfect-information games), which epsilon-greedy cannot; (2) can approach a deterministic policy smoothly rather than retaining a floor of epsilon random actions; (3) handle continuous/large action spaces naturally by parameterizing a distribution rather than enumerating action values; (4) change action probabilities continuously in $\theta$, yielding stronger convergence guarantees than the discontinuous argmax of action-value methods; and (5) allow prior knowledge about policy form to be injected directly. The cost is typically higher variance in the gradient estimate and weaker theoretical understanding than value-based methods.

## Scope
The framework covers the episodic case (performance = value of the start state, $J(\theta)=v_{\pi_\theta}(s_0)$) and the continuing case (performance = average reward rate $r(\pi)$, Section 10.3 / 13.6); both are unified by the policy gradient theorem. Member algorithms include the all-actions method, REINFORCE, REINFORCE with baseline, and actor-critic methods. Modern descendants include natural-gradient, deterministic, off-policy, and entropy-regularized policy gradients (A2C, TRPO, PPO, SAC).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]