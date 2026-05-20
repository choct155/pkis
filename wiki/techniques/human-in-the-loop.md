---
title: "Human-in-the-Loop"
knowledge_type: technique
also_type: [principle]
domain: [deep-learning]
tags: [llm, agentic-ai, safety, human-oversight, agent-control]
related_concepts: []
sources: ["[[gulli-agentic-design-patterns]]", "[[miehling-agentic-systems-theory-2025]]", "[[afroogh-task-driven-human-ai-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: evolving
---

An agent design pattern that inserts defined human review and approval checkpoints into otherwise autonomous workflows — enabling human judgment to validate, redirect, or veto agent actions at critical decision points before irreversible consequences occur.

Classification note: assigned as technique because HITL is a concrete design pattern with implementation structure (checkpoint placement, approval interfaces, callback handlers); also typed as principle because it encodes a normative commitment to human oversight that shapes agent architecture broadly.

## Reading Path
- [[gulli-agentic-design-patterns-ch13]] (unread) — primary treatment: HITL pattern overview, applications, and hands-on code
- [[gulli-agentic-design-patterns-ch18]] (unread) — guardrails chapter treats HITL as a component of the broader safety pattern composition
- [[miehling-agentic-systems-theory-2025]] (unread) — frames HITL governance through residual control rights: humans retain authority over strategic, value-laden, and irreversible decisions; escalation mechanisms needed for uncertain cases
- [[afroogh-task-driven-human-ai-2025]] (unread) — extends HITL with adversarial AI role; provides risk-complexity matrix for principled checkpoint placement and distinguishes initiative, control, and decision-making authority
