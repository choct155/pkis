---
id: "pkis:concept:controllability"
aliases: []
title: "Controllability (DES)"
knowledge_type: concept
also_type: []
domain: [formal-methods, systems-theory]
tags: [supervisory-control, ramadge-wonham, formal-languages, automata-theory, discrete-event-systems]
related_concepts: [discrete-event-systems, supervisory-control, finite-automata]
sources: ["[[cassandras-des-intro]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

In the Ramadge-Wonham supervisory control framework, a language K is controllable with respect to a plant language L and set of uncontrollable events Σ_uc if for every string s in the prefix-closure of K and every uncontrollable event σ_u such that sσ_u ∈ L, we have sσ_u ∈ the prefix-closure of K — meaning uncontrollable transitions cannot be prevented from leading out of the desired behavior.

## Disambiguation
Controllability in DES refers to a language-theoretic property of the specification sublanguage relative to the plant, distinct from Kalman's controllability condition for linear systems (which concerns reachability of all states by choice of input). Both capture the intuition that a controller can steer the system, but the DES version is about event-enabling rather than state-reachability.

## Reading Path
- [[cassandras-des-intro-ch03]] (unread) — primary treatment: Controllability Theorem, nonblocking controllability, algorithms for computing maximal controllable sublanguages
