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
id: pkis:concept:stable-no-confounding
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch06
specializes:
- confounding
tags:
- causality
- confounding
- back-door-criterion
- faithfulness
- stability
- incidental-cancellation
- associational-criterion
title: Stable vs. Incidental Unbiasedness
understanding: 0
uses:
- d-separation
- structural-causal-models
---

## Definition
An effect estimate P(y|x) is *unbiased* (no-confounding, Definition 6.2.1) when P(y|do(x)) = P(y|x). Pearl distinguishes two grades. *Incidental* unbiasedness holds only for a peculiar parameter combination—e.g. in the linear model x=αz+ε1, y=βx+γz+ε2 with cov(ε1,ε2)=r, the regression of Y on X recovers β exactly when r = −αγ, a coincidental cancellation that would not survive a slight change of parameters (Example 6.3.3). *Stable* unbiasedness (Definition 6.4.1) holds across an entire class C_A of models satisfying assumptions A; *structurally stable* no-confounding (Definition 6.4.2) holds for every parameterization of a given causal diagram D.

This distinction is the missing link between statistical association and confounding. The back-door criterion is a graphical, statistics-free test for stable no-confounding; for an acyclic diagram it is necessary and sufficient, and in the no-adjustment case reduces to: X and Y are stably unconfounded iff they share no common ancestor (Theorem 6.4.3). Remarkably, even without the full diagram, knowing only that some Z is unaffected by X yet may affect Y (assumption A_Z) gives a *necessary* statistical test (Theorem 6.4.4): if Z violates both (U1) and (U2), the pair is not stably unconfounded—without enumerating all confounders or assuming a closed world. The notion connects to DAG-isomorphism, stability (Pearl & Verma 1991), and faithfulness (Spirtes et al. 1993), all resting on the conception of a causal model as autonomous mechanisms that may vary independently.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[structural-causal-models]] — uses: stability rests on the conception of a causal model as autonomous mechanisms varying independently
- [[d-separation]] — uses: the back-door criterion (a d-separation test) is necessary and sufficient for stable no-confounding in acyclic diagrams
- [[confounding]] — specializes: stable unbiasedness is a stronger, parameter-robust form of no-confounding
[To be populated during integration]