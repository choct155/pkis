---
aliases: []
also_type: []
analogous-to:
- recurrent-neural-network
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- probabilistic-inference
extends:
- mean-field-variational-inference
id: pkis:concept:mean-field-recurrent-network-connection
instantiates:
- sparse-coding
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
tags:
- recurrent-networks
- mean-field
- explaining-away
- sparse-coding
- LISTA
title: Mean Field Fixed-Point Equations as Recurrent Networks
understanding: 0
uses:
- explaining-away
---

## Definition
For binary sparse coding under mean field, the fixed-point update for variational parameter $\hat{h}_i$ is:

$$\hat{h}_i = \sigma\!\left(b_i + \left(\mathbf{v} - \sum_{j \neq i}\mathbf{W}_{:,j}\hat{h}_j\right)^\top\!\boldsymbol{\beta}\mathbf{W}_{:,i} - \tfrac{1}{2}\mathbf{W}_{:,i}^\top\boldsymbol{\beta}\mathbf{W}_{:,i}\right)$$

Iterating this update over $i=1,\dots,m$ and cycling until convergence defines a **recurrent neural network** whose dynamics implement posterior inference. At each step, unit $i$ encodes the residual $\mathbf{v} - \sum_{j\neq i}\mathbf{W}_{:,j}\hat{h}_j$, implementing competitive (explaining-away) inhibition between units whose weight vectors are aligned.

### Why it matters
This connection reveals that inference in graphical models and computation in recurrent networks are two descriptions of the same process. It motivates architectures such as LISTA that unroll a fixed number of mean-field iterations into a feedforward network and train the weights end-to-end. It also clarifies how the mean field approximation handles explaining away: two competing units inhibit each other, but the factorial $q$ forces the approximation to collapse to a single mode rather than capturing the true bimodal posterior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sparse-coding]] — instantiates
- [[explaining-away]] — uses
- [[recurrent-neural-network]] — analogous-to
- [[mean-field-variational-inference]] — extends
[To be populated during integration]