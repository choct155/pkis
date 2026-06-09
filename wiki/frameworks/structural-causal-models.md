---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
- bayesian-stats
- knowledge-representation
generalizes:
- causal-bayesian-network
id: pkis:framework:structural-causal-models
knowledge_type: framework
maturity: evolving
related_concepts:
- '[[directed-graphical-models]]'
- '[[do-calculus]]'
- '[[d-separation]]'
- '[[counterfactuals]]'
- '[[confounding]]'
sources:
- '[[pearl-causality]]'
- '[[cunningham-causal-inference-mixtape]]'
tags:
- causality
- dag
- structural-equations
- interventions
- counterfactuals
title: Structural Causal Models
understanding: 0
---

## Reading Path
- [[pearl-causality]] (unread) — primary source; the entire book develops SCM theory from first principles through counterfactuals
- [[cunningham-causal-inference-mixtape-ch04]] (unread) — econometrician's introduction to DAGs as identification tools; positions SCMs relative to potential outcomes framework

A Structural Causal Model is a triple M = ⟨U, V, F⟩ where U are exogenous (background) variables, V are endogenous variables, and F are structural equations assigning each V_i := f_i(pa(V_i), U_i). The associated DAG G has an edge X→Y whenever X appears in the structural equation for Y. SCMs are strictly more expressive than probabilistic DAGs: they support interventional queries (the do-operator severs incoming edges and replaces the structural equation) and counterfactual queries (evaluating what Y_x(u) would have been for specific background context u).

## Connections
- [[causal-bayesian-network]] — generalizes