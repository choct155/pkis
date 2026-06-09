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
id: pkis:concept:jeffreys-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch02
specializes:
- noninformative-prior
tags:
- prior
- objective-bayes
- fisher-information
- invariance
title: Jeffreys' Prior
understanding: 0
uses:
- beta-distribution
---

## Definition
**Jeffreys' prior** is the noninformative prior defined to be invariant under reparameterization, given by the square root of the Fisher information:

$$p(\theta) \propto [J(\theta)]^{1/2}, \qquad J(\theta) = -\,E\!\left(\frac{d^2 \log p(y\mid\theta)}{d\theta^2}\,\Big|\,\theta\right).$$

The defining property is Jeffreys' *invariance principle*: any rule for choosing a prior should give the same beliefs whether applied to $\theta$ or to a one-to-one transform $\phi=h(\theta)$. Because the Fisher information transforms as $J(\phi)=J(\theta)\,|d\theta/d\phi|^2$, one has $J(\phi)^{1/2}=J(\theta)^{1/2}\,|d\theta/d\phi|$, which is exactly the Jacobian factor needed for the change-of-variables of a density — so the rule is invariant by construction.

For the binomial parameter, $J(\omega)=n/[\omega(1-\omega)]$, giving

$$p(\omega) \propto \omega^{-1/2}(1-\omega)^{-1/2} = \mathrm{Beta}(\tfrac12,\tfrac12),$$

intermediate between the Bayes–Laplace uniform $\mathrm{Beta}(1,1)$ and the improper $\mathrm{Beta}(0,0)$ (flat in the logit/natural parameter).

## Intuition
The slogan is "be flat in the parameterization the data actually care about." Fisher information measures how sharply the likelihood distinguishes nearby parameter values; weighting the prior by $\sqrt{J(\theta)}$ puts *more* prior mass where the data are most informative, in just the right way that the recipe survives any relabeling of the parameter. This cures the central defect of a naive uniform prior — that flatness is parameterization-dependent.

### Why it matters
Jeffreys' prior is the most principled single-parameter answer to the "what is truly noninformative?" question, and it is the reference point against which other objective priors are judged. Its limits are equally instructive: extended to multiparameter models it becomes controversial and can disagree with component-wise uniform priors, which is one reason Gelman recommends abandoning pure noninformativity for hierarchical or weakly informative models in high dimensions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[beta-distribution]] — uses: For the binomial parameter, Jeffreys' prior is the Beta(1/2, 1/2) density.
- [[noninformative-prior]] — specializes: Jeffreys' prior is the parameterization-invariant construction of a noninformative prior.
[To be populated during integration]