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
contrasts-with:
- n-step-off-policy
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:technique:tree-backup-algorithm
instantiates:
- n-step-bootstrapping
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch07
tags:
- reinforcement-learning
- off-policy
- control
- bootstrapping
title: Tree-backup Algorithm
understanding: 0
---

## Definition
The tree-backup algorithm is an n-step off-policy control method that achieves sound off-policy learning without any importance sampling, generalizing Q-learning and Expected Sarsa to the multi-step case with stochastic target policies. Its backup combines the sampled rewards along the trajectory with the bootstrapped estimated values of all the action nodes that hang off the sides of the trajectory (the actions not taken), each leaf weighted by its probability of being selected under the target policy pi; the probability of the action actually taken propagates the weight to the subtree below it. This yields the recursive n-step return G_{t:t+n} = R_{t+1} + gamma*sum_{a != A_{t+1}} pi(a|S_{t+1})Q(S_{t+1},a) + gamma*pi(A_{t+1}|S_{t+1})*G_{t+1:t+n}, used with the standard n-step Sarsa action-value update. Because it relies on expected values over unselected actions rather than reweighting sampled trajectories, it avoids the high variance of importance-sampling-based off-policy methods; the cost is that when the target and behavior policies differ substantially the effective bootstrapping may span only a few steps even when n is large.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[n-step-off-policy]] — contrasts-with: achieves off-policy learning without importance sampling, unlike the IS-based n-step methods
- [[n-step-bootstrapping]] — instantiates: tree backup is an n-step off-policy control method
[To be populated during integration]