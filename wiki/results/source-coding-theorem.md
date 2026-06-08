---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
- statistical-learning
id: pkis:result:source-coding-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch04
tags:
- source-coding
- data-compression
- entropy
- shannon
- lossless-compression
- typical-set
title: Source Coding Theorem (Shannon's First Theorem)
understanding: 0
uses:
- typical-set
- entropy
- shannon-information-content
---

## Definition
$N$ i.i.d. outcomes from a source $X$ can be losslessly compressed into about $NH(X)$ bits (and no fewer) as $N\to\infty$: the entropy $H(X)$ is the fundamental limit of lossless compression, in bits per symbol. More precisely, for any $\epsilon,\delta$, for large enough $N$ one can encode blocks at $H+\epsilon$ bits/symbol with error probability $<\delta$, and compression below $H$ is impossible with vanishing error.

## Mechanism — via the typical set
The proof rests on **typicality**: almost all probability sits on $\approx 2^{NH}$ typical strings, each of probability $\approx 2^{-NH}$. So you only need to assign codewords to the typical set — $\log_2(2^{NH}) = NH$ bits — and accept negligible error on the rest. The law of large numbers / Chebyshev's inequality (MacKay §4.5) make "almost all" precise.

## Why it matters
It establishes entropy as a physically meaningful limit, not just a formula. It is *instantiated* by practical codes — Huffman (symbol codes) and arithmetic coding (stream codes) — which approach $H$ bits/symbol. It is the data-compression half of Shannon's program; the noisy-channel coding theorem is the transmission half.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[shannon-information-content]] — uses: Optimal codeword length ≈ h(x)
- [[entropy]] — uses: Entropy H is the fundamental compression limit
- [[typical-set]] — uses: Proof: code only the ~2^{NH} typical strings
[To be populated during integration]