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
contrasts-with:
- test-quantity-discrepancy
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
generalizes:
- confidence-interval
id: pkis:concept:bayesian-p-value
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch06
tags:
- p-value
- posterior-predictive
- tail-area-probability
- calibration
- u-value
- model-checking
- bayesian-stats
title: Bayesian (Posterior Predictive) p-value
understanding: 0
---

## Definition
The probability, taken over the joint posterior predictive distribution p(θ, y_rep | y), that replicated data are at least as extreme as the observed data under a test quantity: p_B = Pr(T(y_rep,θ) ≥ T(y,θ) | y) = ∫∫ I_{T(y_rep,θ)≥T(y,θ)} p(y_rep|θ) p(θ|y) dy_rep dθ. It generalizes the classical p_C = Pr(T(y_rep) ≥ T(y) | θ), which fixes θ at a point estimate; the Bayesian version instead averages over the posterior of θ. A value near 0 or 1 flags a model unable to capture that aspect of the data; how extreme beyond that matters little (0.00001 is practically no stronger than 0.001), and statistical significance is not practical significance. BDA3 treats p_B directly as a posterior probability — 'if we believe the model, a 40% chance tomorrow's T(y_rep) exceeds today's T(y)' — not as a frequentist error rate; no multiple-comparisons (Type I error) adjustment is made because checks are used to understand a model's limits, not to accept/reject it. Crucially, p_B is generally NOT a u-value (a statistic with exact U(0,1) sampling distribution under the true model): only when θ is known or T is ancillary is its null distribution uniform; otherwise it is 'stochastically less variable' than uniform, concentrated near ½. The relation is 'the p-value is to the u-value as the posterior interval is to the confidence interval.'

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[test-quantity-discrepancy]] — contrasts-with: p_B is the tail-area summary of the discrepancy measure T
- [[confidence-interval]] — generalizes: p-value is to the u-value as the posterior interval is to the confidence interval
[To be populated during integration]