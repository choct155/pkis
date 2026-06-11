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
- deep-learning
- bayesian-inference
- uncertainty-quantification
extends:
- dropout
id: pkis:technique:monte-carlo-dropout
instantiates:
- bayesian-deep-learning
- variational-inference
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- dropout
- approximate-inference
- test-time-sampling
- calibration
title: Monte Carlo Dropout (MCD)
understanding: 0
uses:
- elbo
---

## Definition
$$p(y|x, D) \approx \frac{1}{S} \sum_{s=1}^{S} p(y|x, \theta^s), \quad \theta^s \sim \text{Bernoulli-masked MAP weights}$$

Monte Carlo Dropout retains stochastic dropout at *test* time, drawing $S$ binary masks to produce an ensemble of thinned networks; their predictive distributions are averaged to approximate the Bayesian posterior predictive.

### Why it matters
MCD requires no changes to model architecture or training procedure beyond keeping dropout active at inference, making it one of the simplest ways to obtain predictive uncertainty estimates from a pretrained deep net. It can be interpreted as a form of variational inference under a mixture-of-delta-functions posterior.

### Limitations
Because the implicit posterior never converges to the true posterior (units are always dropped with constant probability $p$ regardless of dataset size), MCD can give poorly calibrated uncertainty. This pathology is alleviated when the dropout rate is optimised rather than fixed.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[elbo]] — uses
- [[variational-inference]] — instantiates: Can be derived as VI under a mixture-of-delta posterior
- [[dropout]] — extends: Applies dropout at test time rather than only during training
- [[bayesian-deep-learning]] — instantiates
[To be populated during integration]