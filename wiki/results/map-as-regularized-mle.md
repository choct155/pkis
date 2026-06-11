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
- machine-learning
- Bayesian-inference
extends:
- maximum-a-posteriori-estimation-map
- mle-as-kl-minimization
id: pkis:result:map-as-regularized-mle
instantiates:
- weight-decay-as-prior
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- MAP
- regularization
- weight-decay
- ridge-regression
- Bayesian-prior
title: MAP Estimation as Regularized MLE
understanding: 0
uses:
- regularization
- bayesian-linear-regression
---

## Definition
The maximum a posteriori (MAP) estimate is:

$$\boldsymbol{\theta}_{\text{MAP}} = \arg\max_{\boldsymbol{\theta}}\bigl[\log p(\mathbf{x}|\boldsymbol{\theta}) + \log p(\boldsymbol{\theta})\bigr].$$

For a Gaussian prior $p(\mathbf{w})=\mathcal{N}(\mathbf{w};\mathbf{0},\tfrac{1}{\lambda}I)$, the log-prior contributes $-\tfrac{\lambda}{2}\mathbf{w}^\top\mathbf{w}$, so MAP linear regression is exactly $L^2$-regularized (ridge) regression:

$$\boldsymbol{w}_{\text{MAP}} = \arg\min_{\mathbf{w}}\Bigl[\text{MSE}_{\text{train}} + \lambda\,\mathbf{w}^\top\mathbf{w}\Bigr].$$

This establishes a Bayesian interpretation for many regularized estimators.

### Why it matters
The MAP-regularization correspondence gives practitioners a principled language for regularizer design: choosing a prior is equivalent to encoding a preference over parameters, and different priors (Laplace, mixture-of-Gaussians) correspond to different regularizers (L1, spike-and-slab).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-linear-regression]] — uses
- [[weight-decay-as-prior]] — instantiates
- [[mle-as-kl-minimization]] — extends
- [[regularization]] — uses
- [[maximum-a-posteriori-estimation-map]] — extends
[To be populated during integration]