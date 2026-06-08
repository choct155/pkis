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
extends:
- source-coding-theorem
id: pkis:result:slepian-wolf-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch15
tags:
- network-information-theory
- source-coding
- correlated-sources
- joint-entropy
- conditional-entropy
- distributed-coding
title: Slepian–Wolf Theorem (Distributed Source Coding)
understanding: 0
uses:
- joint-entropy
- conditional-entropy
- typical-set
---

## Definition
Two correlated sources $X^{(A)}$ and $X^{(B)}$ can be **separately** encoded—the two encoders never communicate—yet **jointly** decoded at a central node with vanishing error, provided the rate pair $(R_A, R_B)$ satisfies
$$R_A \ge H(X^{(A)}\mid X^{(B)}),\quad R_B \ge H(X^{(B)}\mid X^{(A)}),\quad R_A + R_B \ge H(X^{(A)}, X^{(B)}).$$
The surprise: separate compression loses nothing in total rate versus joint compression—the sum can reach the joint entropy even though neither encoder sees the other's data.

### Intuition
If $X^{(B)}$ is sent verbatim ($R_B = H(X^{(B)})$), then $X^{(A)}$ need only be sent at $H(X^{(A)}\mid X^{(B)})$, because the decoder already knows $X^{(B)}$. The remarkable claim is that the side information can be exploited even when the second encoder does *not* know $X^{(B)}$, by binning typical sequences via random hashes so each $X^{(A)}$ block is disambiguated by the correlated $X^{(B)}$ block.

### Example
For rain-in-two-towns with $P(x^{(A)}{=}x^{(B)})=0.98$, each line must carry only $H_2(0.02)=0.14$ bits and the total need exceed $H_2(0.02)+1 = 1.14$ bits, far below the naive $2$ bits.

### Why it matters
It is the cornerstone of distributed/sensor-network compression and shows that correlation across physically separated sources is a globally shareable resource. It generalizes the single-source coding theorem to multiterminal settings (Slepian and Wolf, 1973).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[typical-set]] — uses: Random binning of jointly-typical sequences underlies the achievability proof.
- [[source-coding-theorem]] — extends: Generalizes single-source compression to separately-encoded correlated sources.
- [[conditional-entropy]] — uses: Per-source lower bounds are the conditional entropies H(X^A|X^B), H(X^B|X^A).
- [[joint-entropy]] — uses: The achievable sum-rate is exactly the joint entropy H(X^A, X^B).
[To be populated during integration]