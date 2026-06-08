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
id: pkis:technique:overrelaxation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch30
tags:
- MCMC
- Gibbs-sampling
- random-walk-suppression
- detailed-balance
- Adler
- Neal
title: Overrelaxation
understanding: 0
---

## Definition
Overrelaxation is a modification of Gibbs sampling that suppresses random-walk behaviour by biasing each coordinate update to the *opposite* side of its conditional distribution, producing directed rather than diffusive motion. In **Adler's (1981) method**, valid when the conditional of $x_i$ is $\mathrm{Normal}(\mu,\sigma^2)$, the update is

$$x_i^{(t+1)} = \mu + \alpha\,(x_i^{(t)} - \mu) + (1-\alpha^2)^{1/2}\sigma\,\nu, \qquad \nu \sim \mathrm{Normal}(0,1),$$

with $\alpha \in (-1,1)$ usually negative. Each single-coordinate transition leaves the conditional invariant ($\alpha = 0$ recovers plain Gibbs).

### Temporal asymmetry is the trick
A full sweep over coordinates in fixed order does **not** satisfy detailed balance even though each individual update does; the chain is non-reversible. This temporal asymmetry is precisely what lets positively-correlated variables evolve in a directed manner along their correlation axis instead of random-walking. Randomizing the update order destroys the benefit.

### Ordered overrelaxation (Neal 1995)
Generalizes the idea to *any* Gibbs-samplable system. Draw $K$ samples from the conditional, sort them together with the current value, find the current value's rank $\kappa$ in the list of $K+1$ points, and replace it with the point of rank $K-\kappa$ (its mirror image). $K$ plays the role of Adler's $\alpha$; $K=1$ is ordinary Gibbs. Often the extra samples cost almost nothing.

### Why it matters
Where applicable, overrelaxation can speed convergence by a factor of ten or twenty over Gibbs sampling without requiring gradients, by converting $\sqrt{t}$ diffusion into directed exploration.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]