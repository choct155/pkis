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
- gibbs-sampling
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- physics
extends:
- metropolis-hastings
id: pkis:technique:hybrid-monte-carlo
instantiates:
- hmc
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- no-u-turn-sampler
related_concepts: []
sources:
- bishop-prml-ch11
tags:
- mcmc
- hamiltonian-dynamics
- leapfrog
- posterior-sampling
- gradient-based
title: Hybrid Monte Carlo (HMC)
understanding: 0
uses:
- leapfrog-integrator
- liouvilles-theorem
- ergodicity-markov-chain-mcmc
- hamiltonian-classical-mechanics
---

## Definition
Hybrid (Hamiltonian) Monte Carlo introduces auxiliary momentum variables $\mathbf{r}$ and simulates Hamiltonian dynamics to propose large, approximately independent moves in the target space. The joint distribution
$$p(\mathbf{z}, \mathbf{r}) = \frac{1}{Z_H}\exp(-H(\mathbf{z},\mathbf{r})), \quad H = E(\mathbf{z}) + \tfrac{1}{2}\|\mathbf{r}\|^2,$$
is invariant under both (i) leapfrog integration of Hamilton's equations and (ii) Gibbs resampling of $\mathbf{r} \sim \mathcal{N}(0, I)$. A Metropolis accept/reject step corrects for discretisation error:
$$A = \min\bigl(1,\exp\{H(\mathbf{z},\mathbf{r}) - H(\mathbf{z}^*,\mathbf{r}^*)\}\bigr).$$
Detailed balance follows from time-reversibility and volume preservation of the leapfrog integrator.

### Why it matters
HMC exploits gradient information $\nabla_z \ln p(\mathbf{z})$ to make coherent, long-range proposals, reducing the autocorrelation time from $O((\sigma_{\max}/\sigma_{\min})^2)$ for random-walk Metropolis to $O(\sigma_{\max}/\sigma_{\min})$. It is the foundation of the No-U-Turn Sampler (NUTS) and is the default inference engine in Stan and PyMC.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hamiltonian-classical-mechanics]] — uses
- [[gibbs-sampling]] — contrasts-with
- [[hmc]] — instantiates
- [[no-u-turn-sampler]] — prerequisite-of
- [[ergodicity-markov-chain-mcmc]] — uses
- [[liouvilles-theorem]] — uses
- [[leapfrog-integrator]] — uses
- [[metropolis-hastings]] — extends
[To be populated during integration]