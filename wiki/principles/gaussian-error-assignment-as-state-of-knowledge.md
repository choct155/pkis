---
aliases: []
also_type: []
applies:
- maximum-entropy-image-reconstruction
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
id: pkis:principle:gaussian-error-assignment-as-state-of-knowledge
instantiates:
- learning-as-inference
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch19
tags:
- jaynes
- maximum-entropy
- measurement-error
- epistemology-of-probability
title: Gaussian Error Assignment as State of Knowledge
understanding: 0
uses:
- gaussian-distribution
- entropy
---

## Definition
In probability theory as logic, assigning a Gaussian probability distribution to measurement errors is a description of one's *state of knowledge* about the errors, not an assumption about their *frequency distribution*. When prior information about errors amounts only to their general magnitude (interpreted as the first two moments), the principle of maximum entropy yields an independent Gaussian as the assignment that agrees with that information while assuming nothing further. The orthodox justification via the central limit theorem (errors as sums of many small independent imperfections) is valid but psychologically misleading: it leads workers to believe that a non-Gaussian *frequency* distribution makes the Gaussian assignment 'wrong' and ruinous. Jaynes argues the opposite. The 'covenant with Nature' is favorable: given second moments, a non-Gaussian frequency distribution will *not* make inferences worse, because the Gaussian assignment already makes the reasonably-probable noise region as large as possible consistent with the variance constraint. The privileged status of the Gaussian rests on a subtler fact: acquiring new information that the errors are *in fact* Gaussian (with the assumed variance) changes nothing, because it is only what one would already have predicted. Conversely, *additional* prior knowledge of a specific departure from Gaussianity is cogent: it constrains the noise to a smaller domain, so data vectors previously dismissed as noise are recognized as signal, enabling strictly better estimates. Bayes' theorem incorporates all of this automatically. The principle thus dissolves the long-standing worry that 'assuming Gaussian errors' is a dangerous idealization.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[learning-as-inference]] — instantiates: Gaussian-as-knowledge is the logical (vs frequentist) reading of probability applied to errors
- [[entropy]] — uses: principle of maximum entropy underwrites the Gaussian as the least-committal assignment
- [[maximum-entropy-image-reconstruction]] — applies: maxent given two moments yields the Gaussian; same justificatory machinery
- [[gaussian-distribution]] — uses: the assignment in question is a Gaussian
[To be populated during integration]