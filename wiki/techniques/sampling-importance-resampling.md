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
- rejection-sampling
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:technique:sampling-importance-resampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- particle-filter
related_concepts: []
sources:
- bishop-prml-ch11
tags:
- monte-carlo
- resampling
- importance-weights
- particle-filter
title: Sampling-Importance-Resampling (SIR)
understanding: 0
uses:
- importance-sampling
---

## Definition
Sampling-importance-resampling (SIR) approximates samples from a target $p(z)$ without requiring a bound constant $k$. It proceeds in two stages:
1. Draw $L$ samples $\{z^{(l)}\}$ from proposal $q(z)$ and compute normalised importance weights $w_l \propto \tilde{p}(z^{(l)})/\tilde{q}(z^{(l)})$.
2. Resample $L$ values from the discrete distribution $(z^{(1)},\ldots,z^{(L)})$ with probabilities $(w_1,\ldots,w_L)$.

In the limit $L\to\infty$, the resampled distribution converges to $p(z)$, as shown by the cumulative-distribution argument
$$p(z\leq a) = \frac{\int I(z\leq a)p(z)\,dz}{\int p(z)\,dz}.$$
For finite $L$, accuracy improves as $q \to p$.

### Why it matters
SIR is a principled alternative to rejection sampling that avoids the need to determine a global envelope constant, making it more practical for complex multivariate distributions. It forms the theoretical core of bootstrap particle filters and sequential Monte Carlo algorithms.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[particle-filter]] — prerequisite-of
- [[rejection-sampling]] — contrasts-with
- [[importance-sampling]] — uses
[To be populated during integration]