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
- mcmc
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:rejection-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch29
tags:
- monte-carlo
- sampling
- proposal-density
- exact-sampling
- mackay
title: Rejection Sampling
understanding: 0
---

## Definition
Rejection sampling generates **independent, exact** samples from a target $P(x)=P^*(x)/Z$ using a simpler proposal $Q(x)$ from which we can sample and a constant $c$ that envelopes the target:
$$c\,Q^*(x) \ge P^*(x)\quad\text{for all }x.$$
The procedure: (1) draw $x\sim Q$; (2) draw $u\sim\text{Uniform}(0,\,c\,Q^*(x))$; (3) accept $x$ if $u \le P^*(x)$, else reject and retry.

### Why it produces exact samples
The pair $(x,u)$ is uniform over the area under $c\,Q^*$. Keeping only points with $u\le P^*(x)$ leaves points uniform over the area under $P^*$, so the accepted $x$-coordinates are distributed exactly as $P(x)$. No bias, no weighting — unlike importance sampling.

### Failure in high dimensions
The acceptance rate equals the ratio of volumes under $P$ and $cQ$, i.e. $1/c$. For two $N$-dimensional Gaussians whose widths differ by just 1% ($\sigma_Q/\sigma_P=1.01$), the enveloping constant is $c=\exp(N\ln(\sigma_Q/\sigma_P))$, which for $N=1000$ gives $c\approx 20{,}000$ and an acceptance rate of $1/20{,}000$. Since $c$ grows exponentially in $N$, acceptance is exponentially rare.

### Why it matters
Rejection sampling is the gold standard in one dimension — exact and i.i.d. — but its exponential inefficiency in high dimensions is precisely the gap that Markov chain methods (Metropolis, Gibbs) are designed to close by abandoning the demand for independent draws.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc]] — contrasts-with: Rejection produces independent samples but fails exponentially in N; MCMC trades independence for tractable high-dimensional mixing.
- [[importance-sampling]] — contrasts-with: Rejection sampling yields exact i.i.d. samples; importance sampling yields weighted, biased-at-finite-R estimates.
[To be populated during integration]