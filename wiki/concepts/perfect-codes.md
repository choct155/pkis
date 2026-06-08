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
contrasts-with:
- channel-capacity
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:perfect-codes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch13
tags:
- coding-theory
- hamming-space
- sphere-packing
- golay-code
- error-correction
title: Perfect Codes
understanding: 0
uses:
- minimum-distance
---

## Definition
A code is a **perfect** $t$-error-correcting code if the $t$-spheres centred on its codewords tile Hamming space with no gaps and no overlaps. Equivalently, every received vector lies within distance $t$ of exactly one codeword. With $S=2^K$ codewords in a space of $2^N$ points, perfection requires the *sphere-packing equality*
$$2^{K}\sum_{w=0}^{t}\binom{N}{w} = 2^{N}, \quad\text{i.e.}\quad \sum_{w=0}^{t}\binom{N}{w} = 2^{N-K}.$$
The number of noise vectors in one sphere then equals the number of distinct syndromes.

### The complete list (binary)
The only non-trivial perfect binary codes are: the **Hamming codes** ($t=1$, $N=2^M-1$, rate $\to 1$); the **odd-length repetition codes** ($t=(N-1)/2$, rate $\to 0$); and the single **binary Golay code** ($N=23$, $K=12$, $t=3$). The Hamming case works because $1+\binom{7}{1}=2^3$; Golay because $\sum_{w=0}^{3}\binom{23}{w}=2^{11}$.

### Why it matters
Perfect codes would be the ideal solution to Shannon's problem -- if they existed in useful sizes. They do not: there are essentially none with large blocklength and moderate rate. Moreover, for $f>1/3$ a simple three-codeword overlap argument shows no perfect $fN$-error-correcting code can exist at all, even though Shannon guarantees good codes there. The lesson: reaching capacity requires decoding *past* the perfect-packing radius, where spheres heavily overlap.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[channel-capacity]] — contrasts-with: useful perfect codes don't exist near capacity; reaching Shannon's limit needs decoding past the packing radius.
- [[minimum-distance]] — uses: perfection means t-spheres (t set by d_min) tile Hamming space without overlap.
[To be populated during integration]