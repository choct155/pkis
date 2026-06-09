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
- bayesian-stats
id: pkis:concept:strong-and-weak-syllogisms
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch01
tags:
- syllogism
- polya
- deductive-reasoning
- plausible-reasoning
- implication
- jaynes
title: Strong and Weak Syllogisms
understanding: 0
---

## Definition
Jaynes (following Pólya and Aristotle) organizes inference around syllogisms sharing the major premise *if A then B*. The two *strong* (deductive) syllogisms yield certainty: $$A \Rightarrow B,\ A\ \text{true} \;\therefore\; B\ \text{true} \qquad A \Rightarrow B,\ B\ \text{false} \;\therefore\; A\ \text{false}.$$

The *weak* (plausible) syllogisms operate on the cases deduction cannot touch: verifying a consequence ($B$ true) makes $A$ *more plausible*; denying the antecedent ($A$ false) makes $B$ *less plausible*; and the weakest form, $$\text{if } A \text{ makes } B \text{ more plausible, and } B \text{ is true, then } A \text{ becomes more plausible,}$$ describes reasoning like the policeman who infers a masked man climbing from a broken jewelry-store window is dishonest. One-line intuition: strong syllogisms transmit certainty; weak syllogisms transmit a graded shift in belief.

### Why it matters
These five forms are the qualitative target that any quantitative theory of inference must reproduce. Jaynes' desiderata are engineered precisely so that the resulting rules recover the weak syllogisms — and contain the strong ones as limiting cases — which is the structural guarantee that probability theory *is* extended logic.

### Logical, not causal
The premise *if A then B* asserts a logical connection, not physical causation: from *rain implies clouds* we may infer rain is more plausible upon seeing clouds, even though clouds do not cause rain. Conflating the two directions is a recurring source of error.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]