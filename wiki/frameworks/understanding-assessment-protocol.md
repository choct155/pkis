---
aliases:
- UAP
- calibration protocol
also_type: []
applies:
- mcmc
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 0
date_created: '2026-06-07'
date_updated: '2026-06-07'
domain:
- bayesian-stats
- deep-learning
- knowledge-representation
- optimization
- causal-analysis
- symbolic-subsymbolic
id: pkis:framework:understanding-assessment-protocol
knowledge_type: framework
maturity: evolving
needs_canonical_source: true
related_concepts: []
sources: []
tags:
- calibration
- spaced-repetition
- assessment
- understanding-scores
- metacognition
- pkis-methodology
title: Understanding Assessment Protocol
understanding: 0
---

## Definition
Framework governing how understanding scores are assigned, maintained, and decayed across all PKIS wiki nodes. Scores are earned through demonstrated behavior in sessions, not self-assessed. Any Claude instance reading this protocol applies it consistently across all chat threads and Code sessions.

## The Five-Level Behavioral Scale

Level 0 — No exposure. Cannot define the term. Has not encountered the concept in a structured way.

Level 1 — Recognition. Can identify the concept when encountered. Can distinguish it from related concepts. Cannot reproduce the definition unprompted or explain the mechanism.

Level 2 — Recall. Can reproduce the definition and key mechanism unprompted. Can explain what the concept does and why it matters. Cannot yet apply it reliably to novel problems.

Level 3 — Application. Can apply the concept to solve novel problems in familiar domains. Can use it as a tool rather than just describe it. Errors occur at the edges but the core application is reliable.

Level 4 — Integration. Can connect the concept to other concepts in non-obvious ways. Can identify when the concept applies in new domains by recognizing structural similarity. Can generate examples and counterexamples independently. Can teach it to someone else.

Level 5 — Generativity. Can identify gaps, limitations, and extensions of the concept. Can use it as a foundation for novel hypotheses. Can critique the concept itself. Can extend it to domains where it has not previously been applied.

## Component Score Definitions by Node Type

### Technique and Concept nodes
Uses standard component_scores anatomy:
- operational_mechanism: can reproduce the algorithm or definition mechanically
- principled_mechanism: understands why it works, not just how
- conditions: knows when to apply it and when not to
- implementation: can implement or instantiate it concretely
- diagnostics: can identify when it is going wrong
- alternatives: can compare to alternatives and reason about tradeoffs
- failure_modes: can anticipate and explain specific failure cases

### Hypothesis nodes
Assessed on:
- hypothesis_statement: can state it precisely without prompting
- evidence_structure: can identify what would confirm or disconfirm it
- failure_modes: can identify where the hypothesis itself might be wrong
- connections: can connect it to adjacent hypotheses unprompted

### Bridge notes
Assessed by whether the connection can be reconstructed unprompted when presented with either of the linked nodes. Level 4 = invokes the bridge note independently during discussion of either node.

### Source nodes
Coverage score = whether the source has been read (set separately). Understanding score = whether key claims have been integrated into relevant concept/technique nodes (demonstrated by application, not recall).

### Research cluster nodes
Assessed by whether the cluster can be navigated coherently: central thesis named, constituent hypotheses identified, relationships explained, advancement path stated.

## Node-Level Score Aggregation

The node-level understanding score = MINIMUM of all non-null component scores. Rationale: a weak section is a genuine gap, not a statistical artifact to be averaged away. A node is only as strong as its weakest assessed component.

## Score Decay Function

Scores decay on the following schedule without reinforcement:
- Level 5 → Level 4 after 90 days
- Level 4 → Level 3 after 60 days
- Level 3 → Level 2 after 30 days
- Level 2 → Level 1 after 21 days
- Level 1 → Level 0 after 14 days

Decay clock resets on any of the three reinforcement triggers below. Score date should be tracked alongside score value via a score_date field (ISO format) in frontmatter. Frontier priority calculation should weight recency — a level 3 earned 90 days ago is higher priority than a level 3 earned 7 days ago.

## The Three Assessment Triggers

These triggers fire continuously across all sessions without requiring explicit invocation. Any Claude instance applies them as a background process.

### Trigger 1 — Organic demonstration (score up)
When the user correctly applies a concept, makes a cross-domain connection independently, identifies a limitation unprompted, or generates a novel hypothesis related to a wiki node, the relevant component score is updated upward. No announcement required. Score updates silently.
Behavioral signals by level:
- Level 3: correct application to a novel problem in a familiar domain
- Level 4: unprompted cross-domain connection or independent example generation
- Level 5: independently identifies a gap, limitation, or extension of the concept

### Trigger 2 — Error detection (score down or hold)
When the user makes a conceptually incorrect statement about something with a wiki node, the instance corrects it and evaluates whether the component score needs downgrading. A corrected error that was close to correct = hold. A fundamental misunderstanding = downgrade one level on that component.

### Trigger 3 — Elapsed time (automatic decay)
Score timestamps are checked against the decay schedule. Decayed scores are updated in the wiki during any session that touches the relevant node. No explicit trigger required.

## Calibration Session Format

Bootstrapping sessions (first assessment of a node):
1. Present the node topic and ask the user to demonstrate at each level
2. Probe with novel problems for level 3, cross-domain for level 4, gaps for level 5
3. Record component scores based on demonstrated behavior
4. Set score_date to today

Re-calibration sessions (periodic):
1. Check which nodes have decayed scores or long elapsed times
2. Probe with questions targeting the specific components that are weakest
3. Update component scores and reset score_date

Implicit calibration (ongoing):
All other sessions. Apply Triggers 1 and 2 as background process. Do not interrupt the conversation to announce score updates unless asked.

## Protocol for Code Sessions

Code sessions touching a concept node should include a brief calibration probe at close if the session involved substantive discussion of that concept. The Code session should call edit_node to update component_scores and understanding fields before session close.

## Scope

This protocol applies to all node types in the PKIS wiki. It is the authoritative specification for understanding scores. Any Claude instance reading this node before a session applies it without requiring explicit instruction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc]] — applies: Protocol governs understanding score assessment for the MCMC node
[To be populated during integration]

## Needs Canonical Source
This stub was created without a source. Suggested references:

**Already in corpus:**
[none in corpus]

**External candidates (Semantic Scholar):**
[none found]

## Session Log Convention
Session logs are persistent artifacts capturing the narrative of each working session. They serve two functions: continuity (enabling a future Claude instance or the user to resume productively) and knowledge archaeology (explaining why nodes have the structure they do).

## Node Type and Slug Convention

knowledge_type: result
also_type: ["session-log"]
slug: session-YYYY-MM-DD (e.g. session-2026-06-07)
If multiple sessions occur on one day: session-YYYY-MM-DD-2, session-YYYY-MM-DD-3

## Required Frontmatter Fields

title: "Session Log — YYYY-MM-DD"
knowledge_type: result
also_type: ["session-log"]
domain: list of domains touched
tags: ["session-log", session_type, ...domain tags]
maturity: settled (logs are fixed after the session closes)

Custom frontmatter fields (set via edit_node after commit):
- session_type: depth | quiz | design | build | review
- duration_estimate: short | medium | long

## Required Body Sections

### Summary
Two to four sentences. What was the session about and what was the primary outcome. Not a list of topics covered — a characterization of what moved.

### Key Insights
Free-form prose. The moments where something clicked, an analogy that resolved confusion, a question that reframed a problem, a connection that was not in any node before. Reference relevant nodes and sources using [[wikilink]] syntax. This section captures the reasoning path, not the conclusions — conclusions belong in the nodes themselves.

### Nodes Created
Bulleted list. IRI and one-line description for each new node created this session.

### Nodes Modified
Bulleted list. IRI and what changed (content, scores, connections).

### Calibration Updates
For each node where understanding scores changed: node IRI, old score, new score, and the behavioral evidence that warranted the change (one sentence).

### Open Questions
Numbered list. Things that came up and were not resolved. These are high-value — they are the seeds of future sessions. Include enough context that a future instance can reconstruct why the question matters.

### Deferred Items
Numbered list. Things explicitly flagged for a future session with a clear answer that was not reached. Distinct from open questions — these have a known resolution path, we just did not execute it.

### Recommended Next Session
One to three sentences. What topic, what the entry point is, what prerequisite reading would help. Written as a direct instruction to the next Claude instance.

## Edge Convention

Session logs connect to touched nodes via the `applies` predicate:
  subject: session log IRI
  target: node IRI
  predicate: applies
  note: brief description of how the session touched this node (e.g. "created", "anatomy filled", "calibrated", "generative discussion")

This makes the graph queryable: "which sessions touched node X" and "what did session Y create or modify."

## Timing

Session logs are written at the end of the session, before the context closes. They are written by Claude, reviewed briefly by the user, then pushed via Code. They are not edited after the session closes — they are historical records.