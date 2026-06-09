---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:framework:knowledge-based-agent
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch07
tags:
- agents
- declarative
- tell-ask
- knowledge-level
title: Knowledge-Based Agent
understanding: 0
---

## Definition
An agent architecture whose central component is a knowledge base (KB) — a set of sentences expressed in a knowledge representation language, each asserting something about the world. The agent interacts with the KB through two operations: TELL (add a sentence) and ASK (query what follows). On each cycle the agent TELLs its percepts, ASKs what action to take, then TELLs the chosen action. Because the answer to an ASK is required to follow logically from prior TELLs (sound inference), the agent is amenable to description at the knowledge level — specified purely by what it knows and what its goals are, independent of its implementation. This embodies the declarative approach to system building (TELL the agent what it needs to know, starting from an empty KB) as opposed to the procedural approach (encode behavior directly as code); a successful agent typically combines both, and declarative knowledge can often be compiled into efficient procedural code.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]