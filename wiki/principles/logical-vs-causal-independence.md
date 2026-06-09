---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
contrasts-with:
- conditional-independence
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- information-theory
id: pkis:principle:logical-vs-causal-independence
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch08
specializes:
- probability-theory
tags:
- independence
- redundant-information
- boolean-algebra
- meta-analysis
- evidence-combination
- data-reuse
title: Logical vs Causal Independence (AA = A)
understanding: 0
---

## Definition
Probability theory as logic counts information, not events; redundant information is never used twice. This is the Boolean identity AA = A: a piece of information changes a conclusion only when it tells us something not already implied by what we know. A datum matters only when it says something the prior does not; prior information matters only when it says something the data do not; anything conveyed by both is redundant and removable from either without effect. The crucial distinction is between CAUSAL independence (the physical mechanisms are unlinked) and LOGICAL independence (given the hypothesis, knowing one datum tells us nothing about another). Valid evidence combination requires logical, not merely causal, independence.

## Consequences across the chapter
- Combining experiments: Bayes' chain consistency p(H|ABI) = p(H|I) p(AB|HI)/p(AB|I) lets evidence be pooled only if the prior is shared and each experiment's prior includes earlier results; naive averaging is valid only when data sets are logically independent given H. The Emperor-of-China fable shows that causally independent but logically dependent opinions defeat the sqrt(N) rule, leaving a systematic error S that survives averaging (error = S +/- R/sqrt(N)).
- Meta-analysis is the full Bayesian procedure in disguise; applied without these qualifications it can be 'utterly misleading'.
- Data re-use fraud: treating the same data D as a second logically-independent set D* squares the likelihood, fabricating accuracy; this underlies 'data-dependent priors' and randomization tests' n! permutations.
- Sam's broken thermometer: fine-grained enumeration of sub-hypotheses is needed only when the breakdown carries information relevant to the question; otherwise only the disjunction's prior probability matters (no need to assign priors to atomic propositions, dissolving Savage's objection).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conditional-independence]] — contrasts-with: Distinguishes logical independence (inferential) from causal/physical independence, sharpening when conditional independence licenses evidence combination.
- [[probability-theory]] — specializes: AA = A non-use of redundant information is a direct consequence of treating probability as extended logic.
[To be populated during integration]