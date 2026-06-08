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
id: pkis:result:gibbs-inequality
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch02
tags:
- kl-divergence
- relative-entropy
- convexity
- inequality
title: Gibbs' Inequality
understanding: 0
---

## Definition
For any two distributions $P$ and $Q$ over the same alphabet $A_X$, the relative entropy is non-negative:
$$D_{KL}(P\|Q) = \sum_x P(x)\log\frac{P(x)}{Q(x)} \geq 0,$$
with equality if and only if $P=Q$.

Intuition: you can never have negative average surprise from believing the truth $P$ rather than a wrong model $Q$ — and zero only when the model is exactly right.

### Proof via Jensen
Write $-D_{KL}(P\|Q) = \sum_x P(x)\log\frac{Q(x)}{P(x)}$ and apply Jensen's inequality to the concave function $\log$: $\mathcal{E}_P[\log(Q/P)] \le \log \mathcal{E}_P[Q/P] = \log\sum_x Q(x) = \log 1 = 0$. Strict concavity gives equality only when $Q/P$ is constant, i.e. $P=Q$.

### Why it matters
MacKay calls this 'probably the most important inequality in this book.' It guarantees that KL divergence is a valid (asymmetric) measure of distributional mismatch, underwrites the source-coding optimality of matched codes, proves the maximum-entropy bound, and makes the ELBO a genuine lower bound on the log-evidence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]