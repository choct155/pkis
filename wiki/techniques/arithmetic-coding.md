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
id: pkis:technique:arithmetic-coding
instantiates:
- source-coding-theorem
- stream-codes
- compression-as-probabilistic-modelling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch06
tags:
- stream-codes
- data-compression
- adaptive
- probabilistic-modeling
title: Arithmetic Coding
understanding: 0
---

## Definition
A stream code that encodes an entire sequence as a single number in $[0,1)$, by recursively subdividing the interval in proportion to a probabilistic model's predictions for each successive symbol. The final interval has width $\approx P(\text{whole sequence})$, so it can be named with $\approx \log_2 1/P = \sum_i h(x_i)$ bits — the total Shannon information content.

### Why it beats Huffman
It escapes the integer-bits-per-symbol limit: a symbol of probability $0.99$ costs $\approx 0.015$ bits, not a whole bit. It also cleanly separates the **model** (which supplies $P(\text{next symbol} \mid \text{context})$) from the **coder**, so any adaptive or context-dependent probabilistic model plugs in — the coder is provably near-optimal for whatever model it is given. This model/coder split is why it underlies modern compressors.

### Why it matters
The practical realization of the source coding theorem's promise: compression to essentially $H$ bits/symbol for an arbitrary, even adaptive, source model. Connects compression directly to probabilistic modeling / prediction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[compression-as-probabilistic-modelling]] — instantiates: Arithmetic coding turns any predictive distribution into a code of length ~ log2 1/P.
- [[stream-codes]] — instantiates: Arithmetic coding is a stream code: maps a whole string to a sub-interval of [0,1) of size = its probability.
- [[source-coding-theorem]] — instantiates: Stream code; reaches ~H bits/symbol for arbitrary models
[To be populated during integration]

## Random sample generation and text entry
Run backwards, an arithmetic *decoder* fed with ordinary random bits selects a point uniformly in $[0,1)$ and hence draws a string from the model's distribution — a way to **generate random samples** using very nearly the minimum number of random bits possible. Inverting the coder also yields information-efficient text entry: in **Dasher** (Ward & MacKay), the user zooms into the unit interval to locate their intended string, with a language model sizing the intervals so probable text is fastest to reach.

## Near-optimality bound
The near-optimality is precise: terminating a message costs at most 2 bits over the ideal length $\log_2 1/P(x\mid H)$, so the expected length is within ~2 bits of the entropy of the whole message. Crucially, encoding $N$ letters requires computing only $N|A|$ conditional probabilities — one predictive distribution per context actually visited — versus a large-block Huffman code, which must evaluate probabilities of all possible blocks.