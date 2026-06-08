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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:simulated-annealing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch30
tags:
- MCMC
- temperature
- global-optimization
- tempering
- annealed-importance-sampling
- multimodal
title: Simulated Annealing
understanding: 0
---

## Definition
Simulated annealing introduces a **temperature** parameter $T$ into a target $P(x) = e^{-E(x)}/Z$ and instead samples from

$$P_T(x) = \frac{1}{Z(T)}\,e^{-E(x)/T},$$

starting with $T$ large — which flattens the landscape and permits transitions that would be wildly improbable at $T=1$ — then gradually cooling to $T=1$. The goal is to escape unrepresentative probability islands (local basins) that trap a single-temperature chain. When the energy splits as $E(x)=E_0(x)+E_1(x)$ with $E_0$ 'nice' and $E_1$ 'nasty', one can anneal only the nasty part via $P'_T(x)\propto e^{-E_0(x)-E_1(x)/T}$, so the high-temperature limit reverts to a well-behaved $E_0$ distribution.

### As an optimizer
Used for optimization, one cools $T\to 0$ rather than $1$, concentrating mass on the global minimizer of $E(x)$.

### It does not sample exactly
Plain annealing is **biased**: there is no guarantee the probability of landing in a basin equals that basin's true mass. Two corrections exist. **Simulated tempering** (Marinari & Parisi 1992) makes $T$ itself a random variable updated by Metropolis, eliminating the bias. **Annealed importance sampling** (Neal 1998) computes importance weights for each generated point to debias and to estimate ratios of normalizing constants.

### Why it matters
Annealing is the canonical tool for multimodal targets and rough energy landscapes where standard MCMC mixes catastrophically between modes; its tempering variants turn an approximate heuristic into an asymptotically exact sampler and a practical estimator of free energies.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]