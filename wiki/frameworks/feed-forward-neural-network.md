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
contrasts-with:
- curse-of-dimensionality
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- machine-learning
- neural-networks
generalizes:
- basis-function-models
id: pkis:framework:feed-forward-neural-network
instantiates:
- multilayer-perceptron
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
- nielsen-nndl-ch04
tags:
- mlp
- universal-approximation
- supervised-learning
- architecture
title: Feed-Forward Neural Network (MLP)
understanding: 0
uses:
- activation-functions
- universal-approximation-theorem-nn
- backpropagation
---

## Definition
$$y_k(\mathbf{x}, \mathbf{w}) = f_k\!\left(\sum_{j=0}^{M} w_{kj}^{(2)}\, h\!\left(\sum_{i=0}^{D} w_{ji}^{(1)} x_i\right)\right)$$

A two-layer adaptive basis-function model in which $M$ hidden units compute nonlinear functions $z_j = h(a_j)$ of learned linear projections of the input, and $K$ output units apply a task-appropriate activation $f_k$ to linear combinations of the hidden activations. All weights $\mathbf{w}$ are learned jointly.

### Why it matters
Universal approximation: a single hidden layer with sufficiently many sigmoidal units can uniformly approximate any continuous function on a compact domain, combining representational power with gradient-based trainability via backpropagation. The architecture is the canonical workhorse of supervised deep learning.

### Key design choices
| Task | Output activation | Error function |
|---|---|---|
| Regression | Identity | Sum-of-squares |
| Binary classification | Logistic sigmoid | Cross-entropy |
| Multiclass | Softmax | Multiclass cross-entropy |

Bias parameters are absorbed by appending a constant input $x_0=1$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[basis-function-models]] — generalizes
- [[curse-of-dimensionality]] — contrasts-with
- [[backpropagation]] — uses
- [[universal-approximation-theorem-nn]] — uses
- [[activation-functions]] — uses
- [[multilayer-perceptron]] — instantiates
[To be populated during integration]