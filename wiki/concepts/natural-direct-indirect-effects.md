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
- causal-analysis
- bayesian-stats
id: pkis:concept:natural-direct-indirect-effects
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch04
tags:
- causality
- mediation
- counterfactuals
- mediation-formula
- pearl
title: Natural Direct and Indirect Effects
understanding: 0
---

## Definition
Effect measures, defined via **nested counterfactuals**, that quantify mediation without holding mediators at fixed constants. The **natural (pure) direct effect** is DE(x,x') = E[Y(x', Z(x))] − E[Y(x)]: the change in Y when X is set to x' while every mediator Z is held at the value it *would have taken* under X=x. The **natural indirect effect** is IE(x,x') = E[Y(x, Z(x'))] − E[Y(x)]: hold X at x but let the mediators move to their X=x' values — capturing the channel one cannot otherwise isolate, since the do-operator cannot disable the direct link X→Y. They satisfy TE(x,x') = DE(x,x') − IE(x',x), reducing to TE = DE + IE in linear models. Because Y(x', Z(x)) mixes two incompatible antecedents, natural effects cannot be written with the do-operator and are **not identifiable even from ideal controlled experiments** in general; under a 'no-confounding' assumption (e.g. Z(x) ⊓ Y(x',z) | W) they reduce to a weighted average of controlled direct effects with weight P(z|do(x)), and in Markovian models to the **Mediation Formula** DE = Σ_z[E(Y|x',z)−E(Y|x,z)]P(z|x), IE = Σ_z E(Y|x,z)[P(z|x')−P(z|x)] — applicable to any nonlinear system, distribution, or variable type. Policy relevance: the natural indirect effect predicts the outcome mix under a 'treat everyone equally' policy that removes direct bias but leaves mediated channels intact.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]