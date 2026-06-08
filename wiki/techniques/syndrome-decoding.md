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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:technique:syndrome-decoding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch01
tags:
- error-correcting-codes
- parity-check-matrix
- maximum-likelihood-decoding
- linear-block-code
- channel-coding
title: Syndrome Decoding
understanding: 0
---

## Definition
An efficient maximum-likelihood decoder for linear block codes. Given received vector $\mathbf{r}=\mathbf{t}+\mathbf{n}$ (mod 2), compute the **syndrome**
$$\mathbf{z}=\mathbf{H}\mathbf{r}=\mathbf{H}\mathbf{n},$$
where $\mathbf{H}$ is the parity-check matrix and codewords satisfy $\mathbf{H}\mathbf{t}=\mathbf{0}$. The syndrome depends only on the noise, not the message, and points to the most probable error pattern $\mathbf{n}$ solving $\mathbf{H}\mathbf{n}=\mathbf{z}$.

The intuition: the syndrome is the pattern of violated parity checks — a compact fingerprint of the error rather than a comparison against every codeword.

### For the (7,4) Hamming code
Three parity checks give $2^3=8$ syndromes: the all-zero syndrome (no action) plus seven non-zero syndromes, each mapped to flipping exactly one suspect bit. This replaces a search over all sixteen codewords with one matrix multiply and a table lookup.

### Why it matters
Syndrome decoding turns optimal decoding from brute-force codeword comparison ($O(2^K)$) into a linear computation, making linear codes practical. It frames decoding as the inference problem 'find the most probable noise given the syndrome', a theme carried into belief-propagation decoding of modern sparse-graph codes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]