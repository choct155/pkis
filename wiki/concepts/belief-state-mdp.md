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
- formal-methods
id: pkis:concept:belief-state-mdp
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch17
specializes:
- markov-decision-processes
tags:
- belief-state
- pomdp
- filtering
- continuous-state-space
- mdp-reduction
title: Belief-State MDP
understanding: 0
---

## Definition
The construction that reduces a partially observable MDP to a fully observable MDP defined over belief states. A belief state b is a probability distribution over the underlying physical states, with b(s) the probability assigned to state s; it is always observable to the agent by definition. Given the POMDP's transition model P(s'|s,a) and sensor model P(e|s), one derives a belief-state transition model P(b'|b,a) = Σ_e P(b'|e,a,b) Σ_{s'} P(e|s') Σ_s P(s'|s,a) b(s) (where P(b'|e,a,b) is 1 iff b'=FORWARD(b,a,e)) and a belief-state reward ρ(b,a) = Σ_s b(s) Σ_{s'} P(s'|s,a) R(s,a,s'). Together these define an ordinary, fully observable MDP on the space of belief states, and an optimal policy for this MDP is also optimal for the original POMDP. The price of observability is that the resulting state space is continuous and high-dimensional: a belief state for an n-state POMDP is a point in an (n−1)-dimensional probability simplex, so the standard finite-state dynamic-programming algorithms must be redesigned. The key structural fact exploited by POMDP solvers is that the optimal value function over this continuous belief space is piecewise-linear and convex.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — specializes: The belief-state construction yields an ordinary, fully observable MDP whose states are probability distributions over the POMDP's physical states.
[To be populated during integration]