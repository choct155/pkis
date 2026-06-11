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
- maximum-likelihood-estimation
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- bayesian-statistics
- machine-learning
- natural-language-processing
generalizes:
- beta-binomial-distribution
id: pkis:technique:dirichlet-categorical-conjugate
instantiates:
- conjugate-prior
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
tags:
- Dirichlet
- categorical
- multinomial
- conjugate-prior
- add-one-smoothing
title: Conjugate Bayesian Analysis for the Dirichlet-Categorical (Multinomial) Model
understanding: 0
uses:
- dirichlet-distribution
- marginal-likelihood
---

## Definition
For observations $y_n\sim\text{Cat}(\theta)$ with $K$ categories, the likelihood is:
$$p(D|\theta)=\prod_{k=1}^K \theta_k^{N_k}$$
The conjugate prior is $p(\theta)=\text{Dir}(\theta|\bar{\alpha})$, yielding the posterior:
$$p(\theta|D)=\text{Dir}\bigl(\theta\mid\bar{\alpha}_1+N_1,\ldots,\bar{\alpha}_K+N_K\bigr)$$
The posterior mode (MAP) is $\hat{\theta}_k=(N_k+\bar{\alpha}_k-1)/(N+\sum_k\bar{\alpha}_k-K)$; with $\bar{\alpha}_k=2$ this gives **add-one smoothing**. The marginal likelihood is:
$$p(D)=\frac{B(N+\bar{\alpha})}{B(\bar{\alpha})}=\frac{\Gamma(\sum_k\bar{\alpha}_k)}{\Gamma(N+\sum_k\bar{\alpha}_k)}\prod_k\frac{\Gamma(N_k+\bar{\alpha}_k)}{\Gamma(\bar{\alpha}_k)}$$

### Why it matters
This model underpins Bayesian language models (Dirichlet-language models, LDA topic models), naive Bayes classifiers, and any categorical data analysis. The closed-form posterior makes inference $O(K)$ and the marginal likelihood enables Bayesian model selection.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-likelihood-estimation]] — contrasts-with
- [[marginal-likelihood]] — uses
- [[beta-binomial-distribution]] — generalizes
- [[dirichlet-distribution]] — uses
- [[conjugate-prior]] — instantiates
[To be populated during integration]