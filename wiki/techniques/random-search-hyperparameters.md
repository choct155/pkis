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
contrasts-with:
- bayesian-optimization
- grid-search
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- hyperparameter-optimization
id: pkis:technique:random-search-hyperparameters
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch11
tags:
- hyperparameter-tuning
- model-selection
- random-search
- Bergstra-Bengio
title: Random Search for Hyperparameter Tuning
understanding: 0
uses:
- cross-validation
---

## Definition
**Random search** (Bergstra & Bengio, 2012) samples each hyperparameter independently from a pre-specified marginal distribution and evaluates the resulting configurations. For a positive real-valued hyperparameter such as the learning rate, sampling is done on a log scale:

$$\log_{10}(\eta) \sim \mathcal{U}(a, b), \quad \eta = 10^{\log_{10}(\eta)}.$$

### Why it matters
Random search is exponentially more sample-efficient than grid search when only a few hyperparameters strongly affect performance. Grid search wastes budget repeating equivalent configurations along irrelevant axes; random search draws a fresh value for every hyperparameter on every trial, giving independent exploration of the influential dimensions at no extra cost. Empirically, random search reaches better validation error in fewer trials than grid search, and repeated rounds of refined random search approximate global optimisation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cross-validation]] — uses
- [[grid-search]] — contrasts-with
- [[bayesian-optimization]] — contrasts-with
[To be populated during integration]