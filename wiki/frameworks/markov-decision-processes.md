---
id: "pkis:framework:markov-decision-processes"
aliases: []
title: "Markov Decision Processes"
knowledge_type: framework
also_type: []
domain: [formal-methods, systems-theory, reinforcement-learning]
tags: [markov-decision-processes, dynamic-programming, bellman-equation, optimal-control, value-iteration, policy-iteration, reinforcement-learning]
related_concepts: [markov-chains, discrete-event-systems, queueing-theory, state-space-models]
sources: ["[[cassandras-des-intro]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A Markov Decision Process (MDP) is a framework for sequential decision-making in stochastic environments: a Markov chain whose transition probabilities depend on a control action chosen at each state, paired with a cost (or reward) function and an optimization criterion (discounted, average-cost, or finite-horizon); solution via dynamic programming yields the Bellman optimality equation and optimal policy.

## Reading Path
- [[cassandras-des-intro-ch09]] (unread) — primary treatment in DES context: cost criteria, Bellman equation, dynamic programming, value/policy iteration, queueing control applications
