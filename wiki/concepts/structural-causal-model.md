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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- causal-inference
- statistics
id: pkis:concept:structural-causal-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
- murphy-pml2-advanced-ch36
tags:
- causal-model
- DAG
- do-operator
- counterfactuals
- Pearl
title: Structural Causal Model (SCM)
understanding: 0
---

## Definition
A **structural causal model** $\mathcal{M} = (\mathbf{U}, \mathbf{V}, \mathcal{F}, P_\mathbf{U})$ consists of:
- $\mathbf{U}$: exogenous (noise) variables with joint distribution $P_\mathbf{U}$,
- $\mathbf{V}$: endogenous variables,
- $\mathcal{F} = \{f_i\}$: structural equations $V_i = f_i(\mathrm{PA}_i, U_i)$ where $\mathrm{PA}_i$ are the causal parents of $V_i$.

The induced graph is a DAG over $\mathbf{V}$. Interventions are modelled by the **do-operator**: $\text{do}(V_j = v)$ replaces $f_j$ with the constant $v$, creating a submodel $\mathcal{M}_{V_j = v}$.

An SCM supports reasoning at all three rungs of Pearl's ladder of causation: association ($P$), intervention ($P_{\text{do}}$), and counterfactuals ($P_{\text{cf}}$).

### Why it matters
SCMs are the formal language for causal inference beyond association. They are the target of causal discovery algorithms and provide the foundation for estimating interventional distributions, counterfactuals, and policy effects from data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]