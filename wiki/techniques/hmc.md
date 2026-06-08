---
aliases: []
also_type: []
component_scores:
  alternatives: 3
  conditions: 2
  diagnostics: 3
  failure_modes: 3
  implementation: 2
  operational_mechanism: 3
  principled_mechanism: 3
contrasts-with:
- gibbs-sampler
coverage: 1
date_created: '2026-06-07'
date_updated: '2026-06-07'
domain:
- bayesian-stats
- optimization
extends:
- mcmc
id: pkis:technique:hmc
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
score_date: '2026-06-07'
sources:
- betancourt-hmc
- betancourt-hmcgeometric
tags:
- MCMC
- posterior-sampling
- gradient-based
- symplectic
- leapfrog
- NUTS
- typical-set
- divergent-transitions
- funnel-geometry
title: Hamiltonian Monte Carlo (HMC)
understanding: 2
uses:
- hamiltonian-classical-mechanics
- typical-set
---

## Definition
Hamiltonian Monte Carlo constructs Markov chain proposals by simulating Hamiltonian dynamics in the joint space of model parameters θ and auxiliary momentum variables p. Unlike random walk Metropolis-Hastings, proposals move along the posterior surface rather than through it, enabling large moves while remaining in the high-probability typical set.

## The Typical Set Motivation

In high dimensions, posterior probability mass does not live at the mode. It lives in a thin shell — the typical set — where probability density times volume is maximized. Random walk proposals almost always leave the typical set because most directions lead to lower probability mass. HMC is designed to move along the typical set.

## The Hamiltonian

H(θ, p) = U(θ) + K(p)
U(θ) = −log p(θ|y)         (potential energy = negative log posterior)
K(p) = ½ pᵀM⁻¹p            (kinetic energy = quadratic in momentum)

U is low where posterior probability is high. K is a Gaussian in p, drawn fresh each trajectory. Total energy H is approximately conserved along leapfrog trajectories, keeping the simulation in the typical set.

Why these specific mappings:
- U = −log p(θ|y) because potential energy should be low where posterior probability is high. The mapping makes the posterior's high-probability region the bottom of the energy landscape.
- K = quadratic in p because the momentum distribution must be a tractable independent Gaussian (easy to sample, independent of θ, factorizes cleanly from the posterior).

## The Algorithm

1. Draw fresh momentum p ~ N(0, M)
2. Simulate L leapfrog steps of size ε:
   - Half-step momentum: p ← p − (ε/2)∇U(θ)
   - Full-step position: θ ← θ + εM⁻¹p
   - Half-step momentum: p ← p − (ε/2)∇U(θ)
3. Metropolis accept/reject: accept with probability min(1, exp(H_current − H_proposed))
4. Record θ; repeat

Gradient ∇U(θ) = −∇log p(θ|y) required at every leapfrog step. This is the epistemological anchor: gradient information along the full trajectory.

## The Leapfrog Integrator

Chosen because it is symplectic — preserves the geometric structure of Hamiltonian dynamics (phase space volumes) in a way that ensures detailed balance and the correct stationary distribution. Non-symplectic integrators accumulate energy drift that corrupts the stationary distribution. The Metropolis step corrects for residual non-conservation.

## NUTS

No-U-Turn Sampler (Hoffman & Gelman 2014). Automatically detects when the trajectory starts doubling back on itself — the U-turn criterion — and stops there. Combined with dual averaging for step size adaptation, NUTS requires almost no manual tuning. Default sampler in Stan and PyMC. Target acceptance rate: 60-90% (higher than MH's 23% because gradient-informed proposals stay closer to typical set).

## Divergent Transitions

When the leapfrog integrator encounters high posterior curvature (funnel necks in hierarchical models), energy conservation fails and the trajectory flies into a low-probability region. These divergent transitions are a diagnostic signal unavailable to random walk samplers — the gradient-based integrator detects geometric pathology that the likelihood ratio alone cannot see. Fix: non-centered parameterization flattens funnel geometry without changing the model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[typical-set]] — uses: HMC is engineered to move along the typical set rather than toward the mode
- [[gibbs-sampler]] — contrasts-with: HMC moves along the posterior surface via gradients; Gibbs updates one coordinate at a time
- [[hamiltonian-classical-mechanics]] — uses: HMC simulates Hamiltonian dynamics over an auxiliary momentum
- [[mcmc]] — extends: HMC is a gradient-based MCMC method
[To be populated during integration]