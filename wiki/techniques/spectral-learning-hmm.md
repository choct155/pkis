---
aliases: []
also_type: []
applies:
- hidden-markov-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- baum-welch-algorithm
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:spectral-learning-hmm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
tags:
- HMM
- spectral-methods
- method-of-moments
- tensor-decomposition
- identifiability
title: Spectral Learning for HMMs
understanding: 0
uses:
- predictive-state-representations
- singular-value-decomposition
- tensor-decompositions
---

## Definition
A method for estimating HMM parameters by working directly with predictive state representations in observable space, avoiding the non-convex likelihood of EM. The key observation is that the matrix of pairwise co-occurrence counts $[P_2]_{ij} = p(y_t = i, y_{t-1} = j)$ has rank $\leq m$ (the number of hidden states), and a basis for this subspace is recovered via SVD. Third-order statistics $[P_3]_{ijk} = p(y_t=i, y_{t-1}=j, y_{t-2}=k)$ enable tensor decomposition to recover the model operators:

$$\hat{\mathbf{A}},\hat{\mathbf{B}} = \text{TensorDecompose}(P_2, P_3)$$

This yields consistent parameter estimates with provable sample complexity guarantees under mild identifiability conditions.

### Why it matters
Spectral methods provide globally consistent estimates free from local optima, in contrast to EM/SGD. They are especially useful for initializing EM or as standalone estimators when the number of hidden states is known. The approach extends to other latent variable models (LDA, mixture models) via method-of-moments.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[baum-welch-algorithm]] — contrasts-with
- [[tensor-decompositions]] — uses
- [[singular-value-decomposition]] — uses
- [[predictive-state-representations]] — uses
- [[hidden-markov-model]] — applies
[To be populated during integration]