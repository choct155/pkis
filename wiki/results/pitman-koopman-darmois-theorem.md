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
- statistics
- information-theory
id: pkis:result:pitman-koopman-darmois-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
tags:
- exponential-family
- sufficient-statistics
- pitman-koopman-darmois
- characterization
title: Pitman-Koopman-Darmois Theorem
understanding: 0
---

## Definition
**Theorem (Pitman-Koopman-Darmois):** For a parametric family of distributions whose support does not depend on the parameter, a sufficient statistic of **bounded dimension** (independent of sample size $N$) exists if and only if the family is an **exponential family**.

Formally: if $\{p_\theta : \theta \in \Theta\}$ has fixed support and admits a sufficient statistic $s(x_1,\ldots,x_N)$ with $\dim(s)$ bounded as $N \to \infty$, then $p_\theta$ must belong to the exponential family.

### Why it matters
This theorem provides a deep characterization of exponential families as the unique distributions admitting finite-dimensional sufficient statistics. It explains why exponential families occupy a privileged role in statistical inference: they are exactly the distributions for which data can be compressed to a fixed-size summary without loss of information about the parameter, regardless of sample size.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]