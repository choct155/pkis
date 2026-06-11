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
- end-to-end-learning
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- speech-synthesis
- generative-models
id: pkis:framework:wavenet
instantiates:
- autoregressive-model-arm
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- WaveNet
- audio-generation
- dilated-convolution
- causal-convolution
- TTS
- autoregressive
title: WaveNet (Dilated Causal CNN for Audio)
understanding: 0
uses:
- causal-convolution
---

## Definition
WaveNet is a conditional autoregressive model $p(x \mid c)$ for raw audio, where $c$ is linguistic/conditioning features and $x$ is a sequence of audio samples. It stacks **dilated causal convolutions** with exponentially increasing dilation rates $d = 1, 2, 4, \ldots, 2^{L-1}$ to achieve a large receptive field while keeping the network depth manageable:
$$h_t^{(l)} = \text{tanh}\!\left(W_{f,l} * x_{t-d_l}\right) \odot \sigma\!\left(W_{g,l} * x_{t-d_l}\right).$$
Generation is sequential ($O(T)$) but training is fully parallel.

### Why it matters
WaveNet set the state of the art in text-to-speech at its introduction (2016), demonstrating that raw waveform autoregressive models can surpass concatenative/parametric TTS. It established dilated causal convolutions as a canonical building block for sequential generative models and inspired Tacotron (end-to-end TTS) and parallel WaveNet (distilled fast sampler).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[end-to-end-learning]] — contrasts-with: Tacotron is end-to-end (words→audio); WaveNet takes linguistic features as input
- [[autoregressive-model-arm]] — instantiates
- [[causal-convolution]] — uses
[To be populated during integration]