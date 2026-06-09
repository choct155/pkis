---
aliases: []
also_type: []
analogous-to:
- ignorability
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- confounding
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- econometrics
- causal-analysis
id: pkis:concept:exogeneity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- instrumental-variables
- attribution-and-but-for-causation
related_concepts: []
sources:
- pearl-causality-ch05
- pearl-causality-ch09
tags:
- identification
- do-operator
- no-confounding
- instrumental-variables
- engle-hendry-richard
title: Exogeneity
understanding: 0
uses:
- back-door-criterion
- counterfactuals
---

## Definition
Pearl's structural reformulation of econometric exogeneity (Definitions 5.4.4-5.4.6). X is exogenous relative to (Y, lambda, T) if a target parameter lambda is identifiable from the CONDITIONAL distribution P(y|x) alone — ignoring the marginal P(x): formally P_{M1}(y|x)=P_{M2}(y|x) => lambda(M1)=lambda(M2) for all models M1,M2 consistent with theory T. When lambda fully specifies the interventional distribution this collapses to P(y|do(x)) = P(y|x), i.e., 'no confounding,' testable graphically by the back-door criterion with Z = empty (no unblocked back-door path X to Y). The general definition (5.4.5) subsumes Engle-Hendry-Richard's weak (statistical lambda), super- (causal-effect lambda), and a generalized instrumental-variable notion (lambda = causal effect among other variables) as special cases. The error-based definition (5.4.6: X independent of all errors influencing Y except those mediated by X) is rehabilitated as coinciding formally with no-confounding once structural errors are properly distinguished from regression errors. Pearl criticizes Engle et al.'s 'invariant to any change in P(x)' as too strong, and 'parameter enters the density' definitions as syntax-dependent.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ignorability]] — analogous-to: strong exogeneity coincides with Rosenbaum-Rubin strong ignorability
- [[confounding]] — contrasts-with: exogeneity is precisely the no-confounding condition; failure of exogeneity is confounding
- [[counterfactuals]] — uses: exogeneity defined via independence of joint potential response {Y_x, Y_{x'}} from X
- [[attribution-and-but-for-causation]] — prerequisite-of: excess-risk-ratio equals PN only under exogeneity (plus monotonicity)
- [[instrumental-variables]] — prerequisite-of: Generalized exogeneity (lambda a causal effect among non-instrument variables) yields the IV identification role.
- [[back-door-criterion]] — uses: Graphical test of exogeneity: no unblocked back-door path (Z=empty in Thm 5.3.2).
[To be populated during integration]