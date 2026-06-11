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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- causal-inference
- statistics
id: pkis:concept:backdoor-criterion-causal
instantiates:
- back-door-criterion
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- causal-DAG
- adjustment
- d-separation
- do-calculus
- identification
title: Backdoor Criterion
understanding: 0
uses:
- d-separation
- adjustment-formula-standardization
- structural-causal-model
---

## Definition
A set of observed variables $S$ satisfies the **backdoor criterion** relative to an ordered pair $(A, Y)$ in a causal DAG $G$ if:
1. No node in $S$ is a descendant of $A$.
2. $S$ blocks every *backdoor path* between $A$ and $Y$ (i.e., every path that contains an arrow *into* $A$).

Whenever $S$ satisfies the backdoor criterion and overlap holds ($0 < P(A=1|S) < 1$), the interventional distribution is identified by the **backdoor adjustment formula**:
$$P(Y=y|\mathrm{do}(A=a)) = \mathbb{E}_S[P(Y=y|A=a, S)].$$
Correspondingly, $\text{ATE} = \mathbb{E}_S[\mathbb{E}[Y|A=1,S]-\mathbb{E}[Y|A=0,S]]$.

### Why it matters
The backdoor criterion gives a graphical, non-parametric sufficient condition for causal identification. It subsumes both the adjust-for-parents rule and the adjust-for-all-common-causes rule, and is strictly more general. It is the primary tool for translating a known causal DAG into a statistical identification formula. Crucially, the criterion rules out conditioning on descendants of $A$ (mediators, colliders), which can introduce or amplify bias.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[structural-causal-model]] — uses
- [[adjustment-formula-standardization]] — uses: Backdoor adjustment formula is the identification result from the backdoor criterion
- [[d-separation]] — uses
- [[back-door-criterion]] — instantiates: Formal non-parametric statement of the backdoor criterion used in do-calculus
[To be populated during integration]