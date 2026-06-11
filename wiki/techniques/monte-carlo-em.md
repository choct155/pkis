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
- statistics
- machine-learning
id: pkis:technique:monte-carlo-em
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch11
tags:
- em-algorithm
- monte-carlo
- latent-variables
- maximum-likelihood
title: Monte Carlo EM Algorithm
understanding: 0
---

## Definition
The Monte Carlo EM algorithm approximates the E-step of the EM algorithm by replacing the intractable expectation over latent variables with a Monte Carlo average. Given model parameters $\theta^{\text{old}}$, the Q-function
$$Q(\theta, \theta^{\text{old}}) = \int p(Z|X,\theta^{\text{old}})\ln p(Z,X|\theta)\,dZ$$
is approximated by drawing $L$ samples $\{Z^{(l)}\}$ from $p(Z|X,\theta^{\text{old}})$:
$$Q(\theta,\theta^{\text{old}}) \simeq \frac{1}{L}\sum_{l=1}^L \ln p(Z^{(l)},X|\theta).$$
The M-step then maximises this approximation as usual.

### Why it matters
Monte Carlo EM extends maximum-likelihood learning to models where the posterior over latent variables has no closed-form, enabling EM-style training for complex graphical models and mixture models. The stochastic EM special case (single sample per E-step) connects to hard-assignment clustering algorithms and simulated annealing schedules.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]