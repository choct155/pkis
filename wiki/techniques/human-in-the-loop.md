---
title: "Human-in-the-Loop"
knowledge_type: technique
also_type: [principle]
domain: [deep-learning]
tags: [llm, agentic-ai, safety, human-oversight, agent-control]
related_concepts: []
sources: ["[[gulli-agentic-design-patterns]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

An agent design pattern that inserts defined human review and approval checkpoints into otherwise autonomous workflows — enabling human judgment to validate, redirect, or veto agent actions at critical decision points before irreversible consequences occur.

Classification note: assigned as technique because HITL is a concrete design pattern with implementation structure (checkpoint placement, approval interfaces, callback handlers); also typed as principle because it encodes a normative commitment to human oversight that shapes agent architecture broadly.

## Reading Path
- [[gulli-agentic-design-patterns-ch13]] (unread) — primary treatment: HITL pattern overview, applications, and hands-on code
- [[gulli-agentic-design-patterns-ch18]] (unread) — guardrails chapter treats HITL as a component of the broader safety pattern composition
