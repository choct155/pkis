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
- statistical-learning
id: pkis:result:weak-law-of-large-numbers
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch04
tags:
- law-of-large-numbers
- chebyshev-inequality
- concentration
- sample-mean
- convergence-in-probability
title: Weak Law of Large Numbers (via Chebyshev)
understanding: 0
---

## Definition
The sample mean of many i.i.d. variables concentrates on the true mean: its spread shrinks like $1/\sqrt{N}$.
$$\text{For } x = \tfrac1N\sum_{n=1}^N h_n \text{ (common mean } \bar h, \text{ variance } \sigma_h^2): \quad P\big((x-\bar h)^2 \ge \alpha\big) \le \frac{\sigma_h^2}{\alpha N}.$$
One line: *average enough independent draws and you land arbitrarily close to the mean, with probability arbitrarily near 1.*

### Proof engine — Chebyshev's inequality
**Markov form:** for non-negative $t$, $P(t\ge\alpha)\le \bar t/\alpha$. **Chebyshev:** setting $t=(x-\bar x)^2$ gives $P((x-\bar x)^2\ge\alpha)\le \sigma_x^2/\alpha$. Using $\bar x=\bar h$ and $\sigma_x^2=\sigma_h^2/N$ yields the WLLN.

### Why it matters
This is the probabilistic engine behind the asymptotic equipartition property and Shannon's source coding theorem. Applying it to $\tfrac1N\log_2\tfrac1{P(x)}$ — an average of $N$ per-symbol Shannon information contents — shows this quantity concentrates on the entropy $H$, so the realized string is almost surely typical. Limits: it needs finite variance — heavy-tailed laws like the Cauchy distribution do not obey it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]