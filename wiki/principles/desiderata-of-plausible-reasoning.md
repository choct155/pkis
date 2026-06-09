---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:principle:desiderata-of-plausible-reasoning
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch01
tags:
- desiderata
- cox
- consistency
- robot
- foundations
- jaynes
- extended-logic
title: Desiderata of Plausible Reasoning
understanding: 0
---

## Definition
Jaynes derives the rules of his inferential 'robot' not from axioms but from *desiderata* — stated goals a rational agent would want, such that on finding it violated one, it would wish to revise its reasoning. There are three:

- **(I) Representation:** degrees of plausibility are represented by real numbers, with greater plausibility a greater number and a continuity property.
- **(II) Qualitative correspondence with common sense:** the rules must move belief in the direction the weak syllogisms prescribe (e.g., if $(A\mid C')>(A\mid C)$ then $(\bar A\mid C')<(\bar A\mid C)$).
- **(III) Consistency**, in three senses: (IIIa) every valid path to a conclusion gives the same result; (IIIb) all relevant evidence is used (nonideological); (IIIc) equivalent states of knowledge get equivalent plausibility assignments.

One-line intuition: state what rationality should *want*, and the math is forced.

### Why it matters
The central surprise — the Cox–Jaynes theorem of Chapter 2 — is that these mild, almost inescapable desiderata *uniquely* determine the rules: there is exactly one calculus (the product and sum rules of probability) satisfying them. Any ad hoc procedure conflicting with it must generate demonstrable inconsistencies beyond its tuned domain. This is the foundational argument for Bayesian probability as the unique logic of science.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]