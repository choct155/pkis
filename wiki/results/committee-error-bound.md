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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:result:committee-error-bound
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch14
tags:
- ensemble
- Jensen's inequality
- variance-reduction
- convex-loss
title: Committee Error Bound
understanding: 0
---

## Definition
$$E_{\text{COM}} \leq E_{\text{AV}}$$

For any convex loss $E(y)$, the expected error of a uniformly weighted committee of $M$ models never exceeds the average expected error of its individual members.

### Why it matters
The result follows directly from Jensen's inequality applied to the convex loss: $E\!\left[L\!\left(\frac{1}{M}\sum_m y_m\right)\right] \leq \frac{1}{M}\sum_m E[L(y_m)]$. It provides a theoretical guarantee that averaging predictions is never harmful in expectation, making model committees a safe default strategy regardless of correlation structure among members.

### Proof sketch
Write $y_{\text{COM}} = \frac{1}{M}\sum_m y_m$. By convexity of $L$, $L(y_{\text{COM}}) \leq \frac{1}{M}\sum_m L(y_m)$. Taking expectations and averaging over $m$ gives the result.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]