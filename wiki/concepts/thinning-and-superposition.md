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
id: pkis:concept:thinning-and-superposition
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch04
tags:
- stochastic-processes
- point-processes
- poisson-process
- thinning
- superposition
- coloring
title: Thinning and Superposition of Poisson Processes
understanding: 0
---

## Definition
Two complementary closure operations under which the Poisson family is invariant. Superposition: the sum (overlay) N_1 + N_2 of independent point processes; superposing independent PRM(μ_1) and PRM(μ_2) yields PRM(μ_1 + μ_2) — immediate from the Laplace functional, whose log is additive. Thinning (splitting/coloring): inspect each point of a PRM(μ) independently and retain it with probability p (delete with q = 1−p). The retained process N_r and deleted process N_d are themselves *independent* Poisson processes with mean measures pμ and qμ respectively. The mechanism is marking by iid Bernoulli labels followed by complete randomness applied to the disjoint label-regions {1} and {−1}. The construction generalizes to k categories (multinomial marks → k independent Poisson substreams) and to location-dependent retention p(t), which produces a non-homogeneous Poisson process of local intensity α p(t). These results justify splitting a Poisson input stream of a queue into independent Poisson substreams and merging independent streams into one Poisson stream.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]