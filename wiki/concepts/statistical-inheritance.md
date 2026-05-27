---
id: "pkis:concept:statistical-inheritance"
aliases: []
title: "Statistical Inheritance"
knowledge_type: concept
also_type: [technique]
domain: [knowledge-representation, bayesian-stats]
tags: [statistics, default-reasoning, databases]
related_concepts: ["[[default-reasoning]]", "[[probability-theory]]"]
sources: ["[[rowe-statistical-inheritance-1982]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: historical
---

The propagation of statistical aggregate properties (mean, maximum, standard deviation, mode) from parent sets to subsets in a weaker form than exact value inheritance: each property is characterized by a four-tuple (upper bound, lower bound, best estimate, standard deviation of possibilities) that inherits more reliably than the raw value, enabling approximate statistical query answering over large databases. Classification note: assigned as concept (the mathematical idea of what it means for statistics to inherit) but may be technique because a production-rule system implements the inference.

## Reading Path
- [[rowe-statistical-inheritance-1982]] (unread) — introduces the four-characteristic framework, six inheritance directions, and a production-system architecture; Stanford KBMS project, AAAI-82
