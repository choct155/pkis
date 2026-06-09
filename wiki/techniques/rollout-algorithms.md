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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:technique:rollout-algorithms
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
tags:
- reinforcement-learning
- decision-time-planning
- monte-carlo-control
- policy-improvement
- simulation
title: Rollout Algorithms
understanding: 0
---

## Definition
Decision-time planning algorithms based on Monte Carlo control applied to simulated trajectories that all start at the current state (Tesauro & Galperin, 1997; the term comes from 'rolling out' backgammon positions to the game's end). For the current state they estimate action values q_pi(s,a') for a fixed rollout policy pi by averaging the returns of many simulated trajectories that begin with each action a' and thereafter follow pi, then execute the highest-valued action and discard the estimates. By the policy improvement theorem, acting greedily over these estimates and then following pi yields a policy that improves on pi (like one step of policy/asynchronous value iteration for the current state only); the goal is improvement over the rollout policy, not finding an optimal policy. They avoid approximating any global value function and need only a sample model, but face strict time budgets governed by the number of actions, trajectory length, rollout-policy cost, and number of trials; trials can be parallelized, trajectories truncated with a stored evaluation function, and weak candidate actions pruned. Surprisingly effective even with random rollout policies.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]