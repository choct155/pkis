---
aliases: []
also_type: []
applies:
- hidden-markov-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- forward-backward-algorithm
- forwards-backwards-algorithm
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- probabilistic-graphical-models
- speech-recognition
id: pkis:technique:viterbi-algorithm
instantiates:
- max-product-algorithm
- viterbi-for-hmm
- mpm-map-mpe-estimators
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
- murphy-pml2-advanced-ch09
specializes:
- max-product-belief-propagation
tags:
- HMM
- decoding
- max-sum
- dynamic-programming
- MAP-sequence
title: Viterbi Algorithm
understanding: 0
uses:
- trellis
---

## Definition
$$\omega(z_{n+1}) = \ln p(x_{n+1}|z_{n+1}) + \max_{z_n}\{\ln p(z_{n+1}|z_n) + \omega(z_n)\}$$

initialized at $\omega(z_1)=\ln p(z_1)+\ln p(x_1|z_1)$, with the most probable state sequence recovered by back-tracking the stored argmax indices $\psi(k_{n+1})$.

A max-sum dynamic-programming algorithm that finds the single most probable hidden-state sequence in an HMM (or any chain-structured model) in $O(K^2 N)$ time, in contrast to the $O(K^N)$ cost of exhaustive enumeration.

### Why it matters
The most-probable sequence differs in general from the sequence of individually most-probable states (obtained from $\gamma(z_n)$); only the Viterbi algorithm guarantees a globally consistent, jointly most-probable path. Widely used in speech recognition for phoneme decoding and in genomics for gene prediction. Because it works in log-space, no scaling factors are needed.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mpm-map-mpe-estimators]] — instantiates
- [[trellis]] — uses
- [[max-product-belief-propagation]] — specializes
- [[viterbi-for-hmm]] — instantiates
- [[forwards-backwards-algorithm]] — contrasts-with: Viterbi finds MAP path; FB finds posterior marginals
- [[forward-backward-algorithm]] — contrasts-with
- [[max-product-algorithm]] — instantiates
- [[hidden-markov-model]] — applies
[To be populated during integration]