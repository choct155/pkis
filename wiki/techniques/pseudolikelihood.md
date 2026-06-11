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
- machine-learning
- probabilistic-graphical-models
- statistics
id: pkis:technique:pseudolikelihood
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
tags:
- undirected-models
- partition-function
- conditional-likelihood
- consistent-estimator
title: Pseudolikelihood
understanding: 0
---

## Definition
**Pseudolikelihood** (Besag, 1975) replaces the intractable joint log-likelihood with a sum of tractable conditional log-likelihoods, one per variable conditioned on all others:
$$\text{PL}(\theta) = \sum_{i=1}^{n} \log p(x_i \mid \mathbf{x}_{-i};\theta).$$
Each conditional $p(x_i \mid \mathbf{x}_{-i})$ is computed as a ratio $\tilde{p}(x_i,\mathbf{x}_{-i})/\sum_{x_i'}\tilde{p}(x_i',\mathbf{x}_{-i})$, cancelling the partition function. This requires only $k \times n$ evaluations of $\tilde{p}$ (where $k$ is the cardinality of each variable) versus $k^n$ for the full partition function.

### Why it matters
Pseudolikelihood is **asymptotically consistent** (Mase, 1995) and computationally efficient. It works well for conditional prediction tasks but poorly for full joint density estimation or sampling, since it does not directly optimize the joint model. A **generalized pseudolikelihood** (Huang & Ogata, 2002) interpolates between pseudolikelihood ($m=n$ singleton sets) and full likelihood ($m=1$, all variables), allowing a trade-off between cost and quality. Pseudolikelihood cannot be used with variational lower bounds on $\tilde{p}$, limiting its applicability to deep models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]