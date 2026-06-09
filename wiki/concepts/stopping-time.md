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
- statistical-learning
id: pkis:concept:stopping-time
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- martingales
related_concepts: []
sources:
- resnick-stochastic-processes-ch01
tags:
- probability-theory
- stochastic-processes
- filtrations
- sigma-fields
- martingales
title: Stopping Time
understanding: 0
---

## Definition
$$\alpha : \Omega \to \{0,1,\ldots,\infty\}, \qquad [\alpha = n] \in \mathcal{F}_n \;\;(\text{equivalently } [\alpha \le n] \in \mathcal{F}_n) \;\; \forall n$$

Given an increasing family of $\sigma$-fields $\mathcal{F}_n \subset \mathcal{F}_{n+1}$ (a *filtration* encoding accumulating information), a random time $\alpha$ is a stopping time if the decision to stop at time $n$ depends only on what has been observed up to time $n$ — never on the future.

### The gambler intuition
Think of a gambler who must decide when to quit. A stopping rule is legitimate only if it uses past plays, not foreknowledge of the next outcome. The value $\infty$ is allowed because the awaited event may never happen (e.g. a random walk that never reaches a target).

### Information at a stopping time
The pre-$\alpha$ $\sigma$-field $\mathcal{F}_\alpha = \{A \in \mathcal{F}_\infty : A \cap [\alpha=n] \in \mathcal{F}_n \;\forall n\}$ captures the information available up to the random time $\alpha$. For i.i.d. sequences the pre- and post-$\alpha$ fields are independent and the post-$\alpha$ process is a fresh copy of the original — a *strong Markov / regeneration* property.

### Why it matters
Stopping times are the formal device that makes "the first time something happens" a rigorous random variable rather than peeking into the future. They are the gateway to optional stopping for martingales, to Wald's identity for randomly stopped sums, and to first-passage and hitting-time analysis throughout stochastic-process theory.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[martingales]] — prerequisite-of: Stopping times are the formal prerequisite for optional stopping and martingale stopping theorems.
[To be populated during integration]