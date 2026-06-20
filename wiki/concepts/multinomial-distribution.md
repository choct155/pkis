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
date_updated: '2026-06-20'
domain:
- probability
- statistics
- machine-learning
generalizes:
- bernoulli-distribution
id: pkis:concept:multinomial-distribution
instantiates:
- exponential-family-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
- kroese-statistical-modeling-ch03
tags:
- discrete-distribution
- categorical
- exponential-family
- sufficient-statistics
title: Multinomial Distribution
understanding: 0
uses:
- dirichlet-distribution
- sufficient-statistics
---

## Definition
$$\text{Mult}(m_1,\ldots,m_K|\boldsymbol{\mu},N) = \binom{N}{m_1\cdots m_K}\prod_{k=1}^K \mu_k^{m_k}$$

where $\binom{N}{m_1\cdots m_K}=N!/(m_1!\cdots m_K!)$, $\mu_k\ge 0$, $\sum_k\mu_k=1$, and $\sum_k m_k=N$. Generalises the binomial to $K>2$ mutually exclusive outcomes; uses the 1-of-$K$ (one-hot) encoding so that $p(\mathbf{x}|\boldsymbol{\mu})=\prod_k \mu_k^{x_k}$.

### Why it matters
The multinomial is the canonical likelihood for categorical data: document word counts, class labels, and next-token prediction in language models all use this family. Its sufficient statistics are the per-category counts $m_k=\sum_n x_{nk}$. Maximum likelihood gives $\hat{\mu}_k = m_k/N$. The Dirichlet distribution is its conjugate prior, enabling closed-form Bayesian inference and the posterior-predictive smoothing used in language-model smoothing.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sufficient-statistics]] — uses: Counts m_k are sufficient statistics for multinomial likelihood
- [[exponential-family-distribution]] — instantiates: Natural parameters eta_k=log(mu_k), sufficient statistics m_k
- [[dirichlet-distribution]] — uses: Dirichlet is conjugate prior for multinomial parameters
- [[bernoulli-distribution]] — generalizes: Multinomial reduces to Bernoulli/Binomial for K=2
[To be populated during integration]