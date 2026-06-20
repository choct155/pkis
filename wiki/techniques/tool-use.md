---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- deep-learning
id: pkis:technique:tool-use
knowledge_type: technique
maturity: evolving
related_concepts: []
sources:
- '[[gulli-agentic-design-patterns]]'
- '[[radhakrishnan-datagemma-2024]]'
- gulli-agentic-design-patterns-ch05
- gulli-agentic-design-patterns-ch10
- gulli-agentic-design-patterns-ch21
- gulli-agentic-design-patterns-ch24
- gulli-agentic-design-patterns-ch25
- gulli-agentic-design-patterns-ch26
tags:
- llm
- agentic-ai
- function-calling
- api-integration
- tool-use
title: Tool Use (Function Calling)
understanding: 0
---

The agent pattern in which an LLM is given a set of callable external tools (functions, APIs, databases, code executors, search engines) and learns to invoke them with structured arguments to retrieve information or take actions beyond text generation — extending the agent's effective capability to the full space of available services.

## Reading Path
- [[gulli-agentic-design-patterns-ch05]] (unread) — primary treatment: tool use pattern overview, applications, and code examples across LangChain, CrewAI, and Google ADK
- [[radhakrishnan-datagemma-2024]] (unread) — RIG (Retrieval Interleaved Generation) as a Toolformer-style tool-use application where the "tool" is a natural-language Data Commons query rather than a structured API call; fine-tuning teaches the LLM when to invoke the tool