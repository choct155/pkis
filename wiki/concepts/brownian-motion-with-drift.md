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
id: pkis:concept:brownian-motion-with-drift
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
specializes:
- brownian-motion
tags:
- stochastic-processes
- brownian-motion
- queueing
- first-passage
title: Brownian Motion with Drift
understanding: 0
uses:
- reflection-principle
---

## Definition
Brownian motion with drift $\mu$ is the process $B_\mu(t) = B(t) + \mu t$, $t \ge 0$, where $B$ is standard Brownian motion. The deterministic linear term $\mu t$ governs long-run behavior: by the strong law, $B_\mu(t)/t \to \mu$ a.s.

For negative drift $\mu < 0$, the path drifts to $-\infty$, so the all-time supremum $M_\mu(\infty) = \sup_{s \ge 0} B_\mu(s)$ is finite. A functional-equation argument using the strong independent-increments property shows $P[M_\mu(\infty) \ge x_1 + x_2] = P[M_\mu(\infty) \ge x_1]\,P[M_\mu(\infty) \ge x_2]$, forcing an exponential tail; matching the constant via the first-passage Laplace transform gives
$$P[M_\mu(\infty) \ge x] = e^{-2|\mu| x}, \quad x \ge 0.$$
This exponential supremum law is the engine behind the heavy-traffic approximation for the equilibrium waiting-time distribution of the G/G/1 queue (traffic intensity $\rho \uparrow 1$): the rescaled waiting time converges to the supremum of a drift-$(-1)$ Brownian motion, yielding $P[|\mu|W_\infty/\sigma^2 > y] \approx e^{-2y}$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reflection-principle]] — uses: The exponential supremum law uses first-passage Laplace transforms obtained via reflection and strong independent increments.
- [[brownian-motion]] — specializes: Adding a deterministic linear drift mu t to standard BM.
[To be populated during integration]