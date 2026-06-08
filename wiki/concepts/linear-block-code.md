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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:linear-block-code
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch11
tags:
- coding-theory
- parity-check
- generator-matrix
- block-code
- mackay
title: Linear Block Code
understanding: 0
---

## Definition
An $(N,K)$ **block code** is a list of $S=2^K$ length-$N$ codewords; a message $\mathbf{s}\in\{1,\dots,2^K\}$ is sent as codeword $\mathbf{x}^{(s)}$. The code is **linear** if its codewords form a $K$-dimensional subspace of $\mathcal{A}_X^N$. Encoding is then a matrix product
$$\mathbf{t}=\mathbf{G}^{\mathsf T}\mathbf{s}\bmod 2,$$
and the codewords are exactly the solutions of
$$\mathbf{H}\mathbf{t}=\mathbf{0}\bmod 2,$$
where $\mathbf{G}$ is the generator matrix and $\mathbf{H}$ the **parity-check matrix**.

### Coverage and difficulty
Most established codes — Hamming, BCH, Reed–Müller, Reed–Solomon, Goppa, and the modern low-density parity-check codes — are linear. Linearity makes *encoding* trivially cheap, and the noisy-channel coding theorem still holds for linear codes (non-constructively). But maximum-likelihood *decoding* of a general linear code is **NP-complete**, so practical effort focuses on families with fast decoders.

### Why it matters
Linearity is the organizing principle of almost all real error-correcting codes: it reduces the encoder to a matrix multiply and reframes decoding around the parity-check structure (syndromes), making it the foundation on which Hamming codes, syndrome decoding, and LDPC codes are built.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]