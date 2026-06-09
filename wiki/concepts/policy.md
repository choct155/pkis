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
- reinforcement-learning
id: pkis:concept:policy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch01
tags:
- policy
- agent
- behavior
- state-action-mapping
title: Policy
understanding: 0
---

## Definition
A policy defines a reinforcement learning agent's way of behaving at a given time. Roughly, it is a mapping from perceived states of the environment to actions to be taken in those states—corresponding to what psychology would call a set of stimulus–response associations.

$$\pi: \mathcal{S} \to \mathcal{A} \quad\text{(or, in general, } \pi(a\mid s)\text{)}$$

It may be as simple as a lookup table or involve extensive computation such as search, and in general it is **stochastic**, specifying a probability for each action in each state.

### Core of the agent
The policy is the core of an RL agent in the sense that it alone is sufficient to determine behavior. Everything else—reward signals, value functions, models—exists to *improve* the policy.

### Policy space as the search target
Both evolutionary methods and value-based methods ultimately search the space of policies. Evolutionary methods hold a policy fixed and evaluate it over many episodes; value-based methods instead use information available *during* interaction to estimate state values and act greedily with respect to them.

### Why it matters
The policy is the object that solution methods are trying to find or improve, making it the central decision-making structure of every RL system and the bridge between value estimates and actual behavior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]