---
aliases: []
also_type: []
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
- nlp
id: pkis:concept:encoder-decoder-architecture
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch15
tags:
- seq2seq
- machine-translation
- attention
- architecture
title: Encoder–Decoder Architecture
understanding: 0
---

## Definition
A neural network design pattern for sequence-to-sequence tasks in which an **encoder** $f_e$ maps a variable-length input $x_{1:T}$ to a fixed-dimensional context vector $\mathbf{c} = f_e(x_{1:T})$, and a **decoder** $f_d$ autoregressively generates the output $y_{1:T'}$ conditioned on $\mathbf{c}$:

$$p(y_{1:T'}|x_{1:T}) = \prod_{t=1}^{T'} p(y_t | y_{1:t-1}, \mathbf{c})$$

The encoder and decoder are typically RNNs, CNNs, or Transformer stacks; the context can be a single vector (bottleneck) or a set of vectors augmented with attention.

### Why it matters
The encoder–decoder pattern decouples input and output lengths and is the foundation of neural machine translation, abstractive summarization, and speech recognition. The information bottleneck of a single context vector motivates attention mechanisms, which replace $\mathbf{c}$ with a dynamic, query-dependent mixture of encoder states.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]