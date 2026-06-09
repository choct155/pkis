---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:result:law-of-total-variance
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch01
tags:
- probability
- variance
- conditional-expectation
- decomposition
title: Law of Total Variance
understanding: 0
---

## Definition
$$E(u) = E\big(E(u\mid v)\big), \qquad \operatorname{var}(u) = E\big(\operatorname{var}(u\mid v)\big) + \operatorname{var}\big(E(u\mid v)\big).$$
The mean of $u$ is the average of its conditional mean (the tower / iterated-expectation law); its variance splits into the average within-group variance plus the variance of the group means.

### Derivation sketch
The mean identity follows by writing $E(u)=\iint u\,p(u\mid v)\,p(v)\,du\,dv=\int E(u\mid v)\,p(v)\,dv$. The variance identity follows from $\operatorname{var}(u)=E(u^2)-(E u)^2$ and adding/subtracting $E[(E(u\mid v))^2]$: $E(\operatorname{var}(u\mid v))$ supplies $E(u^2)-E[(E(u\mid v))^2]$, while $\operatorname{var}(E(u\mid v))$ supplies $E[(E(u\mid v))^2]-(Eu)^2$, and the cross terms cancel. Both identities hold when $u$ is a vector, with $E(u)$ a vector and $\operatorname{var}(u)$ a covariance matrix.

### Interpretation
The 'explained' component $\operatorname{var}(E(u\mid v))$ is the variance attributable to differences in $v$; the 'unexplained' component $E(\operatorname{var}(u\mid v))$ is the residual variance left within fixed $v$. This is the probabilistic ancestor of the ANOVA between/within decomposition and of shrinkage formulas in hierarchical models.

### Why it matters
The decomposition is the algebraic backbone of hierarchical and mixture modeling: it quantifies how much uncertainty hides in a latent grouping variable, justifies modeling complexity through conditioning rather than complicated marginals, and underlies variance-reduction arguments such as Rao–Blackwellization and partial pooling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]