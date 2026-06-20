---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- formal-methods
- systems-theory
id: pkis:framework:supervisory-control
knowledge_type: framework
maturity: settled
related_concepts:
- discrete-event-systems
- finite-automata
- controllability
- petri-nets
sources:
- '[[cassandras-des-intro]]'
- cassandras-des-intro-ch02
- cassandras-des-intro-ch03
- cassandras-des-intro-ch04
tags:
- supervisory-control
- ramadge-wonham
- controllability
- automata-theory
- discrete-event-systems
- formal-methods
title: Supervisory Control Theory
understanding: 0
---

Supervisory control theory (Ramadge and Wonham, 1987) is a framework for synthesizing controllers (supervisors) for discrete event systems that restrict the plant's event sequences to a legal specification language while respecting which events are controllable (disableable) and which are not; the central result is that a specification K is achievable if and only if K is controllable with respect to the plant and the uncontrollable events.

## Reading Path
- [[cassandras-des-intro-ch03]] (unread) — primary treatment: full supervisory control framework including nonblocking, partial observation, and decentralized extensions