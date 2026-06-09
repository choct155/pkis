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
- reinforcement-learning
id: pkis:concept:on-policy-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- state-distribution
- stationary-distribution
- prediction
title: On-policy Distribution
understanding: 0
---

## Definition
The distribution μ(s) of states encountered while following the target policy π, used to weight the VE objective and central to the convergence of semi-gradient methods. In continuing tasks it is the stationary distribution under π. In episodic tasks it depends on the start-state distribution h(s): one solves η(s) = h(s) + Σ_{s̄} η(s̄) Σ_a π(a|s̄) p(s|s̄,a) for the expected number of visits η(s) per episode, then normalizes μ(s) = η(s)/Σ η(s'). Discounting (γ<1) is handled as a form of termination by inserting a γ factor in the recursion. Updating states according to this distribution is what makes bootstrapping with function approximation stable; under other update distributions, bootstrapping methods can diverge.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]