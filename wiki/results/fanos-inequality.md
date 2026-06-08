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
id: pkis:result:fanos-inequality
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch10
tags:
- shannon
- converse
- data-processing-inequality
- fundamental-limit
- channel-coding
title: Fano's Inequality
understanding: 0
uses:
- channel-capacity
---

## Definition
Fano's inequality lower-bounds the mutual information retained between source and reconstruction when communication tolerates a bit-error probability $p_b$. For a system transmitting at rate $R$ over $N$ channel uses with bit-error probability $p_b$,
$$I(s;\hat{s})\ \ge\ NR\big(1-H_2(p_b)\big),$$
where $H_2$ is the binary entropy function. Equality holds when the bit errors are independent; correlations among errors only *increase* the retained information, preserving the inequality.

Intuition: knowing the (possibly noisy) reconstruction $\hat{s}$ leaves at most $NRH_2(p_b)$ bits of residual uncertainty about the $NR$ source bits, so $\hat{s}$ must carry at least $NR(1-H_2(p_b))$ bits of information about $s$.

### Role in the converse
The source–encoder–channel–decoder form a Markov chain $s\to x\to y\to\hat{s}$, so the **data processing inequality** gives $I(s;\hat{s})\le I(x;y)\le NC$. Combining the two bounds:
$$NR(1-H_2(p_b))\le I(s;\hat{s})\le NC\ \Longrightarrow\ R\le \frac{C}{1-H_2(p_b)}.$$
This is exactly the unachievable boundary $R>C/(1-H_2(p_b))$ of the noisy-channel coding theorem.

### Why it matters
Fano's inequality, paired with the data processing inequality, supplies the **converse** half of the coding theorem: no scheme can beat capacity. It is the rigorous statement of why information, once lost to noise, cannot be recovered by clever decoding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[channel-capacity]] — uses: Fano's bound is closed against I(x;y) <= NC to yield the converse boundary.
[To be populated during integration]