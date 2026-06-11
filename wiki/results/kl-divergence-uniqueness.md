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
- machine-learning
id: pkis:result:kl-divergence-uniqueness
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
tags:
- kl-divergence
- uniqueness
- axiomatic
- information-gain
- relative-entropy
title: KL Divergence Uniqueness Theorem
understanding: 0
---

## Definition
$$D_{\mathrm{KL}}(p \| q) \triangleq \sum_k p_k \log \frac{p_k}{q_k}$$

The Kullback-Leibler divergence is the **unique** measure of information gain (up to a multiplicative constant) satisfying: (1) continuity in arguments, (2) non-negativity, (3) permutation invariance, (4) monotonicity for uniform distributions, and (5) a natural chain rule of the form $I[p(x,y)\|q(x,y)] = I[p(x)\|q(x)] + \mathbb{E}_{p(x)}[I[p(y|x)\|q(y|x)]]$.

The choice of logarithm base is the only degree of freedom, corresponding to a choice of units (bits for base 2, nats for base $e$).

### Why it matters
This axiomatic uniqueness result justifies KL divergence as the canonical measure for belief updating, making it foundational for variational inference, maximum likelihood, Bayesian inference, and information theory more broadly.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]