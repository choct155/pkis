---
aliases: []
also_type:
- result
applies:
- identifiability-of-causal-effects
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
- bayesian-stats
id: pkis:technique:do-calculus
knowledge_type: technique
maturity: evolving
related_concepts:
- '[[structural-causal-models]]'
- '[[d-separation]]'
- '[[confounding]]'
- '[[counterfactuals]]'
sources:
- '[[pearl-causality]]'
tags:
- causality
- interventions
- identification
- causal-inference
- pearl
title: do-Calculus
understanding: 0
uses:
- intervention-do-operator
- causal-submodel
---

## Reading Path
- [[pearl-causality-ch03]] (unread) — identification of causal effects; back-door and front-door criteria
- [[pearl-causality-ch04]] (unread) — actions and direct effects; do-operator mechanics

A complete system of three inference rules (deletion of observations, action/observation exchange, deletion of actions) that manipulate expressions containing both observational and interventional distributions `P(·|do(·))`. The do-operator formalizes external intervention by replacing a structural equation and severing all incoming edges to the intervened variable. Pearl (1995) proved completeness: any identifiable causal effect expressible in the do-calculus can be reduced to a purely observational expression using only these three rules.

## Connections
- [[causal-submodel]] — uses
- [[identifiability-of-causal-effects]] — applies
- [[intervention-do-operator]] — uses