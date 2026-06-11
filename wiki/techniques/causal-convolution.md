---
aliases: []
also_type: []
applies:
- language-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- recurrent-neural-network
- teacher-forcing
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- sequence-models
extends:
- convolutional-neural-networks
id: pkis:technique:causal-convolution
instantiates:
- autoregressive-model
- autoregressive-model-arm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch15
- murphy-pml2-advanced-ch22
specializes:
- convolutional-neural-networks
tags:
- cnn
- autoregressive
- wavenet
- generation
- dilated-convolution
title: Causal (Masked) Convolution
understanding: 0
---

## Definition
A causal 1-d convolution restricts each output $y_t$ to depend only on past inputs $y_{1:t-1}$ by masking out future positions in the convolutional filter:

$$p(\mathbf{y}) = \prod_{t=1}^T p(y_t | y_{1:t-1}) = \prod_{t=1}^T \text{Cat}\!\left(y_t \,\Big|\, \text{softmax}\!\left(\varphi\!\left(\sum_{\tau=1}^{t-k} \mathbf{w}^\top \mathbf{y}_{\tau:\tau+k}\right)\right)\right)$$

Long-range dependencies are captured by stacking dilated causal convolutions with exponentially increasing dilation rates (1, 2, 4, …, 512), as in WaveNet.

### Why it matters
Causal convolutions provide a fully parallel training procedure (unlike RNNs) while guaranteeing the autoregressive property required for valid generative models. Stacking $L$ dilated layers gives an effective receptive field of $O(2^L)$ without depth proportional to sequence length, making them practical for raw audio generation (WaveNet) and fast text generation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[autoregressive-model-arm]] — instantiates
- [[convolutional-neural-networks]] — extends: Causal convolution is a CNN with a future-masking constraint
- [[teacher-forcing]] — contrasts-with: Causal CNNs avoid teacher forcing's exposure bias by design
- [[recurrent-neural-network]] — contrasts-with
- [[language-model]] — applies
- [[autoregressive-model]] — instantiates
- [[convolutional-neural-networks]] — specializes
[To be populated during integration]