---
title: "Potential Outcomes Framework"
knowledge_type: framework
also_type: [concept]
domain: [causal-analysis]
tags: [causal-inference, rubin, counterfactuals, ate, selection-bias, randomization, neyman-rubin]
related_concepts: [[[counterfactuals]], [[average-treatment-effect]], [[selection-bias]], [[sutva]], [[structural-causal-models]]]
sources: [[[cunningham-causal-inference-mixtape]]]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Rubin's potential outcomes framework (also called the Neyman-Rubin causal model) formalizes causal effects as comparisons between counterfactual outcomes: Y(1) is the outcome a unit would have under treatment, Y(0) is the outcome under control, and the individual causal effect is Y(1)−Y(0) — which is fundamentally unobservable for any single unit (the fundamental problem of causal inference).

## Reading Path
- [[cunningham-causal-inference-mixtape-ch05]] (unread) — primary treatment: SUTVA, ATE/ATT/ATU, selection bias decomposition, STAR experiment application
- [[cunningham-causal-inference-mixtape]] (unread) — book-level context for how potential outcomes integrates with DAG approach
