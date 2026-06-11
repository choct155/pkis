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
- gaussian-processes
- feature-selection
extends:
- gaussian-process-regression
id: pkis:technique:ard-gaussian-process
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch06
tags:
- ARD
- automatic-relevance-determination
- length-scale
- hyperparameter
- feature-selection
- marginal-likelihood
title: Automatic Relevance Determination (ARD) in Gaussian Processes
understanding: 0
uses:
- marginal-likelihood
- stationary-and-radial-kernels
- automatic-differentiation
---

## Definition
A separate length-scale parameter $\eta_i$ is introduced for each input dimension $i$ in the kernel:

$$k(\mathbf{x},\mathbf{x}') = \theta_0\exp\!\left\{-\frac{1}{2}\sum_{i=1}^{D}\eta_i(x_i - x_i')^2\right\} + \theta_2 + \theta_3\,\mathbf{x}^T\mathbf{x}'.$$

Maximising the log marginal likelihood $\ln p(\mathbf{t}|\boldsymbol{\theta})$ with respect to all $\eta_i$ simultaneously causes irrelevant inputs to drive their $\eta_i$ toward zero, effectively switching them off.

### Why it matters
ARD provides automatic feature selection within the Bayesian kernel framework: no discrete combinatorial search is needed. Originally proposed for Bayesian neural networks (MacKay 1994, Neal 1996), it transfers directly to GP models via the kernel hyperparameter interpretation. In practical applications with many candidate inputs (e.g., genomics, chemoinformatics) ARD is a principled and computationally efficient filter.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[automatic-differentiation]] — uses
- [[stationary-and-radial-kernels]] — uses
- [[marginal-likelihood]] — uses
- [[gaussian-process-regression]] — extends
[To be populated during integration]