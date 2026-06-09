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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:admissibility
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch13
tags:
- decision-theory
- admissibility
- risk
- sampling-theory
- wald
title: Admissibility of Decision Rules
understanding: 0
---

## Definition
A strategy $S$ is **admissible** if no other strategy $S'$ exists with $R_j(S')\le R_j(S)$ for all states of nature $\theta_j$ (with strict inequality for at least one $j$); if such an $S'$ exists, $S$ is **inadmissible**. Admissibility is a *sampling-theory* criterion, not Bayesian, because it invokes only the sampling distribution (the risk function). Wald, thinking in sampling-theory terms, considered it obvious that the optimal strategy should be sought only among admissible rules. Jaynes regards the notion as deeply flawed: an estimator that ignores the data and always returns $\theta^*=5$ is *admissible* whenever $\theta=5$ lies in the parameter space, even though almost any 'inadmissible' rule would beat it. He uses this to illustrate 'the folly of inventing noble-sounding names such as admissible and unbiased for principles that are far from noble', and warns that admissibility produces spurious singular mathematics in infinite parameter spaces precisely because it refuses to consider any prior information, treating all points of an infinite domain as equivalent.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]