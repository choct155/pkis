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
id: pkis:concept:direct-and-indirect-effects
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch04
tags:
- causality
- mediation
- direct-effect
- indirect-effect
- pearl
title: Direct and Indirect Effects
understanding: 0
---

## Definition
A decomposition of the total causal effect of X on Y into the portion transmitted along the direct link X→Y versus the portion mediated by intervening variables. The **total effect** P(y|do(x)) does not always capture the target of inquiry; often one wants the **direct effect** — the sensitivity of Y to X with all other factors held fixed — because it isolates a stable mechanism (e.g., the direct biological effect of a birth-control pill on thrombosis, separate from its indirect protective effect via reduced pregnancy; or whether sex/race directly influences hiring apart from its effect through qualifications). Crucially, mediators must be held fixed by **physical intervention (do)**, not by conditioning or adjustment: conditioning on an intermediate variable can create spurious X–Y association even when there is no direct effect (the collider/selection mechanism X→Z←U→Y). Pearl distinguishes (i) the **controlled** direct effect — mediators fixed at chosen constants — from (ii) the **natural** (pure) direct and indirect effects, defined via nested counterfactuals Y(x', Z(x)). The natural decomposition gives TE(x,x') = DE(x,x') − IE(x',x), reducing to the additive DE+IE in linear models. Path-specific effects (Avin et al. 2005) generalize this to effects transmitted along a selected set of paths.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]