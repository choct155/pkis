---
aliases: []
also_type: []
applies:
- probability-as-extended-logic
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
- information-theory
id: pkis:principle:principle-of-indifference
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- the-bernoulli-urn
- noninformative-prior
related_concepts: []
sources:
- jaynes-probability-ch02
- jaynes-probability-ch03
- jaynes-probability-ch12
specializes:
- noninformative-prior
tags:
- foundations
- prior-assignment
- symmetry
title: Principle of Indifference
understanding: 0
uses:
- sum-rule
---

## Definition
When background information B is indifferent among a set of n mutually exclusive and exhaustive propositions {A_1,...,A_n} — saying the same thing about each, giving no reason to prefer one over another — consistency forces equal plausibilities, p(A_i|B) = 1/n. Named by Keynes (1921), the principle of insufficient reason of Laplace/Bernoulli.

Jaynes derives it rather than postulating it, via a 'baby' group-invariance argument: relabeling (permuting) the propositions yields transformation equations relating the two problems, while the consistency desideratum (IIIc) — equivalent states of knowledge must receive equivalent assignments — yields symmetry equations; combining them forces all p(A_i|B) equal, and exhaustiveness fixes the common value at 1/n. This is the first instance of the group-invariance method for assigning noninformative priors (generalized in Jaynes Ch. 6). Two lessons: (i) it answers how stated information yields *definite numerical values* so a calculation can begin; (ii) the data fix the numerical value of p, not of the underlying plausibility x = A|B — different monotonic regradings p(x) all give the same 1/n, so x fades from the theory and p earns the technical name *probability*. Applied to a Bernoulli urn with M favorable cases out of N, it reproduces p(A|B) = M/N, the original Bernoulli/Laplace definition of probability.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[noninformative-prior]] — prerequisite-of: Indifference is the classical rationale underlying noninformative priors.
- [[the-bernoulli-urn]] — prerequisite-of: the urn rule cannot be stated without first fixing equal probabilities by indifference
- [[noninformative-prior]] — specializes: the uniform assignment 1/N is the discrete, symmetry-compelled instance of a noninformative prior
- [[probability-as-extended-logic]] — applies: first instance of symmetry/group-invariance prior assignment within the extended-logic program
- [[sum-rule]] — uses: exhaustiveness via the sum rule fixes the common value at 1/n
[To be populated during integration]