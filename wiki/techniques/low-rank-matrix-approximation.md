---
aliases: []
also_type: []
applies:
- principal-component-analysis
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:low-rank-matrix-approximation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch04
tags: []
title: Low-Rank Matrix Approximation
understanding: 0
uses:
- singular-value-decomposition
---

## Definition
$$\hat{A}(k) := \sum_{i=1}^{k} \sigma_i u_i v_i^{\top}, \qquad \big\|A-\hat{A}(k)\big\|_2 = \sigma_{k+1}$$

Low-rank approximation replaces a rank-$r$ matrix $A$ with a rank-$k$ matrix ($k<r$) by truncating its SVD to the $k$ largest singular values, yielding the provably optimal approximation in the spectral norm.

### Construction from the SVD
The SVD expands $A=\sum_{i=1}^{r}\sigma_i u_i v_i^\top$ as a weighted sum of rank-1 outer products $A_i=u_i v_i^\top$, ordered by descending singular value. Keeping only the top $k$ terms gives $\hat{A}(k)$. Because the $\sigma_i$ measure each component's contribution, dropping the smallest discards the least information — a form of lossy compression. Storing $\hat{A}(k)$ needs only $k(m+n+1)$ numbers instead of $mn$.

### Eckart-Young optimality
The **Eckart-Young theorem** states $\hat{A}(k)=\arg\min_{\mathrm{rk}(B)=k}\|A-B\|_2$, with residual exactly $\sigma_{k+1}$. No rank-$k$ matrix approximates $A$ better in spectral norm. Geometrically, $\hat{A}(k)$ is the projection of $A$ onto the space of rank-$\le k$ matrices; the proof rests on the rank-nullity theorem.

### Why it matters
Low-rank approximation turns the SVD into a compression and denoising engine: image compression, noise filtering, regularization of ill-posed problems, recommender-system completion of matrices with missing entries, topic modeling, and — most importantly — dimensionality reduction and PCA, where retaining top components captures the directions of greatest data variability at minimal cost.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[principal-component-analysis]] — applies
- [[singular-value-decomposition]] — uses
[To be populated during integration]