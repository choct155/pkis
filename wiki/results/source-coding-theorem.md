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
- essential-bit-content
- prefix-code
---

## Definition
$N$ i.i.d. outcomes from a source $X$ can be losslessly compressed into about $NH(X)$ bits (and no fewer) as $N\to\infty$: the entropy $H(X)$ is the fundamental limit of lossless compression, in bits per symbol. More precisely, for any $\epsilon,\delta$, for large enough $N$ one can encode blocks at $H+\epsilon$ bits/symbol with error probability $<\delta$, and compression below $H$ is impossible with vanishing error.

### Mechanism — via the typical set
The proof rests on **typicality**: almost all probability sits on $\approx 2^{NH}$ typical strings, each of probability $\approx 2^{-NH}$. So you only need to assign codewords to the typical set — $\log_2(2^{NH}) = NH$ bits — and accept negligible error on the rest. The law of large numbers / Chebyshev's inequality (MacKay §4.5) make "almost all" precise.

### Why it matters
It establishes entropy as a physically meaningful limit, not just a formula. It is *instantiated* by practical codes — Huffman (symbol codes) and arithmetic coding (stream codes) — which approach $H$ bits/symbol. It is the data-compression half of Shannon's program; the noisy-channel coding theorem is the transmission half.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[prefix-code]] — uses: Thm 5.1 constructs a prefix code with lengths ceil(log 1/p_i) attaining L<H+1.
- [[essential-bit-content]] — uses: The theorem is phrased as the convergence of the essential bit content per symbol to the entropy.
- [[shannon-information-content]] — uses: Optimal codeword length ≈ h(x)
- [[entropy]] — uses: Entropy H is the fundamental compression limit
- [[typical-set]] — uses: Proof: code only the ~2^{NH} typical strings
[To be populated during integration]

## Converse — the two-sided bound
The theorem has two distinct halves. **Part 1** ($\tfrac1N H_\delta(X^N) < H+\epsilon$): even for vanishingly small permitted error $\delta$, the bits/symbol need not exceed $H+\epsilon$. **Part 2 / converse** ($\tfrac1N H_\delta(X^N) > H-\epsilon$): even for $\delta$ close to 1 (errors most of the time!), you still cannot get below $H-\epsilon$ bits/symbol. Together: the answer is $H$, no more and no less, regardless of error tolerance.

## Source coding theorem for symbol codes
**Symbol-code form (MacKay Thm 5.1).** For an ensemble $X$ there exists a prefix code with $H(X)\le L(C,X) < H(X)+1$. Proof: set $l_i=\lceil\log_2(1/p_i)\rceil$; these satisfy Kraft since $\sum_i 2^{-\lceil\log_2(1/p_i)\rceil}\le\sum_i p_i=1$, so a prefix code exists, and $L < H(X)+1$. The lower bound $L\ge H(X)$ holds for any uniquely decodable code (Gibbs + Kraft).