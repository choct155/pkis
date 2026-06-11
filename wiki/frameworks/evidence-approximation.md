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
- bayesian-statistics
id: pkis:framework:evidence-approximation
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
tags:
- empirical-bayes
- hyperparameter-optimization
- model-selection
- marginal-likelihood
title: Evidence Approximation (Empirical Bayes for Linear Models)
understanding: 0
---

## Definition
A type-II maximum likelihood procedure that selects hyperparameters $\alpha$ (weight precision) and $\beta$ (noise precision) by maximising the **marginal likelihood** (model evidence) obtained by integrating over weights:

$$\ln p(\mathbf{t}|\alpha,\beta) = \frac{M}{2}\ln\alpha + \frac{N}{2}\ln\beta - E(\mathbf{m}_N) - \frac{1}{2}\ln|\mathbf{A}| - \frac{N}{2}\ln(2\pi)$$

where $\mathbf{A} = \alpha\mathbf{I}+\beta\boldsymbol{\Phi}^T\boldsymbol{\Phi}$, $E(\mathbf{m}_N) = \frac{\beta}{2}\|\mathbf{t}-\boldsymbol{\Phi}\mathbf{m}_N\|^2 + \frac{\alpha}{2}\mathbf{m}_N^T\mathbf{m}_N$. Fixed-point re-estimation equations are:

$$\alpha = \frac{\gamma}{\mathbf{m}_N^T\mathbf{m}_N}, \quad \frac{1}{\beta} = \frac{1}{N-\gamma}\sum_n\{t_n - \mathbf{m}_N^T\boldsymbol{\phi}(x_n)\}^2, \quad \gamma = \sum_i \frac{\lambda_i}{\alpha+\lambda_i}$$

where $\lambda_i$ are eigenvalues of $\beta\boldsymbol{\Phi}^T\boldsymbol{\Phi}$. Also known as **empirical Bayes**, **type-2 ML**, or **generalised maximum likelihood**.

### Why it matters
Automates regularisation coefficient selection from training data alone—no cross-validation, no held-out set. The effective parameter count $\gamma$ quantifies how many parameters are actually determined by the data, correcting the ML noise estimate and providing model selection directly via the evidence curve.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]