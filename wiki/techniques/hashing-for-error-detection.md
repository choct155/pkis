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
[To be populated during integration]