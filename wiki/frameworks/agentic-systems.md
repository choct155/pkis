---
aliases: []
also_type:
- concept
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- deep-learning
- symbolic-subsymbolic
id: pkis:framework:agentic-systems
knowledge_type: framework
maturity: evolving
related_concepts: []
sources:
- '[[gulli-agentic-design-patterns]]'
- '[[liu-symagent]]'
- '[[miehling-agentic-systems-theory-2025]]'
- gulli-agentic-design-patterns-ch05
- gulli-agentic-design-patterns-ch07
- gulli-agentic-design-patterns-ch08
- gulli-agentic-design-patterns-ch10
- gulli-agentic-design-patterns-ch21
- gulli-agentic-design-patterns-ch23
- gulli-agentic-design-patterns-ch24
- gulli-agentic-design-patterns-ch26
- gulli-agentic-design-patterns-ch28
- gulli-agentic-design-patterns-ch29
specializes:
- rational-agent
tags:
- llm
- agentic-ai
- autonomous-agents
- multi-agent-systems
title: Agentic Systems
understanding: 0
---

Autonomous computational entities powered by LLMs as cognitive engines that perceive their environment, maintain state, plan sequences of actions, invoke external tools, and execute those actions toward goals — with a degree of flexibility and initiative absent from traditional rule-based software.

Classification note: assigned as framework because agentic systems define an architectural paradigm organizing concepts (autonomy, state, perception), techniques (planning, tool use, prompt chaining), and results (agent trajectories, evaluation metrics) into a coherent design space; also typed as concept because "agentic system" names an idea with a precise definition and boundary.

## Reading Path
- [[gulli-agentic-design-patterns]] (unread) — primary treatment; defines the concept and catalogs 21 architectural patterns
- [[liu-symagent]] (unread) — SymAgent: neural-symbolic agent with KG as dynamic environment; self-learning framework via online exploration and offline iterative policy updating
- [[miehling-agentic-systems-theory-2025]] (unread) — systems-theoretic grounding: defines functional agency (action generation + outcome model + adaptation), identifies emergence mechanisms, and frames open governance challenges

## Connections
- [[rational-agent]] — specializes: LLM-powered agentic systems are a modern specialization of the classical rational-agent paradigm.