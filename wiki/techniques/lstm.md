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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
id: pkis:technique:lstm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch21
tags:
- recurrent-network
- gating
- memory-cell
- long-range-dependencies
title: Long Short-Term Memory (LSTM)
understanding: 0
---

## Definition
A specialized recurrent neural network architecture (Hochreiter & Schmidhuber, 1997) designed to preserve information over many time steps and mitigate vanishing/exploding gradients. Its long-term memory component, the memory cell c, is copied essentially unchanged from step to step and updated additively rather than multiplicatively, so gradient contributions do not accumulate multiplicatively over time. Information flow is controlled by soft gating units in [0,1] obtained as sigmoid outputs of the current input and previous hidden state: the forget gate f determines whether each memory element is retained or reset; the input gate i determines whether each element is updated additively from the current input; the output gate o determines whether each element is transferred to the short-term state z. The update equations use elementwise multiplication: c_t = c_{t-1} ⊙ f_t + i_t ⊙ tanh(W_{x,c} x_t + W_{z,c} z_{t-1}); z_t = tanh(c_t) ⊙ o_t. LSTMs were among the first practically usable RNNs and excel at speech recognition, handwriting recognition, and language tasks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]