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
- optimization
id: pkis:concept:optimal-policy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch03
tags: []
title: Optimal Policy
understanding: 0
---

## Definition
$$\pi \ge \pi' \iff v_\pi(s) \ge v_{\pi'}(s)\ \forall s; \qquad v_*(s) = \max_\pi v_\pi(s),\quad q_*(s,a) = \max_\pi q_\pi(s,a)$$

An **optimal policy** $\pi_*$ is one whose expected return is at least as great as that of every other policy in every state; it achieves the optimal value functions $v_*$ and $q_*$.

### Intuition
Value functions impose a partial order on policies. In a finite MDP there is always at least one policy that dominates all others in every state simultaneously — the optimal policy. Although several optimal policies may exist, they all share the same unique optimal value functions.

### Greedy characterization
Any policy that puts probability only on actions attaining the maximum in the Bellman optimality equation is optimal: $\pi_*(s) \in \arg\max_a q_*(s,a)$, or equivalently a one-step-greedy choice on $v_*$. This is why obtaining the optimal value function effectively solves the control problem.

### Approximation in practice
Exact optimal policies are usually unreachable: the dynamics may be unknown, the state space astronomically large (e.g. $\sim 10^{20}$ for backgammon), or the Markov property only approximate. RL therefore settles for approximations, often concentrating effort on frequently visited states.

### Why it matters
The optimal policy is the ideal that defines the RL objective and anchors the analysis of every learning algorithm, even though agents only approximate it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]