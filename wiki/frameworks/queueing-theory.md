---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- formal-methods
- systems-theory
id: pkis:framework:queueing-theory
knowledge_type: framework
maturity: settled
related_concepts:
- discrete-event-systems
- markov-chains
- generalized-semi-markov-process
- markov-decision-processes
sources:
- '[[cassandras-des-intro]]'
tags:
- queueing-theory
- little-law
- markovian-queues
- queueing-networks
- performance-analysis
- stochastic-processes
title: Queueing Theory
understanding: 0
uses:
- random-walk
---

Queueing theory is an analytical framework for modeling and analyzing service systems where entities (customers, jobs, packets) arrive, wait for service, and depart; it provides performance measures (throughput, mean queue length, mean waiting time) via the Markovian analysis of M/M/c queues, the fundamental Little's Law (L=λW), queueing network product-form results, and mean-value analysis for non-Markovian cases.

## Reading Path
- [[cassandras-des-intro-ch08]] (unread) — primary treatment: Kendall notation, Little's Law, M/M/* queues, open/closed networks, product-form, M/G/1 mean value analysis

## Connections
- [[random-walk]] — uses