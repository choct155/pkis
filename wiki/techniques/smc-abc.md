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
- computational-biology
id: pkis:technique:smc-abc
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- abc
- likelihood-free
- simulation-based-inference
- smc-sampler
title: SMC-ABC (Approximate Bayesian Computation via SMC)
understanding: 0
---

## Definition
SMC-ABC approximates the posterior of a simulator model (one with an intractable or unavailable likelihood) by constructing a sequence of distributions with decreasing discrepancy thresholds $\epsilon_0 > \epsilon_1 > \cdots$:
$$\pi_t(\theta, \mathbf{y}) = \frac{1}{Z_t}\,\pi_0(\theta)\,p(\mathbf{y}|\theta)\,\mathcal{I}(d(s(\mathbf{y}), s(\mathbf{y}^*)) < \epsilon_t)$$
where $s(\cdot)$ is a low-dimensional summary statistic. MCMC kernels move particles in $\theta$-space, while new synthetic data $\mathbf{y}$ are simulated for each proposal.

### Why it matters
SMC-ABC is a principled extension of likelihood-free inference to the sequential setting, avoiding the poor mixing of MCMC-ABC and the sample-size sensitivity of rejection ABC. It is widely used in genetics, epidemiology, and ecology where mechanistic simulators exist but likelihoods are intractable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]