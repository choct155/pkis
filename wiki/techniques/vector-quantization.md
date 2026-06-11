---
aliases: []
also_type: []
analogous-to:
- source-coding-theorem
applies:
- k-means-clustering
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-01'
date_updated: '2026-06-02'
domain:
- deep-learning
id: pkis:technique:vector-quantization
instantiates:
- vector-quantization-clustering
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- '[[oord-neural-2017]]'
tags:
- vq-vae
- discrete-representations
- codebook
title: Vector Quantization
understanding: 0
uses:
- source-coding-theorem
- k-means-algorithm
- information-theory
---

## Definition
Mapping continuous vectors to a finite learned codebook of discrete codes (VQ-VAE), enabling discrete representation learning — the foundational technique for learning symbolic abstractions from data.

## Reading Path
- [[oord-neural-2017]] — canonical source

## Connections
- [[vector-quantization-clustering]] — instantiates
- [[source-coding-theorem]] — analogous-to
- [[information-theory]] — uses: connects to rate-distortion theory
- [[k-means-algorithm]] — uses
- [[source-coding-theorem]] — uses: variable-length codeword coding lowers the rate toward the codeword entropy
- [[k-means-clustering]] — applies: VQ codebook construction is K-means (Lloyd's algorithm) on image blocks
[To be populated during integration]

## Needs Canonical Source
Resolved — canonical source(s) attached above.