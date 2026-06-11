---
aliases: []
also_type: []
applies:
- gaussian-mixture-model
- mixture-models
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
- machine-learning
- statistics
id: pkis:concept:cluster-responsibility
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- em-algorithm
related_concepts: []
sources:
- murphy-pml1-intro-ch03
tags:
- mixture-models
- EM-algorithm
- clustering
- latent-variables
title: Cluster Responsibility (Soft Assignment)
understanding: 0
---

## Definition
In a mixture model with $K$ components, the **responsibility** of component $k$ for observation $n$ is the posterior probability:
$$r_{nk} \triangleq p(z_n = k | \mathbf{y}_n, \boldsymbol{\theta}) = \frac{\pi_k\, p(\mathbf{y}_n|\boldsymbol{\theta}_k)}{\sum_{k'=1}^K \pi_{k'} p(\mathbf{y}_n|\boldsymbol{\theta}_{k'})}$$

Responsibilities are fractional, non-negative, and sum to 1 over $k$; they form the E-step of EM for mixture models.

### Why it matters
Responsibilities provide **soft clustering**: each point contributes to every cluster proportionally to its posterior probability. Taking $\hat{z}_n = \arg\max_k r_{nk}$ yields **hard clustering**. In the EM algorithm, responsibilities are the sufficient statistics needed to update the model parameters, making them the central quantity linking latent variable models to parameter estimation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mixture-models]] — applies
- [[em-algorithm]] — prerequisite-of
- [[gaussian-mixture-model]] — applies
[To be populated during integration]