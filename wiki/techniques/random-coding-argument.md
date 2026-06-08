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
id: pkis:technique:random-coding-argument
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch10
tags:
- shannon
- probabilistic-method
- achievability
- expurgation
- channel-coding
title: Random Coding Argument
understanding: 0
uses:
- joint-typicality-decoding
---

## Definition
Shannon's probabilistic-method proof technique: instead of constructing a single good code and bounding its error, *average* the error probability over an **ensemble of randomly generated codes** and show the average is small. If the average block error $\langle p_B\rangle$ over all codes is $<2\delta$, then at least one code $C$ must have $p_B(C)<2\delta$ — a good code must exist even though none is exhibited.

MacKay's analogy: to prove some baby in a class weighs under 10 kg, don't catch each baby; weigh them all at once. If the total is under 1000 kg, an underweight baby must exist.

### The construction
Fix an input distribution $P(x)$ and generate $S=2^{NR'}$ codewords i.i.d. from $\prod_n P(x_n)$. Transmit over the channel, decode by joint typicality. By symmetry the averaged error is independent of which message was sent.

### From average to maximal error: expurgation
A small *average* error still permits a few terrible codewords. **Expurgation** fixes this: discard the worst-performing 50% of codewords. The survivors each have conditional error $<4\delta$, at the cost of reducing rate from $R'$ to $R'-1/N$ (negligible for large $N$), yielding small *maximal* error $p_B^M<4\delta$.

### Why it matters
This is one of the founding uses of the probabilistic method in applied mathematics. It proves capacity is achievable but is non-constructive — implementing a random code of large $N$ costs exponentially in $N$ — which is precisely the gap that decades of practical coding theory set out to close.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[joint-typicality-decoding]] — uses: The averaged-error analysis decodes each random code by joint typicality.
[To be populated during integration]