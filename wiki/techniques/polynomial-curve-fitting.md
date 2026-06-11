---
aliases: []
also_type: []
applies:
- overfitting-and-underfitting
- bias-variance-tradeoff
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:polynomial-curve-fitting
instantiates:
- supervised-learning
- model-selection-problem
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-predictive-marginalisation
related_concepts: []
sources:
- bishop-prml-ch01
specializes:
- linear-regression
tags:
- regression
- model-complexity
- least-squares
- overfitting
title: Polynomial Curve Fitting
understanding: 0
uses:
- regularization
- ridge-regression
- maximum-likelihood-estimation
- cross-validation
---

## Definition
$$y(x, \mathbf{w}) = \sum_{j=0}^{M} w_j x^j, \quad E(\mathbf{w}) = \frac{1}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2$$

Fit a degree-$M$ polynomial to $N$ scalar observations by minimising the sum-of-squares error; because $y$ is linear in **w**, the minimiser $\mathbf{w}^*$ has a unique closed-form solution via a linear system $A\mathbf{w}=\mathbf{T}$.

### Why it matters
Serves as a canonical running example that simultaneously illustrates supervised regression, the role of model complexity (order $M$), overfitting vs underfitting, the equivalence of least-squares with maximum-likelihood under Gaussian noise, and the effect of L2 regularisation. The RMS error on a held-out test set provides a direct empirical probe of generalisation.

### Connections
- [[bayesian-predictive-marginalisation]] — prerequisite-of
- [[cross-validation]] — uses
- [[model-selection-problem]] — instantiates
- [[bias-variance-tradeoff]] — applies
- [[maximum-likelihood-estimation]] — uses
- [[ridge-regression]] — uses
- [[regularization]] — uses
- [[overfitting-and-underfitting]] — applies
- [[linear-regression]] — specializes
- [[supervised-learning]] — instantiates
Choosing $M$ is an instance of model selection; adding an L2 penalty $\frac{\lambda}{2}\|\mathbf{w}\|^2$ recovers ridge regression and is equivalent to MAP estimation under a zero-mean Gaussian prior on **w** with precision $\alpha=\lambda\beta$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]