---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- causal-analysis
- bayesian-stats
- statistical-learning
id: pkis:concept:confounding
instantiates:
- causal-statistical-distinction
knowledge_type: concept
maturity: settled
related_concepts:
- '[[structural-causal-models]]'
- '[[do-calculus]]'
- '[[d-separation]]'
- '[[directed-graphical-models]]'
- '[[bias-variance-tradeoff]]'
sources:
- '[[pearl-causality]]'
- '[[cunningham-causal-inference-mixtape]]'
- li-forecaster-pearl-causality-2023
- cunningham-causal-inference-mixtape-ch03
- cunningham-causal-inference-mixtape-ch04
tags:
- causality
- causal-inference
- back-door
- front-door
- common-cause
- spurious-correlation
title: Confounding
understanding: 0
uses:
- d-separation
---

## Reading Path
- [[pearl-causality-ch06]] (unread) — Simpson's paradox, confounding, and collapsibility; causal definition of confounding
- [[pearl-causality-ch03]] (unread) — back-door and front-door identification criteria
- [[cunningham-causal-inference-mixtape-ch04]] (unread) — confounders in DAGs vs. colliders; backdoor criterion for practitioners; econometric examples

In Pearl's causal framework, confounding arises when there exists an open back-door path from treatment X to outcome Y — a path entering X through an arrowhead (a common cause). A set Z satisfies the back-door criterion if it blocks all back-door paths and excludes descendants of X; conditioning on such Z identifies the causal effect `P(Y|do(X)) = Σ_z P(Y|X,Z=z)P(Z=z)`. Pearl's causal definition supersedes the purely statistical notion: confounding is not simply correlation between treatment and covariates, but a structural property of the DAG.

## Connections
- [[causal-statistical-distinction]] — instantiates: Confounding is Pearl's paradigm example of a concept that cannot be defined from the distribution alone.
- [[d-separation]] — uses: the back-door criterion blocking open back-door paths is a d-separation test