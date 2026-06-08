---
aliases: []
also_type: []
applies:
- binary-symmetric-channel
- channel-capacity
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
id: pkis:result:good-linear-codes-exist
instantiates:
- noisy-channel-coding-theorem
- source-coding-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch14
tags:
- linear-codes
- random-coding
- channel-capacity
- binary-symmetric-channel
- weight-enumerator
- existence-proof
title: Very Good Linear Codes Exist (Random Linear Codes Achieve Capacity)
understanding: 0
uses:
- typical-set-decoder
- typical-set
- syndrome-decoding
---

## Definition
For the binary symmetric channel with flip probability $f$, **almost all** linear codes are very good: for any rate
$$R < 1 - H_2(f),$$
there exist linear codes (defined by a parity-check matrix $\mathbf{H}$ with $R = 1 - M/N$) whose optimal-decoder error probability vanishes as the block length $N \to \infty$. Since $1 - H_2(f)$ is exactly the capacity of the BSC, linear codes alone suffice to achieve capacity — no nonlinear structure is needed.

### Proof strategy (the random-coding / averaging argument)
Rather than exhibit one good code, average performance over an ensemble of random matrices $\mathbf{H}$. Decoding reduces (via the syndrome $\mathbf{z} = \mathbf{Hx}$) to finding the noise $\mathbf{x}$. Using the easy-to-analyze typical-set decoder, the error splits into $P^{(\mathrm{I})}$ (true noise atypical, vanishes by the AEP) and $P^{(\mathrm{II})}$ (a second typical vector collides). The key ensemble fact: for any nonzero $\mathbf{v}$, $\langle \mathbb{1}[\mathbf{Hv}=0]\rangle_{\mathbf{H}} = 2^{-M}$. Hence
$$\bar{P}^{(\mathrm{II})}_{\text{TS}} \le |T|\,2^{-M} \approx 2^{NH(X)}2^{-M},$$
which vanishes iff $H(X) < M/N$, i.e. $R < 1 - H(X)$. If the *average* error vanishes, at least one code (indeed almost all) is good.

### Why it matters
This is a constructive-in-spirit, fully elementary proof of the noisy-channel coding theorem for the BSC, using only typical sets and the expected weight enumerator. It shows capacity is reachable within the structured, efficiently representable class of linear codes, and the same template (needing only an approximate expected weight enumerator) proves good-ness of practical families such as low-density parity-check codes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[channel-capacity]] — applies: Shows linear codes reach the BSC capacity C = 1 - H2(f).
- [[source-coding-theorem]] — instantiates: Re-read as uncompression, the same argument proves linear compressors attain the entropy limit.
- [[binary-symmetric-channel]] — applies: The achievable rate 1 - H2(f) equals the BSC capacity.
- [[syndrome-decoding]] — uses: Reception is reduced to recovering noise x from the syndrome z = Hx.
- [[typical-set]] — uses: Type-I error vanishes by the AEP; |T| ≈ 2^{NH(X)} controls the type-II bound.
- [[typical-set-decoder]] — uses: The proof bounds the analyzable typical-set decoder's error to show good codes exist.
- [[noisy-channel-coding-theorem]] — instantiates: Establishes the achievability half of the noisy-channel coding theorem for the BSC using linear codes.
[To be populated during integration]