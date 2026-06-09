---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
contrasts-with:
- expected-utility-theory
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:problem:st-petersburg-paradox
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch13
tags:
- decision-theory
- expected-value
- utility
- bernoulli
- gambling
- moral-expectation
title: St Petersburg Paradox
understanding: 0
---

## Definition
A gambling problem exposing the failure of the maximize-expected-profit criterion. An honest coin is tossed until it first comes up heads; if heads first occurs on the $n$th throw, the player receives $2^n$ dollars. If a 'fair' entrance fee equals the expected profit, the fee is infinite: $\sum_{k=1}^\infty (2^{-k})(2^k)=\sum_{k=1}^\infty 1=\infty$. Yet no sane person would risk more than a small amount. Daniel Bernoulli (1738) resolved the paradox by replacing money with its **moral value** (utility), proposing utility $\propto\log(M)$; the fair fee $f(m)$ for a player of fortune $m$ then solves $\log(m)=\sum_{n=1}^\infty 2^{-n}\log(m-f+2^n)$, giving small finite fees (Laplace: $\approx 8.72$ francs for $m=200$; only $\approx 21$ francs even for a millionaire). Jaynes contrasts this with Feller's frequentist 'resolution', which he argues merely analyzes a *different* game; and uses Savage's example (a coin flip turning \$1M into \$1000 or \$1B) to show utility must grow even slower than $\log$ for very large fortunes and is plausibly bounded.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[expected-utility-theory]] — contrasts-with: The paradox exposes the failure of maximizing expected profit, motivating utility.
[To be populated during integration]