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
- reinforcement-learning
id: pkis:technique:count-based-exploration
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch35
tags:
- exploration
- UCB
- intrinsic-motivation
- sample-efficiency
title: Count-Based Exploration with Intrinsic Bonus
understanding: 0
---

## Definition
Augment the observed reward with an exploration bonus inversely proportional to the visit count:
$$\tilde{r}(s,a) = r(s,a) + \frac{\alpha}{\sqrt{N_{s,a}}}$$
where $N_{s,a}$ is the number of times action $a$ has been taken in state $s$ and $\alpha\geq 0$ controls the exploration weight. For large or continuous state spaces, pseudo-counts derived from density models or hashing replace raw counts.

### Why it matters
Count-based exploration gives a practical approximation to UCB-style exploration in MDPs (MBIE-EB). The $1/\sqrt{N}$ bonus follows from optimistic initialisation and the standard UCB confidence interval, connecting bandit exploration theory to tabular and deep RL. Variants include hash-based counts (SimHash), CTS density models, and random network distillation (RND).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]