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
- speech-recognition
- sequence-modeling
id: pkis:concept:left-to-right-hmm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
tags:
- HMM
- left-to-right
- speech
- handwriting
- constrained
title: Left-to-Right HMM
understanding: 0
---

## Definition
A constrained Hidden Markov Model in which the transition matrix $A$ is upper-triangular ($A_{jk}=0$ for $k<j$) and the initial distribution is concentrated on state 1 ($p(z_{11})=1$). Transitions may be further restricted to $A_{jk}=0$ for $k>j+\Delta$.

This forces all state trajectories to progress monotonically through states $1,2,\ldots,K$, preventing the model from revisiting earlier states.

### Why it matters
Critical for applications where the underlying process is inherently sequential and non-repeating, such as speech recognition (phoneme sequences) and on-line handwriting recognition (pen-stroke stages). The monotonic constraint also provides invariance to local time-axis warping (compression/stretching of segments), because variations in relative segment durations are absorbed by varying the number of self-transitions ($A_{kk}$) vs. forward transitions ($A_{k,k+1}$). Zero-initialized elements remain zero under EM updates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]