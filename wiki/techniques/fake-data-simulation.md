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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:fake-data-simulation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch10
tags:
- debugging
- model-checking
- validation
- interval-coverage
- fake-data
- diagnostics
title: Fake-Data Simulation (Debugging)
understanding: 0
---

## Definition
A procedure for building confidence in posterior inferences (and catching programming/modeling errors) by fitting the model to data simulated from the model itself. The basic recipe (BDA3, ch. 10.7): (1) pick a reasonable 'true' parameter vector theta -- strictly a draw from the prior, but for noninformative priors any reasonable value works; for hierarchical models pick hyperparameters first, then draw lower-level parameters from the prior given them; (2) simulate a large fake dataset y^fake from p(y|theta); (3) perform posterior inference p(theta|y^fake); (4) compare the inferences to the known true theta -- e.g. a 50% posterior interval should contain the truth about 50% of the time. A single fake dataset is revealing if the true value lands far outside the computed posterior. For higher-dimensional theta one computes coverage diagnostics (proportion of 50% intervals containing the truth) and 'residual plots' of (true minus posterior-mean) errors against predicted values, which should have zero mean if the computation is correct. Repeating over many resampled true thetas checks average calibration -- the conceptual ancestor of simulation-based calibration. Model-checking and convergence-checking (Chs. 6-7, 11.4) are complementary debugging tools.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]