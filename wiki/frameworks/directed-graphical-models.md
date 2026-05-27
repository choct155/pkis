---
id: "pkis:framework:directed-graphical-models"
aliases: []
title: "Directed Graphical Models (Bayesian Networks)"
knowledge_type: framework
also_type: []
domain: [bayesian-stats, knowledge-representation, causal-analysis]
tags: [probability-theory, graph-theory]
related_concepts: ["[[probability-theory]]", "[[undirected-graphical-models]]", "[[structural-causal-models]]", "[[d-separation]]"]
sources: ["[[deisenroth-mml]]", "[[pearl-causality]]", "[[blei-vi-review]]", "[[cunningham-causal-inference-mixtape]]", "[[kroese-statistical-modeling]]", "[[pearl-reverend-bayes-1982]]", "[[capretto-bambi-2022]]", "[[kurz-hybrid-modeling-2022]]", "[[davis-marcus-simulation-cognitive-2015]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 6
understanding: 0
maturity: settled
---

## Reading Path
- [[deisenroth-mml]] (unread) — probabilistic treatment; DAG factorization and Bayesian network inference
- [[pearl-causality-ch01]] (unread) — Pearl's treatment; d-separation and the bridge from probability to causal DAGs
- [[blei-vi-review]] (unread) — Section 4.2: conditional conjugacy expressed through DGM structure; factorization exploited in CAVI coordinate updates
- [[cunningham-causal-inference-mixtape-ch04]] (unread) — practitioner DAG tutorial: nodes, directed edges, confounders, colliders, backdoor criterion for econometric identification
- [[kroese-statistical-modeling-ch08]] (unread) — Bayesian networks as graphical representations of conditional independence in hierarchical Bayesian models; §8.3
- [[pearl-reverend-bayes-1982]] (unread) — proto-Bayesian-network formulation; inference net with belief propagation; shows CI as structural consequence of tree topology
- [[capretto-bambi-2022]] (unread) — Bambi's hierarchical models implicitly define a DGM with hyperprior structure
- [[kurz-hybrid-modeling-2022]] (unread) — joint model p(ν,d|y) ∝ p(y|ν,d)·p(ν)·p(d) is a three-node DGM; Gibbs sampling exploits conditional independence structure
- [[davis-marcus-simulation-cognitive-2015]] (unread) — §2.2: noisy Newton cognitive models (Sanborn, Battaglia) implicitly define DGMs over physical state variables with Monte Carlo sampling over uncertain initial conditions; Davis & Marcus critique these models as too strong — their probabilistic machinery predicts better performance than humans exhibit, and cannot account for systematic non-noise errors

Framework for representing joint probability distributions as directed acyclic graphs (DAGs) where edges encode conditional dependencies; the joint factors as $p(x_{1:n}) = \prod_i p(x_i | \text{pa}(x_i))$ where $\text{pa}(x_i)$ are the parents of node $i$ — the probabilistic counterpart to causal DAGs and the structural backbone of Bayesian networks and many generative models. Pearl's SCMs extend this framework to the interventional and counterfactual layers by adding structural equations to the probabilistic skeleton.
