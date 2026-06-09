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
id: pkis:concept:inus-condition
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch10
tags:
- causality
- philosophy-of-causation
- logic
- law
- epidemiology
title: INUS Condition
understanding: 0
---

## Definition
The INUS condition (Mackie 1965) is the influential logical/regularity account of singular causation: an event C is a cause of E if C is "an Insufficient but Necessary part of a condition which is itself Unnecessary but Sufficient for the result." Formally, writing the conditions for E in disjunctive normal form as a collection {S_1,S_2,...} of minimally sufficient sets, C is an INUS condition if it is a conjunct of some S_i, and a cause if additionally the other conjuncts of that S_i were present on the occasion (e.g. in E = AB v CD, C is a cause when D is present). The same intuition recurs across disciplines under different names: legal scholars' NESS test ("Necessary Element of a Sufficient Set," Wright 1988), epidemiology's sufficient-component / first-completed-sufficient-cause criterion (Rothman 1976), and Hoover's reading of Simon-causation in econometrics. Pearl argues the account has a basic flaw: pure logical necessity/sufficiency cannot distinguish stable mechanisms (dispositional relations) from circumstantial conditions, so it breaks under contraposition ("disease causes symptom" wrongly yields "removing symptom causes removing disease"), transduction through common causes, and syntax-sensitivity (substituting A=C into D=A v B makes A vanish as a conjunct; permitting nonminimal forms like y = x v x'p also licenses absurd equivalents). The structural framework (causal beam) recovers and corrects the INUS intuition by representing dispositional information as structural equations y_i=f_i(pa_i,u) that disallow arbitrary truth-preserving substitutions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]