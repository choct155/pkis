---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
contrasts-with:
- actual-causation
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
id: pkis:principle:but-for-vs-actual-cause
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch10
tags:
- causality
- counterfactuals
- legal-reasoning
- preemption
- overdetermination
title: But-For Test vs. Actual Cause
understanding: 0
uses:
- counterfactuals
---

## Definition
The but-for (counterfactual dependence) test -- x caused y iff y would not have occurred but for x -- is the classical criterion of causation (Lewis 1986) and the legal standard, but it systematically fails in multi-cause scenarios, which is why a structural notion (sustenance/causal beam) is needed. Two failure modes: (1) PREEMPTION, where a backup cause stands ready so the effect does not depend on the actual cause -- the desert traveler (enemy 2 shoots the canteen, preempting enemy 1's poison: y = x v x'p, structurally asymmetric though logically equal to x v p), or switch 1 disconnecting switch 2; here x is intuitively the cause yet fails the but-for test because y persists without it. (2) OVERDETERMINATION, where two sufficient causes co-occur (firing squad: both riflemen shoot; two fires; D = A v B) so neither passes the but-for test yet each is intuitively a contributory cause. Lewis's repairs -- requiring a counterfactual-dependence chain of intermediate links, and treating dependence as "intrinsic" to a process so quasi-dependence survives peculiar surroundings -- are ad hoc and, as Hall (2004) noted, leave "what is a process?" undefined. Temporal preemption (fire A burns first) cannot even be expressed in static structural models and requires dynamic, time-indexed models. The principle: but-for captures only Hall's "dependence"; actual causation also requires "production," and the right replacement is sustenance against structural contingencies, with but-for recovered as the W=empty special case.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[counterfactuals]] — uses: the but-for criterion is the counterfactual-dependence account (Lewis)
- [[actual-causation]] — contrasts-with: the but-for test fails to capture actual causation under preemption/overdetermination
[To be populated during integration]