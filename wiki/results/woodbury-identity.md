---
aliases: []
also_type: []
applies:
- bayesian-linear-regression
- gaussian-process-regression
- kalman-filter
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
- linear-algebra
- machine-learning
- statistics
id: pkis:result:woodbury-identity
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch07
specializes:
- solving-linear-systems
tags:
- matrix-inversion
- rank-one-update
- computational-efficiency
- Gaussian-process
- Bayesian-regression
title: Sherman–Morrison–Woodbury Formula
understanding: 0
uses:
- schur-complement
---

## Definition
The **matrix inversion lemma** (Sherman–Morrison–Woodbury identity) states:
$$\left(\mathbf{A} + \mathbf{U}\mathbf{C}\mathbf{V}^T\right)^{-1} = \mathbf{A}^{-1} - \mathbf{A}^{-1}\mathbf{U}\left(\mathbf{C}^{-1} + \mathbf{V}^T\mathbf{A}^{-1}\mathbf{U}\right)^{-1}\mathbf{V}^T\mathbf{A}^{-1}.$$
The rank-one special case (Sherman–Morrison) sets $\mathbf{U}=\mathbf{u}$, $\mathbf{V}=\mathbf{v}$, $\mathbf{C}=1$:
$$(\mathbf{A}+\mathbf{u}\mathbf{v}^T)^{-1} = \mathbf{A}^{-1} - \frac{\mathbf{A}^{-1}\mathbf{u}\mathbf{v}^T\mathbf{A}^{-1}}{1+\mathbf{v}^T\mathbf{A}^{-1}\mathbf{u}}.$$
When $\mathbf{A}=\boldsymbol{\Sigma}$ is $N\times N$ diagonal and $\mathbf{U}=\mathbf{X}$ is $N\times D$, it converts an $O(N^3)$ inversion into an $O(D^3)$ inversion.

### Why it matters
In Bayesian linear regression and Gaussian processes, the posterior requires inverting $(\boldsymbol{\Sigma} + \mathbf{X}\mathbf{X}^T)$; the Woodbury identity makes this tractable when $D \ll N$. It also enables online/rank-one updates to an existing inverse, critical in sequential learning and active learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[solving-linear-systems]] — specializes
- [[kalman-filter]] — applies
- [[gaussian-process-regression]] — applies
- [[bayesian-linear-regression]] — applies
- [[schur-complement]] — uses
[To be populated during integration]