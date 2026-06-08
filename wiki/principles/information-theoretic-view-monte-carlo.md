---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:principle:information-theoretic-view-monte-carlo
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch30
tags:
- MCMC
- information-theory
- acceptance-rate
- channel-capacity
- Metropolis
title: Information-Theoretic View of Monte Carlo
understanding: 0
---

## Definition
MacKay frames Monte Carlo sampling as **communication**: generating a sample from $P(x)$ involves two information flows. (1) Selecting a particular $x$ consumes at least $\log 1/P(x)$ random bits. (2) The sample conveys information about $P(x)$ from the subroutine that evaluates $P^*(x)$ to the user. Treating the algorithm as a channel and maximizing its rate of information transfer is the organizing principle for designing efficient samplers.

### The Metropolis bottleneck
In a 'dumb' Metropolis method whose proposals ignore $P$, all information about $P$ is mediated solely by the binary string $a$ of accept/reject decisions. Replacing $P$ by another distribution would change *only* this string. The information learned after $T$ steps is therefore upper-bounded by the entropy of $a$, namely $T\,H_2(f)$, where $f$ is the acceptance rate.

### Why it matters
This bound yields a one-line justification for the classic rule of thumb that a dumb Metropolis sampler should be tuned to an acceptance rate of about **one half**: $H_2(f)$ is maximized at $f=1/2$, so that setting maximizes the information about $P$ acquired per iteration. The corollary — dumb Metropolis can learn at most about **one bit per iteration** — is the strong motivation for 'smart' methods (Gibbs, HMC) and multi-state methods whose proposals depend on $P$, and an open question is whether they can beat the one-bit-per-iteration ceiling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]