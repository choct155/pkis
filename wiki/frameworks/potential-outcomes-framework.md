---
aliases: []
also_type:
- concept
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
id: pkis:framework:potential-outcomes-framework
knowledge_type: framework
maturity: settled
related_concepts:
- - - counterfactuals
- - - average-treatment-effect
- - - selection-bias
- - - sutva
- - - structural-causal-models
sources:
- - - cunningham-causal-inference-mixtape
tags:
- causal-inference
- rubin
- counterfactuals
- ate
- selection-bias
- randomization
- neyman-rubin
title: Potential Outcomes Framework
understanding: 0
uses:
- strong-ignorability
---

Rubin's potential outcomes framework (also called the Neyman-Rubin causal model) formalizes causal effects as comparisons between counterfactual outcomes: Y(1) is the outcome a unit would have under treatment, Y(0) is the outcome under control, and the individual causal effect is Y(1)−Y(0) — which is fundamentally unobservable for any single unit (the fundamental problem of causal inference).

## Reading Path
- [[cunningham-causal-inference-mixtape-ch05]] (unread) — primary treatment: SUTVA, ATE/ATT/ATU, selection bias decomposition, STAR experiment application
- [[cunningham-causal-inference-mixtape]] (unread) — book-level context for how potential outcomes integrates with DAG approach

## Connections
- [[strong-ignorability]] — uses: Strong ignorability is the unconfoundedness assumption central to identification in the potential-outcomes framework.