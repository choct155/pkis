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
coverage: 0
date_created: '2026-06-07'
date_updated: '2026-06-07'
domain:
- bayesian-stats
- optimization
- deep-learning
id: pkis:concept:posterior-geometry-coordinate-systems
knowledge_type: concept
maturity: evolving
needs_canonical_source: true
prerequisite-of:
- hmc
related_concepts: []
sources: []
tags:
- reparameterization
- non-centered-parameterization
- normalizing-flows
- coordinate-transformation
- HMC
- funnel-geometry
- divergent-transitions
- change-of-variables
title: Posterior Geometry and Coordinate Systems
understanding: 0
illustrated-by:
- hmc-explainer
---

## Definition
The posterior distribution is a fixed geometric object determined by the model and data. The coordinate system used to represent it during inference is a design choice. A poor coordinate system can make a tractable posterior appear intractable. A good coordinate system can make a difficult geometry navigable. The model is unchanged; only the parameterization changes.

## The Funnel Problem in Hierarchical Models

Hierarchical models generically produce funnel-shaped posterior geometry. The variance parameter σ controls the scale of group-level parameters θ_group. When σ is small, group-level parameters are tightly constrained — posterior is narrow. When σ is large, they are free — posterior is wide. The joint posterior has a funnel shape.

The leapfrog integrator uses a fixed step size. A step size calibrated for the wide region is too large for the narrow neck — energy conservation fails, divergent transitions occur. The chain is systematically repelled from the funnel neck, missing the scientifically interesting region where hierarchical structure is most informative.

R-hat appears good (chains agree) while coverage is wrong (all chains missing the neck). Divergent transitions are the only diagnostic signal — detectable only because HMC uses gradient information at every step.

## The Non-Centered Parameterization Fix

Natural (centered) parameterization:
  θ_group ~ N(μ, σ²)   ← geometry depends on σ

Non-centered parameterization:
  z ~ N(0, 1)           ← geometry independent of σ
  θ_group = μ + σ·z    ← reconstruct on natural scale

The standardized offset z does not depend on σ. Its posterior geometry does not change as you move through the variance dimension. The funnel is gone. The posterior over θ_group is identical — only the coordinate system has changed.

## General Principle: Instances Across the Research Program

Non-centered parameterization: Flattens funnel geometry in hierarchical models

Reparameterization trick in VAEs: Makes sampling operation differentiable by transforming stochastic nodes to deterministic transformations of noise variables: z = μ + σ·ε, ε ~ N(0,1) (instead of z ~ N(μ, σ²))

Normalizing flows: Learn an expressive coordinate transformation mapping a simple base distribution to a complex posterior — the most general instance

Natural gradient methods: Use the Fisher information metric as the optimization geometry — the coordinate system in which the posterior looks locally Gaussian

## Diagnostic Connection

Richer epistemological anchors produce richer diagnostics. Metropolis-Hastings cannot detect funnel geometry — it simply rejects more proposals in the neck and slows down silently. HMC detects it because the gradient changes dramatically in the neck, causing measurable energy conservation failure. The coordinate system problem is visible only to samplers that use geometric information.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hmc]] — prerequisite-of: Coordinate-system choice governs HMC behavior and divergent-transition failure modes
[To be populated during integration]

## Needs Canonical Source
This stub was created without a source. Suggested references:

**Already in corpus:**
[none in corpus]

**External candidates (Semantic Scholar):**
[none found]