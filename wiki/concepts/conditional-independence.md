---
title: "Conditional Independence"
knowledge_type: concept
also_type: []
domain: [bayesian-stats, causal-analysis, knowledge-representation]
tags: [probability-theory, graph-theory]
related_concepts: ["[[directed-graphical-models]]", "[[d-separation]]", "[[belief-propagation]]", "[[bayesian-networks]]"]
sources: ["[[pearl-reverend-bayes-1982]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The property that X⊥Y|Z — knowing Z renders X and Y statistically independent; in graphical models, conditional independence is a structural consequence of network topology (single-link connectivity between network regions), not an additional assumption — Pearl's 1982 paper shows that the standard Bayesian product rule for multi-valued variables requires only this weak topological form of CI.

## Reading Path
- [[pearl-reverend-bayes-1982]] (unread) — demonstrates CI as structural consequence of single-link connectivity; key distinction from over-restrictive CI assumptions (Pednault et al.)
