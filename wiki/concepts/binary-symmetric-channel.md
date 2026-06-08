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
id: pkis:concept:binary-symmetric-channel
instantiates:
- information-theory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch01
tags:
- channel
- noise
- bsc
- error-probability
- communication
- channel-capacity
title: Binary Symmetric Channel
understanding: 0
uses:
- entropy
---

## Definition
The binary symmetric channel (BSC) is the simplest model of a noisy communication channel: each transmitted bit is flipped independently with probability $f$ (the noise level) and received correctly with probability $1-f$:
$$P(y{=}1\mid x{=}0)=P(y{=}0\mid x{=}1)=f,\qquad P(y{=}0\mid x{=}0)=P(y{=}1\mid x{=}1)=1-f.$$
It is *symmetric* because the flip probability is identical for both input symbols.

### Capacity
Its capacity is $C = 1 - H_2(f)$ bits per channel use, where $H_2(f)=f\log_2\tfrac1f+(1-f)\log_2\tfrac1{1-f}$ is the binary entropy function. The noisy-channel coding theorem says reliable communication is achievable at any rate $R<C$ and impossible above it — so even a very noisy channel ($f$ close to but below $1/2$) still carries information.

### Why it matters
The BSC is the canonical testbed of information theory. MacKay frames the book's central engineering problem — achieving arbitrarily reliable communication over an unreliable channel — on it, and every error-correcting code in the book (Hamming, LDPC, turbo, fountain) is first understood as a strategy for the BSC.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[information-theory]] — instantiates: The BSC is the canonical channel on which information theory's communication problem is posed.
- [[entropy]] — uses: Channel capacity 1 - H_2(f) is defined via the binary entropy function.
[To be populated during integration]

## MacKay's framing
MacKay uses the BSC as the running model for a noisy disk drive: each bit is correct with probability $1-f$ and flipped with probability $f$. He frames the noise as a sparse vector $\mathbf{n}$ added mod 2, so the received vector is $\mathbf{r}=\mathbf{t}+\mathbf{n}$ — recasting decoding as inferring the most probable noise pattern.