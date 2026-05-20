---
title: "Markov Logic Networks"
knowledge_type: technique
also_type: [framework]
domain: [symbolic-subsymbolic, bayesian-stats, knowledge-representation]
tags: [probabilistic-logic, first-order-logic, markov-networks, weighted-formulas, knowledge-graphs, statistical-relational-learning]
related_concepts: [statistical-relational-learning, neurosymbolic-ai, inductive-logic-programming, directed-graphical-models]
sources: ["[[delong-nsai-kg-survey-2024]]", "[[belle-future-neurosymbolic-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Markov Logic Networks (MLNs) ground a set of weighted first-order formulas over a finite set of constants to produce a Markov random field: nodes are all groundings of all atoms appearing in the formulas, edges connect atoms co-occurring in a formula, and the probability of a possible world is proportional to the exponential of the sum of weights of satisfied formula groundings.

Classification note: assigned as technique (a procedure for defining and computing probability distributions over relational domains), but also_type framework because MLNs organize a research ecosystem with associated inference algorithms and learning procedures.

## Reading Path
- [[delong-nsai-kg-survey-2024]] (unread) — MLNs as background probabilistic logic for KG reasoning; motivates soft neurosymbolic approaches
- [[belle-future-neurosymbolic-2025]] (unread) — MLNs within the SRL lineage leading to modern probabilistic NSAI
