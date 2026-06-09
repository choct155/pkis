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
id: pkis:concept:probability-of-causation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch09
tags:
- counterfactuals
- attribution
- epidemiology
- legal-reasoning
- identification
title: Probability of Causation
understanding: 0
---

## Definition
An umbrella term for a family of counterfactual quantities that measure, for binary cause X and effect Y, the degree to which the occurrence of x was responsible for the occurrence of y in a population or in a singular case. The central members are the probability of necessity (PN), the probability of sufficiency (PS), and the probability of necessity and sufficiency (PNS); auxiliary members include the probability of disablement PD = P(y'_{x'} | y) and the probability of enablement PE = P(y_x | y'). All are defined within structural causal model semantics in terms of the potential responses Y_x(u) and Y_{x'}(u), and all condition on the actually observed event (e.g. on x,y for PN), which is what gives them their singular, attributive character. Because each conditions on y (presumed affected by x), none is identifiable from the causal diagram and the observational distribution P(x,y) alone, not even under no-confounding: knowledge of the functional mechanism (or extra assumptions such as monotonicity) is required. They are central to epidemiological attribution ('was this disease case caused by the exposure?') and to legal 'but-for' standards of causation. Pearl, Causality 2nd ed., Ch. 9 (Definitions 9.2.1-9.2.5, Lemma 9.2.6).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]