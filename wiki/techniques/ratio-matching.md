---
aliases: []
also_type: []
analogous-to:
- pseudolikelihood
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- partition-function
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- probabilistic-graphical-models
extends:
- score-matching
id: pkis:technique:ratio-matching
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
tags:
- undirected-models
- partition-function
- binary-data
- energy-based-models
- consistent-estimator
title: Ratio Matching
understanding: 0
---

## Definition
**Ratio Matching** (Hyvärinen, 2007b) extends the partition-function-free training idea to **binary discrete data** by minimizing, over examples $x$, the objective:
$$L^{(\text{RM})}(x,\theta) = \sum_{j=1}^{n}\left(\frac{1}{1 + \dfrac{p_{\text{model}}(x;\theta)}{p_{\text{model}}(f(x,j);\theta)}}\right)^2,$$
where $f(x,j)$ flips bit $j$ of $x$. The ratio of model probabilities cancels $Z$. Like pseudolikelihood, it requires $O(n)$ evaluations of $\tilde{p}$ per example (vs. $O(k^n)$ for the full partition function).

### Why it matters
Ratio matching addresses the failure of score matching (which requires continuous $x$) and generalized score matching (which fails in high-dimensional sparse discrete spaces) on binary data. Empirically (Marlin et al., 2010), ratio matching outperforms SML, pseudolikelihood, and generalized score matching on image denoising. It also motivates stochastic approximations for sparse high-dimensional data (e.g., word counts). Conceptually, it suppresses all fantasy states within Hamming distance 1 of each training example.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partition-function]] — contrasts-with
- [[pseudolikelihood]] — analogous-to
- [[score-matching]] — extends
[To be populated during integration]