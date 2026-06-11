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
id: pkis:concept:potential-outcomes-notation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- rubin
- counterfactual
- fundamental-problem
- interventional
- potential-outcomes
title: Potential Outcomes and Counterfactual Notation
understanding: 0
uses:
- counterfactuals
- structural-causal-model
- average-treatment-effect
- causal-hierarchy
---

## Definition
In the potential outcomes (Rubin) framework, for each unit $i$ and treatment level $a$, the **potential outcome** $Y_i(a)$ is the outcome that unit $i$ *would* exhibit if treatment were set to $a$, holding all other unit-specific factors fixed:
$$Y_i(a) \triangleq f_Y(\text{Pa}(Y_i), a, \xi_{Y,i})$$
in the language of SCMs. Only the *factual* potential outcome $Y_i(A_i)$ is observed; the others are counterfactual.

Key quantities expressible in this notation:
- $\text{ATE} = \mathbb{E}[Y_i(1)-Y_i(0)]$ — requires only *marginal* distributions.
- $\mathbb{E}[Y_i(0)|Y_i(1)=1, A_i=1]$ — requires the *joint* distribution of $(Y_i(0), Y_i(1))$ within individuals (a Level-3/cross-world query).

### Why it matters
Potential outcomes notation is mathematically equivalent to do-calculus for interventional queries but makes individual-level counterfactual reasoning more direct. It clarifies the *fundamental problem of causal inference*: we can never simultaneously observe $Y_i(1)$ and $Y_i(0)$ for the same unit. The distinction between queries requiring only marginal vs. joint distributions of potential outcomes separates interventional (Level-2) from counterfactual (Level-3) queries.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[causal-hierarchy]] — uses
- [[average-treatment-effect]] — uses: ATE = E[Y(1)-Y(0)] in potential outcomes notation
- [[structural-causal-model]] — uses: Potential outcomes Y_i(a) are defined via SCM noise replay
- [[counterfactuals]] — uses
[To be populated during integration]