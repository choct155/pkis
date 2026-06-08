---
aliases: []
also_type: []
applies:
- likelihood-ratio-evidence
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
id: pkis:technique:bayesian-codebreaking
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch18
tags:
- banburismus
- enigma
- weight-of-evidence
- match-statistics
- bletchley-park
- turing
title: Bayesian Codebreaking (Banburismus)
understanding: 0
uses:
- redundancy-of-natural-language
- mutual-information
---

## Definition
The Bletchley Park method (Turing, refined by Good) for deciding whether two Enigma cyphertexts were enciphered in the *same* machine state, framed as accumulating Bayesian weight of evidence rather than decrypting. Two cyphertexts $x,y$ of length $T$ are compared position-by-position; the redundancy of the underlying plaintext language makes synchronized matches slightly more frequent under the 'same-state' hypothesis $H_1$ than under the unrelated-state null $H_0$.

For a monogram language model, the **match probability** is $m = \sum_i p_i^2$ ($\approx 2/26$ for English/German, versus $1/26$ for random text). Each of the $M$ matching positions contributes $\log mA$ in favour of $H_1$; each of the $N$ non-matches contributes $\log\frac{(1-m)A}{A-1}$ (slightly favouring $H_0$):
$$\log\frac{P(x,y\mid H_1)}{P(x,y\mid H_0)} = M\log mA + N\log\frac{(1-m)A}{A-1}.$$

### Why it matters
This is a canonical real-world instance of sequential evidence accumulation: weak per-character signal summed into decisive odds, with evidence tallied in **decibans** (the smallest weight of evidence a human can discern). Roughly 400 characters yield 20 decibans (100:1) toward one hypothesis. Banburismus narrowed which wheels were in use; the logic-based bombes, fed with plaintext cribs, then cracked the settings.

### Stronger language models
Because English bigrams/trigrams are non-uniform, real matches arrive in bursts of consecutive coincidences. Turing and Good scored runs with better-than-monogram models, sharpening the evidence per observed coincidence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mutual-information]] — uses: Exercise 18.3: the Enigma flaw of never mapping a letter to itself leaks information per character, exploitable for crib alignment.
- [[redundancy-of-natural-language]] — uses: The method works only because plaintext redundancy makes synchronized matches more frequent than chance (m > 1/A).
- [[likelihood-ratio-evidence]] — applies: Each character match/non-match contributes a fixed log-likelihood-ratio toward the same-state hypothesis; odds accumulate multiplicatively.
[To be populated during integration]