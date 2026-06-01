---
aliases: []
cross_cluster_dependencies:
- model-evolution
- evaluation-infrastructure
date_created: 2026-05-30
date_updated: '2026-06-01'
domain:
- knowledge-representation
frontier_hypotheses:
- formal-coverage-model-sourcing-efficiency
hypotheses:
- formal-coverage-model-sourcing-efficiency
id: pkis:research-cluster:ontological-coverage-planning
knowledge_type: research-cluster
origin: research-program
status: active
tags:
- coverage-completeness
- source-acquisition
- ontology-gap-analysis
title: Ontological Coverage Planning
uses:
- formal-ontology
- information-theory
---

## Thesis
Maintaining an explicit ontological coverage model enables systematic identification of knowledge gaps prior to source acquisition, converting sourcing decisions from opinion-driven to hypothesis-driven.

## Summary
Without a formal coverage model, you cannot know what you don't know before acquiring it. The ontology makes it possible to ask whether a proposed source fills a structural gap or overlaps with existing coverage — a question that informal coverage knowledge cannot answer systematically.

## Research Program Context
Primarily a Theme 2 (operational implications) cluster. Directly relevant to IKS source acquisition design. Also a methodological contribution opportunity — no standard coverage completeness metrics exist.

## Constituent Hypotheses
- **formal-coverage-model-sourcing-efficiency** — Organizations with formal ontological coverage models exhibit lower redundant source acquisition and higher marginal coverage yield per new source

## Current Frontier
Anchored to `formal-ontology` (the coverage model's input) and `information-theory` (completeness measure). Lead (and only) hypothesis **`formal-coverage-model-sourcing-efficiency`**: a formal coverage model lowers redundant source acquisition and raises marginal coverage yield per source — converting sourcing from opinion-driven to hypothesis-driven (the meta-goal this whole de-orphaning effort serves). Coverage gap: `information-theory` is a sourceless stub.

## Connections
- [[information-theory]] — uses: coverage completeness is an information-theoretic concept
- [[formal-ontology]] — uses: coverage planning requires a formal ontological model as input
- [[ontology]] — uses: coverage planning requires a formal ontological model as input
- [[information-theory]] — uses: coverage completeness is an information-theoretic concept