---
aliases: []
also_type: []
applies:
- confounding
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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- bayesian-stats
id: pkis:concept:back-door-criterion
instantiates:
- identification-strategy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- identifiability-of-causal-effects
related_concepts: []
sources:
- pearl-causality-ch03
- pearl-causality-ch05
tags:
- causality
- identification
- confounding
- adjustment
- d-separation
- pearl
title: Back-Door Criterion
understanding: 0
uses:
- d-separation
---

## Definition
[To be filled during deepening]

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[identification-strategy]] — instantiates: The back-door criterion is a concrete graphical identification strategy.
- [[identifiability-of-causal-effects]] — prerequisite-of: Satisfying the back-door criterion is a sufficient condition for identifiability.
- [[confounding]] — applies: Identifies total effects by blocking confounding back-door paths.
- [[d-separation]] — uses: Adjustment set Z must d-separate X from Y in the mutilated graph G_X.
[To be populated during integration]