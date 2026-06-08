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
id: pkis:result:jensens-inequality
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch02
tags:
- convexity
- expectation
- inequality
- entropy
title: Jensen's Inequality
understanding: 0
---

## Definition
For a convex $\smile$ function $f$ and a random variable $x$,
$$\mathcal{E}[f(x)] \geq f(\mathcal{E}[x]),$$
with the inequality reversed for concave $\frown$ $f$. If $f$ is strictly convex and equality holds, then $x$ is a constant (almost surely).

Intuition: averaging *after* bending a convex curve never undershoots bending the average — the chord lies above the curve.

### Convexity
A function is convex on $(a,b)$ if every chord lies above it: $f(\lambda x_1 + (1-\lambda)x_2) \leq \lambda f(x_1) + (1-\lambda)f(x_2)$ for $0\le\lambda\le1$. Examples: $x^2$, $e^x$, and $\log(1/x)$, $x\log x$ for $x>0$.

### Centre-of-gravity picture
Place masses $p_i$ on a convex curve at $(x_i, f(x_i))$; their centre of gravity $(\mathcal{E}[x], \mathcal{E}[f(x)])$ lies above the curve.

### Why it matters
Jensen is the engine behind the most important inequalities in information theory and inference: it yields Gibbs' inequality ($D_{KL}\ge0$), the maximum-entropy bound $H(X)\le\log|A_X|$, and the variational (ELBO) lower bound used throughout approximate Bayesian inference and the EM algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]