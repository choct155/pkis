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
contrasts-with:
- polynomial-basis-rl
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
id: pkis:technique:fourier-basis-rl
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
- fourier-series
- cosine-basis
- linear-methods
title: Fourier Basis for RL
understanding: 0
---

## Definition
A linear feature set built from the Fourier series (Konidaris, Osentoski & Thomas 2011). For an aperiodic function on a bounded interval one sets the period to twice the interval and keeps only the cosine terms, since any function on the half-period can be approximated by cosines (and 'half-even' functions are easier to approximate than 'half-odd' ones, avoiding discontinuity at the origin). The order-n one-dimensional basis is x_i(s) = cos(iπ s) for i = 0..n; in k dimensions, x_i(s) = cos(π sᵀ cⁱ) with each c_jⁱ ∈ {0,…,n}, giving (n+1)^k features—the integer vector cⁱ sets the frequency along each dimension and encodes interactions. A per-feature step size α_i = α/‖cⁱ‖ is recommended. Fourier features outperform polynomials and often RBFs on benchmarks, but struggle with discontinuities ('ringing') and, being globally non-zero, represent global rather than local properties; the basis grows exponentially in dimension and requires subset selection for high k.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[polynomial-basis-rl]] — contrasts-with: Fourier features outperform polynomials in online RL, which are not recommended
- [[linear-function-approximation-rl]] — specializes: the Fourier cosine basis is a feature set for linear value approximation
[To be populated during integration]