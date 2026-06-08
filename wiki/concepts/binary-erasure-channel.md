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
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:binary-erasure-channel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch09
tags:
- channel
- erasure
- capacity
- noise
- mackay
title: Binary Erasure Channel
understanding: 0
---

## Definition
The binary erasure channel (BEC) has input alphabet $\{0,1\}$ and output alphabet $\{0,?,1\}$. With probability $1-f$ the bit passes through unchanged; with probability $f$ it is replaced by an erasure symbol $?$. Crucially, bits are never *flipped* — only lost:
$$P(?\mid 0)=P(?\mid 1)=f,\quad P(0\mid 0)=P(1\mid 1)=1-f.$$

### Capacity
When the receiver sees a $0$ or $1$ it knows the input exactly; only on $?$ (probability $f$) is the input uncertain, contributing $H_2(0.5)$ of conditional entropy. Hence
$$C_{\text{BEC}} = 1 - f,$$
attained by the uniform input. This is simply the fraction of the time the channel is reliable — a strikingly clean result.

### Comparison with the BSC
For every $f<0.5$ the BEC has higher capacity than the binary symmetric channel (BSC capacity $1-H_2(f)$), because an erasure announces its own location whereas a flip hides among the correct bits. Erasures are easier to correct than substitutions.

### Why it matters
The BEC models packet loss in networks and is the canonical example where capacity is intuitive ($1-f$) yet the *code* achieving it is non-obvious. It motivates rateless and fountain codes, and serves throughout as the friendly contrast to the harder BSC and Z channels.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]