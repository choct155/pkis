---
aliases: []
also_type: []
applies:
- deep-reinforcement-learning
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
- optimization
- deep-learning
extends:
- rmsprop
- sgd-momentum
- gradient-descent
- stochastic-gradient-descent
generalizes:
- adagrad
id: pkis:technique:adam-optimizer
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
- murphy-pml1-intro-ch08
tags:
- adaptive-learning-rate
- momentum
- bias-correction
- deep-learning
title: Adam Optimizer
understanding: 0
uses:
- nesterov-accelerated-gradient
---

## Definition
Adam (Kingma & Ba, 2014 — *Ada*ptive *M*oments) maintains exponentially-decaying estimates of the first moment $\mathbf{s}$ and second moment $\mathbf{r}$ of the gradient, with bias corrections:
$$\mathbf{s} \leftarrow \rho_1\mathbf{s}+(1-\rho_1)\mathbf{g}, \quad \mathbf{r} \leftarrow \rho_2\mathbf{r}+(1-\rho_2)\mathbf{g}\odot\mathbf{g},$$
$$\hat{\mathbf{s}} = \frac{\mathbf{s}}{1-\rho_1^t}, \quad \hat{\mathbf{r}} = \frac{\mathbf{r}}{1-\rho_2^t}, \quad \Delta\theta = -\epsilon\frac{\hat{\mathbf{s}}}{\sqrt{\hat{\mathbf{r}}}+\delta}.$$
Suggested defaults: $\epsilon=10^{-3}$, $\rho_1=0.9$, $\rho_2=0.999$, $\delta=10^{-8}$.

Intuition: Adam combines RMSProp's adaptive second-moment scaling with a momentum-style first-moment estimate, both corrected for initialisation bias at early time steps.

### Why it matters
Adam is currently the default optimiser for most deep learning research. Its bias correction is critical in early training when the moving averages are far from their stationary values. It is generally robust to hyperparameter choice, though tuning $\epsilon$ is still sometimes necessary.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[deep-reinforcement-learning]] — applies
- [[stochastic-gradient-descent]] — extends
- [[nesterov-accelerated-gradient]] — uses
- [[gradient-descent]] — extends
- [[adagrad]] — generalizes
- [[sgd-momentum]] — extends: first moment estimate is a form of momentum
- [[rmsprop]] — extends: Adam adds first-moment (momentum) term and bias correction to RMSProp
[To be populated during integration]