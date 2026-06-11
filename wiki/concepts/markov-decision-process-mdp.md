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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- reinforcement learning
- AI
- operations research
id: pkis:concept:markov-decision-process-mdp
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
tags:
- reinforcement learning
- sequential decision making
- Bellman
- policy
- state transition
title: Markov Decision Process (MDP)
understanding: 0
---

## Definition
$$\langle S, A, p, R, p_0 \rangle$$

An MDP models agent–environment interaction: at each step $t$ the agent observes state $s_t$, takes action $a_t \sim \pi(\cdot|s_t)$, receives reward $r_t \sim p_R(s_t,a_t,s_{t+1})$, and transitions to $s_{t+1} \sim p(\cdot|s_t,a_t)$. The joint trajectory probability is:
$$p(\tau) = p_0(s_0)\prod_{t=0}^{T-1}\pi(a_t|s_t)\,p(s_{t+1}|s_t,a_t)\,p_R(r_t|s_t,a_t,s_{t+1})$$

The reward function $R(s,a) = \mathbb{E}_{s'}[\mathbb{E}_r[r|s,a,s']]$ marginalises over next states. When $S$ and $A$ are finite, a tabular representation is used.

### Why it matters
MDPs are the foundational model for sequential decision-making under uncertainty and form the mathematical basis of reinforcement learning. They generalise contextual bandits by allowing the agent's actions to influence future states, enabling credit assignment across time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]