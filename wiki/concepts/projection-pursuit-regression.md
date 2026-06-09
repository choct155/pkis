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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:concept:projection-pursuit-regression
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch11
tags:
- additive-model
- ridge-function
- semiparametric
- derived-features
- smoothing
- universal-approximator
title: Projection Pursuit Regression
understanding: 0
---

## Definition
## Definition
Projection pursuit regression (PPR), proposed by Friedman & Stuetzle (1981), models a target as a **sum of nonparametric ridge functions of linear projections** of the inputs:
$$f(X) = \sum_{m=1}^{M} g_m(\omega_m^{T} X),$$
where each $\omega_m$ is a unit $p$-vector (a *direction*) and each $g_m$ is an unspecified univariate smooth function (a *ridge function* in $\mathbb{R}^p$, varying only along $\omega_m$). It is an additive model not in the inputs but in the *derived features* $V_m = \omega_m^{T} X$ — the scalar projections of $X$ onto the directions sought so the model fits well, hence "projection pursuit." The $M=1$ case is the **single index model** of econometrics.

### Universal approximator
Because forming nonlinear functions of linear combinations generates a very large model class (e.g. $X_1 X_2 = [(X_1+X_2)^2 - (X_1-X_2)^2]/4$), taking $M$ arbitrarily large lets PPR approximate any continuous function on $\mathbb{R}^p$ arbitrarily well. The price is interpretability: each input enters in a complex, multifaceted way, so PPR is a tool for prediction rather than for describing the data-generating process.

### Fitting
The directions $\omega_m$ and ridge functions $g_m$ are estimated jointly by minimizing squared error $\sum_i [y_i - \sum_m g_m(\omega_m^T x_i)]^2$, with complexity constraints on the $g_m$ to avoid overfitting. For a single term the procedure alternates: (i) given $\omega$, form $v_i=\omega^T x_i$ and fit $g$ by any one-dimensional scatterplot smoother (smoothing spline, local regression); (ii) given $g$, update $\omega$ by a **Gauss–Newton** step — a quasi-Newton method that discards the second-derivative-of-$g$ part of the Hessian, reducing the update to a weighted least-squares regression with no intercept. Multiple terms are added in a forward stage-wise manner, with $M$ chosen by when added terms stop improving the fit (or by cross-validation).

### Why it matters
PPR is the conceptual ancestor of the single-hidden-layer neural network: both take nonlinear functions of linear combinations of the inputs. The neural network is recovered by restricting the ridge function to the parametric form $g_m(\omega_m^T X) = \beta_m \sigma(\alpha_{0m} + \|\alpha_m\|\,\omega_m^T X)$. Because this $\sigma$-based form is simpler than a free nonparametric $g$, neural nets use many more terms ($M=20$–$100$) than PPR typically does ($M=5$–$10$). Despite its intellectual importance, PPR was little used in statistics, partly because its 1981 computational demands exceeded available hardware; the idea reincarnated in neural networks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]