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
id: pkis:result:noisy-channel-coding-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch01
tags:
- shannon
- capacity
- channel-coding
- fundamental-limit
- reliable-communication
title: Noisy-Channel Coding Theorem
understanding: 0
---

## Definition
Shannon's central theorem (1948): for any noisy channel there exist codes permitting communication with **arbitrarily small** error probability $p_b$ at any rate $R$ below the channel **capacity** $C$, and reliable communication at rates above $C$ is impossible.
$$R<C \;\Rightarrow\; p_b \text{ can be made} \to 0; \qquad R>C \;\Rightarrow\; \text{reliable communication impossible.}$$

The intuition: the achievable boundary in the $(R,p_b)$ plane meets the rate axis at the *non-zero* value $R=C$, not at the origin — you can have both finite rate and vanishing error.

### Limitations and possibilities
The theorem is two-sided: a **converse** (no scheme beats capacity) and an **achievability** result (capacity is reachable). It is non-constructive — it proves good codes exist without exhibiting practical ones, a gap that coding theory spent decades closing.

### Why it matters
This result created information theory and overturned the prevailing 'no pain, no gain' belief. It is the destination of the first half of MacKay's book: entropy, typical sets, and source coding are all developed to prove and exploit it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]