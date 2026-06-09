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
- optimization
- deep-learning
id: pkis:concept:planning-rl
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
tags:
- reinforcement-learning
- planning
- model-based
- value-functions
title: Planning (Reinforcement Learning)
understanding: 0
uses:
- markov-decision-processes
---

## Definition
Any computational process that takes a model of the environment as input and produces or improves a policy for interacting with it (model -> policy). In reinforcement learning the relevant variety is state-space planning, which searches the state space for an optimal policy and shares a common structure with learning: model -> simulated experience -> backups -> values -> policy. This contrasts with plan-space planning (search through the space of plans, e.g. partial-order planning), which is hard to apply to stochastic sequential decision problems. The key insight is that planning and learning differ only in the source of experience (simulated vs. real); any learning method can be applied to simulated experience to become a planning method. Sutton distinguishes background planning (gradually improving a global policy/value function from simulated experience, as in Dyna and DP) from decision-time planning (computing a single action for the current state).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — uses: State-space planning searches the MDP state space and backs up MDP value functions.
[To be populated during integration]