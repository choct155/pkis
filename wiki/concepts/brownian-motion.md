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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
- state-space-models
id: pkis:concept:brownian-motion
instantiates:
- gaussian-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- martingales
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
specializes:
- diffusion-processes
tags:
- stochastic-processes
- continuous-time
- gaussian
- wiener-process
title: Brownian Motion
understanding: 0
uses:
- gaussian-distribution
- invariance-principle
- borel-cantelli-lemma
---

## Definition
Standard Brownian motion (the Wiener process) is the continuous-time stochastic process $B = \{B(t), t \ge 0\}$ characterized by four properties: (1) independent increments; (2) for $0 \le s < t$, the increment $B(t) - B(s) \sim N(0, t-s)$ (Gaussian, with variance equal to the increment length); (3) almost surely continuous paths, $P[B \in C[0,\infty)] = 1$; and (4) the normalization $B(0) = 0$. Properties (1) and (2) are the essential ones — given a process satisfying them, a version satisfying (3) always exists (Doob, 1953), and (4) is mere convenience. It is the central object of the modern theory of stochastic processes and of large-sample statistics, basic to descriptions of financial markets, the construction of diffusions, queueing approximations, and asymptotic distribution theory.

Intuitively, Brownian motion is the continuous-time scaling limit of a random walk: for iid $X_n$ with mean 0 and variance 1 and partial sums $S_n$, the process $B_n(t) = S_{[nt]}/\sqrt{n}$ converges in distribution to $B$. It can be constructed rigorously from a supply of iid $N(0,1)$ variables by dyadic interpolation (Levy construction), with the Borel-Cantelli lemma controlling the uniform convergence of successive refinements in $C[0,1]$.

Key structural properties:
- **Markov** with stationary transition density $n(x, t, \cdot)$;
- **Differential property**: $\{B(t+s) - B(s), t \ge 0\}$ is again a standard BM, independent of the past;
- **Scaling**: $\{\sqrt{c}\,B(t/c)\} \stackrel{d}{=} \{B(t)\}$;
- **Symmetry**: $-B \stackrel{d}{=} B$;
- **Time reversal**: $\{tB(1/t), t>0\} \stackrel{d}{=} \{B(t)\}$;
- **Gaussian-process characterization**: $B$ is the unique continuous, zero-mean Gaussian process with $B(0)=0$ and covariance $\mathrm{Cov}(B(s),B(t)) = s \wedge t$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[borel-cantelli-lemma]] — uses: Borel-Cantelli controls the dyadic-refinement errors in the Levy construction and proves nowhere-differentiability and quadratic-variation convergence.
- [[invariance-principle]] — uses: BM's role in large-sample statistics flows through the invariance principle and the continuous mapping theorem.
- [[martingales]] — prerequisite-of: BM is the prototypical continuous martingale; its quadratic-variation/submartingale decompositions underlie martingale stochastic calculus.
- [[gaussian-distribution]] — uses: Increments B(t)-B(s) are exactly N(0, t-s); the normal density and tail dominate every BM calculation.
- [[gaussian-process]] — instantiates: BM is characterized as the continuous zero-mean Gaussian process with B(0)=0 and covariance s wedge t.
- [[diffusion-processes]] — specializes: Standard Brownian motion is the canonical diffusion (zero drift, unit infinitesimal variance); diffusions are built as solutions of SDEs driven by it.
[To be populated during integration]