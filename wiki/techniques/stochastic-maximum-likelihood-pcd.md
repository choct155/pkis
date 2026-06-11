---
aliases: []
also_type: []
applies:
- restricted-boltzmann-machine
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- spurious-modes
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- probabilistic-graphical-models
extends:
- contrastive-divergence
id: pkis:technique:stochastic-maximum-likelihood-pcd
instantiates:
- positive-negative-phase-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
tags:
- RBM
- undirected-models
- partition-function
- persistent-MCMC
- training-algorithm
title: Stochastic Maximum Likelihood / Persistent Contrastive Divergence
understanding: 0
uses:
- gibbs-sampler
---

## Definition
**Stochastic Maximum Likelihood (SML)** (Younes, 1998), independently rediscovered as **Persistent Contrastive Divergence (PCD-$k$)** (Tieleman, 2008), trains undirected models by maintaining a persistent set of fantasy particles $\{\tilde{x}^{(j)}\}$ across gradient steps. Rather than reinitializing chains at data or at random, chains are carried over between updates:
$$\tilde{x}^{(j)} \leftarrow \text{gibbs\_update}^k(\tilde{x}^{(j)}_{\text{prev}}),$$
and the negative phase gradient is computed from these persistent samples. The rationale is that for small learning-rate steps, consecutive model distributions are nearly identical, so persistent chains stay approximately stationary.

### Why it matters
SML/PCD avoids the spurious-mode failure mode of CD because persistent chains can wander to all modes of the model distribution over many gradient steps. It also naturally handles latent variables (providing initialization for both visible and hidden units), making it more suitable for deep models. Empirically (Marlin et al., 2010), it achieves better test log-likelihood and downstream classification accuracy than CD for RBMs. The key vulnerability is chain lag when learning rate or model change is too fast relative to $k$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[restricted-boltzmann-machine]] — applies
- [[gibbs-sampler]] — uses
- [[spurious-modes]] — contrasts-with
- [[contrastive-divergence]] — extends
- [[positive-negative-phase-learning]] — instantiates
[To be populated during integration]