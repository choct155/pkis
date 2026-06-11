---
aliases: []
also_type: []
analogous-to:
- partial-pooling-shrinkage
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
date_updated: '2026-06-11'
domain:
- bayesian-statistics
- statistics
id: pkis:concept:equivalent-sample-size
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
tags:
- prior-strength
- pseudo-counts
- hyperparameters
- shrinkage
- beta-distribution
title: Equivalent Sample Size (Prior Strength)
understanding: 0
uses:
- conjugate-prior
- beta-distribution
---

## Definition
The **equivalent sample size** of a prior is the number of real data observations the prior is worth in terms of its influence on the posterior. For a $\text{Beta}(\tilde{\alpha},\tilde{\beta})$ prior on a Bernoulli parameter, the equivalent sample size is $\tilde{N}=\tilde{\alpha}+\tilde{\beta}$. The posterior mean is:
$$E[\theta|D]=\frac{\tilde{N}}{N+\tilde{N}}\cdot m + \frac{N}{N+\tilde{N}}\cdot\hat{\theta}_{\text{MLE}}$$
where $m=\tilde{\alpha}/\tilde{N}$ is the prior mean. As $N\gg\tilde{N}$, the posterior approaches the MLE.

### Why it matters
The equivalent sample size provides an intuitive scale for setting hyperparameters: a $\text{Beta}(2,2)$ prior is worth about 4 'pseudo-observations'. It makes explicit the shrinkage towards the prior and facilitates comparison across different models and datasets.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partial-pooling-shrinkage]] — analogous-to
- [[beta-distribution]] — uses
- [[conjugate-prior]] — uses
[To be populated during integration]