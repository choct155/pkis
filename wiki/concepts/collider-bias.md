---
id: "pkis:concept:collider-bias"
aliases: []
title: "Collider Bias"
knowledge_type: concept
also_type: []
domain: [causal-analysis]
tags: [dag, collider, selection-bias, conditioning, berksons-paradox, confounding, causal-graphs]
related_concepts: [[[confounding]], [[directed-graphical-models]], [[selection-bias]], [[d-separation]], [[identification-strategy]]]
sources: [[[cunningham-causal-inference-mixtape]]]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Collider bias occurs when a researcher conditions on a variable X that is a common *effect* of both treatment D and outcome Y (D→X←Y): unlike confounders (which open spurious paths when uncontrolled), colliders *block* back-door paths when uncontrolled, but *open* spurious paths when conditioned on — the opposite of naive intuition about controlling for variables.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch04]] (unread) — primary treatment: DAG notation, collider definition, Berkson's paradox, beauty-talent simulation demonstrating the bias from controlling for a collider
