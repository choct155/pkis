---
aliases: []
also_type: []
applies:
- noninformative-prior
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- information-theory
generalizes:
- jeffreys-prior
id: pkis:technique:transformation-group-priors
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- entropy
related_concepts: []
sources:
- jaynes-probability-ch12
specializes:
- principle-of-indifference
tags:
- prior
- objective-bayes
- invariance
- group-theory
- ignorance-prior
- jaynes
title: Transformation-Group Priors
understanding: 0
uses:
- group-theory
---

## Definition
## Definition
The **transformation-group method** (Jaynes) derives an ignorance prior by demanding that the prior be *unchanged* under a group of transformations that the statement of the problem cannot distinguish. The recipe has two universal steps: (i) a **transformation equation** relating how a fixed distribution re-expresses itself after a change of variables (holds regardless of symmetry); (ii) a **symmetry equation** asserting that the two re-expressed problems are *the same problem* (same state of knowledge), so consistency forces the prior to be the same function. Combining them yields a functional equation whose solution is the prior.

## The construction
For a location parameter $\nu$ and scale parameter $\sigma$, ignorance is defined as invariance under the group $(a,b)$: $\nu'=\nu+b,\ \sigma'=a\sigma,\ x'-\nu'=a(x-\nu)$. The Jacobian gives the transformation equation $g(\nu',\sigma')=a^{-1}f(\nu,\sigma)$; consistency demands $f=g$; combining yields

$$f(\nu,\sigma)=a\,f(\nu+b,\,a\sigma)\ \Rightarrow\ f(\nu,\sigma)\propto \frac{1}{\sigma},$$

the Jeffreys rule. The result is determined by the *transformation group*, not by the form of the sampling distribution: a different group (e.g. scale-then-translate, $\nu'=a\nu+b$) is also consistent with a location/scale family yet yields $1/\sigma^2$, so 'complete ignorance' is only well-defined relative to a specified group.

## Intuition
"If a change of scale (or shift of location) can make the problem appear in any way different to us, then we were not completely ignorant." Ignorance is thus encoded as a symmetry; the prior is whatever measure that symmetry leaves invariant. This is the statistical analogue of the invariant (Haar) measure on a group and of the invariant line element in Riemannian geometry, which restore 'rigidity' to an otherwise mollusk-like parameter space.

## Worked results
- **Poisson rate** $\lambda$ (unknown time scale): $f(\lambda)\propto \lambda^{-1}$.
- **Bernoulli probability** $\theta$, invariant under the Bayes-rule remapping $\theta'=a\theta/(1-\theta+a\theta)$ induced by new evidence: $f(\theta)\propto [\theta(1-\theta)]^{-1}$ (Haldane prior), reproducing the qualitative weight at the endpoints anticipated by Jeffreys.
- **Bertrand straws**: combined rotational + scale + translational invariance uniquely select $f(r,\theta)=1/(2\pi R r)$ and the chord-length law $p(x)=x/\sqrt{1-x^2}$.

### Why it matters
It supplies the *invariant measure* $m(x)$ that the maximum-entropy principle needs for continuous distributions (without which continuous MaxEnt is mathematically indeterminate), and recasts the discredited principle of indifference as legitimate indifference *between problems* rather than between events. The priors it produces are typically improper (non-normalizable), interpreted as idealized 'pre-priors' that fix the measure rather than describe a realistic state of knowledge.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[entropy]] — prerequisite-of: Supplies the invariant measure m(x) required for continuous maximum entropy.
- [[group-theory]] — uses: Encodes problem symmetries as a transformation group; priors are invariant measures.
- [[noninformative-prior]] — applies: Constructs noninformative (pre-)priors as invariant measures.
- [[jeffreys-prior]] — generalizes: The 1/sigma Jeffreys scale prior is one instance of a transformation-group ignorance prior.
- [[principle-of-indifference]] — specializes: Operationalizes indifference between problems via invariance groups.
[To be populated during integration]