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
- statistics
id: pkis:technique:ffbs-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- smoothing
- FFBS
- forward-backward
- offline-inference
- state-space-model
title: Forwards Filtering Backwards Smoothing (FFBS)
understanding: 0
---

## Definition
$$p(\mathbf{z}_t|\mathbf{y}_{1:T}) = p(\mathbf{z}_t|\mathbf{y}_{1:t})\int \frac{p(\mathbf{z}_{t+1}|\mathbf{z}_t)\, p(\mathbf{z}_{t+1}|\mathbf{y}_{1:T})}{p(\mathbf{z}_{t+1}|\mathbf{y}_{1:t})}\, d\mathbf{z}_{t+1}$$

A general two-pass offline smoothing algorithm: a **forward pass** runs the Bayes filter to produce filtered beliefs $p(\mathbf{z}_t|\mathbf{y}_{1:t})$; a **backward pass** combines these with future information using the above recursion to produce smoothed marginals $p(\mathbf{z}_t|\mathbf{y}_{1:T})$. In the linear-Gaussian case it instantiates as the RTS smoother; in the discrete case as the HMM forward-backward algorithm.

### Why it matters
FFBS is the canonical template for exact fixed-interval smoothing across all tractable SSM families. The same backwards recursion also enables forwards-filtering backwards-sampling (FFBS sampling), which draws exact posterior trajectories and is the E-step in Bayesian parameter learning for SSMs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]