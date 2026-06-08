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
id: pkis:concept:z-channel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch09
tags:
- channel
- asymmetric-channel
- capacity
- optimal-input-distribution
- mackay
title: Z Channel
understanding: 0
---

## Definition
The Z channel is an *asymmetric* binary channel: input $0$ is transmitted perfectly, but input $1$ is flipped to $0$ with probability $f$:
$$P(0\mid 0)=1,\ P(1\mid 0)=0,\qquad P(0\mid 1)=f,\ P(1\mid 1)=1-f.$$
A received $1$ therefore proves the input was $1$ (posterior $P(x{=}1\mid y{=}1)=1$), while a received $0$ is ambiguous.

### Asymmetric optimal input
Because noise enters only on the $1$ input, the capacity-achieving distribution is *not* uniform. Maximizing $I(X;Y)=H_2(p_1(1-f)) - p_1 H_2(f)$ gives
$$p_1^* = \frac{1/(1-f)}{1 + 2^{H_2(f)/(1-f)}},$$
which is always below $1/2$ and tends to $1/e$ as $f\to 1$. For $f=0.15$, $p_1^*\approx 0.445$ and $C_{Z}\approx 0.685$ bits — higher than the BSC at the same $f$.

### Intuition
Using input $1$ injects channel entropy; input $0$ injects none. So one favours $0$ slightly, but not overwhelmingly, since the $1$ output is the only fully-informative symbol.

### Why it matters
The Z channel is MacKay's standard example that the optimal input distribution can be non-uniform, breaking the symmetry shortcut. It shows capacity is a genuine optimization over $P_X$, and it models physical media (e.g. optical or flash storage) where one symbol degrades but the other does not.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]