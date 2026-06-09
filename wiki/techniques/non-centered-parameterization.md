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
id: pkis:technique:non-centered-parameterization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch15
tags:
- mcmc
- hmc
- multilevel-models
- sampling
title: Non-Centered Parameterization
understanding: 0
---

## Definition
A reparameterization of a hierarchical model that decouples group-level parameters from their variance parameter to improve MCMC geometry. Instead of the centered form omega_j ~ N(mu, tau^2), one writes omega_j = mu + tau * eta_j with eta_j ~ N(0, 1), so the unit-scale auxiliary variables eta_j no longer have a posterior width that depends on tau. The centered form creates a 'whirlpool'/funnel geometry in which no single step size works for the whole posterior and samplers get stuck when tau is near zero; this is the canonical failure illustrated by the eight-schools model. The non-centered form removes the dependence and is the standard fix for funnel pathologies in Hamiltonian Monte Carlo and Gibbs sampling of hierarchical models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]