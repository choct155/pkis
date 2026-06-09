---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- knowledge-representation
id: pkis:problem:data-association
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch15
specializes:
- open-universe-probability-model
tags:
- tracking
- identity-uncertainty
- state-estimation
- kalman-filter
- open-universe
- control-theory
title: Data Association
understanding: 0
uses:
- kalman-filter
- particle-filter
---

## Definition
The problem of associating observations with the objects that generated them when multiple objects produce indistinguishable percepts over time — identity uncertainty in a temporal setting. Originating in radar tracking of multiple targets, it is the obstacle that separates multitarget tracking from ordinary state estimation: at each step several blips appear with no label tying time-t observations to time-(t-1) ones. Each possible world fixes an association (the Source(b) variables); for n objects over T steps there are (n!)^T assignments, and real settings add false alarms (clutter), detection failures, and object birth/death. No efficient exact algorithm exists (the filtering distribution is a mixture of exponentially many components, as in the switching Kalman filter). Approximate methods: the nearest-neighbor filter; the Hungarian algorithm for the single most-likely assignment; and far more robust sampling methods (particle filtering, MCMC over assignment histories), often accelerated by Rao-Blackwellization (run an exact Kalman filter per hypothesized object given an association). Applications include radar/air tracking and wide-area traffic surveillance across cameras.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[particle-filter]] — uses: particle filtering maintains a population of candidate associations
- [[kalman-filter]] — uses: per-hypothesis state filtering (linear-Gaussian) via Rao-Blackwellization
- [[open-universe-probability-model]] — specializes: data association is identity uncertainty in a temporal context, an important special case of open-universe modeling
[To be populated during integration]