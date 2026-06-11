---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- machine-learning
id: pkis:result:nn-size-doubling-trend
instantiates:
- scaling-laws
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
specializes:
- neural-scaling-laws
tags:
- scaling
- hardware
- historical-trends
- model-size
title: 'Scaling Law: Neural Network Size Doubling'
understanding: 0
---

## Definition
Empirically, **the number of neurons (or parameters) in state-of-the-art neural networks has roughly doubled every 2.4 years** since the introduction of hidden units, a trend analogous to Moore's law for transistor counts.

This is an observational regularity documented across decades of benchmark architectures, from the Perceptron (1958) through GoogLeNet (2014).

### Why it matters
The trend implies that raw scale — driven by faster hardware (CPUs → GPUs → TPUs), larger memory, and distributed computing — is a primary driver of capability improvement, independent of algorithmic innovation. It grounds the empirical forecasting that artificial networks will not reach human-brain neuron counts until at least the 2050s under current trajectories.

### Caveat
Simple neuron-count comparisons ignore architectural differences, connection density, and the representational complexity of individual biological vs. artificial neurons.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[scaling-laws]] — instantiates
- [[neural-scaling-laws]] — specializes: The ~2.4-year doubling of network size is an early empirical scaling law for neural networks.
[To be populated during integration]