---
aliases: []
also_type: []
applies:
- machine-translation
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
- NLP
- sequence-modelling
extends:
- encoder-decoder-seq2seq
id: pkis:technique:attention-mechanism
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- transformer-attention-mechanisms
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
tags:
- alignment
- machine-translation
- RNN
- transformer
- soft-attention
title: Attention Mechanism (Soft Alignment)
understanding: 0
uses:
- neural-language-model
---

## Definition
In the attention mechanism of Bahdanau et al. (2015), the decoder at step $t$ computes a context vector $\mathbf{c}_t$ as a weighted sum of encoder hidden states $\{\mathbf{h}_s\}$:
$$\mathbf{c}_t = \sum_s \alpha_{t,s}\,\mathbf{h}_s, \quad \alpha_{t,s} = \frac{\exp(e_{t,s})}{\sum_{s'}\exp(e_{t,s'})},$$
where the alignment score $e_{t,s} = a(\mathbf{d}_{t-1}, \mathbf{h}_s)$ is computed by a small learnable scoring function $a$ (e.g., an MLP or dot product). The weights $\alpha_{t,s}$ form a soft, differentiable distribution over source positions, allowing the model to 'focus' on relevant source tokens when generating each target token.

### Why it matters
Solves the information bottleneck of fixed-size context vectors for long sequences; enables end-to-end differentiable alignment learning; and is the key conceptual precursor to the Transformer's self-attention, making it one of the most influential architectural innovations in deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[machine-translation]] — applies
- [[neural-language-model]] — uses
- [[transformer-attention-mechanisms]] — prerequisite-of
- [[encoder-decoder-seq2seq]] — extends
[To be populated during integration]