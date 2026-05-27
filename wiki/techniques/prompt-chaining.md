---
id: "pkis:technique:prompt-chaining"
aliases: []
title: "Prompt Chaining"
knowledge_type: technique
also_type: []
domain: [deep-learning]
tags: [llm, agentic-ai, prompt-engineering, structured-output]
related_concepts: []
sources: ["[[gulli-agentic-design-patterns]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

A technique for solving complex tasks by decomposing them into a sequence of simpler subtasks, where each prompt takes the structured output of the previous step as input — improving reliability by constraining each LLM call to a well-defined scope rather than demanding the full solution in a single prompt.

## Reading Path
- [[gulli-agentic-design-patterns-ch01]] (unread) — primary treatment: overview, applications, and hands-on code examples
