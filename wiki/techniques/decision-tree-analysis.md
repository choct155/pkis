---
aliases: []
also_type: []
applies:
- value-of-information
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
- bayesian-stats
id: pkis:technique:decision-tree-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch09
tags:
- decision-theory
- sequential-decisions
- backward-induction
- bayesian-updating
- value-of-information
title: Decision Tree Analysis
understanding: 0
uses:
- bayesian-inference
- bayesian-decision-analysis
---

## Definition
## Definition
A decision tree represents a multistage decision problem as a branching structure that alternates **decision nodes** (where the agent chooses) and **chance/uncertainty nodes** (where the world resolves). When a later decision depends on data gathered after an earlier one, the tree is solved by **backward induction**: evaluate expected utility at the deepest decision node first, conditioning on all information available there, then fold the resulting optimal values back toward the root. Bayesian inference enters at every chance node, updating the state of knowledge with new information via
$$ \Pr(\text{state}\mid T)=\frac{\Pr(\text{state})\,p(T\mid \text{state})}{\sum_{s}\Pr(s)\,p(T\mid s)}, $$
so the posterior after a test replaces the prior in the downstream branch.

### Why it matters
Decision trees make the *value of testing before acting* computable. Gelman's bronchoscopy example shows the subtle payoff: a diagnostic test is only worth doing if some outcome would change the chosen treatment. There, radiotherapy maximizes quality-adjusted life expectancy whether the test is positive or negative, so the test's information is worthless and (given its own 5% fatality risk) strictly harmful — it lowers expected QALE from 17.5 to 16.6 months. The tree framework exposes this by forcing the analyst to specify, at each node, exactly what would be done with the information, and is the natural home for value-of-information calculations in multistage problems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[value-of-information]] — applies
- [[bayesian-decision-analysis]] — uses
- [[bayesian-inference]] — uses
[To be populated during integration]