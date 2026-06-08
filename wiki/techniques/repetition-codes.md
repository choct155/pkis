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
- hamming-7-4-code
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:technique:repetition-codes
instantiates:
- maximum-likelihood-estimation
- linear-block-code
- code-goodness-taxonomy
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch01
tags:
- error-correcting-codes
- channel-coding
- redundancy
- majority-vote
- binary-symmetric-channel
title: Repetition Codes
understanding: 0
uses:
- binary-symmetric-channel
---

## Definition
The simplest error-correcting code: repeat every source bit $N$ times (odd $N$). The code $R_N$ encodes $0\to\underbrace{0\cdots0}_{N}$, $1\to\underbrace{1\cdots1}_{N}$, and decodes by **majority vote**. For a binary symmetric channel with flip probability $f$, majority vote is the optimal (maximum-likelihood) decoder when source bits are equiprobable.

The decoded bit-error probability is
$$p_b = \sum_{n=(N+1)/2}^{N}\binom{N}{n} f^n (1-f)^{N-n},$$
for odd $N$, dominated by the $f^{(N+1)/2}$ term. For $R_3$ at $f=0.1$, $p_b\approx 3f^2\approx0.03$.

The intuition: redundancy buys reliability, but at a brutal price. The rate is $R=1/N$, so error falls only as you crush throughput.

### The catch
To reach $p_b\approx10^{-15}$ at $f=0.1$ requires about $N=61$ repetitions. Reliability is bought by driving the rate toward zero.

### Why it matters
Repetition codes are the baseline against which all coding is measured. They make the central tension vivid — error vs. rate — and motivate block codes and ultimately Shannon's discovery that *both* small error and finite rate are simultaneously achievable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[code-goodness-taxonomy]] — instantiates: repetition codes are the canonical example of a 'bad' code family
- [[linear-block-code]] — instantiates: repetition codes are linear block codes (and the textbook example of a 'bad' code)
- [[maximum-likelihood-estimation]] — instantiates: Majority-vote decoding is the maximum-likelihood decoder for R3 over a BSC.
- [[binary-symmetric-channel]] — uses: Error probability of R_N is computed for the binary symmetric channel with flip probability f.
- [[hamming-7-4-code]] — contrasts-with: Both correct errors at O(f^2), but the Hamming code achieves rate 4/7 versus the repetition code's 1/3.
[To be populated during integration]