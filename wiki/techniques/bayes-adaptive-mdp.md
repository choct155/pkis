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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- reinforcement-learning
- bayesian-methods
id: pkis:technique:bayes-adaptive-mdp
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch35
tags:
- exploration
- belief-state
- POMDP
- meta-RL
- Bayesian-RL
title: Bayes-Adaptive MDP (BAMDP)
understanding: 0
---

## Definition
A BAMDP augments the state space of a standard MDP with a belief state $b_t = p(R,T\mid h_t)$ over unknown reward and transition models. The augmented transition is
$$T^+(s_{t+1},b_{t+1}\mid s_t,b_t,a_t,r_t) = \mathbb{E}_{b_t}[T(s_{t+1}|s_t,a_t)]\cdot\mathbf{1}[b_{t+1}=p(R,T|h_{t+1})]$$
Solving the BAMDP exactly yields the Bayes-optimal exploration-exploitation policy.

### Why it matters
The BAMDP formalism extends the Gittins-index / bandit framework to full sequential decision problems, providing a principled (if computationally demanding) solution to exploration. It underpins approximate methods such as BOSS, BEB, PSRL, and meta-RL approaches that learn a belief representation via a VAE and use it as a proxy belief state for fast adaptation to new tasks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]