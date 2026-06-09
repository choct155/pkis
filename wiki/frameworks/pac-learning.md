---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:framework:pac-learning
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- empirical-risk-minimization
- no-free-lunch-theorem
related_concepts: []
sources:
- russell-norvig-aima-ch19
tags: []
title: PAC Learning (Probably Approximately Correct)
understanding: 0
uses:
- supervised-learning
---

## Definition
The central framework of computational learning theory: any hypothesis consistent with a sufficiently large set of training examples is unlikely to be seriously wrong, hence is probably approximately correct (PAC). A learning algorithm is a PAC-learning algorithm if it returns such hypotheses, and the framework yields distribution-free bounds on how many examples suffice.

The formal setup, for Boolean functions under 0/1 loss, defines error(h) as the probability that h misclassifies a new example drawn from the stationary distribution. A hypothesis is approximately correct if error(h) <= epsilon (it lies inside the epsilon-ball around f); the rest of the space is H_bad. A seriously wrong hypothesis agrees with one example with probability at most (1-epsilon), so it survives N i.i.d. examples with probability at most (1-epsilon)^N. Bounding the chance that any of the |H| hypotheses in H_bad stays consistent below delta and using 1-epsilon <= e^{-epsilon} gives the key sample-complexity bound:

  N >= (1/epsilon)(ln(1/delta) + ln|H|).

Thus with probability >= 1-delta, after this many examples the returned hypothesis has error at most epsilon. The required N is the sample complexity. The 'juice' connecting past to future is the stationarity assumption; one also assumes f is deterministic and lies in H.

For the class of all Boolean functions on n attributes |H|=2^{2^n}, so sample complexity grows as 2^n -- essentially all examples are needed, no generalization. Escaping this requires restricting H: bring prior knowledge, prefer simple consistent hypotheses, or focus on learnable subsets. The canonical learnable subset is k-DL (decision lists with tests of at most k literals): |k-DL(n)| = 2^{O(n^k log n^k)}, giving a sample complexity polynomial in n, so k-DL is PAC-learnable for small k by a greedy consistent-list algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[no-free-lunch-theorem]] — prerequisite-of
- [[empirical-risk-minimization]] — prerequisite-of
- [[supervised-learning]] — uses
[To be populated during integration]