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
id: pkis:result:constrained-channel-optimal-transitions
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch17
tags:
- eigenvector
- markov-chain
- maximum-entropy
- variational
- transition-matrix
- mackay
title: Optimal Transition Probabilities for a Constrained Channel
understanding: 0
---

## Definition
The capacity-achieving way to drive a constrained channel is to traverse its state machine as a Markov chain with carefully chosen transition probabilities. Let $\lambda$ be the leading eigenvalue of the connection matrix $A$, and $\mathbf{e}^{(R)},\mathbf{e}^{(L)}$ its principal right- and left-eigenvectors ($A\mathbf{e}^{(R)}=\lambda\mathbf{e}^{(R)}$, $\mathbf{e}^{(L)\top}A=\lambda\mathbf{e}^{(L)\top}$). The optimal transition matrix is
$$Q_{s'\mid s}=\frac{e^{(L)}_{s'}\,A_{s's}}{\lambda\,e^{(L)}_{s}},$$
whose invariant distribution is proportional to $e^{(R)}_s e^{(L)}_s$.

### Why it matters
Generating sequences with this $Q$ makes the source asymptotically *maximum-entropy among legal strings*: the per-symbol entropy reaches $\log_2\lambda$, exactly the channel capacity. The conditional entropy of one symbol given the previous (under the invariant distribution) collapses to $\log\lambda$ because the $A_{s's}\log A_{s's}$ terms vanish (entries are 0 or 1) and the eigenvector sums telescope. This is the noiseless analogue of finding the optimal input distribution for a noisy channel.

### Variational / time-cost view
When symbols have unequal durations $l_i$, the optimal usage frequency mirrors optimal symbol-code lengths: $p_i^{*}=2^{-\beta l_i}$, where $\beta$ (the capacity in bits per unit time) solves $\sum_i 2^{-\beta l_i}=1$. For a long max-runlength-$L$ channel, $\beta\approx 1-2^{-(L+2)}/\ln 2$, and the per-step probability of emitting a 1 falls from $\tfrac12$ toward $\tfrac13$ as a run approaches length $L$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]