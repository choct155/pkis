---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- epsilon-insensitive-loss
- hinge-loss
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- decision-theory
extends:
- bayesian-point-estimation
id: pkis:result:optimal-regression-loss-estimators
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- L2-loss
- L1-loss
- Huber-loss
- posterior-mean
- posterior-median
- robust-regression
title: Optimal Regression Estimators Under Common Loss Functions
understanding: 0
uses:
- loss-function-posterior-expected-loss
---

## Definition
Under Bayesian decision theory with a posterior $p(h|x)$ over the hidden state $h\in\mathbb{R}$:

| Loss | Optimal action |
|---|---|
| $\ell_2(h,a)=(h-a)^2$ | $\pi^*(x)=\mathbb{E}[h|x]$ (posterior mean) |
| $\ell_1(h,a)=|h-a|$ | $\pi^*(x)=\text{median}(p(h|x))$ |
| Huber $\ell_\delta$ | Interpolates between mean and median |

Derivation for $\ell_2$: differentiate $\rho(a|x)=\mathbb{E}[(h-a)^2|x]$ with respect to $a$ and set to zero.

### Why it matters
This result gives the principled justification for reporting the **posterior mean** as the point estimate under squared error, and the **posterior median** as the robust alternative. It also motivates the **Huber loss**, which is equivalent to $\ell_2$ for small residuals ($|r|\leq\delta$) and $\ell_1$ for large ones, providing outlier robustness while retaining a unique, differentiable minimum.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hinge-loss]] — contrasts-with
- [[epsilon-insensitive-loss]] — contrasts-with
- [[bayesian-point-estimation]] — extends
- [[loss-function-posterior-expected-loss]] — uses
[To be populated during integration]