---
aliases: []
also_type: []
analogous-to:
- mean-field-approximation
applies:
- ising-model
- gaussian-mixture-models
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
- probability-theory
extends:
- overrelaxation-mcmc
- gibbs-sampler
generalizes:
- data-augmentation-algorithm
id: pkis:technique:gibbs-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch11
- murphy-pml2-advanced-ch12
specializes:
- metropolis-hastings
- metropolis-hastings-algorithm
tags:
- mcmc
- posterior-sampling
- graphical-models
- markov-chain
title: Gibbs Sampling
understanding: 0
uses:
- markov-chains
- detailed-balance
- markov-blanket
- adaptive-rejection-sampling
- ergodicity-markov-chain-mcmc
- full-joint-probability-distribution
---

## Definition
Gibbs sampling is an MCMC algorithm for distributions $p(z_1,\ldots,z_M)$ that cycles through each variable and samples it from its full conditional distribution given all others:
$$z_i^{(\tau+1)} \sim p(z_i \mid z_1^{(\tau+1)},\ldots,z_{i-1}^{(\tau+1)},z_{i+1}^{(\tau)},\ldots,z_M^{(\tau)}).$$
Each step is a special case of the Metropolis-Hastings algorithm with acceptance probability $A = 1$, because the proposal $q_k(z^*|z) = p(z_k^*|z_{\setminus k})$ cancels exactly in the MH ratio.

### Why it matters
Gibbs sampling requires only the ability to sample from univariate (or low-dimensional block) conditionals, which are often tractable in graphical models — especially those built from exponential-family conditionals with conjugate parents. Its main limitation is slow mixing under strong correlations, since state evolution proceeds by a random walk with step size governed by the conditional variance rather than the marginal variance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mean-field-approximation]] — analogous-to: Gibbs update equation mirrors mean-field variational update
- [[gaussian-mixture-models]] — applies
- [[ising-model]] — applies
- [[gibbs-sampler]] — extends: gibbs-sampler is the existing node
- [[full-joint-probability-distribution]] — uses
- [[metropolis-hastings-algorithm]] — specializes: Gibbs is MH with acceptance probability 1
- [[data-augmentation-algorithm]] — generalizes
- [[ergodicity-markov-chain-mcmc]] — uses
- [[overrelaxation-mcmc]] — extends
- [[adaptive-rejection-sampling]] — uses
- [[markov-blanket]] — uses: conditionals in graphical models depend only on Markov blanket
- [[detailed-balance]] — uses
- [[markov-chains]] — uses
- [[metropolis-hastings]] — specializes
[To be populated during integration]