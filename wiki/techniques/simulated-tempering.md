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
- bayesian-stats
- optimization
id: pkis:technique:simulated-tempering
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch12
tags:
- mcmc
- multimodal
- temperature-ladder
- tempering
- parallel-tempering
- mode-hopping
- auxiliary-variable
title: Simulated Tempering
understanding: 0
---

## Definition
Simulated tempering is an MCMC strategy for sampling multimodal posterior distributions, where modes separated by regions of very low density trap ordinary Gibbs or Metropolis chains near a single mode for long periods. It augments the target p(ω|y) with a ladder of K+1 distributions p_k(ω|y), k = 0,...,K, sharing the same basic shape but progressively flattened so they mix freely across modes; p_0 is the true target. A single composite chain carries state (ω_t, s_t), where s_t indexes which distribution is currently active, and it randomly hops up and down the ladder. Only draws taken at the bottom rung (s = 0, the true target) are used for inference.

## The Temperature Ladder
A common ladder is q_k(ω) = p(ω|y)^{1/T_k} p_0(ω)^{1-1/T_k} for temperatures T_k > 0, with T_0 = 1 recovering the target. Large T_k 'adds thermal noise', flattening the modes toward a high-variance base measure that bridges between them. Only unnormalized densities q_k are needed. Moves between rungs are accepted with a Metropolis ratio r = c_j q_j(ω) J_{j,s}/(c_s q_s(ω) J_{s,j}); the normalizing constants c_k are set adaptively so the chain spends roughly equal time at each rung.

## Parallel Tempering
Parallel tempering is the variant that runs K+1 parallel chains, one per ladder distribution, each evolving on its own with occasional Metropolis-controlled swapping of states between adjacent chains. At convergence, chain 0 supplies draws from the target. It is often more convenient than single-chain simulated tempering because it avoids estimating the c_k normalizers.

## Relation to Simulated Annealing
Tempering shares the temperature device with simulated annealing but has a different goal: annealing cools a single chain toward a global optimum (a point), whereas tempering maintains a stationary distribution over the full ladder in order to sample the entire multimodal posterior (a distribution). The flattened high-temperature rungs serve as a bridge that lets the cold chain hop between well-separated modes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]