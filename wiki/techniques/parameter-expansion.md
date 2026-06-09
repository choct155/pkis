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
id: pkis:technique:parameter-expansion
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch12
tags:
- mcmc
- gibbs-sampler
- convergence
- auxiliary-variable
- reparameterization
- hierarchical-models
- overparameterization
title: Parameter Expansion
understanding: 0
---

## Definition
Parameter expansion is a strategy for accelerating the convergence of a Gibbs sampler (or EM algorithm) by deliberately adding an extra, redundant parameter to the model, so the sampler performs its random walk in a larger space. Paradoxically, enlarging the parameter space can break problematic posterior dependence among the original parameters that a simple linear reparameterization cannot resolve, letting the chain move in more directions and avoid getting stuck.

## Mechanism: An Unidentified Working Parameter
The added parameter (often a multiplicative scale, e.g. α with V_i = α²U_i and σ = ατ) is not identified by the data on its own — the likelihood does not pin it down. Its only job is to give the Gibbs sampler additional moves. Convergence is monitored on the identified summaries of interest (e.g. μ, σ = ατ, V_i = α²U_i), or one simply saves the original-model parameters from the simulations. The whole model remains identified even though the expanded parameters individually are not.

## Why It Works (t-model Example)
In the latent-scale (data-augmented) t model, a draw of σ near zero pulls the latent variances V_i toward zero, which in turn pulls the next σ draw toward zero — a self-reinforcing trap that makes the plain Gibbs sampler converge slowly. Adding the scale parameter α (whose conditional update is a simple normal-variance draw) breaks the dependence between τ and the V_i's, so the chain mixes reliably.

## Relation to Reparameterization and Data Augmentation
Parameter expansion is distinct from ordinary reparameterization: rather than re-expressing the same parameters in better coordinates, it genuinely adds a dimension. It is especially natural on top of a data-augmented (auxiliary-variable) model and is widely used to speed convergence of hierarchical-model variance parameters. The deterministic analog for optimization is PX-EM (parameter-expanded EM).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]