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
contrasts-with:
- one-way-hash-function
- hamming-7-4-code
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
- computer-science
id: pkis:technique:hashing-for-error-detection
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch12
tags:
- error-detection
- checksum
- crc
- false-negative
- mackay-itila
title: Hashing for Error Detection
understanding: 0
---

## Definition
To confirm that two remote files are identical without transferring them, each party computes an $M$-bit hash of its file with the *same* hash function; equal hashes imply the files are almost surely equal.

### False-negative probability
If the hash is random and the corrupting process is independent of it, the probability of a **false negative** — the files differ yet the hashes agree — is
$$P(\text{false negative}) = 2^{-M}.$$
A 32-bit hash therefore misses a discrepancy with probability $\approx 10^{-10}$, so $M=32$ bits is plenty when errors are pure noise. The widely used **32-bit cyclic redundancy check (CRC)** is exactly this: a *linear* hash, a set of 32 parity-check bits analogous to the 3 parity bits of the (7,4) Hamming code.

### Detection versus correction
Detection is cheap; *correction* is far more expensive. To locate, say, 8 corrupted bits in a megabyte file requires at least $\log_2\binom{2^{23}}{8} \approx 180$ parity-check bits by the counting argument — vastly more than the 32 needed merely to flag that *something* changed. This is why checksums detect but do not correct.

### Casting out nines
The schoolroom **casting-out-nines** check is the same idea: $h(a+b+\cdots) = (\text{sum of all digits}) \bmod 9$ is invariant under correct addition, so a hash mismatch proves an error while a match gives evidence (about 9:1) of correctness.

### Why it matters
A tiny fixed-size hash protects an arbitrarily large file: redundancy is added in proportion to the *confidence* required, not the data size — a clean illustration of information-theoretic error detection.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hamming-7-4-code]] — contrasts-with: A CRC is a set of parity-check bits like the (7,4) Hamming code but detects only, without correcting.
- [[one-way-hash-function]] — contrasts-with: Linear hashes suffice against random noise but fail against an adversary, motivating one-way hashes.
[To be populated during integration]

## Checksum codes and the ISBN check digit
A **checksum** appends a redundant symbol computed as a weighted modular sum of the data, trading a tiny rate cost for guaranteed detection of structured errors. The classic example is the 10-digit **ISBN**: nine source digits $x_1,\dots,x_9$ and a check digit
$$x_{10} = \Big(\sum_{n=1}^{9} n\,x_n\Big) \bmod 11,$$
so that every valid ISBN satisfies $\big(\sum_{n=1}^{10} n\,x_n\big) \bmod 11 = 0$.

Working modulo the **prime** 11 is what makes it powerful: it detects **any single-digit modification** (a wrong digit changes the weighted sum by $n\,\Delta \not\equiv 0 \pmod{11}$ since $n,\Delta \in \{1,\dots,10\}$ are non-zero mod 11) and **any transposition of two distinct digits** (swapping positions $i,j$ shifts the sum by $(i-j)(x_i-x_j)\not\equiv 0 \pmod{11}$). Using mod $10$ instead would fail: $10$ is not prime, so factors sharing a divisor with 10 can produce changes that vanish mod 10, leaving some single-digit and transposition errors undetected (and 10 cannot represent the full check range without the special symbol X).

## Detection versus correction: redundancy cost
MacKay Ex. 15.16 contrasts the redundancy needed to merely **detect** corruption with that needed to **correct** it. An error-*detecting* code only needs enough redundancy to make corrupted blocks fall outside the codebook with high probability—a single parity or checksum symbol can flag a wide class of errors, so its rate cost is small and nearly independent of how many positions might be affected. An error-*correcting* code must, in addition, leave every plausible error pattern closer to its true codeword than to any other; this demands codewords spread far apart in Hamming distance, costing redundancy that scales with the number of correctable errors (cf. minimum distance and the bounds on binary codes). The practical upshot: when a cheap retransmission is available, detection plus repeat-request is far more rate-efficient than forward correction.