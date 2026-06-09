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
- bayesian-stats
- statistical-learning
id: pkis:concept:alternating-renewal-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- stochastic-processes
- reliability
- availability
title: Alternating Renewal Process
understanding: 0
---

## Definition
An alternating renewal process models a system that switches between two states — on/off, operative/down, open/closed — where successive on-periods are i.i.d. with mean mu_o, successive off-periods are i.i.d. with mean mu_c, and the two sequences are independent. Each renewal cycle is one on-period plus one off-period, so the cycle mean is mu_o + mu_c. By the renewal reward theorem (with reward = time spent on per cycle), the long-run proportion of time the system is in the on-state is mu_o/(mu_o + mu_c); this is the reliability-theory *availability*. It is the simplest non-trivial regenerative process and the prototypical application of 'expected on-time per cycle over expected cycle length'.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]