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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:technique:adaptive-rejection-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch11
- murphy-pml2-advanced-ch11
tags:
- monte-carlo
- sampling
- log-concave
- gibbs-sampling
- envelope-function
title: Adaptive Rejection Sampling
understanding: 0
---

## Definition
For a log-concave target $p(z)$ (i.e., $\ln p(z)$ has non-increasing derivative), the envelope function $kq(z)$ is constructed automatically by evaluating $\ln p(z)$ and its gradient at a set of grid points and forming piecewise linear upper tangent lines. The resulting envelope is a piecewise exponential distribution
$$q(z) = k_i \lambda_i \exp\{-\lambda_i(z - z_{i-1})\}, \quad z_{i-1} < z \leq z_i.$$
When a proposed sample is rejected, it is added to the grid, refining the envelope for future proposals.

### Why it matters
Adaptive rejection sampling removes the need to specify an analytic envelope by construction, making rejection sampling practical for a broad class of log-concave conditionals (e.g., exponential-family directed graphical models with conjugate parents). It is widely used as a subroutine inside Gibbs samplers. For non-log-concave targets it can be extended with a Metropolis-Hastings accept/reject step (adaptive rejection Metropolis sampling).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]