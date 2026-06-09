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
id: pkis:concept:attribution-and-but-for-causation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch09
tags:
- epidemiology
- legal-reasoning
- attributable-fraction
- excess-risk-ratio
- counterfactuals
title: Attribution and But-For Causation
understanding: 0
---

## Definition
The problem of assigning causal responsibility for an observed outcome to a specific antecedent -- the question 'was the exposure (or defendant's action) the cause of this disease (or harm)?'. The legal 'but-for' standard ('judgment for the plaintiff iff it is more probable than not that the defendant's action was the cause') is exactly a probability-of-necessity (PN > 1/2) criterion. Epidemiologists routinely estimate attribution by the excess risk ratio ERR = [P(y|x) - P(y|x')]/P(y|x), variously (mis)named 'attributable fraction', 'attributable-rate percent', or 'attributable proportion', and the risk difference, misnamed 'attributable risk'. Pearl's central caution: these purely statistical formulas equal the counterfactual PN only under the tacit assumptions of exogeneity (no confounding) and monotonicity (no prevention); when monotonicity fails ERR is merely a lower bound on PN, and when confounding is present ERR must be corrected by an additive term [P(y|x') - P(y_{x'})]/P(x,y), which can make true PN far larger than ERR. Combining experimental and nonexperimental data can identify attribution that neither study alone reveals (e.g. drug-lawsuit example, PN = 1.0). Pearl, Causality 2nd ed., Ch. 9 (Sections 9.3, 9.3.4, Table 9.3).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]