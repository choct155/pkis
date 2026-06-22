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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-22'
domain:
- statistics
- probability-theory
id: pkis:concept:ergodicity-markov-chain-mcmc
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- metropolis-hastings
related_concepts: []
sources:
- bishop-prml-ch11
- betancourt-short-2021
- cassandras-des-intro-ch07
- lange-applied-probability-ch07
- betancourt-a-2021
- livingstone-on-2016
specializes:
- markov-chains
tags:
- mcmc
- markov-chains
- convergence
- stationary-distribution
- detailed-balance
title: Ergodicity of Markov Chains (MCMC)
understanding: 0
uses:
- stationary-distribution
- detailed-balance
---

## Definition
A homogeneous Markov chain is **ergodic** if for any initial distribution $p(z^{(0)})$, the marginal distribution $p(z^{(m)})$ converges to a unique invariant (equilibrium) distribution $p^*(z)$ as $m \to \infty$:
$$\lim_{m\to\infty} p(z^{(m)}) = p^*(z).$$
A sufficient (not necessary) condition for ensuring $p^*$ is invariant is **detailed balance**:
$$p^*(z)\,T(z,z') = p^*(z')\,T(z',z).$$
Ergodicity additionally requires that the chain is irreducible (every state reachable from every other) and aperiodic.

### Why it matters
Ergodicity is the theoretical guarantee that MCMC samples eventually represent the target distribution regardless of initialisation, and that time averages equal ensemble averages. Practical consequences include requirements on step sizes and proposal supports: Metropolis-Hastings requires $q(z_A|z_B)>0$ for all $z_A,z_B$; Gibbs sampling requires no zero conditional probabilities. Diagnosing failures of ergodicity (e.g., multimodal trapping) is central to MCMC practice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[metropolis-hastings]] — prerequisite-of
- [[detailed-balance]] — uses
- [[stationary-distribution]] — uses
- [[markov-chains]] — specializes
[To be populated during integration]