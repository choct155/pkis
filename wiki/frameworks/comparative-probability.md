---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:framework:comparative-probability
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-appA
tags:
- probability-foundations
- qualitative-reasoning
- ordering-relations
title: Comparative (Qualitative) Probability Theory
understanding: 0
---

## Definition
An approach that seeks to found probability on purely qualitative ordering relations $(A|C) \ge (B|C)$ ('given C, A is at least as plausible as B') rather than on real-valued degrees of plausibility, hoping to deduce the existence of a (not necessarily unique) additive measure from weaker axioms (Savage 1954; survey in Fine 1973). Jaynes (Appendix A) dissects his first desideratum (plausibilities are real numbers) into two more elementary axioms: (Ia) **transitivity** of the ordering, and (Ib) **universal comparability** (for any A, B, C exactly one of $>$, $=$, $<$ holds).

His analysis: any comparative theory holding *both* axioms can be faithfully represented by real (indeed rational) numbers within any finite set of propositions, after which Cox's theorems force it to be identical to standard numerical probability theory. Transitivity cannot be dropped (its violation gives circular reasoning and immediate grounds for rejection). Dropping universal comparability yields a looser *lattice* theory in which some propositions are incomparable, representable only by a lattice of vectors, not a single real number. But Jaynes argues such efforts are futile: ordering relations cannot be assigned arbitrarily because the field of discourse must be extendable without contradiction, and as the relations become 'everywhere dense' from impossibility to certainty, consistency forces convergence to the ordinary numerical theory; moreover any computer must ultimately represent orderings as numerical inequalities. The genuine residual value of the idea is twofold: (i) for choosing between two hypotheses or actions, a comparative ordering is a useful *approximation* to numerical probability when precise values are unnecessary; and (ii) a lattice theory may better describe how real, incompletely-educated human brains actually reason — with locally dense, mutually-isolated 'domains' of comparable propositions that collapse to a single line (the Laplace–Bayes ideal) only in the limit of an 'infinitely educated' brain.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]