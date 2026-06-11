---
aliases: []
also_type: []
analogous-to:
- fishers-linear-discriminant
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- quadratic-discriminant-analysis
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:result:gaussian-lda-linear-boundary
instantiates:
- probabilistic-generative-classifier
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
tags:
- LDA
- QDA
- Bayes-classifier
- Gaussian-generative
- linear-decision-boundary
- shared-covariance
title: Gaussian Class-Conditional ⟹ Linear Decision Boundary
understanding: 0
uses:
- logistic-sigmoid-logit
- gaussian-distribution
---

## Definition
If class-conditional densities are Gaussian with a **shared** covariance matrix $\Sigma$,

$$p(\mathbf{x}|C_k) = \mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\Sigma),$$

then the posterior probability $p(C_1|\mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x}+w_0)$ where

$$\mathbf{w} = \Sigma^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2), \quad w_0 = -\tfrac{1}{2}\boldsymbol{\mu}_1^T\Sigma^{-1}\boldsymbol{\mu}_1 + \tfrac{1}{2}\boldsymbol{\mu}_2^T\Sigma^{-1}\boldsymbol{\mu}_2 + \ln\frac{p(C_1)}{p(C_2)}.$$

The quadratic terms in $\mathbf{x}$ cancel due to the shared $\Sigma$, yielding a linear decision boundary. Distinct per-class covariances $\Sigma_k$ restore the quadratic terms, giving quadratic discriminant analysis (QDA).

### Why it matters
This result is the generative derivation of Linear Discriminant Analysis, showing that LDA is the Bayes-optimal classifier under Gaussian class-conditionals with equal covariance. It also shows that the prior $p(C_k)$ affects only the bias $w_0$, shifting decision boundaries in parallel.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[quadratic-discriminant-analysis]] — contrasts-with
- [[fishers-linear-discriminant]] — analogous-to: Both yield the same linear projection under shared-covariance Gaussian assumption
- [[gaussian-distribution]] — uses
- [[logistic-sigmoid-logit]] — uses
- [[probabilistic-generative-classifier]] — instantiates
[To be populated during integration]