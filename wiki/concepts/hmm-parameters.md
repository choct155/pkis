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
- probabilistic-graphical-models
id: pkis:concept:hmm-parameters
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
tags:
- HMM
- transition-matrix
- emission
- parameters
title: HMM Transition and Emission Parameters
understanding: 0
---

## Definition
The parameters of an HMM $\theta = \{\pi, A, \varphi\}$ consist of:
- **Initial state probabilities** $\pi_k = p(z_{1k}=1)$, $\sum_k \pi_k=1$.
- **Transition matrix** $A_{jk} = p(z_{nk}=1\mid z_{n-1,j}=1)$, with $K(K-1)$ free parameters, written $p(z_n|z_{n-1},A)=\prod_j\prod_k A_{jk}^{z_{n-1,j}\,z_{nk}}$.
- **Emission parameters** $\varphi$, determining $p(x_n|z_n,\varphi)=\prod_k p(x_n|\varphi_k)^{z_{nk}}$ (Gaussian, discrete table, mixture, etc.).

Together they completely specify the generative process: sample $z_1\sim\pi$, emit $x_1\sim p(x|z_1)$, then propagate $z_n|z_{n-1}\sim A$ and emit $x_n$.

### Why it matters
The clean separation of transition and emission parameters allows the Baum-Welch M-step to decouple: $\pi$ and $A$ are updated by normalized counts of $\gamma(z_{1k})$ and $\xi(z_{n-1,j},z_{nk})$, while $\varphi_k$ is updated as a weighted maximum-likelihood problem with weights $\gamma(z_{nk})$—identical in form to mixture-model re-estimation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]