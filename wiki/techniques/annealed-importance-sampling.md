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
- statistics
- probabilistic-graphical-models
id: pkis:technique:annealed-importance-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
- murphy-pml2-advanced-ch11
tags:
- partition-function
- importance-sampling
- model-evaluation
- RBM
- Monte-Carlo
title: Annealed Importance Sampling (AIS)
understanding: 0
---

## Definition
**Annealed Importance Sampling** (AIS; Jarzynski 1997; Neal 2001) estimates the ratio of partition functions $Z_1/Z_0$ by introducing a sequence of intermediate distributions $p_{\eta_0}, \ldots, p_{\eta_n}$ (with $\eta_0=0$, $\eta_n=1$) bridging a tractable base $p_0$ (known $Z_0$) to the target $p_1$. A common choice is the geometric average: $p_{\eta_j} \propto p_1^{\eta_j} p_0^{1-\eta_j}$. Importance weights are accumulated across the annealing sequence:
$$w^{(k)} = \prod_{j=0}^{n-1}\frac{\tilde{p}_{\eta_{j+1}}(x_{\eta_{j+1}}^{(k)})}{\tilde{p}_{\eta_j}(x_{\eta_{j+1}}^{(k)})}, \quad \frac{Z_1}{Z_0} \approx \frac{1}{K}\sum_k w^{(k)}.$$
AIS is formally valid as importance sampling on an extended state space (Neal, 2001).

### Why it matters
AIS is the **standard method** for evaluating partition functions of undirected deep generative models (e.g., RBMs, DBNs; Salakhutdinov & Murray, 2008). It enables rigorous model comparison by log-likelihood when the partition function is otherwise intractable. Combining AIS with parallel tempering (Desjardins et al., 2011) allows partition function tracking during training. The method degrades gracefully when intermediate distributions are well-chosen: many intermediate steps reduce variance at the cost of computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]