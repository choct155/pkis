---
aliases: []
also_type: []
applies:
- counterfactuals
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
id: pkis:technique:twin-network-method
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch07
specializes:
- abduction-action-prediction
tags:
- counterfactuals
- bayesian-networks
- d-separation
- structural-causal-models
- causality
title: Twin-Network Method
understanding: 0
uses:
- d-separation
- directed-graphical-models
---

## Definition
A graphical construction (Balke and Pearl 1994b) that reduces the computation of a counterfactual probability $P(Y_x = y \mid z)$ to ordinary evidence propagation in a single augmented Bayesian network. Two copies of the causal diagram—one for the **actual** world and one for the **hypothetical** world under $do(X=x)$—are laid side by side; like Siamese twins they **share the background variables $U$** (invariant), while endogenous variables are duplicated (e.g. $Y$ and $Y^*$) because they may differ across worlds.

*Intuition:* counterfactuals compare two worlds sharing the same boundary conditions $U$; gluing the two networks at $U$ lets standard inference do the abduction–action–prediction in one pass.

### Construction
The hypothetical-world copy deletes the arrows entering $X^*$ (mirroring the equation removed in submodel $M_x$) and fixes $X^* = x$. Computing $P(Y_x = y \mid z)$ then reduces to computing the conditional $P(y^* \mid z)$ in the twin network, which standard belief-propagation handles—without ever explicating the posterior $P(u \mid z)$.

### Why it matters
Naive abduction–action–prediction must store the full joint posterior $P(u \mid e)$, which loses the independence structure of the prior and can be prohibitively large. The twin network sidesteps this: it exploits conditional independencies, enables local computation, and turns a counterfactual query into a familiar Bayesian-network query.

### Bonus: testing counterfactual independencies
The twin network also lets one read off independencies among counterfactual variables via **d-separation**. For a chain $X \to Z \to Y$, conditioning on $Z$ d-connects $X$ and $Y^*$ through a collider, so $Y_x \not\perp X \mid Z$. The error term $U_Z$ serves as a one-way proxy for any counterfactual $Z_{pa_Z}$. Generalizes to multi-networks (Shpitser and Pearl 2007).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[counterfactuals]] — applies
- [[directed-graphical-models]] — uses
- [[d-separation]] — uses
- [[abduction-action-prediction]] — specializes
[To be populated during integration]