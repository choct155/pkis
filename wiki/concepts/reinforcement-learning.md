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
date_updated: '2026-06-20'
domain:
- reinforcement-learning
id: pkis:concept:reinforcement-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch01
- gulli-agentic-design-patterns-ch09
- gulli-agentic-design-patterns-ch20
tags:
- agent
- reward
- sequential-decision-making
- trial-and-error
- delayed-reward
title: Reinforcement Learning
understanding: 0
uses:
- markov-decision-processes
---

## Definition
Reinforcement learning is the problem of learning *what to do*—how to map situations to actions—so as to maximize a cumulative numerical reward signal. The learner is not told which actions to take; it must discover which actions yield the most reward by trying them. The two defining features that distinguish it from other learning are **trial-and-error search** and **delayed reward**: an action may affect not only the immediate reward but also the next state and, through it, all subsequent rewards.

Formally, the problem is the optimal control of an incompletely-known Markov decision process, capturing three aspects of a learning agent: sensation (sensing state), action (affecting state), and goal.

### Three senses of the term
"Reinforcement learning" simultaneously names a *problem*, a *class of solution methods* that work well on it, and the *field* that studies both. Keeping problem and method conceptually separate is essential.

### A third paradigm
RL is distinct from **supervised learning** (mapping labeled examples to correct actions) and **unsupervised learning** (finding hidden structure). It seeks to maximize a reward signal rather than reproduce labels or expose structure, and is regarded as a third machine-learning paradigm.

### Why it matters
It is the first framework to seriously address the computational problem of learning from direct interaction to achieve long-term goals, and is the closest machine learning comes to how humans and animals actually learn.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — uses: RL formalizes its problem as the optimal control of an incompletely-known MDP.
[To be populated during integration]