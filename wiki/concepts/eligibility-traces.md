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
- optimization
- deep-learning
id: pkis:concept:eligibility-traces
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch12
tags:
- reinforcement-learning
- temporal-difference
- credit-assignment
title: Eligibility Traces
understanding: 0
---

## Definition
A short-term memory vector z_t in R^d that parallels the long-term weight vector w_t and provides an efficient, incremental mechanism for temporal credit assignment in reinforcement learning. When a component of w_t participates in producing a value estimate, the corresponding component of z_t is bumped up and then fades away at rate gamma*lambda; learning occurs in that component when a nonzero TD error arrives before the trace decays to zero. Eligibility traces unify and generalize TD and Monte Carlo methods, spanning a spectrum from one-step TD (lambda=0) to Monte Carlo (lambda=1), and their chief advantage over n-step methods is requiring only a single trace vector (O(d) memory and per-step compute) rather than storing the last n feature vectors, with learning distributed uniformly in time. Crucially, eligibility traces are not specific to TD learning: they arise even in Monte Carlo/LMS learning, suggesting the need for a trace emerges whenever one tries to learn long-term predictions efficiently. Variants include accumulating, replacing, and dutch traces.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]