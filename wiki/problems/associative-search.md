---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
generalizes:
- multi-armed-bandit
id: pkis:problem:associative-search
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- markov-decision-processes
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- contextual-bandits
- policy
- associative
- context
title: Associative Search (Contextual Bandits)
understanding: 0
---

## Definition
$$\pi: \text{context} \mapsto \text{action}$$

An intermediate problem between the nonassociative $k$-armed bandit and full reinforcement learning: the learner faces different bandit tasks signaled by an observable context clue and must learn a *policy* mapping each context to its best action.

### Setup
Suppose several bandit tasks are presented in random order, each accompanied by a distinctive signal (e.g. a slot machine that changes color with its action values). The learner cannot see the action values but can associate each signal with the action that is best under it — "if red, pull arm 1; if green, pull arm 2." With the right policy it outperforms any context-blind strategy.

### Position in the RL hierarchy
Associative search combines trial-and-error *search* for good actions with *association* of actions to the situations in which they are best. It is like full RL in that it learns a policy, but like the plain bandit in that each action affects only the immediate reward, not the next situation. Allowing actions to influence the next state yields the full reinforcement-learning problem.

### Why it matters
Now usually called *contextual bandits*, associative search is heavily used in practice (recommendation, ad placement, clinical treatment selection) and is the conceptual stepping-stone to state-dependent policies. It connects to the operant-conditioning notion of a *discriminative stimulus*, where a signal marks which reinforcement contingency is in force — the psychological analogue of a state.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — prerequisite-of: contextual bandits are the stepping-stone toward the full MDP/RL problem
- [[multi-armed-bandit]] — generalizes: adds an observable context, requiring a context-to-action policy
[To be populated during integration]