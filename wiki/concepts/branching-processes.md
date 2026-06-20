---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- bayesian-stats
id: pkis:concept:branching-processes
knowledge_type: concept
maturity: settled
related_concepts:
- '[[markov-chains]]'
- '[[probability-theory]]'
- '[[generating-functions]]'
sources:
- '[[lange-applied-probability]]'
- lange-applied-probability-ch09
tags:
- stochastic-processes
- probability-theory
- epidemiology
- population-genetics
- generating-functions
title: Branching Processes
understanding: 0
uses:
- random-sum-compound-distribution
- probability-generating-function
---

A stochastic process modeling population growth where each individual independently produces a random number of offspring; extinction probability is the smallest fixed point of the offspring generating function, and survival requires the basic reproduction number R₀ > 1.

## Reading Path
- [[lange-applied-probability-ch09]] (unread) — elementary theory, extinction, immigration, multitype processes, HIV reproduction, basic reproduction numbers

## Connections
- [[probability-generating-function]] — uses: Extinction probability is the smallest fixed point of the offspring PGF; generation distributions are gf iterates.
- [[random-sum-compound-distribution]] — uses: Each generation is a random sum over the previous generation, so generation gfs compose.