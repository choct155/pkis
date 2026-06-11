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
- deep-learning
- sequence-modeling
- NLP
id: pkis:framework:encoder-decoder-seq2seq
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
- goodfellow-deeplearning-ch12
tags:
- RNN
- machine-translation
- encoder
- decoder
- context-vector
- seq2seq
title: Encoder-Decoder (Sequence-to-Sequence) Architecture
understanding: 0
---

## Definition
An **encoder-decoder** (seq2seq) architecture maps a variable-length input sequence $(x^{(1)},\ldots,x^{(n_x)})$ to a variable-length output sequence $(y^{(1)},\ldots,y^{(n_y)})$ via two coupled RNNs:
1. **Encoder RNN** reads the full input and produces a fixed-size context vector $C$ (typically the final hidden state $h^{(n_x)}$).
2. **Decoder RNN** is conditioned on $C$ and generates the output sequence token by token.

The model is trained jointly to maximize $\log P(y^{(1)},\ldots,y^{(n_y)}\mid x^{(1)},\ldots,x^{(n_x)})$ over all training pairs. The key innovation over fixed-length I/O architectures is that $n_x \neq n_y$ is permitted.

### Why it matters
Introduced by Cho et al. (2014) and Sutskever et al. (2014), seq2seq became the dominant paradigm for machine translation, summarization, and speech recognition. A core limitation — the fixed-size bottleneck $C$ struggles with long inputs — motivated the attention mechanism (Bahdanau et al., 2015) and eventually the Transformer.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]