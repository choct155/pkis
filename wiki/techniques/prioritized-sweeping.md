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
date_updated: '2026-06-20'
domain:
- optimization
- deep-learning
extends:
- dyna-q
id: pkis:technique:prioritized-sweeping
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
- gulli-agentic-design-patterns-ch20
tags:
- reinforcement-learning
- planning
- backward-focusing
- priority-queue
- dyna
title: Prioritized Sweeping
understanding: 0
uses:
- expected-vs-sample-updates
---

## Definition
A planning method (Moore & Atkeson, 1993; Peng & Williams, 1993) that focuses computational updates where they will do the most good rather than sampling state-action pairs uniformly as in Dyna-Q. It implements backward focusing: when a state's value changes, only the predecessor state-action pairs leading into it are worth updating, and changes propagate backward. A priority queue holds every state-action pair whose estimated value would change nontrivially if updated, prioritized by the magnitude of that change (the absolute TD error). The top pair is updated, then the effect on each of its predecessor pairs is computed and any pair whose induced change exceeds a threshold theta is (re)inserted with the new priority. This propagates changes efficiently until quiescence, dramatically speeding maze solutions (often 5-10x over unprioritized Dyna-Q). Extensions to stochastic environments keep transition counts and use expected updates; a limitation is that expected updates can waste computation on low-probability transitions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[expected-vs-sample-updates]] — uses: Prioritized sweeping prioritizes by TD-error magnitude and (for stochastic envs) uses expected updates.
- [[dyna-q]] — extends: Prioritized sweeping focuses Dyna-style planning updates via a priority queue instead of uniform sampling.
[To be populated during integration]