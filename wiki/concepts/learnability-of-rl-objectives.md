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
contrasts-with:
- bellman-error-vs-projected-bellman-error
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- statistical-learning
id: pkis:concept:learnability-of-rl-objectives
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch11
tags:
- learnability
- bellman-error
- value-error
- data-distribution
- identifiability
- off-policy
title: Learnability of RL Objectives
understanding: 0
---

## Definition
A foundational notion (distinct from the ML sense of efficient/PAC learnability) asking whether a quantity can be estimated AT ALL from the observable stream of feature vectors, actions, and rewards, given any amount of experience. Many quantities that are well-defined given the environment's internal structure are NOT learnable because distinct MRPs can produce identical data distributions. Sutton & Barto distinguish three cases via paired indistinguishable MRPs: (1) the Value Error (VE) is not learnable (its value differs across data-equivalent MRPs), but its MINIMIZER w* is learnable — provably so, because VE = RE - variance, where the mean square Return Error (RE) is observable and the variance term is parameter-independent, so VE and RE share the same optimizer; (2) the Bellman Error (BE) is not learnable AND, unlike VE, its minimizer is not learnable either — a counterexample pair of MRPs has BE=0 vs BE=2/3 at w=0 and different BE-minimizing parameters (limiting to (-1/2, 0)^T as gamma->1 for one MRP), so no algorithm can target the BE from data; (3) objectives like the RE and PBE are learnable. This is the chapter's strongest argument against the Bellman error and in favor of the projected Bellman error as the practical objective for off-policy learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bellman-error-vs-projected-bellman-error]] — contrasts-with: Learnability analysis shows the BE (and its minimizer) is not learnable, while the PBE is — the decisive argument between the two objectives.
[To be populated during integration]