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
date_updated: '2026-06-20'
domain:
- machine-learning
- artificial-intelligence
extends:
- representation-learning
- connectionism
id: pkis:framework:deep-learning
instantiates:
- data-driven-ai
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
- goodfellow-deeplearning
- nielsen-nndl-ch06
specializes:
- neural-networks
tags:
- neural-networks
- representation-learning
- hierarchical-features
- deep-learning
title: Deep Learning
understanding: 0
uses:
- multilayer-perceptron
- backpropagation
- stochastic-gradient-descent
- supervised-learning
- unsupervised-learning
- convolutional-neural-networks
- lstm
- deep-reinforcement-learning
---

## Definition
$$\hat{y} = f^{(L)}(f^{(L-1)}(\cdots f^{(1)}(\mathbf{x})))$$

Deep learning is an approach to machine learning that represents the world as a **nested hierarchy of concepts**, where each concept is defined in terms of simpler ones and more abstract representations are computed from less abstract ones via a composition of learned functions across multiple layers.

### Why it matters
By stacking learned transformations, deep learning sidesteps the need for hand-engineered features: the hierarchy itself discovers which intermediate representations are most useful, enabling systems to tackle raw sensory inputs (pixels, waveforms) end-to-end with state-of-the-art accuracy on vision, speech, and language tasks.

### Depth interpretations
Depth can be measured either as the length of the longest computational path (flow-chart depth) or as the depth of the probabilistic-concept graph describing how latent concepts relate. These two measures can differ substantially for the same architecture.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[deep-reinforcement-learning]] — uses
- [[lstm]] — uses
- [[convolutional-neural-networks]] — uses
- [[unsupervised-learning]] — uses
- [[supervised-learning]] — uses
- [[data-driven-ai]] — instantiates: Deep learning is the preeminent instantiation of the data-driven AI principle.
- [[connectionism]] — extends: Deep learning grew out of the connectionist movement of the 1980s.
- [[stochastic-gradient-descent]] — uses: SGD and its variants are the standard optimizers for deep learning.
- [[backpropagation]] — uses: Backpropagation is the dominant algorithm for training deep networks.
- [[neural-networks]] — specializes: Deep learning is a subfield of neural network research focused on depth and hierarchical representations.
- [[multilayer-perceptron]] — uses: The MLP / feedforward deep network is the canonical deep learning architecture.
- [[representation-learning]] — extends: Deep learning is a specific approach to representation learning that uses hierarchical composition of learned functions.
[To be populated during integration]