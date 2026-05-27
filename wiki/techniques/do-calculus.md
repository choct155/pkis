---
id: "pkis:technique:do-calculus"
aliases: []
title: "do-Calculus"
knowledge_type: technique
also_type: [result]
domain: [causal-analysis, bayesian-stats]
tags: [causality, interventions, identification, causal-inference, pearl]
related_concepts: ["[[structural-causal-models]]", "[[d-separation]]", "[[confounding]]", "[[counterfactuals]]"]
sources: ["[[pearl-causality]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

## Reading Path
- [[pearl-causality-ch03]] (unread) — identification of causal effects; back-door and front-door criteria
- [[pearl-causality-ch04]] (unread) — actions and direct effects; do-operator mechanics

A complete system of three inference rules (deletion of observations, action/observation exchange, deletion of actions) that manipulate expressions containing both observational and interventional distributions `P(·|do(·))`. The do-operator formalizes external intervention by replacing a structural equation and severing all incoming edges to the intervened variable. Pearl (1995) proved completeness: any identifiable causal effect expressible in the do-calculus can be reduced to a purely observational expression using only these three rules.
