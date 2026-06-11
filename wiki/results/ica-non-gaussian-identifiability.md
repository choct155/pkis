---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- signal-processing
- machine-learning
id: pkis:result:ica-non-gaussian-identifiability
instantiates:
- identifiability-of-mixtures
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch13
tags:
- identifiability
- blind-source-separation
- non-gaussian
- information-theory
title: ICA Non-Gaussian Identifiability
understanding: 0
uses:
- independent-component-analysis
- gaussian-distribution
---

## Definition
**Theorem (Comon 1994):** In the linear model $\mathbf{x} = \mathbf{W}\mathbf{h}$ with independent components, the mixing matrix $\mathbf{W}$ is identifiable (up to permutation and scaling of columns) if and only if at most one component $h_i$ has a Gaussian distribution.

### Why it matters
This result is the theoretical cornerstone of ICA: the Gaussian distribution is the unique distribution that is invariant under orthogonal transformations with independent marginals. If all components were Gaussian, any rotation of $\mathbf{W}$ would produce an equally valid factorisation, making the model unidentifiable. Requiring non-Gaussian (typically super-Gaussian / sparse) priors is therefore not merely a modelling choice but a mathematical necessity for source separation.

### Contrast with PCA
PCA finds orthogonal directions maximising variance and decorrelates sources, but cannot achieve statistical independence; ICA goes further by exploiting higher-order statistics to resolve the remaining rotational ambiguity left by PCA.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-distribution]] — uses
- [[identifiability-of-mixtures]] — instantiates
- [[independent-component-analysis]] — uses
[To be populated during integration]