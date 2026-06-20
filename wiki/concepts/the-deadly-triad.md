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
date_updated: '2026-06-20'
domain:
- reinforcement-learning
- optimization
- deep-learning
id: pkis:concept:the-deadly-triad
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- gradient-td-methods
- emphatic-td
related_concepts: []
sources:
- sutton-reinforcement-2018-ch11
- sutton-reinforcement-2018
tags:
- off-policy
- divergence
- stability
- bootstrapping
- function-approximation
- td-learning
title: The Deadly Triad
understanding: 0
uses:
- semi-gradient-td
---

## Definition
The deadly triad names the three properties whose simultaneous presence makes a value-learning algorithm prone to instability and divergence: (1) function approximation (generalizing over a state space far larger than available memory/compute, e.g. linear features or ANNs); (2) bootstrapping (update targets that include current estimates, as in DP and TD, rather than full Monte Carlo returns); and (3) off-policy training (updating on a transition distribution other than the one induced by the target policy, which includes uniform DP sweeps). If any two are present but not all three, instability can be avoided. Crucially, the danger is NOT due to control, generalized policy iteration, learning, or environmental uncertainty: divergence appears even in the simplest prediction case and even in planning (DP) where the environment is fully known. Sutton & Barto argue each element is individually hard to give up — function approximation is essential for scale, bootstrapping is too valuable for data/compute efficiency to abandon, and off-policy learning is needed for parallel learning of many predictions from one experience stream — which is why the chapter pursues new algorithms that keep all three while restoring stability. Identified by Sutton (1995) and analyzed by Tsitsiklis & Van Roy (1997); the name is due to Sutton (2015).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[emphatic-td]] — prerequisite-of: Emphatic-TD is the second remedy for off-policy instability under the deadly triad.
- [[gradient-td-methods]] — prerequisite-of: Gradient-TD is motivated as a remedy that keeps all three triad elements while restoring stability.
- [[semi-gradient-td]] — uses: The triad's instability manifests specifically in bootstrapping semi-gradient TD methods.
[To be populated during integration]