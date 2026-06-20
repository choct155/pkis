---
aliases: []
also_type: []
applies:
- brownian-motion
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- martingales
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- bayesian-stats
- statistical-learning
id: pkis:result:reflection-principle
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
- lange-applied-probability-ch11
tags:
- stochastic-processes
- hitting-time
- brownian-motion
- first-passage
title: Reflection Principle
understanding: 0
---

## Definition
The reflection principle states that if $B$ is a standard Brownian motion and $T_a = \inf\{t : B(t) = a\}$ is the first hitting time of level $a > 0$, then the reflected process
$$B^*(t) = \begin{cases} B(t), & t \le T_a, \\ 2a - B(t), & t > T_a, \end{cases}$$
is again a standard Brownian motion. Heuristically: after the path attains level $a$, the post-$T_a$ increments form a fresh BM (strong independent increments) which, by symmetry, is distributionally unchanged under negation; reflecting the path about the line $y=a$ therefore yields a process with the same law. A rigorous proof writes $B$ and $B^*$ as the image of $(f, T_a, \pm g)$ under a path-splicing map and invokes $g \stackrel{d}{=} -g$.

Consequences (all derived from reflection):
- $P[M(t) \ge a] = 2P[B(t) \ge a] = P[|B(t)| \ge a]$, where $M(t) = \sup_{0\le s\le t} B(s)$;
- the first-passage density $f_{T_a}(x) = \frac{a}{\sqrt{2\pi}} x^{-3/2} e^{-a^2/2x}$ with Laplace transform $Ee^{-\lambda T_a} = e^{-\sqrt{2\lambda}\,a}$;
- the joint density of $(M(t), B(t))$ and the arcsine-type law $\frac{2}{\pi}\arccos\sqrt{t_0/t_1}$ for a zero in $(t_0, t_1)$;
- iterated reflection yields the exact distribution of the supremum of $|B^{(0)}|$ (the Kolmogorov-Smirnov limit).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[martingales]] — contrasts-with: Reflection gives elementary first-passage/exit results that martingale optional-stopping methods obtain by a different route.
- [[brownian-motion]] — applies: Reflection is a property of Brownian sample paths used to compute hitting-time and maximum distributions.
[To be populated during integration]