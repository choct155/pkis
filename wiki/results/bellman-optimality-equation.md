---
aliases: []
also_type: []
applies:
- markov-decision-processes
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
id: pkis:result:bellman-optimality-equation
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch03
specializes:
- bellman-equation
tags: []
title: Bellman Optimality Equation
understanding: 0
---

## Definition
$$v_*(s) = \max_{a} \sum_{s', r} p(s', r \mid s, a)\big[\,r + \gamma\, v_*(s')\,\big], \qquad q_*(s,a) = \sum_{s',r} p(s',r\mid s,a)\Big[r + \gamma \max_{a'} q_*(s',a')\Big]$$

The **Bellman optimality equation** is the self-consistency condition that the optimal value functions must satisfy: a state's optimal value equals the expected return of the *best* action from it.

### Intuition
It is the ordinary Bellman equation with the policy-average over actions replaced by a maximum. Written without reference to any specific policy, it captures the requirement that under an optimal policy you always act so as to maximize expected reward-plus-discounted-future-value.

### Uniqueness and solution
For a finite MDP it has a *unique* solution. It is a system of $n$ nonlinear (because of the $\max$) equations in $n$ unknowns; if the dynamics $p$ are known, it can in principle be solved directly for $v_*$ (or $q_*$).

### From values to policy
Any policy greedy with respect to $v_*$ is optimal: the $\max$ already accounts for all future consequences, so a one-step-ahead choice is globally optimal. With $q_*$, even the lookahead is unnecessary.

### Why it matters
Dynamic programming, heuristic search, and most RL methods can be read as ways of approximately solving the Bellman optimality equation, often replacing known transitions with sampled experience. It is the formal target of "solving" an MDP.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — applies: For a finite MDP it has a unique solution and characterizes the optimal value functions.
- [[bellman-equation]] — specializes: Replaces the policy-average over actions with a maximum.
[To be populated during integration]