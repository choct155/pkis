---
aliases: []
also_type: []
applies:
- markov-chains
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
id: pkis:result:data-processing-inequality
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch08
tags:
- mutual-information
- markov-chain
- data-processing
- mackay
title: Data-Processing Inequality
understanding: 0
uses:
- mutual-information
- chain-rule-for-entropy
---

## Definition
Processing data can only destroy information, never create it. If three variables form a Markov chain $W \to D \to R$ — the state of the world $W$, gathered data $D$, and processed data $R$, with $P(w,d,r) = P(w)P(d\mid w)P(r\mid d)$ — then
$$I(W; R) \leq I(W; D).$$
No deterministic or stochastic function of $D$ can reveal more about $W$ than $D$ itself does.

### Proof via the chain rule
Markovity means $W$ and $R$ are conditionally independent given $D$, so $I(W; R \mid D) = 0$. Expand $I(W; D, R)$ two ways with the mutual-information chain rule:
$$I(W; D, R) = I(W; D) + \underbrace{I(W; R \mid D)}_{=0} = I(W; R) + \underbrace{I(W; D \mid R)}_{\geq 0},$$
so $I(W; R) - I(W; D) = -I(W; D \mid R) \leq 0.$

### Why it matters
As MacKay notes, this is as much a caution about the *definition* of information as about processing: a clever summary may be far more *useful* than raw data even though it carries no more Shannon information. The result underpins sufficiency, the sanity of channel-coding bounds, and modern uses (e.g. bounding what a learned representation can know).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-chains]] — applies: Stated for the Markov chain W -> D -> R where W and R are conditionally independent given D.
- [[chain-rule-for-entropy]] — uses: Proof expands I(W;D,R) two ways using the mutual-information chain rule.
- [[mutual-information]] — uses: The theorem bounds I(W;R) <= I(W;D) between processed and raw data.
[To be populated during integration]