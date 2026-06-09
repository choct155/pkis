---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- knowledge-representation
extends:
- open-world-assumption
id: pkis:concept:default-reasoning
knowledge_type: concept
maturity: settled
prerequisite-of:
- defeasibility
related_concepts:
- '[[statistical-inheritance]]'
- '[[open-world-assumption]]'
sources:
- '[[rowe-statistical-inheritance-1982]]'
tags:
- logic
- expert-systems
- epistemology
title: Default Reasoning
understanding: 0
---

Reasoning from the absence of explicit information using a closed-world assumption — inferring that properties not explicitly listed are "normal" or typical; in statistical inheritance, the default is that unlisted subsets have aggregate statistics consistent with what inheritance predicts from the parent set.

## Reading Path
- [[rowe-statistical-inheritance-1982]] (unread) — invokes closed-world defaults to handle combinatorial explosion of possible subsets in statistical query answering

## Connections
- [[open-world-assumption]] — extends: circumscription generalizes the closed-world assumption with predicate minimization
- [[defeasibility]] — prerequisite-of: default-status conclusions are precisely the ones that may be defeated/retracted