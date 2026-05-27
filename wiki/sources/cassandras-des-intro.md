---
id: "pkis:source:cassandras-des-intro"
aliases: ["Introduction to Discrete Event Systems", "Cassandras DES"]
title: "Introduction to Discrete Event Systems (Third Edition)"
authors: "Christos G. Cassandras, Stéphane Lafortune"
year: 2021
type: book
domain: [formal-methods, systems-theory, optimization]
tags: [automata-theory, formal-languages, petri-nets, supervisory-control, markov-chains, queueing-theory, simulation, dynamic-programming, probability-theory, discrete-event-systems]
source_url: "https://doi.org/10.1007/978-3-030-72274-6"
drive_id: "1dSYKjRi76A9-XYGBdIuGDisoxUFWvraG"
drive_path: "PKIS/sources/books/Introduction to Discrete Event Systems - Cassandras Lafortune.pdf"
isbn: "978-3-030-72272-2"
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts:
  - "[[discrete-event-systems]]"
  - "[[finite-automata]]"
  - "[[petri-nets]]"
  - "[[supervisory-control]]"
  - "[[timed-automata]]"
  - "[[markov-chains]]"
  - "[[markov-decision-processes]]"
  - "[[queueing-theory]]"
  - "[[perturbation-analysis]]"
  - "[[discrete-event-simulation]]"
  - "[[model-checking]]"
  - "[[temporal-logic]]"
  - "[[controllability]]"
  - "[[generalized-semi-markov-process]]"
---

## Summary

Cassandras and Lafortune's *Introduction to Discrete Event Systems* is the canonical graduate textbook for the formal study of systems whose dynamics are driven by instantaneous events rather than continuous differential equations. A discrete event system (DES) is characterized by a discrete state space and state transitions triggered by events — paradigmatic examples include manufacturing systems, communication networks, computer programs, and traffic systems.

The book develops a layered formal treatment across three levels of abstraction: the untimed logical level (what events can occur and in what order), the timed deterministic level (when events occur under deterministic timing), and the timed stochastic level (when events occur under probabilistic timing). These correspond, respectively, to automata/language theory (Ch. 1–3), Petri nets and timed automata (Ch. 4–5), and stochastic timed automata and Markov chains (Ch. 6–7).

The supervisory control theory of Ramadge and Wonham (Ch. 3) is treated in depth: given a plant modeled as a finite automaton and a specification language, the central problem is to synthesize a supervisor that restricts the plant's behavior to the legal sublanguage while remaining controllable and nonblocking. The book covers the key theorems (Controllability Theorem, Nonblocking Controllability Theorem) and algorithms for computing maximally permissive supervisors, including extensions to partial observation and decentralized control.

The second half of the book turns to performance analysis: Markov chains and Markov decision processes (Ch. 7, 9) for steady-state and optimal control analysis of stochastic DES; queueing theory (Ch. 8) as a practically important class of stochastic DES; discrete-event simulation (Ch. 10) as an alternative when analytical solutions are intractable; and perturbation analysis / infinitesimal perturbation analysis (IPA) (Ch. 11) as a gradient estimation technique that extracts sensitivity information from a single simulation sample path.

The third edition adds new material on labeled transition systems, opacity, model checking, timed automata with guards, stochastic fluid models, and expanded treatment of hybrid automata, reflecting twenty years of advances since the first edition.

## Key Knowledge Objects

- [[discrete-event-systems]] (concept, high) — systems with discrete state spaces driven by instantaneous events; the subject of the book
- [[finite-automata]] (concept, high) — deterministic and nondeterministic automata as formal models for DES logical behavior
- [[supervisory-control]] (framework, high) — Ramadge-Wonham theory for synthesizing controllers that enforce specifications on DES
- [[petri-nets]] (framework, high) — concurrent graphical model of computation enabling analysis of concurrency, conflict, and causality
- [[timed-automata]] (framework, high) — automata extended with real-valued clock variables to model timing constraints
- [[markov-chains]] (concept, high) — discrete-time and continuous-time stochastic processes with the Markov property; central tool for stochastic DES analysis
- [[markov-decision-processes]] (framework, high) — Markov chains with control actions and cost criteria; connects DES to optimal control and reinforcement learning
- [[queueing-theory]] (framework, high) — performance modeling framework for service systems using Markovian and non-Markovian arrival/service processes
- [[perturbation-analysis]] (technique, high) — gradient estimation for DES performance measures from simulation sample paths; includes IPA and SPA
- [[discrete-event-simulation]] (technique, high) — event-scheduling and process-oriented simulation schemes for DES performance evaluation
- [[model-checking]] (technique, high) — algorithmic formal verification of temporal-logic specifications against automata models of DES
- [[temporal-logic]] (concept, moderate — could be framework) — logical formalism for specifying properties of system trajectories over time; used as DES specification language in formal verification
- [[controllability]] (concept, high) — language-theoretic property of a sublanguage: a language K is controllable w.r.t. plant L if all uncontrollable continuations of K-strings that are also in L remain in K's prefix-closure
- [[generalized-semi-markov-process]] (concept, high) — stochastic process generalizing Markov chains by allowing non-exponential state holding times via general clock structures

## Key Extractions

1. **Controllability Theorem (Ch. 3):** A language K (the desired controlled behavior) is achievable by a supervisor if and only if K is controllable with respect to the plant language L and the set of uncontrollable events. Controllability is defined as: for all strings s in the prefix-closure of K, and all uncontrollable events σ_u such that sσ_u is in L, the string sσ_u must also be in the prefix-closure of K. This is the fundamental result of supervisory control theory.

2. **Three levels of DES abstraction (Ch. 1):** Logical/untimed level (which events can occur — modeled by automata/languages), timed deterministic level (when events occur under fixed timing — modeled by timed automata), and timed stochastic level (when events occur under random timing — modeled by stochastic timed automata and Markov chains). The book treats all three systematically.

3. **Petri nets vs. automata (Ch. 4):** Petri nets are strictly more expressive than finite automata: they can model unbounded concurrency compactly (exponential blow-up in automata state space). However, decidability results degrade — reachability in Petri nets is decidable but EXPSPACE-complete, and liveness is undecidable for general Petri nets.

4. **Infinitesimal Perturbation Analysis (IPA) (Ch. 11):** For a DES simulation sample path with performance measure L(θ) where θ is a parameter, the IPA estimator dL/dθ is computed by propagating event-time derivatives through the sample path. Under a regularity condition (sample function differentiability almost everywhere), the IPA estimator is unbiased: E[dL/dθ] = dE[L]/dθ. IPA extracts gradient information from a single simulation run rather than finite differences requiring multiple runs.

5. **Markov Decision Processes and dynamic programming (Ch. 9):** The optimality equation (Bellman equation) for the discounted-cost MDP is V(x) = min_u [g(x,u) + α Σ_y P(y|x,u) V(y)]. Value iteration and policy iteration both converge to the optimal value function under standard conditions. The connection to DES: MDPs provide the framework for optimal scheduling, admission control, and routing in stochastic queueing systems.

6. **Little's Law (Ch. 8):** For any stable queueing system: L = λW, where L is the average number of customers in the system, λ is the average arrival rate, and W is the average time a customer spends in the system. This result holds under minimal assumptions and connects the three fundamental performance measures of queueing systems.

7. **Opacity (Ch. 2, new in 3rd edition):** A DES is opaque with respect to a secret S if for every observation-equivalent string that reaches a secret state, there exists another explanation consistent with not being in S. Opacity formalizes information-hiding requirements in security-aware DES, connecting automata theory to formal security specifications.

## Connection Candidates

- [[state-space-models]] — DES state-space formalism parallels continuous state-space models; shared vocabulary of states, transitions, observability; `equivalent-in-context` with DES timed automata state-space
- [[reinforcement-learning]] — Markov Decision Processes (Ch. 9) are the shared mathematical substrate; supervisory control and RL both solve optimal control problems over MDPs; `uses` predicate
- [[directed-graphical-models]] — Markov chains are special cases of directed graphical models; Ch. 7 CTMC dynamics have Bayesian network representations; `specializes` predicate
- [[formal-methods]] — supervisory control theory and model checking (Ch. 2–3) are applications of formal methods to control engineering; new domain introduced
- [[optimization]] — dynamic programming for MDPs (Ch. 9) and IPA gradient estimation (Ch. 11) connect to continuous optimization methods; `uses` predicate
- [[kalman-filter]] — both Kalman filtering and DES state estimation involve partially-observed stochastic processes; `contrasts-with` (continuous vs. discrete state)

## Chapters

| Ch | Stub | Title |
|---|---|---|
| 1 | [[cassandras-des-intro-ch01]] | Systems and Models |
| 2 | [[cassandras-des-intro-ch02]] | Languages and Automata |
| 3 | [[cassandras-des-intro-ch03]] | Supervisory Control |
| 4 | [[cassandras-des-intro-ch04]] | Petri Nets |
| 5 | [[cassandras-des-intro-ch05]] | Timed and Hybrid Models |
| 6 | [[cassandras-des-intro-ch06]] | Stochastic Timed Automata |
| 7 | [[cassandras-des-intro-ch07]] | Markov Chains |
| 8 | [[cassandras-des-intro-ch08]] | Introduction to Queueing Theory |
| 9 | [[cassandras-des-intro-ch09]] | Controlled Markov Chains |
| 10 | [[cassandras-des-intro-ch10]] | Introduction to Discrete-Event Simulation |
| 11 | [[cassandras-des-intro-ch11]] | Sensitivity Analysis and Concurrent Estimation |
