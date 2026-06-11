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
id: pkis:technique:baum-welch-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
- murphy-pml2-advanced-ch29
tags:
- HMM
- EM
- maximum-likelihood
- Baum-Welch
- training
title: Baum-Welch Algorithm (EM for HMM)
understanding: 0
---

## Definition
An instance of the EM algorithm for maximum-likelihood training of Hidden Markov Models:

**E step:** Run the forward-backward algorithm to compute $\gamma(z_{nk})=p(z_{nk}=1|X,\theta^{\text{old}})$ and $\xi(z_{n-1,j},z_{nk})=p(z_{n-1,j}=1,z_{nk}=1|X,\theta^{\text{old}})$.

**M step:**
$$\pi_k = \frac{\gamma(z_{1k})}{\sum_j\gamma(z_{1j})}, \quad A_{jk} = \frac{\sum_{n=2}^N \xi(z_{n-1,j},z_{nk})}{\sum_l\sum_{n=2}^N \xi(z_{n-1,j},z_{nl})}$$
Emission parameters $\varphi_k$ are re-estimated as weighted MLE with weights $\gamma(z_{nk})$.

The $Q$ function is $Q(\theta,\theta^{\text{old}})=\sum_Z p(Z|X,\theta^{\text{old}})\ln p(X,Z|\theta)$, which decomposes additively over $\pi$, $A$, and $\varphi$.

### Why it matters
Guarantees non-decreasing likelihood at each iteration and scales as $O(K^2N)$ per EM cycle. Multiple independent sequences are handled by summing $\gamma$ and $\xi$ statistics across sequences. The algorithm is the workhorse of HMM training in speech recognition, bioinformatics, and NLP.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]