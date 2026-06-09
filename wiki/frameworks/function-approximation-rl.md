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
- deep-learning
- optimization
id: pkis:framework:function-approximation-rl
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
- sutton-reinforcement-2018-ch10
tags:
- value-function
- generalization
- supervised-learning
title: Function Approximation in Reinforcement Learning
understanding: 0
---

## Definition
Representing a value function not as a lookup table but as a parameterized functional form v̂(s,w) ≈ v_π(s) with a weight vector w ∈ R^d, where d ≪ |S|. Each tabular update s ↦ u (Monte Carlo, TD(0), n-step, or DP target) is reinterpreted as a supervised-learning training example whose input is the state and whose output is the update target. Because changing one weight changes the estimated value of many states, a single update generalizes across the state space—the source of both the power and the difficulty of approximation. Function approximation also extends RL to partial observability: aspects of state not exposed to v̂ are effectively unobservable. RL imposes special demands on the approximator: it must learn online and incrementally from a single example at a time, and it must cope with nonstationary target functions (targets that drift as the policy improves under GPI, or that move because they are bootstrapped). These requirements rule out methods that assume a static training set traversed in multiple passes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]