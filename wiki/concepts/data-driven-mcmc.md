---
aliases: []
also_type: []
analogous-to:
- amortized-inference
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
- machine-learning
- computer-vision
- statistics
extends:
- metropolis-hastings-algorithm
id: pkis:concept:data-driven-mcmc
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
tags:
- mcmc
- proposal-distribution
- learned-proposals
- recognition-network
- generate-and-test
title: Data-Driven MCMC
understanding: 0
---

## Definition
An MCMC framework in which the proposal distribution is conditioned on both the current state and the observed data, $q(x'|x, \mathcal{D})$, typically implemented via learned discriminative models (recognition networks or task-specific detectors):
$$q(x'|x, \mathcal{D}) = \pi_0 q_0(x'|x) + \sum_k \pi_k q_k(x'_k|f_k(\mathcal{D}))$$
where $q_0$ is a standard data-independent proposal and each $q_k$ is a learned expert that proposes updates to the $k$-th component of the hidden state.

### Why it matters
Data-driven proposals can be orders of magnitude more efficient than generic proposals in structured settings (e.g., estimating 3D human pose from images) because they concentrate proposal mass near high-posterior regions identified by discriminative cues. The method retains the exactness of MCMC: the learned proposals are used only to generate candidates, which are then accepted or rejected based on the exact posterior ratio, ensuring the correct stationary distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[amortized-inference]] — analogous-to
- [[metropolis-hastings-algorithm]] — extends
[To be populated during integration]