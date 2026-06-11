---
aliases: []
also_type: []
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
- bayesian-inference
id: pkis:technique:probit-approximation-logistic-gaussian
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
tags:
- posterior-predictive
- Laplace-approximation
- logistic-regression
- deterministic-approximation
- probit
title: Probit Approximation to Logistic-Gaussian Integral
understanding: 0
---

## Definition
$$p(y_*=1 \mid x_*) \approx \int \sigma(f_*)\,\mathcal{N}(f_* \mid \mu_*, \sigma_*^2)\,df_* \approx \sigma\!\left(\frac{\mu_*}{\sqrt{1 + \frac{\pi}{8}\sigma_*^2}}\right)$$

An analytic approximation to the predictive posterior of a binary logistic classifier by replacing the sigmoid with the probit $\Phi$, exploiting the closed-form convolution $\int \Phi(f)\mathcal{N}(f|\mu,\sigma^2)df = \Phi(\mu/\sqrt{1+\sigma^2})$.

### Why it matters
When the parameter posterior is approximated as Gaussian (e.g., via Laplace or EP), this trick yields a cheap, deterministic estimate of the posterior predictive probability that closely matches Monte Carlo approximations and avoids expensive sample-based integration. The generalised probit approximation extends this to the multiclass softmax setting.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]