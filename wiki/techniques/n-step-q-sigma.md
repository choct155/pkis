---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:technique:n-step-q-sigma
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch07
tags:
- reinforcement-learning
- off-policy
- control
- unification
- bootstrapping
title: n-step Q(sigma)
understanding: 0
---

## Definition
n-step Q(sigma) is a unifying multi-step action-value algorithm that subsumes n-step Sarsa, n-step Expected Sarsa, and the tree-backup algorithm as special cases by deciding, on a per-step basis, whether to take the transition as a full sample (as in Sarsa) or as an expectation over all actions (as in tree backup). A parameter sigma_t in [0,1] sets the degree of sampling at step t: sigma=1 is full sampling (Sarsa), sigma=0 is pure expectation (tree backup), and choosing sigma=1 for all but the last step gives Expected Sarsa. The n-step return slides linearly between the importance-sampling ratio rho_{t+1} and the action probability pi(A_{t+1}|S_{t+1}): G_{t:h} = R_{t+1} + gamma*(sigma_{t+1}*rho_{t+1} + (1-sigma_{t+1})*pi(A_{t+1}|S_{t+1}))*(G_{t+1:h} - Q_{h-1}(S_{t+1},A_{t+1})) + gamma*Vbar_{h-1}(S_{t+1}). Because the importance-sampling correction is folded into the return, the plain n-step Sarsa update (without an external ratio) is used. Q(sigma) thus allows a continuous trade-off between the lower-variance expectation-based backups and the sampling-based backups within a single framework.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]