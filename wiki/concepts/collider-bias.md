---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
id: pkis:concept:collider-bias
instantiates:
- causal-statistical-distinction
knowledge_type: concept
maturity: settled
related_concepts:
- - - confounding
- - - directed-graphical-models
- - - selection-bias
- - - d-separation
- - - identification-strategy
sources:
- "[[cunningham-causal-inference-mixtape]]"
tags:
- dag
- collider
- selection-bias
- conditioning
- berksons-paradox
- confounding
- causal-graphs
title: Collider Bias
understanding: 0
---

Collider bias occurs when a researcher conditions on a variable X that is a common *effect* of both treatment D and outcome Y (D→X←Y): unlike confounders (which open spurious paths when uncontrolled), colliders *block* back-door paths when uncontrolled, but *open* spurious paths when conditioned on — the opposite of naive intuition about controlling for variables.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch04]] (unread) — primary treatment: DAG notation, collider definition, Berkson's paradox, beauty-talent simulation demonstrating the bias from controlling for a collider

## Connections
- [[causal-statistical-distinction]] — instantiates: Conditioning on post-treatment colliders opens spurious paths even in randomized trials, a hazard invisible at the distribution level.