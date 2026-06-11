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
- information-theory
- machine-learning
id: pkis:concept:cross-entropy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
tags:
- entropy
- divergence
- loss-function
- compression
title: Cross Entropy
understanding: 0
---

## Definition
$$\mathbb{H}_{ce}(p, q) \triangleq -\sum_{k=1}^{K} p_k \log q_k$$

The expected number of bits required to encode samples drawn from distribution $p$ when using a code optimised for distribution $q$; minimised (to the Shannon entropy $\mathbb{H}(p)$) when $q = p$.

### Why it matters
Cross entropy decomposes as $\mathbb{H}_{ce}(p,q) = \mathbb{H}(p) + D_{\mathrm{KL}}(p\|q)$, revealing that minimising it over $q$ is equivalent to minimising KL divergence. As the `cross-entropy-loss` used in classification directly corresponds to $\mathbb{H}_{ce}(p_{\mathcal{D}}, q_\theta)$, this relationship gives maximum-likelihood training a clean information-theoretic interpretation: reduce the extra bits wasted by mis-specifying the model distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]