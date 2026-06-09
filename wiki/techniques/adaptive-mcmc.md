---
aliases: []
also_type: []
applies:
- metropolis-algorithm
- mcmc
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
id: pkis:technique:adaptive-mcmc
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch12
tags:
- MCMC
- tuning
- warm-up
- detailed-balance
- acceptance-rate
- metropolis
- convergence
title: Adaptive MCMC
understanding: 0
uses:
- detailed-balance
---

## Definition
Adaptive MCMC refers to modifying the parameters of a Markov chain simulation algorithm (e.g. the covariance and scale of a Metropolis jumping kernel, or the mass matrix and step size of HMC) while the chain is running, using information from the simulations so far, in order to improve sampling efficiency. The motivating idea is that good tuning parameters — for instance, a jumping covariance proportional to the posterior covariance, scaled to hit a target acceptance rate — are usually unknown in advance and are best estimated from the chain itself.

## The Central Hazard: Adaptation Breaks Detailed Balance
If the transition rule at iteration t depends on the previous simulation history, then the transition probabilities are no longer those assumed by the Metropolis-Hastings derivation, detailed balance is violated, and the chain does not in general converge to the target distribution. The intuition: an adaptation that, say, moves quickly through flat regions and slowly through sharply varying regions will make the chain spend disproportionately little time in the flat parts — so the empirical draws systematically misrepresent the target unless a correction is applied.

## The Standard Safe Recipe: Two Phases
To adapt safely, run the algorithm in two phases. (1) An adaptive (warm-up) phase, in which tuning parameters may be adjusted as often as desired to improve efficiency; these draws are discarded. (2) A fixed phase, in which the now-frozen algorithm is run long enough for approximate convergence; only these draws are used for inference. This recipe underlies the warm-up adaptation in HMC and NUTS, and Stan implements exactly this pattern.

## Target Acceptance Rates
A practical adaptive Metropolis scheme adjusts the jumping covariance toward the estimated posterior covariance and scales it to drive the acceptance rate toward its theoretically optimal value — about 0.44 in one dimension, declining to about 0.23 in high dimensions (d > 5) — with scale roughly 2.4/√d for a normal target. For HMC the analogous optimal acceptance rate is about 0.65. Acceptance rate far above the target means steps are too cautious (increase scale); far below means steps are too ambitious (decrease scale).

## Properly Validated Adaptive Schemes
Specially constructed adaptive algorithms (e.g. the diminishing-adaptation schemes of Andrieu and collaborators, and the NUTS dual-averaging adaptation) can adapt continuously while still provably converging to the target, but these require careful design beyond the naive 'tune on the fly' approach.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc]] — applies: adaptive MCMC is a family of strategies for tuning MCMC samplers on the fly
- [[metropolis-algorithm]] — applies: the canonical adaptive scheme tunes the Metropolis jumping covariance and scale toward the optimal acceptance rate
- [[detailed-balance]] — uses: the whole hazard of adaptive MCMC is that history-dependent tuning breaks detailed balance
[To be populated during integration]