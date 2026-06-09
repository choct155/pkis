---
aliases: []
also_type: []
applies:
- metropolis-algorithm
- gibbs-sampler
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:principle:detailed-balance
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- mcmc
related_concepts: []
sources:
- mackay-itila-ch29
specializes:
- stationary-distribution
tags:
- mcmc
- markov-chain
- invariant-distribution
- reversibility
- mackay
title: Detailed Balance
understanding: 0
---

## Definition
Detailed balance is the central design condition for proving that a Markov chain Monte Carlo method converges to its target $P(x)$. A transition probability $T(x';x)$ satisfies detailed balance with respect to $P$ if
$$T(x_a;x_b)\,P(x_b) = T(x_b;x_a)\,P(x_a)\quad\text{for all }x_a,x_b.$$
In words: at equilibrium, the probability flux from $x_b$ to $x_a$ exactly matches the reverse flux. Chains satisfying it are called **reversible**.

### Detailed balance implies invariance
Summing (integrating) both sides over $x_b$ shows that $P$ is an *invariant* (stationary) distribution of $T$: $P(x')=\int d^N x\, T(x';x)P(x)$. Invariance — $P$ being a fixed point, an eigenvector of $T$ with eigenvalue 1 — is the property MCMC ultimately needs; detailed balance is a convenient *sufficient* way to guarantee it, and the Metropolis method and Gibbs sampling both satisfy it.

### Sufficient, not necessary
Detailed balance is not required for correct MCMC. Concatenating two base transitions that each satisfy detailed balance need not yield a chain that does, yet the composite can still preserve invariance. Irreversible chains that violate detailed balance can be deliberately useful, since they may have better random-walk (mixing) properties.

### Why it matters
Proving detailed balance is the standard route to validating a new sampler. Together with **ergodicity** (the chain must reach all of $P$'s support and avoid periodicity), it guarantees that $p^{(t)}(x)\to P(x)$ as $t\to\infty$, the convergence guarantee underpinning all of MCMC.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stationary-distribution]] — specializes: detailed balance is a sufficient (reversibility) condition for a distribution to be stationary
- [[gibbs-sampler]] — applies: Gibbs conditional updates leave P invariant via detailed balance of each base transition.
- [[metropolis-algorithm]] — applies: The Metropolis acceptance rule is constructed to satisfy detailed balance.
- [[mcmc]] — prerequisite-of: Detailed balance is the standard sufficient condition for the target to be the chain's invariant distribution.
[To be populated during integration]