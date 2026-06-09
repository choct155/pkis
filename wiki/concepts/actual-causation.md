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
id: pkis:concept:actual-causation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch10
tags:
- causality
- explanation
- legal-responsibility
- token-vs-type
title: Actual Causation
understanding: 0
---

## Definition
Actual causation is the singular, token-level relation that designates a specific event as responsible for producing a given outcome in a particular scenario ("Socrates' drinking hemlock was the actual cause of his death"), as opposed to type-level or generic causal claims ("car accidents cause deaths"). It is the criterion legal scholars call "cause in fact" and the target of causal explanation. Pearl argues that necessity and sufficiency alone (PN, PS) are insufficient to characterize it, because they are global input-output features of the response function Y_x(u) and ignore the structure of the process mediating cause and effect; the asymmetry that makes us name fire A (which burned first) rather than fire B the actual cause, or switch 1 rather than switch 2, lives in that structure. In the structural account, type and token claims are instances of the same species differing only in how much scenario-specific evidence e is brought to bear on P(u|e); gathering more episode-specific evidence moves a claim along a spectrum from type-level toward the token-level ideal of an actual cause. Pearl's formal explication (Definition 10.3.3) defines X=x as an actual cause of Y=y in state u via the existence of a natural causal beam in which Y counterfactually depends on X; the later Halpern-Pearl (2005) definition (Def 10.4.2: AC1-AC3) replaces the beam with a partition of variables into Z and W and a counterfactual test under a contingency W=w constrained by AC2(b).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]