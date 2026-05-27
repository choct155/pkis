---
id: "pkis:concept:local-average-treatment-effect"
aliases: []
title: "Local Average Treatment Effect"
knowledge_type: concept
also_type: []
domain: [causal-analysis]
tags: [causal-inference, late, iv, compliers, instrumental-variables, heterogeneous-treatment-effects]
related_concepts: [[[average-treatment-effect]], [[instrumental-variables]], [[potential-outcomes-framework]], [[regression-discontinuity]]]
sources: [[[cunningham-causal-inference-mixtape]]]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The local average treatment effect (LATE) is the average causal effect for *compliers* — units whose treatment status is changed by the instrument (they take treatment when assigned to treatment group and do not when assigned to control); IV and fuzzy RDD identify LATE, not ATE, unless all units are compliers or treatment effects are homogeneous.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch08]] (unread) — primary treatment via IV: complier/defier typology, Angrist-Imbens-Rubin 1996 interpretation
- [[cunningham-causal-inference-mixtape-ch07]] (unread) — LATE in fuzzy RDD context
