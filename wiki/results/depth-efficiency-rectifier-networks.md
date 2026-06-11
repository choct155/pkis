---
aliases: []
also_type: []
applies:
- relu
- maxout-unit
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
- deep-learning
- complexity-theory
extends:
- universal-approximation-theorem-mlp
id: pkis:result:depth-efficiency-rectifier-networks
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
tags:
- depth
- width
- expressivity
- piecewise-linear
- rectifier-network
title: Depth-Efficiency of Rectifier Networks (Montufar et al.)
understanding: 0
uses:
- inductive-bias
---

## Definition
A deep rectifier network with $d$ inputs, $l$ hidden layers, and $n$ units per layer carves out $$O\!\left(\binom{n}{d}^{d(l-1)} n^d\right)$$ linear regions in input space—exponential in depth $l$. A maxout network with $k$ filters per unit achieves $O(k^{(l-1)+d})$ regions. Equivalently, functions representable by a depth-$l$ rectifier network may require exponentially many units (in $n$) to be expressed by a depth-1 (shallow) network (Montufar et al., 2014).

Deep networks achieve exponentially richer piecewise-linear partitions of input space compared to shallow networks of similar width.

### Why it matters
This result provides a formal, complexity-theoretic justification for the empirical observation that deeper networks generalize better with fewer parameters. It shows that depth is not merely a convenience but offers an exponential representational advantage for piecewise-linear functions, underpinning the design choice of stacking many thin layers rather than using a single wide layer.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inductive-bias]] — uses: Deep architecture encodes prior that functions compose simpler sub-functions.
- [[maxout-unit]] — applies
- [[relu]] — applies
- [[universal-approximation-theorem-mlp]] — extends
[To be populated during integration]