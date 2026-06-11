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
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:concept:beta-binomial-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch04
tags:
- conjugate-prior
- Beta-distribution
- Bernoulli
- Bayesian-updating
- add-one-smoothing
title: Beta-Binomial Conjugate Model
understanding: 0
---

## Definition
$$p(\theta|\mathcal{D}) = \text{Beta}(\theta|\tilde{\alpha}+N_1,\, \tilde{\beta}+N_0)$$

where $N_1, N_0$ are the observed counts of heads/tails and $(\tilde{\alpha}, \tilde{\beta})$ are the prior pseudo-counts. The Beta prior is conjugate to the Bernoulli/Binomial likelihood, so Bayesian updating reduces to adding observed counts to pseudo-counts.

### Why it matters
The beta-binomial model is the canonical example of conjugate Bayesian inference: the posterior has a closed form, the prior strength $\tilde{N} = \tilde{\alpha}+\tilde{\beta}$ acts as an **equivalent sample size**, and the posterior mean $\hat{\theta} = (\tilde{\alpha}+N_1)/(\tilde{N}+N)$ interpolates between the prior mean $\tilde{\alpha}/\tilde{N}$ and the MLE $N_1/N$. Setting $\tilde{\alpha}=\tilde{\beta}=1$ gives a uniform prior; setting $\tilde{\alpha}=\tilde{\beta}=2$ gives **add-one smoothing** (MAP estimate = $(N_1+1)/(N+2)$), which avoids the zero-count problem.

### Predictive distribution
The posterior predictive probability of the next coin toss being heads is $p(\tilde{y}=1|\mathcal{D}) = (\tilde{\alpha}+N_1)/(\tilde{N}+N)$, equal to the posterior mean.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]