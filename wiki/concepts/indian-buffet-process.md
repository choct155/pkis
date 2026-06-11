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
- machine-learning
- statistics
- probability
id: pkis:concept:indian-buffet-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- indian-buffet-process
- feature-allocation
- latent-features
- nonparametric-bayes
- infinite-factorial-model
title: Indian Buffet Process
understanding: 0
---

## Definition
The Indian Buffet Process (IBP) with parameter $\alpha>0$ is a distribution over infinite binary matrices $\mathbf{Z}\in\{0,1\}^{N\times\infty}$ describing which of infinitely many latent features each of $N$ objects possesses. The sequential construction: customer $n$ takes dish $k$ previously sampled with probability $m_k/n$ (where $m_k$ is prior count), and samples $\mathrm{Poisson}(\alpha/n)$ new dishes.

The IBP is to feature allocation what the CRP is to clustering: an exchangeable prior over binary feature assignments with an unbounded number of features.

### Why it matters
The IBP serves as the prior in infinite latent feature models (e.g., infinite ICA, infinite factor analysis), letting the posterior determine the number of relevant features rather than fixing it in advance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]