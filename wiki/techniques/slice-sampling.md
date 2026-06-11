---
aliases: []
also_type: []
analogous-to:
- rejection-sampling
- gibbs-sampling
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- metropolis-algorithm
- metropolis-hastings-algorithm
- gibbs-sampling
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:slice-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch29
specializes:
- mcmc
- metropolis-hastings
tags:
- monte-carlo
- mcmc
- sampling
- self-tuning
- auxiliary-variable
- mackay
title: Slice Sampling
understanding: 0
uses:
- detailed-balance
- mcmc-mixing-time
---

## Definition
Slice sampling (Neal, 1997, 2003) is an MCMC method that draws samples from $P(x)\propto P^*(x)$ by sampling uniformly from the two-dimensional region under the curve $P^*(x)$ via an auxiliary height variable $u$. A single transition $(x,u)\to(x',u')$ proceeds: (1) draw $u'\sim\text{Uniform}(0,P^*(x))$; (2) form a horizontal interval $(x_l,x_r)$ around $x$ — the 'slice'; (3) repeatedly draw $x'\sim\text{Uniform}(x_l,x_r)$, accepting when $P^*(x')>u'$, otherwise shrinking the interval toward $x'$.

It blends ideas from rejection sampling (uniform fill under the curve, but no upper-bounding $c$ needed), Gibbs sampling (one-dimensional moves), and Metropolis (applicable wherever $P^*$ can be evaluated).

### Self-tuning step size
Slice sampling's signal advantage is robustness to its width parameter $w$. If $w$ is too small by a factor $f$, the stepping-out procedure expands the interval at cost only **linear** in $f$ (versus $f^2$ for random-walk Metropolis). If $w$ is too large by a factor $F$, shrinking costs only $\log F$, whereas Metropolis rejects almost everything (cost exponential in $F$). There are essentially no rejections.

### Why it matters
Slice sampling removes the painful manual tuning of Metropolis step sizes. It still explores by a random walk (so does not escape the $(L/\epsilon)^2$ mixing penalty), but it automatically picks a sensible step scale, making it an attractive default for getting a model running. Skilling's integer variant uses bit operations to guarantee exact detailed balance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc-mixing-time]] — uses
- [[gibbs-sampling]] — contrasts-with
- [[metropolis-hastings-algorithm]] — contrasts-with: slice sampling needs only unnormalized joint, not full conditionals
- [[gibbs-sampling]] — analogous-to
- [[metropolis-hastings]] — specializes
- [[rejection-sampling]] — analogous-to: Both draw samples uniformly from the area under P*(x), but slice sampling needs no upper-bounding constant c.
- [[metropolis-algorithm]] — contrasts-with: Slice sampling self-tunes its step size; Metropolis requires manual step-size tuning.
- [[detailed-balance]] — uses: Slice sampling's interval construction must satisfy detailed balance to keep the under-curve uniform distribution invariant.
- [[mcmc]] — specializes: Slice sampling is an MCMC method blending rejection, Gibbs, and Metropolis ideas.
[To be populated during integration]