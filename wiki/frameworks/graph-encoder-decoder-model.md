---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- graph-learning
- deep-learning
generalizes:
- node-embedding
- graph-neural-networks
id: pkis:framework:graph-encoder-decoder-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- graph-embeddings
- encoder-decoder
- unifying-framework
- GRL
title: Graph Encoder-Decoder Model (GraphEDM)
understanding: 0
uses:
- variational-autoencoder
- elbo
---

## Definition
$$\mathbf{Z} = \text{ENC}(\mathbf{W}, \mathbf{X}; \Theta^E), \quad \hat{\mathbf{W}} = \text{DEC}(\mathbf{Z}; \Theta^D), \quad \hat{y}^S = \text{DEC}(\mathbf{Z}; \Theta^S)$$

with total loss

$$\mathcal{L} = \alpha \mathcal{L}^S_{\text{SUP}}(y^S, \hat{y}^S; \Theta) + \beta \mathcal{L}_{G,\text{RECON}}(\mathbf{W}, \hat{\mathbf{W}}; \Theta) + \gamma \mathcal{L}_{\text{REG}}(\Theta)$$

GraphEDM (Chami et al.) is a unifying framework that expresses virtually all graph representation learning methods — shallow embeddings, matrix factorisation, skip-gram walks, label propagation, and graph neural networks — through a common encoder/decoder vocabulary, with supervision signal $S \in \{N, E, G\}$ for node, edge, or graph labels.

### Why it matters
Having a single formal vocabulary lets practitioners compare methods by their choices of encoder architecture, decoder function, similarity transformation $s(\mathbf{W})$, and loss hyperparameters $\alpha,\beta,\gamma$, rather than treating each method as a separate algorithm. It also clarifies the transductive vs. inductive distinction and unsupervised vs. supervised regimes within one notation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[elbo]] — uses
- [[variational-autoencoder]] — uses
- [[graph-neural-networks]] — generalizes
- [[node-embedding]] — generalizes
[To be populated during integration]