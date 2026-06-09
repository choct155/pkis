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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
id: pkis:framework:sequence-to-sequence-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch24
tags:
- nlp
- machine-translation
- encoder-decoder
- attention
- rnn
title: Sequence-to-Sequence Model
understanding: 0
---

## Definition
A neural architecture that maps an input sequence to an output sequence of possibly different length, using an encoder network to read the source into a representation and a decoder network to generate the target one token at a time, each output conditioned on the entire source and all previously generated outputs. The basic form (Sutskever et al. 2015) couples two RNNs: the encoder's final hidden state initializes the decoder. This breaks the one-to-one tagging assumption, supporting word reordering and length mismatch (e.g. 'caballo de mar' to 'seahorse'). Basic seq2seq suffers three weaknesses: nearby-context bias (recent source words dominate the fixed hidden state), fixed-context-size limit (the whole source is compressed into one vector), and slow sequential processing. The attentional variant addresses the first two: at each decoding step the decoder computes attention scores r_ij = h_{i-1}.s_j over all source hidden states s_j, normalizes them with a softmax into weights a_ij, and forms a context vector c_i = sum_j a_ij s_j that is concatenated to the decoder input. This 'context-based summarization' is differentiable (gradients flow back to both RNNs even though attention has no weights of its own), lets the model attend to any source position, and yields human-interpretable word alignments. Used for machine translation, image captioning, summarization, and question answering.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]