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
id: pkis:result:bounds-on-binary-codes
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch13
tags:
- coding-theory
- gilbert-varshamov
- sphere-packing
- hamming-bound
- rate-distance-tradeoff
title: Bounds on Binary Codes (Sphere-Packing and Gilbert–Varshamov)
understanding: 0
---

## Definition
Two complementary bounds delimit the achievable trade-off between rate $R=K/N$ and minimum distance $d$ for binary codes.

### Sphere-packing (Hamming) bound
Disjoint $t$-spheres ($t=\lfloor(d-1)/2\rfloor$) about $2^K$ codewords cannot exceed the $2^N$ points of Hamming space:
$$2^{K}\sum_{w=0}^{t}\binom{N}{w} \le 2^{N}.$$
This upper-bounds how many codewords a code of given $N,d$ may have; perfect codes meet it with equality.

### Gilbert–Varshamov bound and distance
A random linear code typically achieves minimum distance near the **Gilbert–Varshamov distance**
$$d_{GV} \equiv N\,H_2^{-1}(1-R), \qquad\text{i.e.}\qquad H_2(d_{GV}/N) = 1-R,$$
from the point where $\langle A(w)\rangle = \binom{N}{w}2^{-M}$ falls through $1$. The (widely believed) GV conjecture asserts one cannot do significantly better.

### Bounded-distance vs Shannon
With a bounded-distance decoder the tolerable flip fraction is $f_{bd}=\tfrac12 d/N$, giving achievable rate
$$R_{GV} = 1 - H_2(2 f_{bd}),$$
whereas Shannon's capacity is $C = 1 - H_2(f)$. Comparing at fixed rate yields
$$f_{bd} = f/2.$$

### Why it matters
Bounded-distance decoding -- and hence any approach worshipping minimum distance -- can cope with only **half** the noise Shannon proves tolerable. The gap is exactly the cost of "worst-case-ism." For $f>1/4$ such decoders cannot communicate at all, yet good codes exist.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]