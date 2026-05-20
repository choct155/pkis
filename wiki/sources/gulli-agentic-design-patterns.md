---
title: "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems"
authors: "Antonio Gullí"
year: 2025
type: book
domain: [deep-learning, symbolic-subsymbolic, knowledge-representation]
tags: [llm, agentic-ai, design-patterns, multi-agent-systems, rag, prompt-engineering, tool-use, safety]
source_url: "https://doi.org/10.1007/978-3-032-01402-3"
drive_id: "1_ODFqJ10y3xF1JFUcyDGOZljFJhDaRop"
drive_path: "PKIS/sources/books/AgenticDesignPatterns.pdf"
isbn: "978-3-032-01401-6"
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts:
  - "[[agentic-systems]]"
  - "[[prompt-chaining]]"
  - "[[tool-use]]"
  - "[[multi-agent-systems]]"
  - "[[human-in-the-loop]]"
  - "[[retrieval-augmented-generation]]"
  - "[[graph-rag]]"
  - "[[in-context-learning]]"
---

## Summary

Agentic Design Patterns catalogs 21 architectural patterns for building autonomous AI systems powered by large language models. The central thesis mirrors software engineering's pattern movement: just as design patterns gave developers a shared vocabulary for recurring architectural challenges, agentic patterns provide reusable solutions for the recurring problems in designing agent behavior — perception, planning, action, memory, coordination, and safety. The organizing metaphor is a "canvas": the underlying infrastructure (frameworks, state stores, tool registries) on which patterns are composed into working systems.

Part I (Ch. 1–21) covers all 21 patterns in depth. Each chapter follows a consistent structure: pattern overview, practical applications, and hands-on code using LangChain, Google ADK, and/or CrewAI. The patterns span foundational flow control (Prompt Chaining, Routing, Parallelization), self-improvement (Reflection, Learning and Adaptation), knowledge and memory (RAG, Memory Management), coordination (Multi-Agent Collaboration, Inter-Agent Communication), and safety and oversight (Guardrails, Human-in-the-Loop, Exception Handling, Evaluation). Chapter 14 is particularly relevant to the wiki: it covers standard RAG, GraphRAG, and the emerging Agentic RAG pattern. Chapter 10 covers Model Context Protocol as a standardized tool integration layer.

Part II (Ch. 22–29) provides supplementary material: advanced prompting techniques, a survey of agent frameworks (LangChain, LangGraph, Google ADK, CrewAI), CLI agents (Claude Code, Gemini CLI, Aider), and an inside look at reasoning processes of major LLMs. Practically oriented; Google's ecosystem is featured prominently.

## Key Knowledge Objects

- [[agentic-systems]] (framework, high) — autonomous LLM-powered entities that perceive, plan, and act toward goals; the central organizing concept of the book
- [[prompt-chaining]] (technique, high) — sequential decomposition of complex tasks into chained prompt sequences with structured output passing
- [[tool-use]] (technique, high) — agent capability to invoke external tools, APIs, databases, and services via function calling
- [[multi-agent-systems]] (framework, high — also technique) — systems of multiple coordinated specialized agents collaborating or competing to achieve complex goals
- [[human-in-the-loop]] (technique, moderate — also principle) — engineering human oversight and intervention checkpoints into autonomous agent workflows
- [[retrieval-augmented-generation]] (existing, coverage +1) — Ch. 14 gives comprehensive treatment including standard RAG, GraphRAG, and Agentic RAG
- [[graph-rag]] (existing, coverage +1) — Ch. 14 explicitly covers GraphRAG as an advanced agentic retrieval pattern
- [[in-context-learning]] (existing, coverage +1) — Ch. 22 formalizes prompting techniques that operationalize ICL as engineered pipelines

## Key Extractions

1. **The canvas metaphor:** "The canvas is not a blank visual space, but rather the underlying infrastructure and frameworks that provide the environment and tools for your agents to exist and operate... Managing state, communication, tool access, and flow of logic." Patterns are compositions on top of this canvas.

2. **Agentic system properties:** Autonomy (acting without constant human oversight), proactiveness (initiating actions toward goals), and flexibility (adapting to context). Contrast with traditional software that "follows rigid, step-by-step instructions."

3. **Agentic RAG distinction (Ch. 14):** Standard RAG retrieves passively from a fixed index. Agentic RAG uses the agent to dynamically decide what to retrieve, when, and in what sequence — the retrieval itself becomes a planned action, not a fixed pipeline step.

4. **Model Context Protocol (Ch. 10) vs. function calling:** MCP provides a standardized server-client protocol for tool integration, enabling reusable tool servers that multiple agents can consume. Function calling is direct but non-standardized; MCP is indirected but composable and reusable across agent frameworks.

5. **Safety as pattern composition (Ch. 18):** Guardrails are not a single control mechanism but a composed pattern: input filtering + output filtering + content moderation + human checkpoints + exception recovery chains. "Engineering Reliable Agents" is the chapter's unifying frame.

6. **Learning and Adaptation (Ch. 9):** Covers AlphaEvolve/OpenEvolve — agents that use evolutionary strategies to improve their own code or strategies over time, bridging agentic patterns with reinforcement-like self-improvement.

7. **Pattern combination:** The conclusion frames complex systems as combinations of patterns applied in sequence or hierarchy. No single pattern is sufficient; production systems layer multiple patterns (e.g., Prompt Chaining + Reflection + Human-in-the-Loop + Guardrails).

## Connection Candidates

- [[retrieval-augmented-generation]] — uses: Ch. 14 covers RAG comprehensively as a first-class agentic pattern
- [[graph-rag]] — uses: Ch. 14 treats GraphRAG as an advanced variant within the knowledge retrieval pattern
- [[in-context-learning]] — uses: prompt chaining and few-shot techniques (Ch. 22) operationalize ICL as structured engineering patterns
- [[knowledge-graph]] — uses: knowledge retrieval patterns use KGs as backends; GraphRAG explicitly uses KG structure
- [[directed-graphical-models]] — contrasts-with: agent planning graphs encode execution sequences while DGMs encode probabilistic dependencies — same directed graph structure, very different semantics
- [[human-in-the-loop]] — grounds: the safety-as-pattern-composition framing grounds human oversight as an architectural concern, not an afterthought
- [[zhang-graphrag-survey]] — extends: this source covers GraphRAG as one of 21 patterns; zhang-graphrag-survey gives the deep theoretical treatment of the same concept

## Connection Candidates (new → existing)

- [[agentic-systems]] uses [[in-context-learning]]: ICL is the substrate; agentic systems orchestrate multiple ICL calls with persistent state and tool access
- [[tool-use]] uses [[retrieval-augmented-generation]]: RAG is a specialized retrieval tool that agents invoke via the tool-use pattern
- [[multi-agent-systems]] uses [[agentic-systems]]: multi-agent systems compose individual agentic entities into coordination structures
- [[prompt-chaining]] prerequisite-of [[multi-agent-systems]]: structured prompt sequences are a primitive that agent orchestration builds on

## Chapters

| Ch | Stub | Title |
|---|---|---|
| 1 | [[gulli-agentic-design-patterns-ch01]] | Prompt Chaining |
| 2 | [[gulli-agentic-design-patterns-ch02]] | Routing |
| 3 | [[gulli-agentic-design-patterns-ch03]] | Parallelization |
| 4 | [[gulli-agentic-design-patterns-ch04]] | Reflection |
| 5 | [[gulli-agentic-design-patterns-ch05]] | Tool Use (Function Calling) |
| 6 | [[gulli-agentic-design-patterns-ch06]] | Planning |
| 7 | [[gulli-agentic-design-patterns-ch07]] | Multi-Agent Collaboration |
| 8 | [[gulli-agentic-design-patterns-ch08]] | Memory Management |
| 9 | [[gulli-agentic-design-patterns-ch09]] | Learning and Adaptation |
| 10 | [[gulli-agentic-design-patterns-ch10]] | Model Context Protocol |
| 11 | [[gulli-agentic-design-patterns-ch11]] | Goal Setting and Monitoring |
| 12 | [[gulli-agentic-design-patterns-ch12]] | Exception Handling and Recovery |
| 13 | [[gulli-agentic-design-patterns-ch13]] | Human-in-the-Loop |
| 14 | [[gulli-agentic-design-patterns-ch14]] | Knowledge Retrieval (RAG) |
| 15 | [[gulli-agentic-design-patterns-ch15]] | Inter-Agent Communication (A2A) |
| 16 | [[gulli-agentic-design-patterns-ch16]] | Resource-Aware Optimization |
| 17 | [[gulli-agentic-design-patterns-ch17]] | Reasoning Techniques |
| 18 | [[gulli-agentic-design-patterns-ch18]] | Guardrails/Safety Patterns |
| 19 | [[gulli-agentic-design-patterns-ch19]] | Evaluation and Monitoring |
| 20 | [[gulli-agentic-design-patterns-ch20]] | Prioritization |
| 21 | [[gulli-agentic-design-patterns-ch21]] | Exploration and Discovery |
| 22 | [[gulli-agentic-design-patterns-ch22]] | Advanced Prompting Techniques |
| 23 | [[gulli-agentic-design-patterns-ch23]] | AI Agentic Interactions: From GUI to Real World Environment |
| 24 | [[gulli-agentic-design-patterns-ch24]] | A Quick Overview of Agentic Frameworks |
| 25 | [[gulli-agentic-design-patterns-ch25]] | Building an Agent with AgentSpace |
| 26 | [[gulli-agentic-design-patterns-ch26]] | AI Agents on the CLI |
| 27 | [[gulli-agentic-design-patterns-ch27]] | Under the Hood: An Inside Look at the Agents' Reasoning Engines |
| 28 | [[gulli-agentic-design-patterns-ch28]] | Coding Agents |
| 29 | [[gulli-agentic-design-patterns-ch29]] | Conclusion |
