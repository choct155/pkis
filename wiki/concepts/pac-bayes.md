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
- statistical-learning-theory
- deep-learning
- generalisation
id: pkis:concept:pac-bayes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- PAC-learning
- KL-divergence
- generalisation-bounds
- stochastic-networks
title: PAC-Bayes Generalisation Bounds
understanding: 0
---

## Definition
PAC-Bayes bounds provide distribution-free, non-vacuous upper bounds on the generalisation error of *stochastic* predictors. For any prior $P$ and any data-dependent posterior $Q$ over parameters, with probability at least $1-\delta$ over the draw of $N$ training points:
$$\text{gen-err}(Q) \leq \text{train-err}(Q) + \sqrt{\frac{D_{\text{KL}}(Q \| P) + c}{2(N-1)}}$$

### Why it matters
PAC-Bayes [McAllester 1999] is one of the few frameworks that can yield provably non-vacuous bounds for large neural networks by sampling predictions from a distribution $Q$. The bound trades off fit (training error) against complexity measured by $D_{\text{KL}}(Q\|P)$. Despite their theoretical appeal, current bounds are often loose and prescriptively limited: actions that tighten the bound (e.g., shrinking parameter count, using tight priors) do not always improve generalisation, and BMA over multimodal posteriors has only a logarithmic effect on the bound.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]