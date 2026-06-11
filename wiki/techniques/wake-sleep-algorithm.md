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
- deep-learning
- neuroscience
id: pkis:technique:wake-sleep-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
tags:
- amortized-inference
- generative-model
- recognition-network
- dreaming
- Helmholtz-machine
title: Wake-Sleep Algorithm
understanding: 0
---

## Definition
The wake-sleep algorithm jointly trains a **generative network** (top-down, $p(\mathbf{v}|\mathbf{h})$) and a **recognition/inference network** (bottom-up, $q(\mathbf{h}|\mathbf{v})$) using two alternating phases:

- **Wake phase**: Use the recognition network to infer $\mathbf{h}$ given observed $\mathbf{v}$; update the generative network to better explain the data.
- **Sleep phase**: Sample $\mathbf{h}$ and $\mathbf{v}$ from the generative network; update the recognition network to predict $\mathbf{h}$ from the generated $\mathbf{v}$.

The sleep phase sidesteps the need for a supervised training signal for inference by generating synthetic (h, v) pairs from the model itself (Hinton et al., 1995).

### Why it matters
Wake-sleep was a precursor to the variational autoencoder, introducing the idea of amortized approximate inference via a learned recognition network. Its main limitation is that the recognition network is trained on model-generated data, not real data, causing mismatch early in learning. The VAE fixes this by optimising a single unified ELBO objective for both networks simultaneously.

### Connection to Neuroscience
The sleep phase has been proposed as a computational model for the role of dreaming: generating samples from $p(\mathbf{h}, \mathbf{v})$ to train the brain's inference machinery.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]