---
aliases: []
also_type: []
applies:
- posterior-predictive-distribution
- binary-logistic-regression
- uncertainty-quantification
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
- Bayesian-inference
id: pkis:technique:probit-approximation-bayesian-logistic
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch10
tags:
- Bayesian-logistic-regression
- posterior-predictive
- probit
- Gaussian-posterior
- uncertainty-quantification
title: Probit Approximation to Bayesian Logistic Posterior Predictive
understanding: 0
uses:
- laplace-approximation
- gaussian-distribution
---

## Definition
Given a Gaussian posterior $p(w|D)=\mathcal{N}(w|\mu,\Sigma)$ for a binary logistic model, the posterior predictive is approximated as
$$p(y=1|x,D) \approx \sigma(\kappa(v)\,m), \quad m = x^T\mu,\; v = x^T\Sigma x,\; \kappa(v)=(1+\pi v/8)^{-1/2}$$
by exploiting the near-identity $\sigma(a)\approx\Phi(\sqrt{\pi/8}\,a)$ and the closed-form integral $\int\Phi(\lambda a)\mathcal{N}(a|m,v)\,da = \Phi(m/(\lambda^{-2}+v)^{1/2})$.

### Why it matters
The probit approximation gives a deterministic, closed-form alternative to Monte Carlo integration of the posterior predictive, avoiding $S$ forward passes at test time. Predictions are **less extreme** than the plug-in MAP estimate (since $0<\kappa(v)<1$) but share the same decision boundary. The generalisation to multiclass uses class-wise variances $v_c = x^TV_{cc}x$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[uncertainty-quantification]] — applies
- [[gaussian-distribution]] — uses
- [[binary-logistic-regression]] — applies
- [[posterior-predictive-distribution]] — applies
- [[laplace-approximation]] — uses
[To be populated during integration]