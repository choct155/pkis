---
aliases: []
also_type: []
applies:
- brownian-motion
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:result:law-of-iterated-logarithm
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
tags:
- stochastic-processes
- brownian-motion
- almost-sure-asymptotics
- oscillation
title: Law of the Iterated Logarithm
understanding: 0
uses:
- borel-cantelli-lemma
---

## Definition
The law of the iterated logarithm (Khintchine) precisely describes the almost-sure oscillation envelope of Brownian motion. With $h(t) = \sqrt{2t \log\log t^{-1}}$,
$$P\Big[\limsup_{t \downarrow 0} \frac{B(t)}{h(t)} = 1\Big] = 1, \qquad P\Big[\liminf_{t \downarrow 0} \frac{B(t)}{h(t)} = -1\Big] = 1,$$
the second following from the first by the symmetry $B \stackrel{d}{=} -B$. A companion law near infinity, $\limsup_{t\to\infty} B(t)/\sqrt{2t\log\log t} = 1$, follows via the time-reversal property. A key qualitative corollary: almost every Brownian path crosses 0 infinitely often in every neighborhood of the origin, oscillating between the upper and lower $h$-envelopes infinitely many times.

The upper bound uses an exponential maximal inequality for BM with drift ($P[\sup_{s\le t}(B(s) - \alpha s/2) > \beta] \le e^{-\alpha\beta}$, from the exponential law of the all-time supremum) plus Borel-Cantelli along a geometric sequence $t_n = \theta^n$; the lower bound uses independent increments, Mill's ratio for the normal tail, and the divergent Borel-Cantelli.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[borel-cantelli-lemma]] — uses: Both bounds in the LIL are obtained by summing tail probabilities and invoking the two halves of Borel-Cantelli.
- [[brownian-motion]] — applies: The LIL gives the exact almost-sure oscillation envelope of Brownian paths near 0 and infinity.
[To be populated during integration]