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
- centered-deep-boltzmann-machine
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- generative-models
- approximate-inference
extends:
- deep-boltzmann-machine
id: pkis:technique:multi-prediction-deep-boltzmann-machine
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- joint-training
- back-propagation-through-inference
- pseudo-likelihood
- missing-data
title: Multi-Prediction Deep Boltzmann Machine (MP-DBM)
understanding: 0
uses:
- mean-field-approximation
- backpropagation
---

## Definition
A training approach for deep Boltzmann machines that replaces maximum-likelihood with a **generalised pseudo-likelihood** objective: for each training example, a random subset of variables is treated as observed (inputs) and the remainder as targets, with the mean-field inference graph unrolled as a recurrent network and trained by back-propagation to predict the targets accurately:
$$\min_{\theta}\mathbb{E}_{\mathbf{v},\mathcal{S}}\left[-\log\tilde{p}(\mathbf{v}_{\bar{\mathcal{S}}}|\mathbf{v}_{\mathcal{S}};\theta)\right],$$
where $\mathcal{S}$ is a random observed subset and gradients flow through the unrolled mean-field graph.

### Why it matters
MP-DBM enables joint training of DBMs (no greedy pretraining needed) and produces better classifiers and missing-data imputations than the original DBM training scheme, because the model is trained in the way it is actually used. It sacrifices log-likelihood quality for inference accuracy and inspired the NADE-k extension.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[centered-deep-boltzmann-machine]] — contrasts-with: MP-DBM prioritises inference accuracy; centered DBM prioritises likelihood/sample quality.
- [[backpropagation]] — uses: Back-propagates through the unrolled mean-field inference graph.
- [[mean-field-approximation]] — uses
- [[deep-boltzmann-machine]] — extends
[To be populated during integration]