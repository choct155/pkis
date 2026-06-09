---
aliases: []
also_type: []
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
- causal-analysis
extends:
- inus-condition
id: pkis:technique:causal-beam
instantiates:
- sustenance-causal
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch10
tags:
- causality
- structural-causal-models
- process
- projection
- do-operator
title: Causal Beam
understanding: 0
uses:
- structural-causal-models
- do-calculus
---

## Definition
A causal beam is a structural-semantic explication of the intuitive notion of a causal "process," constructed from a causal model M and a state U=u by projecting each mechanism f_i onto the actual scenario. For each variable V_i, its parents PA_i are partitioned into a sustaining set S (any subset sufficient to entail the actual value V_i(u) regardless of how the rest are set) and the complement S-bar; one then finds a setting W=w of (a subset of) S-bar that renders f_i nontrivial in S, and replaces f_i by its projection f_i^u(s)=f_i(s, S-bar_w(u), u), so V_i's new parent set is just S (Definition 10.3.1). A beam is natural (Definition 10.3.2) when condition 2 holds with W=empty for every variable, i.e. all non-sustaining variables are frozen at their actual values. X=x is then an ACTUAL CAUSE of Y=y if there exists a natural beam in which Y_x=y but Y_{x'}!=y for some x'!=x (Def 10.3.3); x is a CONTRIBUTORY CAUSE if such a beam exists but no natural one does (Def 10.3.4) -- the contingency W!=empty must depart from the actual state, as in symmetric overdetermination E=A1 v A2 where each disjunct is contributory. The beam thus formalizes Lewis's "quasi-dependence": Y is quasi-dependent on A1 when tested in the submodel created by do(A2=false). For uncertain states, P(caused(x,y|e)) = P(U_xy intersect U_e)/P(U_e) sums P(u|e) over states where the actual-cause assertion holds (Def 10.3.5). The beam definition was later found to need refinement (the voting-machine counterexample with a tabulating variable M), motivating the Halpern-Pearl (2005) AC1-AC3 definition.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inus-condition]] — extends: the beam recovers and corrects the INUS intuition in single-mechanism models
- [[do-calculus]] — uses: freezing non-sustaining variables and testing contingencies relies on the do(.) operator
- [[sustenance-causal]] — instantiates: the beam test (Def 10.3.3) is the operational embodiment of sustenance
- [[structural-causal-models]] — uses: a beam is a projection of an SCM's mechanisms onto a state u
[To be populated during integration]