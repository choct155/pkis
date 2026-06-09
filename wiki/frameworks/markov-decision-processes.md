---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- formal-methods
- systems-theory
- reinforcement-learning
id: pkis:framework:markov-decision-processes
knowledge_type: framework
maturity: settled
prerequisite-of:
- return-and-discounting
- policy-rl
related_concepts:
- markov-chains
- discrete-event-systems
- queueing-theory
- state-space-models
sources:
- '[[cassandras-des-intro]]'
tags:
- markov-decision-processes
- dynamic-programming
- bellman-equation
- optimal-control
- value-iteration
- policy-iteration
- reinforcement-learning
title: Markov Decision Processes
understanding: 0
---

A Markov Decision Process (MDP) is a framework for sequential decision-making in stochastic environments: a Markov chain whose transition probabilities depend on a control action chosen at each state, paired with a cost (or reward) function and an optimization criterion (discounted, average-cost, or finite-horizon); solution via dynamic programming yields the Bellman optimality equation and optimal policy.

## Reading Path
- [[cassandras-des-intro-ch09]] (unread) — primary treatment in DES context: cost criteria, Bellman equation, dynamic programming, value/policy iteration, queueing control applications

## Connections
- [[policy-rl]] — prerequisite-of: A policy maps the MDP's states to actions.
- [[return-and-discounting]] — prerequisite-of: The MDP reward sequence is what the return aggregates.