---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
id: pkis:technique:residual-belief-propagation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch09
tags:
- message-scheduling
- loopy-BP
- priority-queue
- convergence
- approximate-inference
title: Residual Belief Propagation
understanding: 0
---

## Definition
An adaptive message-scheduling algorithm for loopy BP in which messages are prioritised by their **residual**—the $\ell_\infty$ norm of the log-ratio between the prospective new message and the current message:

$$r(s,t,k) = \|\log m_{s\to t} - \log m^k_{s\to t}\|_\infty = \max_j\left|\log\frac{m_{s\to t}(j)}{m^k_{s\to t}(j)}\right|$$

Messages are stored in a max-priority queue. At each step the highest-residual message is sent; all dependent messages $m_{t\to u}$ are recomputed and reinserted. Initialise with all messages equal to $\mathbf{1}$.

Intuition: spend computation where beliefs are changing fastest, analogous to residual-driven adaptive methods in numerical linear algebra.

### Why it matters
Residual BP (Elidan et al., 2006) converges more often and much faster than synchronous or fixed-order asynchronous scheduling. It is a practical tool for making LBP tractable on difficult graphs. The variant that uses upper bounds on residuals (Sutton & McCallum, 2007) achieves ~5× speedup by avoiding computing messages that will not be sent.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]