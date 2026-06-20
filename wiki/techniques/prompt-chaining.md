---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- deep-learning
id: pkis:technique:prompt-chaining
knowledge_type: technique
maturity: evolving
related_concepts: []
sources:
- '[[gulli-agentic-design-patterns]]'
- gulli-agentic-design-patterns-ch01
- gulli-agentic-design-patterns-ch05
tags:
- llm
- agentic-ai
- prompt-engineering
- structured-output
title: Prompt Chaining
understanding: 0
---

A technique for solving complex tasks by decomposing them into a sequence of simpler subtasks, where each prompt takes the structured output of the previous step as input — improving reliability by constraining each LLM call to a well-defined scope rather than demanding the full solution in a single prompt.

## Reading Path
- [[gulli-agentic-design-patterns-ch01]] (unread) — primary treatment: overview, applications, and hands-on code examples