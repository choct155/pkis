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
- reinforcement-learning
id: pkis:technique:polynomial-basis-rl
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
specializes:
- linear-function-approximation-rl
tags:
- feature-construction
- linear-methods
- interpolation
- regression
title: Polynomial Basis for RL
understanding: 0
---

## Definition
Representing states by polynomial features of their numeric dimensions, the simplest family borrowed from interpolation and regression. For a two-dimensional state, x(s) = (1, s₁, s₂, s₁s₂)ᵀ adds a constant (allowing affine functions and nonzero value at the origin) and a product term (capturing interaction); higher-order vectors yield arbitrary quadratics while remaining linear in the weights. The general order-n basis for k dimensions has features x_i(s) = ∏_j s_j^{c_{i,j}} with each c_{i,j} ∈ {0,…,n}, totaling (n+1)^k features, which grows exponentially in k. Polynomials are simple and familiar but generalize poorly in online RL; Sutton & Barto explicitly do not recommend them for online learning, preferring the Fourier basis or coarse coding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-function-approximation-rl]] — specializes: polynomial features form a linear basis for value approximation
[To be populated during integration]