---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- interpretability
- fairness
- law
id: pkis:problem:algorithmic-recourse
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
tags:
- recourse
- actionability
- counterfactual
- fairness
- GDPR
- interpretability
title: Recourse in Automated Decision-Making
understanding: 0
uses:
- counterfactual-explanation
- algorithmic-fairness
- causal-analysis
---

## Definition
**Algorithmic recourse** is the problem of providing an individual subject to an adverse automated decision with an actionable set of changes $\delta$ to their features such that the revised decision becomes favorable:
$$\text{Find } \delta \in \mathcal{A}(x) \quad \text{s.t.} \quad f(x+\delta) \neq f(x), \quad \text{minimizing cost}(\delta)$$
where $\mathcal{A}(x)$ restricts $\delta$ to *actionable* and *plausible* changes (mutable features, within-distribution).

This differs from a standard counterfactual in that (1) cost must reflect real-world effort/feasibility, (2) immutable attributes (age, race) must be excluded, and (3) the recourse must remain valid under model updates (robustness).

### Why it matters
Recourse operationalizes the *right to explanation* mandated in regulations such as GDPR Article 22 and the US Equal Credit Opportunity Act. Without recourse, denied loan applicants, rejected job candidates, or flagged travelers have no path to appeal or improvement. Research challenges include: defining appropriate cost functions, ensuring recourse robustness to model changes, handling feature correlations (structural causal models), and distinguishing recourse (what to change) from explanation (why the decision was made).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[causal-analysis]] — uses: Structural causal models can constrain recourse to causally plausible interventions.
- [[algorithmic-fairness]] — uses
- [[counterfactual-explanation]] — uses
[To be populated during integration]