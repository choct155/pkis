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
contrasts-with:
- de-finetti-coherence
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:framework:kolmogorov-axioms
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-appA
specializes:
- probability-theory
tags:
- mathematical-foundations
- measure-theory
- probability-foundations
title: Kolmogorov System of Probability (Measure-Theoretic Axioms)
understanding: 0
---

## Definition
The standard measure-theoretic foundation of probability (Kolmogorov 1933), defining probability as a game played on a sample space $\Omega$ of elementary outcomes $\omega_i$. A field (sigma-field) $F$ of subsets $f_j$ of $\Omega$ is required to (I) contain $\Omega$; (II) be closed under complementation ($f_j \in F \Rightarrow \Omega - f_j \in F$); (III) be closed under countable unions. A probability measure $P$ on $F$ must satisfy four axioms: (1) normalization, $P(\Omega)=1$; (2) non-negativity, $P(f_i)\ge 0$; (3) (countable) additivity, $P(\cup_j f_j)=\sum_j P(f_j)$ for disjoint $f_j$; (4) continuity at zero, $f_1\supseteq f_2\supseteq\cdots\to\varnothing \Rightarrow P(f_j)\to 0$.

Jaynes (Appendix A) treats KSP as the dominant alternative to his probability-as-extended-logic development. His key claims: (a) the four measure axioms are not arbitrary stipulations but coincide exactly with the four properties derivable in his Chapter 2 from consistency requirements (non-negativity, additivity, normalization, and a continuity property closely tied to additivity); (b) any change of scale $u=f(p)$ by a monotonic $f$ merely re-expresses the same content with modified sum/product rules, so a normalized, non-negative, additive scale is the unique consistent convention rather than an arbitrary one; (c) the principal differences are conceptual, not formal: KSP concentrates on additive measure and treats conditional probability and Bayes' theorem as reluctant afterthoughts, whereas the extended-logic view makes the product rule (hence conditioning and Bayes) primary; and (d) KSP resolves every proposition into a disjunction of elementary outcomes in $\Omega$, which need not always be possible for real-world propositions, making the set-theoretic formulation less general in applications even though it is identical 'as far as it goes'.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[probability-theory]] — specializes: The Kolmogorov system is the measure-theoretic instantiation of probability theory.
- [[de-finetti-coherence]] — contrasts-with: Both work on uncountable sets but treat additivity differently; de Finetti's onion-layer zero probabilities depart from Kolmogorov's countable additivity.
[To be populated during integration]