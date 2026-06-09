---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- formal-methods
- systems-theory
id: pkis:framework:partially-observable-mdp
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch17
tags:
- pomdp
- belief-state
- sensor-model
- partial-observability
- sequential-decision-making
- value-of-information
title: Partially Observable Markov Decision Process (POMDP)
understanding: 0
---

## Definition
A POMDP extends a Markov decision process to the case where the agent cannot directly observe the underlying state. It has the same elements as an MDP — a transition model P(s'|s,a), action sets A(s), and reward function R(s,a,s') — plus a sensor (observation) model P(e|s) giving the probability of perceiving evidence e in state s. Because the agent never knows its true state, the utility of a state and the optimal action depend not just on the state but on what the agent knows, so the central object becomes the belief state b (a probability distribution over states) rather than the physical state. The fundamental insight is that the optimal action depends only on the current belief state, so an optimal policy is a mapping π*(b) from belief states to actions, and the decision cycle is: act with a=π*(b), observe percept e, update b' = α·FORWARD(b,a,e), repeat. The belief update b'(s') = α P(e|s') Σ_s P(s'|s,a) b(s) is exactly the filtering recursion of dynamic Bayesian networks. POMDPs subsume sensorless and contingency planning, and because actions affect which percepts are received, they natively incorporate the value of information — optimal POMDP policies often include information-gathering actions. Solving general POMDPs is PSPACE-hard. The historical reduction of a POMDP to a belief-state MDP is due to Astrom (1965) and Aoki (1965); the first exact algorithm to Sondik (1971).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]