---
aliases: []
also_type: []
applies:
- principal-components-analysis
- autoencoder
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
- machine-learning
- linear-algebra
id: pkis:result:linear-autoencoder-pca-equivalence
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch20
tags:
- pca
- autoencoders
- theoretical-result
- reconstruction-error
- neural-networks
title: Equivalence of Linear Autoencoder and PCA
understanding: 0
---

## Definition
A linear autoencoder $\hat{x} = W_2 W_1 x$ trained to minimise squared reconstruction error $\sum_n \|x_n - W_2 W_1 x_n\|^2$ learns a weight matrix $\hat{W} = W_2 W_1$ that is an orthogonal projection onto the span of the top-$L$ eigenvectors of the empirical covariance $\hat{\Sigma}$—identical to the PCA solution.

### Why it matters
This result (Baldi & Hornik 1989; Krogh & Hertz 1995) establishes that PCA is the unique global minimiser of the linear autoencoder objective, and that introducing nonlinearities strictly increases representational power beyond PCA. It justifies using PCA as the linear baseline and motivates deep nonlinear autoencoders.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[autoencoder]] — applies
- [[principal-components-analysis]] — applies
[To be populated during integration]