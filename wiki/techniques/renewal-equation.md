---
aliases: []
also_type: []
applies:
- branching-processes
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
- statistical-learning
id: pkis:technique:renewal-equation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- convolution
- integral-equations
- laplace-transform
title: Renewal Equation
understanding: 0
uses:
- renewal-function
---

## Definition
The renewal equation is the convolution integral equation Z = z + F*Z, i.e. Z(t) = z(t) + integral_0^t Z(t-y) F(dy), where z is a known locally bounded function (vanishing on (-infinity,0)), F is a distribution on [0,infinity) with F(0)<1, and Z is unknown; it is *proper* when F(infinity)=1. Its unique locally bounded solution vanishing on the negatives is Z = U*z = integral_0^t z(t-u) U(du), where U = sum_{n>=0} F^{n*} is the renewal function (uniqueness follows because any difference H of two solutions satisfies H = F^{n*}*H -> 0). The *renewal method* is the dominant problem-solving strategy of the theory: to find a quantity Z(t), derive a renewal equation for it by conditioning on the first (or last) renewal/jump, write the solution as U*z, and extract t->infinity behaviour via the key renewal theorem. The equation arises pervasively — for the distributions of the age A(t) and excess B(t), for the mean population size in age-dependent branching (in the form Z = z + mF*Z with m = E[offspring]), for ruin probabilities in risk processes, and for state probabilities of regenerative processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[branching-processes]] — applies
- [[renewal-function]] — uses
[To be populated during integration]