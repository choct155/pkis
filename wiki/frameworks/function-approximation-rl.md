---
aliases: []
also_type: []
applies:
- markov-decision-processes
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
generalizes:
- state-aggregation
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
uses:
- stochastic-gradient-descent
- mean-square-value-error
- neural-networks
- backpropagation
- convolutional-neural-networks
---

## Definition
Representing a value function not as a lookup table but as a parameterized functional form v̂(s,w) ≈ v_π(s) with a weight vector w ∈ R^d, where d ≪ |S|. Each tabular update s ↦ u (Monte Carlo, TD(0), n-step, or DP target) is reinterpreted as a supervised-learning training example whose input is the state and whose output is the update target. Because changing one weight changes the estimated value of many states, a single update generalizes across the state space—the source of both the power and the difficulty of approximation. Function approximation also extends RL to partial observability: aspects of state not exposed to v̂ are effectively unobservable. RL imposes special demands on the approximator: it must learn online and incrementally from a single example at a time, and it must cope with nonstationary target functions (targets that drift as the policy improves under GPI, or that move because they are bootstrapped). These requirements rule out methods that assume a static training set traversed in multiple passes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[convolutional-neural-networks]] — uses: deep convolutional networks approximate value functions over spatial inputs (e.g. AlphaGo, Atari)
- [[backpropagation]] — uses: backpropagation computes the weight gradients for ANN value approximation
- [[neural-networks]] — uses: multi-layer ANNs trained by backpropagation provide nonlinear value approximation (deep RL)
- [[mean-square-value-error]] — uses: VE is the objective the approximate value function aims to minimize
- [[state-aggregation]] — generalizes: general approximation subsumes tabular and state-aggregation methods as special cases
- [[stochastic-gradient-descent]] — uses: value prediction adjusts the weight vector by SGD on per-example squared value error
- [[markov-decision-processes]] — applies: function approximation is used to estimate value functions for MDPs that are too large for tabular methods
[To be populated during integration]