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
- machine-learning
- statistics
id: pkis:result:lda-logistic-regression-equivalence
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- LDA
- logistic-regression
- softmax
- equivalence
- joint-vs-conditional
title: LDA–Logistic Regression Equivalence
understanding: 0
---

## Definition
When the class-conditional densities are Gaussian with a **shared** covariance $\Sigma$, the LDA posterior takes the softmax form:

$$p(y=c\mid x,\theta) = \frac{\exp(\beta_c^\top x + \gamma_c)}{\sum_{c'}\exp(\beta_{c'}^\top x + \gamma_{c'})}, \quad \beta_c = \Sigma^{-1}\mu_c,\quad \gamma_c = -\tfrac{1}{2}\mu_c^\top\Sigma^{-1}\mu_c + \log\pi_c$$

In the binary case this collapses to a sigmoid: $p(y=1\mid x) = \sigma(w^\top(x - x_0))$ where $w = \Sigma^{-1}(\mu_1-\mu_0)$.

### Why it matters
This result reveals that LDA and multinomial logistic regression are the **same functional family**, but differ in the likelihood they optimise: LDA maximises the joint likelihood (learning Gaussian parameters and deriving $w$ from them), while logistic regression maximises the conditional likelihood (estimating $w$ directly). Because the conditional likelihood is a marginalisation of the joint, logistic regression imposes strictly fewer assumptions, generally achieving equal or better calibration but potentially lower data-efficiency when the Gaussian assumption holds.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]