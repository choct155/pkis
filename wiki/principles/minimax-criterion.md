---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:principle:minimax-criterion
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch13
tags:
- decision-theory
- minimax
- minimin
- game-theory
- loss-matrix
title: Minimax Criterion
understanding: 0
---

## Definition
A decision criterion that, for each decision $D_i$, computes the maximum possible loss $M_i=\max_j(L_{ij})$ and then chooses the $D_i$ minimizing $M_i$. It is the strategy of one who regards Nature as an intelligent adversary that foresees the decision and deliberately picks the worst state — sensible in genuine adversarial games (von Neumann–Morgenstern), where minimax strategies are of fundamental importance. Its mirror image is the **minimin** criterion of the starry-eyed optimist, who picks the $D_i$ minimizing the best-case loss $m_i=\min_j(L_{ij})$. Jaynes argues that for the scientist, engineer, or economist there is no intelligent adversary, so minimax is the criterion of 'the long-faced pessimist who concentrates all his attention on the worst possible thing'; a reasonable criterion is intermediate, expressing the belief that Nature is *neutral* toward our goals. Many proposed criteria (maximin utility, Hurwicz $\alpha$-optimism–pessimism, Savage minimax regret) are tested against qualitative common-sense conditions such as transitivity and strong domination, but the only class passing all tests turns out to be the Bayes rules, reached more easily by another route.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]