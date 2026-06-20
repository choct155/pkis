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
- importance-sampling
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- statistics
- machine-learning
- probability
id: pkis:technique:metropolis-hastings-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
- kroese-statistical-modeling-ch07
specializes:
- mcmc
- metropolis-hastings
tags:
- mcmc
- bayesian-inference
- sampling
- markov-chain
- acceptance-rejection
title: Metropolis-Hastings Algorithm
understanding: 0
uses:
- detailed-balance
- stationary-distribution
- markov-chains
---

## Definition
$$x^{s+1} = \begin{cases} x' & \text{if } u \leq \min\!\left(1,\, \frac{\tilde{p}(x')\,q(x|x')}{\tilde{p}(x)\,q(x'|x)}\right) \\ x^s & \text{otherwise} \end{cases}$$

where $x' \sim q(x'|x)$ is a proposed move and $u \sim U(0,1)$. A general-purpose MCMC algorithm that constructs an ergodic Markov chain whose stationary distribution equals the target $p^*(x)$ by accepting or rejecting proposed moves according to the Hastings ratio, allowing sampling from any distribution known only up to a normalising constant.

### Why it matters
The $Z$-cancellation in the acceptance ratio $\alpha = \tilde{p}(x')q(x|x')/[\tilde{p}(x)q(x'|x)]$ means the algorithm requires only an unnormalised density — the key enabler of Bayesian posterior sampling. Correctness follows from detailed balance (Theorem 12.2.1): the MH transition kernel satisfies $p^*(x)p(x'|x) = p^*(x')p(x|x')$, guaranteeing $p^*$ is the unique invariant distribution when the chain is ergodic and irreducible.

### Key design choices
Proposal validity requires $q(x'|x)>0$ for all $x'$ in the support of $p^*$. Symmetric proposals ($q(x'|x)=q(x|x')$) simplify to the Metropolis ratio $p^*(x')/p^*(x)$. Asymmetric proposals require the Hastings correction. Common instantiations include the random walk Metropolis (Gaussian proposal) and the independence sampler.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[importance-sampling]] — contrasts-with: independence sampler is the MH analogue of importance sampling
- [[metropolis-hastings]] — specializes: metropolis-hastings is the existing node; this new node provides the full algorithmic treatment
- [[markov-chains]] — uses
- [[stationary-distribution]] — uses
- [[detailed-balance]] — uses
- [[mcmc]] — specializes
[To be populated during integration]