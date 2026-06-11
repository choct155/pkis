---
aliases: []
also_type: []
applies:
- knowledge-graph-completion
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
- graph-learning
- generative-models
extends:
- variational-autoencoder
id: pkis:technique:variational-graph-auto-encoder
instantiates:
- graph-encoder-decoder-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- VAE
- graph-generation
- link-prediction
- VGAE
- GCN
- ELBO
title: Variational Graph Auto-Encoder (VGAE)
understanding: 0
uses:
- graph-convolutional-network
- elbo
---

## Definition
VGAE (Kipf & Welling, 2016) models graph structure as a latent variable model:
$$p(\mathbf{W}|\mathbf{Z}) = \prod_{i,j}\sigma(\tilde{W}_{ij})^{W_{ij}}(1-\sigma(\tilde{W}_{ij}))^{1-W_{ij}}, \quad \tilde{\mathbf{W}}=\mathbf{Z}\mathbf{Z}^\top$$
$$q_\Phi(\mathbf{Z}|\mathbf{W},\mathbf{X}) = \mathcal{N}(\boldsymbol{\mu},\text{diag}(\boldsymbol{\sigma}^2)), \quad \text{(GCN amortised encoder)}$$
and is trained by minimising the NELBO:
$$\text{NELBO} = \mathcal{L}_{G,\text{RECON}} + \text{KL}(q_\Phi(\mathbf{Z}|\mathbf{W},\mathbf{X})\|\mathcal{N}(\mathbf{0},\mathbf{I}))$$

The encoder is a GCN producing per-node mean and log-variance; the decoder reconstructs edge probabilities via an outer product of latent node vectors.

### Why it matters
VGAE extends the VAE framework to graph-structured data, enabling link prediction and graph generation with principled uncertainty estimates. Its deterministic counterpart GAE and the iterative extension Graphite build on the same encoder-decoder skeleton. VGAE is widely used for knowledge-graph completion and molecular generation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[knowledge-graph-completion]] — applies
- [[elbo]] — uses
- [[graph-encoder-decoder-model]] — instantiates
- [[graph-convolutional-network]] — uses
- [[variational-autoencoder]] — extends
[To be populated during integration]