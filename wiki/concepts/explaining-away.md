---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:explaining-away
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch21
tags:
- bayesian-inference
- conditional-independence
- graphical-models
- inference
title: Explaining Away
understanding: 0
---

## Definition
Explaining away is the phenomenon in which two causes that are independent a priori become anti-correlated in the posterior once a common effect is observed: confirming one cause makes the other less probable, because the observed effect is now already accounted for. Formally, if $b$ and $e$ are marginally independent causes of $a$, then in general

$$P(b\mid a)\,P(e\mid a) \neq P(b,e\mid a),$$

so the posterior over $(b,e)$ given $a$ does not factorize — conditioning on the shared child induces a dependence between the parents.

### Worked intuition
Fred's alarm ($a{=}1$) gives a burglar a ~50% posterior. Learning that an earthquake occurred ($e{=}1$) — an alternative explanation of the same alarm — drops the burglar's probability to ~8%. The earthquake 'explains away' the alarm even though earthquakes and burglars are independent events in the world.

### Why it matters
Explaining away is a hallmark of correct probabilistic reasoning and a signature behavior of inference in directed graphical models: observing a collider (common effect) activates a path between its parents (the 'v-structure' of d-separation). It is exactly the kind of context-sensitive reasoning that naive rule-based or modular AI systems fail to reproduce, and it explains why joint inference, rather than per-variable updating, is required.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]