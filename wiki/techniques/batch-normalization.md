---
aliases: []
also_type: []
applies:
- vanishing-gradient-problem
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
- deep-learning
id: pkis:technique:batch-normalization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch21
tags:
- training-dynamics
- normalization
- convergence
- minibatch
title: Batch Normalization
understanding: 0
uses:
- stochastic-gradient-descent
---

## Definition
A technique (Ioffe & Szegedy, 2015) that improves the convergence rate of stochastic gradient descent by rescaling the values generated at internal layers using statistics from the current minibatch. For a node z with minibatch values z_1,...,z_m, each value is replaced by z_hat_i = γ (z_i − μ)/sqrt(ε + σ²) + β, where μ and σ are the minibatch mean and standard deviation, ε prevents division by zero, and γ and β are learned (node- or layer-specific) parameters included in training and fixed after. By standardizing the mean and variance of layer activations, it prevents information loss when a layer's weights are too small (standard deviation decaying to near zero) and reduces the need for careful weight initialization to keep nodes in their useful operating region. Its effectiveness is not well understood theoretically, but it has effects similar to those of residual connections.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[vanishing-gradient-problem]] — applies: prevents layer standard deviations from decaying to zero, preserving signal propagation
- [[stochastic-gradient-descent]] — uses: rescales per-minibatch activations to improve SGD convergence
[To be populated during integration]