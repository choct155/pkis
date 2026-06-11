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
- information-theory
- statistics
id: pkis:result:information-inequality
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
tags:
- kl-divergence
- non-negativity
- jensen-inequality
- information-inequality
- foundational
title: Information Inequality (Non-negativity of KL)
understanding: 0
---

## Definition
**Theorem (Information Inequality):** For any two probability distributions $p$ and $q$:

$$D_{\mathrm{KL}}(p \| q) \geq 0$$

with equality if and only if $p(x) = q(x)$ for all $x$.

**Proof sketch:** Applying Jensen's inequality to the concave function $\log$:
$$-D_{\mathrm{KL}}(p\|q) = \mathbb{E}_p\left[\log\frac{q}{p}\right] \leq \log\mathbb{E}_p\left[\frac{q}{p}\right] = \log\sum_{x\in A} q(x) \leq \log 1 = 0$$
Equality requires $q/p = \text{const}$ and full support, forcing $p = q$.

### Why it matters
Non-negativity of KL is one of the most-used inequalities in machine learning and statistics. Any expression rearranged to expose a KL term immediately yields a bound, underpinning the ELBO in variational inference, PAC-Bayes bounds, and proofs throughout information theory.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]