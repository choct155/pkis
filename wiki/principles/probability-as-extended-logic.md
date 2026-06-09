---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
contrasts-with:
- kolmogorov-axioms
- de-finetti-coherence
- comparative-probability
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- information-theory
- knowledge-representation
extends:
- probability-theory
id: pkis:principle:probability-as-extended-logic
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch02
- jaynes-probability-appA
tags:
- foundations
- bayesian-philosophy
- objective-bayes
title: Probability as Extended Logic
understanding: 0
uses:
- cox-theorem
---

## Definition
The principle (Cox-Polya-Jeffreys lineage, articulated by Jaynes) that probability theory is the unique consistent extension of deductive logic to situations of incomplete information. A probability p(A|B) is a real number encoding a *state of knowledge* about proposition A given evidence B, not a physical property or long-run frequency. Aristotelian deductive logic is recovered as the limiting case as plausibilities approach certainty (p -> 0 or p -> 1): the strong syllogisms become the boundary values of the product rule.

Key commitments: (1) plausibilities attach to *propositions*, manipulated by the product and sum rules derived via Cox's theorem; (2) assignments are 'subjective' in describing a state of knowledge yet 'objective' in being determined by the stated information alone, independent of the user's personality — the consistency desiderata (IIIb, IIIc) make this so; (3) probability distributions are carriers of incomplete information, which (per Jaynes) gives the framework analytical reach beyond the Kolmogorov set-theoretic formulation, enabling treatment of ill-posed and generalized-inverse problems. The view contrasts with both the frequentist interpretation and the purely measure-theoretic (Kolmogorov) axiomatization, which Jaynes argues is *derived* rather than primitive. It also reframes Godel undecidability as a signal that a question requires inference rather than deduction — precisely the regime probability-as-logic is built for.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[comparative-probability]] — contrasts-with: Extended logic insists on real-number plausibilities; comparative probability tries to do without them.
- [[de-finetti-coherence]] — contrasts-with: Extended logic uses the stronger Cox consistency rather than de Finetti coherence as its basis.
- [[kolmogorov-axioms]] — contrasts-with: Jaynes contrasts proposition-based extended logic with Kolmogorov's set-based measure axioms; identical 'as far as it goes' but more general and Bayes-primary.
- [[probability-theory]] — extends: recasts probability theory as the unique consistent extension of deductive logic
- [[cox-theorem]] — uses: Cox's theorem is the formal justification of the extended-logic stance
[To be populated during integration]