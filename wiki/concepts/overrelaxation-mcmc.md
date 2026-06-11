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
contrasts-with:
- random-walk-behaviour-mcmc
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
extends:
- gibbs-sampling
id: pkis:concept:overrelaxation-mcmc
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch11
tags:
- mcmc
- gibbs-sampling
- mixing
- correlated-variables
title: Overrelaxation (MCMC)
understanding: 0
---

## Definition
In overrelaxation, the Gibbs sampling update for variable $z_i$ with conditional mean $\mu_i$ and variance $\sigma_i^2$ is replaced by
$$z_i' = \mu_i + \alpha(z_i - \mu_i) + \sigma_i(1-\alpha^2)^{1/2}\nu, \quad \nu \sim \mathcal{N}(0,1),$$
where $-1 < \alpha < 1$. For $\alpha = 0$ this reduces to standard Gibbs sampling; for $\alpha < 0$ the update is biased toward the opposite side of the mean, encouraging directed motion.

### Why it matters
Overrelaxation reduces the random-walk character of Gibbs sampling in highly correlated distributions by introducing anti-correlated consecutive steps, improving mixing. The ordered overrelaxation generalisation (Neal, 1999) extends the idea to non-Gaussian conditionals.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[random-walk-behaviour-mcmc]] — contrasts-with
- [[gibbs-sampling]] — extends
[To be populated during integration]