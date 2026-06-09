---
aliases: []
also_type: []
analogous-to:
- neural-networks
- gradient-boosting
- independent-component-analysis
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
instantiates:
- universal-approximation-theorem
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
uses:
- gradient-descent
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
- [[independent-component-analysis]] — analogous-to: Exploratory projection pursuit underlies ICA; both seek interesting projection directions of the inputs.
- [[gradient-boosting]] — analogous-to: PPR builds its sum of ridge functions in a forward stage-wise manner, structurally like additive forward-stagewise boosting.
- [[gradient-descent]] — uses: Directions omega_m are updated by a Gauss-Newton (quasi-Newton) least-squares step alternating with smoothing of g_m.
- [[universal-approximation-theorem]] — instantiates: With M arbitrarily large, PPR approximates any continuous function on R^p arbitrarily well.
- [[neural-networks]] — analogous-to: Both PPR and the single-hidden-layer net take nonlinear functions of linear combinations of inputs; PPR is the semiparametric-statistics ancestor of the neural net.
[To be populated during integration]