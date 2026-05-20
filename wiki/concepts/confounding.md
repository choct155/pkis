---
title: "Confounding"
knowledge_type: concept
also_type: []
domain: [causal-analysis, bayesian-stats, statistical-learning]
tags: [causality, causal-inference, back-door, front-door, common-cause, spurious-correlation]
related_concepts: ["[[structural-causal-models]]", "[[do-calculus]]", "[[d-separation]]", "[[directed-graphical-models]]", "[[bias-variance-tradeoff]]"]
sources: ["[[pearl-causality]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

## Reading Path
- [[pearl-causality-ch06]] (unread) — Simpson's paradox, confounding, and collapsibility; causal definition of confounding
- [[pearl-causality-ch03]] (unread) — back-door and front-door identification criteria

In Pearl's causal framework, confounding arises when there exists an open back-door path from treatment X to outcome Y — a path entering X through an arrowhead (a common cause). A set Z satisfies the back-door criterion if it blocks all back-door paths and excludes descendants of X; conditioning on such Z identifies the causal effect `P(Y|do(X)) = Σ_z P(Y|X,Z=z)P(Z=z)`. Pearl's causal definition supersedes the purely statistical notion: confounding is not simply correlation between treatment and covariates, but a structural property of the DAG.
