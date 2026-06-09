---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- st-petersburg-paradox
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:result:von-neumann-morgenstern-axioms
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- expected-utility-theory
related_concepts: []
sources:
- russell-norvig-aima-ch16
tags:
- decision-theory
- utility
- preferences
- representation-theorem
- rationality
title: Von Neumann–Morgenstern Axioms
understanding: 0
---

## Definition
## Definition
The **von Neumann–Morgenstern axioms** are six constraints on an agent's preferences over **lotteries** (probability distributions over outcomes) whose satisfaction guarantees the existence of a real-valued **utility function** $U$ such that the agent's preferences are exactly captured by expected utility. The axioms are: **orderability** (any two lotteries are comparable), **transitivity**, **continuity**, **substitutability**, **monotonicity** (preferring higher probability of a preferred outcome), and **decomposability** (compound lotteries reduce to simple ones). This is a *representation theorem*: from preferences alone it derives the existence and uniqueness-up-to-affine-transformation of $U$ (R&N Section 16.2).

### Status and scope
The construction was first carried out by Ramsey (1931); the modern axiom form is due to von Neumann and Morgenstern (1944), who derived utility from preferences, while Savage (1954) and Jeffrey (1983) derived subjective probability *and* utility jointly. The theorem says nothing about *what* an agent should prefer — an agent may rationally prefer a prime number of dollars — only that *if* preferences obey the axioms, they are representable by expected-utility maximization. Beardon et al. (2002) show a utility function cannot represent nontransitive or otherwise anomalous preferences.

### Descriptive failures
The axioms are normative; real human preferences violate them in predictable ways — the Allais paradox (certainty effect) and the Ellsberg paradox (ambiguity aversion) both produce choice pairs inconsistent with *any* $U$. These violations motivate descriptive theories of "predictable irrationality" and the evolutionary-psychology rebuttal that humans are rational in evolutionarily appropriate framings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[st-petersburg-paradox]] — contrasts-with: the St Petersburg paradox motivated the move from expected money to expected utility that the axioms formalize
- [[expected-utility-theory]] — prerequisite-of: the axioms establish the existence of the utility function EU theory assumes
- Provides the foundational justification for the maximum-expected-utility principle.
- Its descriptive failures are catalogued by the Allais and Ellsberg paradoxes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]