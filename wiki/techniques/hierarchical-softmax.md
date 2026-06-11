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
- NLP
- deep-learning
- computational-efficiency
id: pkis:technique:hierarchical-softmax
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
- murphy-pml1-intro-ch10
tags:
- language-model
- vocabulary
- softmax
- efficiency
- NLP
title: Hierarchical Softmax
understanding: 0
---

## Definition
Hierarchical softmax organises the vocabulary $\mathcal{V}$ as the leaves of a binary tree of depth $O(\log|\mathcal{V}|)$ and factorises the output probability as a product of binary decisions along the path from root to leaf:
$$P(w \mid C) = \prod_{\ell=1}^{L(w)} \sigma\!\bigl(\!\left[\![n(w,\ell+1) = \text{left}(n(w,\ell))\right]\!\bigr]\cdot \mathbf{v}_{n(w,\ell)}^\top \mathbf{h}\bigr),$$
where $L(w)$ is the path length and $\sigma$ is the logistic function. Training and inference cost reduce from $O(|\mathcal{V}|\, n_h)$ to $O(n_b\, n_h)$ with $n_b = O(\log|\mathcal{V}|)$.

### Why it matters
Addresses the computational bottleneck of large-vocabulary output layers in neural language models; provides exact normalised probabilities (unlike noise-contrastive estimation) at reduced cost and is still used in specialised settings such as word2vec.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]