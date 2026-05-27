---
id: "pkis:framework:supervisory-control"
aliases: []
title: "Supervisory Control Theory"
knowledge_type: framework
also_type: []
domain: [formal-methods, systems-theory]
tags: [supervisory-control, ramadge-wonham, controllability, automata-theory, discrete-event-systems, formal-methods]
related_concepts: [discrete-event-systems, finite-automata, controllability, petri-nets]
sources: ["[[cassandras-des-intro]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Supervisory control theory (Ramadge and Wonham, 1987) is a framework for synthesizing controllers (supervisors) for discrete event systems that restrict the plant's event sequences to a legal specification language while respecting which events are controllable (disableable) and which are not; the central result is that a specification K is achievable if and only if K is controllable with respect to the plant and the uncontrollable events.

## Reading Path
- [[cassandras-des-intro-ch03]] (unread) — primary treatment: full supervisory control framework including nonblocking, partial observation, and decentralized extensions
