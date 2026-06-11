---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
extends:
- pac-learning
generalizes:
- maximum-likelihood-estimation
- maximum-a-posteriori-estimation-map
id: pkis:framework:empirical-risk-minimization-erm
instantiates:
- empirical-risk-minimization
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- overfitting-and-underfitting
related_concepts: []
sources:
- murphy-pml2-advanced-ch14
specializes:
- structural-risk-minimization
tags:
- loss-function
- regularisation
- MLE
- MAP
- optimisation
title: Empirical Risk Minimization (ERM)
understanding: 0
uses:
- regularization
---

## Definition
$$\hat{\theta} = \arg\min_{\theta \in \Theta}\; r(\theta) = \arg\min_{\theta \in \Theta}\; \frac{1}{N}\sum_{n=1}^N \ell_n(\theta)$$

ERM replaces the intractable expectation over the true data-generating distribution with the sample average of a per-example loss $\ell_n$. Regularised ERM adds a penalty $\lambda C(\theta)$ to control model complexity; choosing $C(\theta) = -\log\pi_0(\theta)$ and $\lambda=1$ recovers the MAP estimate. When $\ell_n = -\log p(y_n\mid\mathbf{x}_n,\theta)$ ERM reduces to MLE.

### Why it matters
ERM unifies MLE, MAP, and a large family of loss-based learning rules under one optimisation template, making it the foundation for the theory of generalisation (VC theory, PAC learning) and the starting point for understanding overfitting and regularisation.

### Connection to Gibbs posterior
Replacing the point-estimate in ERM with a distribution over parameters, and adding a KL penalty toward a prior, generalises ERM to Bayesian and PAC-Bayes learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[overfitting-and-underfitting]] — prerequisite-of
- [[structural-risk-minimization]] — specializes
- [[empirical-risk-minimization]] — instantiates: This node IS the canonical ERM concept — link to existing structural-risk-minimization node
- [[pac-learning]] — extends
- [[regularization]] — uses
- [[maximum-a-posteriori-estimation-map]] — generalizes
- [[maximum-likelihood-estimation]] — generalizes
[To be populated during integration]