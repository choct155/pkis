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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:result:invariance-principle
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
tags:
- stochastic-processes
- weak-convergence
- central-limit-theorem
- donsker
title: Invariance Principle (Functional Central Limit Theorem)
understanding: 0
---

## Definition
The invariance principle (functional central limit theorem) is the strengthening of the central limit theorem from convergence of one-dimensional or finite-dimensional distributions to weak convergence of the entire sample path as a random element of the function space $C[0,\infty)$. For iid $X_n$ with mean 0 and variance 1, partial sums $S_n$, and the polygonal (linearly interpolated) process $B_n^{(c)}(t)$ built from $\{(j/n, S_j/\sqrt{n})\}$, one has $B_n^{(c)} \Rightarrow B$, standard Brownian motion, in the metric of local uniform convergence.

Its power comes from the **continuous mapping theorem**: for any functional $\psi: C[0,\infty) \to X$ continuous at $P$-almost every Brownian path, $\psi(B_n^{(c)}) \Rightarrow \psi(B)$. This converts limit problems for functionals of partial sums (e.g. the maximum $\sup_{0\le t\le1} S_{[nt]}/\sqrt{n} \Rightarrow M(1)$) into computable Brownian-motion calculations. The term *invariance* reflects that the limit does not depend on the particular increment distribution, only on its mean and variance. This is the mechanism by which estimators that are functions of partial sums acquire Brownian-functional asymptotic distributions, and underlies heavy-traffic queueing limits and the Kolmogorov-Smirnov limit law.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]