---
id: "pkis:framework:multi-agent-systems"
aliases: []
title: "Multi-Agent Systems"
knowledge_type: framework
also_type: [technique]
domain: [deep-learning, symbolic-subsymbolic]
tags: [llm, agentic-ai, multi-agent-systems, agent-coordination, distributed-ai]
related_concepts: []
sources: ["[[gulli-agentic-design-patterns]]", "[[miehling-agentic-systems-theory-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: evolving
---

An architectural paradigm in which multiple specialized LLM-powered agents are coordinated to collaborate on tasks that exceed the capabilities or context limits of a single agent — each agent holding a distinct role, toolset, and perspective, with inter-agent communication structured by defined protocols.

Classification note: assigned as framework because multi-agent coordination defines a design space of patterns (orchestrator-worker, peer-to-peer, hierarchical) organizing individual agentic techniques; also typed as technique because multi-agent collaboration is itself an invocable pattern with inputs (task, agent roster) and outputs (result, trajectory).

## Reading Path
- [[gulli-agentic-design-patterns-ch07]] (unread) — multi-agent collaboration patterns with code examples
- [[gulli-agentic-design-patterns-ch15]] (unread) — inter-agent communication (A2A) protocol
- [[miehling-agentic-systems-theory-2025]] (unread) — systems-theoretic treatment: agent-agent interaction as mechanism of emergence; subgoal delegation, trust transfer, and cooperative/competitive interaction dynamics
