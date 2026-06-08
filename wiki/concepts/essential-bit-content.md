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
- statistical-learning
id: pkis:concept:essential-bit-content
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch04
tags:
- essential-bit-content
- raw-bit-content
- lossy-compression
- source-coding
- information-content-measure
title: Essential Bit Content (Raw Bit Content)
understanding: 0
---

## Definition
A family of lossy measures of information content, indexed by a permitted failure probability $\delta$. Drop the rarest outcomes until only probability $\delta$ is unnamed, then count the survivors.
$$H_\delta(X) \equiv \log_2 |S_\delta|, \qquad S_\delta = \text{smallest subset of } A_X \text{ with } P(x\in S_\delta) \ge 1-\delta.$$
The one-line intuition: *give binary names only to the outcomes you can't afford to lose.*

### Raw bit content
The special case $\delta = 0$ is the **raw bit content** $H_0(X) = \log_2 |A_X|$ — the log of the alphabet size, the cost of a fixed-length name for every outcome with no probabilistic discount. It is additive, $H_0(X,Y)=H_0(X)+H_0(Y)$.

### Why it matters
$H_\delta$ is the bridge from the naive counting measure $H_0$ to the entropy $H$. For a single ensemble it depends strongly and awkwardly on $\delta$. The payoff comes for extended ensembles $X^N$: as $N\to\infty$, $\tfrac1N H_\delta(X^N)$ flattens and converges to $H(X)$ for *every* $0<\delta<1$ — which is precisely the source coding theorem. So the essential bit content is the object whose asymptotics the theorem describes. Caution: $H_0$ and $H_\delta$ are unrelated to the binary entropy function $H_2(p)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]