---
aliases: []
also_type: []
applies:
- vanishing-exploding-gradients-rnn
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
extends:
- lstm
- leaky-units-multiscale-rnn
generalizes:
- gated-recurrent-unit
id: pkis:framework:long-short-term-memory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
tags:
- gated-RNN
- cell-state
- forget-gate
- long-term-dependencies
- LSTM
title: Long Short-Term Memory (LSTM)
understanding: 0
uses:
- backpropagation-through-time
---

## Definition
The **LSTM** (Hochreiter & Schmidhuber, 1997) is a gated RNN cell with a dedicated cell state $s_i^{(t)}$ that carries information across time via a learnable, context-dependent self-loop, preventing gradient vanishing over long sequences.

Core update equations:
$$f_i^{(t)} = \sigma\!\left(b_i^f + U^f x^{(t)} + W^f h^{(t-1)}\right) \quad\text{(forget gate)}$$
$$g_i^{(t)} = \sigma\!\left(b_i^g + U^g x^{(t)} + W^g h^{(t-1)}\right) \quad\text{(input gate)}$$
$$s_i^{(t)} = f_i^{(t)} s_i^{(t-1)} + g_i^{(t)}\,\sigma\!\left(b_i + U x^{(t)} + W h^{(t-1)}\right)$$
$$q_i^{(t)} = \sigma\!\left(b_i^o + U^o x^{(t)} + W^o h^{(t-1)}\right) \quad\text{(output gate)}$$
$$h_i^{(t)} = \tanh\!\left(s_i^{(t)}\right) q_i^{(t)}$$

The forget gate $f_i^{(t)}$ controls how much of the previous cell state is retained; the input gate $g_i^{(t)}$ controls how much new information is written; the output gate $q_i^{(t)}$ filters the cell state for the hidden output.

### Why it matters
LSTMs achieve near-constant error flow through the cell-state highway, enabling learning of dependencies spanning hundreds of steps — a major advance over vanilla RNNs. They underpinned state-of-the-art results in speech recognition, machine translation, and language modeling through the 2010s and remain widely used today.

### Key ablation findings
Greff et al. (2015) and Jozefowicz et al. (2015) show the forget gate is the most critical component; initializing its bias to 1 (Gers et al., 2000) significantly helps.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gated-recurrent-unit]] — generalizes
- [[backpropagation-through-time]] — uses
- [[leaky-units-multiscale-rnn]] — extends: LSTM generalises leaky units with context-dependent gating
- [[vanishing-exploding-gradients-rnn]] — applies: LSTM solves the vanishing gradient problem via gated cell-state highway
- [[lstm]] — extends: lstm existing node is a stub; this node provides full LSTM definition
[To be populated during integration]