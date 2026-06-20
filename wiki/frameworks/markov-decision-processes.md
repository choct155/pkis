---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
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
- sutton-reinforcement-2018
- cassandras-des-intro-ch09
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

## Role in Reinforcement Learning
Sutton & Barto adopt the MDP as *the* formalization of the reinforcement learning problem, characterizing RL as "the optimal control of incompletely-known Markov decision processes." The MDP is intended to capture, in their simplest non-trivial forms, exactly three aspects of a learning agent interacting with its environment over time: **sensation** (sensing state), **action** (taking actions that affect state), and **goal** (a reward-defined objective). It thereby encodes a sense of cause and effect, a sense of uncertainty and nondeterminism, and the existence of explicit goals.

Historically the discrete stochastic optimal-control problem now called the MDP was introduced by Bellman (1957) alongside dynamic programming and the Bellman equation, with policy iteration added by Howard (1960); the full integration of these MDP/dynamic-programming methods with online learning came with Watkins's Q-learning (1989). A key qualifier in the RL setting is *incompletely known*: classical dynamic programming requires a complete and accurate model of the MDP, whereas reinforcement learning methods are designed to solve the same MDP through experience when that model is unavailable.