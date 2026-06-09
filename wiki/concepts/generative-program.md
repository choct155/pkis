---
aliases: []
also_type: []
analogous-to:
- open-universe-probability-model
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
- knowledge-representation
id: pkis:concept:generative-program
instantiates:
- probabilistic-programming-language
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch15
tags:
- execution-trace
- probabilistic-programming
- random-choice
- open-universe
- sample-space
title: Generative Program
understanding: 0
uses:
- importance-sampling
---

## Definition
An executable program in which every random choice defines a random variable of an associated probability model. Unrolling an execution, the i-th random choice is variable X_i; an execution trace omega = {x_i} is one run, and the space of all traces Omega is the model's sample space with P(omega) = prod_i P(x_i | x_1..x_{i-1}). Because the number of random choices a program makes can depend on earlier choices (e.g. a sampled count n), a generative program generally defines an open-universe model with an a priori unbounded number of variables. Any OUPM can be mechanically converted into an equivalent generative program (the extra work is building data structures for objects, functions, and relations). Illustrated by the degraded-text/CAPTCHA reading example, where GENERATE-IMAGE samples a letter sequence then renders it with noise; inference inverts the program via rejection sampling, likelihood weighting, or MCMC over execution traces (carefully handling trace edits that invalidate downstream choices).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[importance-sampling]] — uses: likelihood weighting reweights traces; learned proposals enable importance sampling
- [[open-universe-probability-model]] — analogous-to: trace distribution P(omega)=prod P(x_i|x_<i) mirrors OUPM world distribution; any OUPM converts to a generative program
- [[probabilistic-programming-language]] — instantiates: the programming-language route to a PPL: programs define distributions over execution traces
[To be populated during integration]