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
date_updated: '2026-06-20'
domain:
- bayesian-stats
extends:
- weak-law-of-large-numbers
id: pkis:result:ergodic-theorem-markov
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch02
- betancourt-short-2021
tags:
- stochastic-processes
- markov-property
- ergodicity
- coupling
- law-of-large-numbers
- limiting-distributions
- convergence
title: Ergodic Theorem for Markov Chains (Convergence to Stationarity)
understanding: 0
uses:
- stationary-distribution
- recurrence-and-transience
---

## Definition
For an irreducible, aperiodic, positive-recurrent (i.e. ergodic) Markov chain with stationary distribution \pi, the n-step transition probabilities converge to \pi independently of the start state: \lim_{n\to\infty} p_{ij}^{(n)} = \pi_j for all i,j, and every \pi_j>0. Equivalently P^n -> \Pi, the matrix with identical rows \pi. Resnick's Theorem 2.13.2 packages a powerful test: for an irreducible aperiodic chain the mere existence of a stationary distribution implies positive recurrence, uniqueness of \pi, and that \pi is the limit distribution.

Two complementary limit theorems hold. (1) The Markov-chain strong law of large numbers (Prop. 2.12.4): for irreducible positive-recurrent chains and well-behaved f, N^{-1}\sum_{n=0}^N f(X_n) -> \pi(f) = \sum_j f(j)\pi_j almost surely, regardless of initial distribution; with f=1_{{i}} this says the long-run fraction of time in state i is \pi_i. The proof rests on the dissection of the path into iid excursions between visits to a reference state plus the iid SLLN. (2) The convergence p_{ij}^{(n)}->\pi_j is proved by the coupling method: run an independent copy {Y_n} started from \pi, form the product chain \zeta_n=(X_n,Y_n) (irreducible by a number-theoretic aperiodicity lemma, positive recurrent with stationary law \pi_k\pi_l), let \tau be the first time both coordinates meet at a fixed state, and bound |p_{ij}^{(n)}-\pi_j| <= P[\tau>n] -> 0. Aperiodicity is essential: a period-2 chain has p_{jj}^{(2n+1)}=0, so P^n cannot converge though a Cesaro (time-average) limit still exists.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[weak-law-of-large-numbers]] — extends: the Markov-chain SLLN generalizes the iid law of large numbers via iid path excursions
- [[recurrence-and-transience]] — uses: ergodicity = irreducible + aperiodic + positive recurrent
- [[stationary-distribution]] — uses: states convergence of P^n to the stationary distribution
[To be populated during integration]