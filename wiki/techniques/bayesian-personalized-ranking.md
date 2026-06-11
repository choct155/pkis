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
- machine-learning
- recommender-systems
id: pkis:technique:bayesian-personalized-ranking
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch22
tags:
- ranking-loss
- implicit-feedback
- pairwise-learning
- negative-sampling
title: Bayesian Personalized Ranking (BPR)
understanding: 0
---

## Definition
$$\mathcal{L}(\theta) = \sum_{(u,i,j) \in D} \log \sigma\!\left(f(u,i;\theta) - f(u,j;\theta)\right) - \lambda\|\theta\|^2$$

where the training set $D = \{(u,i,j): i \in I_u^+,\; j \in I \setminus I_u^+\}$ consists of pairwise comparisons derived from implicit feedback — item $i$ was interacted with by user $u$ and item $j$ was not. The likelihood of the ordering $(i \succ_u j)$ is modelled as a sigmoid of the score difference.

### Why it matters
BPR is the canonical method for learning-to-rank from implicit (positive-only) feedback. By treating unobserved interactions as a pool of sampled negatives rather than as explicit zeroes, it avoids the systematic bias introduced by negative-labelling all unseen items. The hinge-loss variant connects directly to SVM-style large-margin ranking.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]