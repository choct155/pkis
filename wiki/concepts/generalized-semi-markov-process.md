---
id: "pkis:concept:generalized-semi-markov-process"
aliases: []
title: "Generalized Semi-Markov Process"
knowledge_type: concept
also_type: []
domain: [formal-methods, systems-theory]
tags: [stochastic-processes, gsmp, discrete-event-systems, non-markovian, clock-structures, simulation]
related_concepts: [discrete-event-systems, markov-chains, timed-automata, queueing-theory]
sources: ["[[cassandras-des-intro]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A Generalized Semi-Markov Process (GSMP) is a stochastic process model for discrete event systems where each active event has an associated clock drawn from a general (not necessarily exponential) distribution, and the next event to fire is the one whose clock runs out first; GSMPs subsume Markov chains (exponential clocks) and are the canonical stochastic DES model for general service-time distributions.

## Reading Path
- [[cassandras-des-intro-ch06]] (unread) — primary treatment: stochastic clock structures, GSMP definition and dynamics, relationship to CTMCs
