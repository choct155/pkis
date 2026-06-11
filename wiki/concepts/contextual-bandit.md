---
aliases: []
also_type: []
applies:
- collaborative-filtering
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
- reinforcement-learning
- machine-learning
extends:
- multi-armed-bandit
generalizes:
- multi-armed-bandit
id: pkis:concept:contextual-bandit
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
- murphy-pml2-advanced-ch34
specializes:
- reinforcement-learning
- markov-decision-processes
tags:
- exploration
- exploitation
- recommendation
- online-learning
- bandit
title: Contextual Bandit
understanding: 0
uses:
- exploration-exploitation-tradeoff
- policy
- belief-state-mdp
---

## Definition
A contextual bandit is a sequential decision problem in which at each round an agent observes a context $\mathbf{x}_t$, selects an action $a_t$ from a finite set $\mathcal{A}$, and receives a reward $r_t = r(\mathbf{x}_t, a_t)$, but does **not** observe rewards for unchosen actions. Formally it is a one-step Markov decision process: there is no persistent state transition—rewards depend only on the current context and action, not on history.

The policy $\pi: \mathcal{X} \to \mathcal{A}$ maps contexts to actions and is evaluated by cumulative reward. Learning requires managing the exploration–exploitation trade-off: the agent must sometimes take sub-optimal actions to gather information.

### Why it matters
Formalises the feedback structure of online recommendation, personalised advertising, and clinical trial allocation, where training data is collected by the learner's own policy, creating selection bias; provides the theoretical grounding for why supervised learning is insufficient for recommendation systems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[belief-state-mdp]] — uses
- [[markov-decision-processes]] — specializes
- [[multi-armed-bandit]] — extends
- [[policy]] — uses
- [[collaborative-filtering]] — applies
- [[exploration-exploitation-tradeoff]] — uses
- [[reinforcement-learning]] — specializes
- [[multi-armed-bandit]] — generalizes
[To be populated during integration]