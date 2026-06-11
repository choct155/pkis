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
- deep-learning
- representation-learning
- semi-supervised-learning
id: pkis:technique:greedy-layer-wise-unsupervised-pretraining
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch15
tags:
- pretraining
- unsupervised
- initialization
- regularization
- deep-networks
- historical
title: Greedy Layer-Wise Unsupervised Pretraining
understanding: 0
---

## Definition
A two-phase training procedure in which each layer $k$ of a deep network is trained independently with an unsupervised objective (e.g., RBM, sparse autoencoder) while all lower layers are held fixed, followed by supervised fine-tuning of the full network:
$$\theta^{(k)*} = \arg\min_{\theta^{(k)}} \mathcal{L}_{\text{unsup}}\!\left(h^{(k)}; \theta^{(k)}\right), \quad \text{with } h^{(k)} = f_{\theta^{(k)}}(h^{(k-1)}).$$
The pretrained weights serve as a warm-start initialization that places the network in a more favourable region of parameter space before supervised training.

### Why it matters
Historically enabled the first successful training of fully connected deep networks (Hinton et al., 2006; Bengio et al., 2007), sparking the 2006 deep learning renaissance. Acts simultaneously as a regularizer (reduces variance of final solutions, constrains parameters to a consistent region of function space) and as an informed initializer. Still influential via its generalization to supervised pretraining and transfer learning for NLP word embeddings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]