---
aliases: []
also_type: []
applies:
- mechanism-design
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- multi-agent-systems
id: pkis:framework:contract-net-protocol
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
- gulli-agentic-design-patterns-ch02
- gulli-agentic-design-patterns-ch07
- gulli-agentic-design-patterns-ch15
tags:
- task-sharing
- distributed-problem-solving
- manager-contractor
- bidding
title: Contract Net Protocol
understanding: 0
---

## Definition
One of the oldest and most widely used multiagent task-sharing protocols (Reid Smith, 1980), modeled on how firms use contracts. An agent identifying a task it cannot (or should not) do alone becomes the *manager* and broadcasts a *task announcement* with enough detail (specification, deadlines, quality requirements) for others to judge whether to bid. Capable and willing agents return *bids*; the manager evaluates them and sends an *award message* to the chosen *contractor(s)*, who take responsibility for the task and may recursively announce subtasks. Its three computational stages are task-announcement processing, bid processing, and award processing. Despite (or because of) its simplicity it is repeatedly reinvented — a variant runs every time a ride is requested via Uber.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mechanism-design]] — applies
[To be populated during integration]