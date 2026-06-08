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
contrasts-with:
- expected-utility-theory
coverage: 1
date_created: '2026-06-01'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:expected-loss
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- '[[berger-statistical-1985]]'
tags:
- expected-loss
- risk
- decision-theory
title: Expected Loss
understanding: 0
---

## Definition
The probability-weighted average loss of a decision under a loss function — the quantity minimized in statistical decision theory and the basis of the retrieval-vs-inference cost model.

## Reading Path
- [[berger-statistical-1985]] — canonical source

## Connections
- [[expected-utility-theory]] — contrasts-with: Expected loss is the pessimist's dual L = -U; minimising one is maximising the other.
[To be populated during integration]

## Needs Canonical Source
Resolved — canonical source(s) attached above.

## Loss as Negative Utility (MacKay)
MacKay frames expected loss as the pessimist's mirror of expected utility: set $L(x,a) = -U(x,a)$ and replace maximisation of $\mathcal{E}[U\mid a]$ with minimisation of $\mathcal{E}[L\mid a] = \int d^K x\, L(x,a)\,P(x\mid a)$. The two are formally identical — the same $\arg$, opposite sign — so all expected-utility machinery (averaging over a state distribution, then optimising over actions) carries over unchanged. The practical content lies entirely in choosing $L$: a *linear* loss in a Gaussian return problem makes the optimal action depend only on posterior means and ignore variances, whereas a *nonlinear* (e.g. concave-utility) loss is what makes posterior uncertainty bear on the decision. This is also where pathologies enter — e.g. a **regret**-based loss (minimise the maximum possible regret) can be constructed but, as the lottery-ticket example shows, may prescribe behaviour hard to justify on coherence grounds.