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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
- machine-learning
id: pkis:technique:expected-sufficient-statistics-pgm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch04
tags:
- EM
- missing-data
- latent-variable
- sufficient-statistics
- family-marginal
title: Expected Sufficient Statistics (ESS) for EM in Graphical Models
understanding: 0
---

## Definition
In the EM algorithm for DPGMs with missing data, the E-step computes fractional counts
$$\bar{N}_{ijk} = \sum_{n=1}^N p(x_{ni}=k,\, x_{n,\text{pa}(i)}=j \mid \mathcal{D}_n, \theta^{\text{old}})$$
known as **family marginals**, by running a graphical model inference algorithm. The M-step then maximizes
$$\mathbb{E}[\log p(\mathcal{D}\mid\theta)] = \sum_i\sum_j\sum_k \bar{N}_{ijk}\log\theta_{ijk}$$
yielding $\hat{\theta}_{ijk} = \bar{N}_{ijk}/\sum_{k'}\bar{N}_{ijk'}$.

Replaces hard sufficient statistics with soft probabilistic expectations, coupling inference and learning in latent variable models.

### Why it matters
ESS-based EM is the standard method for learning DPGMs with hidden variables (e.g., HMMs, mixture models, factor graphs). Unlike SGD, each iteration guarantees monotone likelihood improvement; unlike complete-data MLE, it handles arbitrary patterns of missingness.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]