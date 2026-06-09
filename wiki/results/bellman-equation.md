---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
id: pkis:result:bellman-equation
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch03
tags: []
title: Bellman Equation
understanding: 0
---

## Definition
$$v_\pi(s) = \sum_a \pi(a\mid s) \sum_{s', r} p(s', r \mid s, a)\big[\,r + \gamma\, v_\pi(s')\,\big]$$

The **Bellman equation** is the self-consistency condition relating the value of a state to the (discounted, expected) values of its successor states under a fixed policy $\pi$.

### Intuition
It formalizes "the value of where you are equals the reward you expect along the way plus the discounted value of where you land." Derived directly from the recursive return $G_t = R_{t+1} + \gamma G_{t+1}$ by taking expectations over actions (via $\pi$) and transitions (via $p$).

### Backup diagrams
The averaging structure — branch over actions weighted by $\pi$, then over $(s',r)$ weighted by $p$ — is depicted as a backup diagram: information is transferred *back* from successors to the root state. These diagrams underlie the update/backup operations at the heart of RL.

### Uniqueness and use
For a finite MDP and fixed $\pi$, $v_\pi$ is the *unique* solution of its Bellman equation — a linear system, one equation per state. This makes value functions computable by solving linear equations or by iterative dynamic-programming backups.

### Why it matters
The Bellman equation is the structural backbone of RL: it turns the definition of value into a solvable recursion and justifies bootstrapping, the technique that lets value estimates be updated from other value estimates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]