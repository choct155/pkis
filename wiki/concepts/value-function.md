---
aliases: []
also_type: []
applies:
- credit-assignment-problem
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
id: pkis:concept:value-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- temporal-difference-learning
related_concepts: []
sources:
- sutton-reinforcement-2018-ch01
tags:
- value
- expected-return
- long-term-reward
- prediction
title: Value Function
understanding: 0
---

## Definition
Whereas a reward signal indicates what is good in an immediate sense, a value function specifies what is good *in the long run*. The **value** of a state is, roughly, the total amount of reward an agent can expect to accumulate over the future starting from that state.

$$v_\pi(s) = \mathbb{E}_\pi\!\left[ \textstyle\sum_{k} R_{t+k} \,\middle|\, S_t = s \right]$$

Values take into account the states likely to follow and the rewards available there: a state may yield low immediate reward yet have high value because it reliably leads to high-reward states, or vice versa.

### Why decisions use values, not rewards
Action choices are made on the basis of value judgments—we seek states of highest *value*, not highest immediate reward, because doing so secures the greatest reward over the long run.

### The estimation challenge
Rewards are given directly by the environment, but values must be **estimated and re-estimated** from sequences of observations the agent makes over its lifetime. Most RL methods are structured around efficiently estimating value functions; this is what distinguishes them from evolutionary methods that search policy space directly.

### Why it matters
The value function is the central object of most RL algorithms: it converts the long-horizon credit-assignment problem into a sequence of local prediction updates, making efficient search through policy space possible.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[credit-assignment-problem]] — applies: Estimating per-state values converts the global credit problem into local prediction updates.
- [[temporal-difference-learning]] — prerequisite-of: TD methods learn by incrementally estimating a value function.
[To be populated during integration]