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
- bayesian-inference
- deep-learning
- uncertainty-quantification
id: pkis:technique:laplace-bridge
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- Dirichlet
- Gaussian-logits
- uncertainty
- top-k-prediction
- post-processing
title: Laplace Bridge Approximation
understanding: 0
---

## Definition
Given a Gaussian approximation to the logits $p(z|x,D) = \mathcal{N}(z|m,V)$, the Laplace bridge converts it to a Dirichlet distribution $\text{Dir}(\pi|\alpha)$ via:
$$\alpha_i = \frac{1}{V_{ii}}\left(1 - \frac{2}{C} + \frac{\exp(m_i)}{C^2}\sum_j^C \exp(-m_j)\right)$$
after first projecting the Gaussian onto the zero-sum constraint surface to match the Dirichlet's degrees of freedom.

### Why it matters
The Laplace bridge [Hobbhahn et al. 2022] provides a cheap, closed-form post-processing step that upgrades a point-predicted softmax distribution into a full Dirichlet distribution over class probabilities. Because Dirichlet marginals are Beta distributions, one can compute per-class uncertainty and adaptive top-$k$ prediction sets, capturing instance-level ambiguity in a natural Bayesian way—similar in spirit to conformal prediction but probabilistically principled.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]