---
title: "Actionable Conversational Quality Indicators for Improving Task-Oriented Dialog Systems"
authors: "Michael Higgins, Dominic Widdows, Beth Ann Hockey, Akshay Hazare, Kristen Howell, Gwen Christian, Sujit Mathi, Chris Brew, Andrew Maurer, George Bonev, Matthew Dunn, Joseph Bradley"
year: 2024
type: paper
domain: [agentic-ai, knowledge-representation]
tags: [task-oriented-dialog, conversational-ai, dialog-quality, nlp, nlu, chatbot, evaluation, annotation, sentence-bert]
source_url: "https://doi.org/10.1017/S1351324923000372"
drive_id: "1hY4JQnPY9sl_Xmujdzj4yzVRm2nmmZzt"
drive_path: "PKIS/sources/papers/Actionable Conversational Quality Indicators for Improving Task-Oriented Dialog Systems - Higgins, Widdows, Hockey et al.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[acqi-taxonomy]]", "[[interaction-quality-score]]", "[[task-oriented-dialog-systems]]", "[[dialog-evaluation-framework]]"]
---

## Summary

Published in Natural Language Engineering (2024), this paper by Higgins, Widdows, Hockey et al. (LivePerson / IonQ) addresses a practical problem in commercial dialog system deployment: bot-builders — typically customer service specialists rather than ML engineers — have no principled method for diagnosing why a chatbot is failing and what specific actions to take to fix it. Existing metrics like automation/containment rate, task success, or the Interaction Quality (IQ) score of Schmitt et al. (2011) can identify *where* a conversation degrades but not *why* or *how to fix it*.

The paper's central contribution is the **Actionable Conversational Quality Indicator (ACQI) taxonomy**: a set of 8 architecture-independent dialog quality indicators (Does Not Understand, Input Rejected, Ignored Consumer, Restart, Bad Transfer, Unable to Resolve, Ask for Information, Provide Assistance, Ask for Confirmation) each paired with an explicit set of recommended bot-builder actions. ACQIs are designed to be (a) actionable — each maps to a defined remediation step; (b) understandable to non-engineers; (c) architecture-independent, relying only on conversation text; and (d) aggregable for statistical analysis.

The paper demonstrates ACQIs on two datasets: the public LEGOv2 corpus (541 transcribed phone conversations, travel domain) and 520 LivePerson commercial text-based customer service conversations across 4 bot systems (retail, travel, tech, food). Key empirical findings: (1) ACQIs are not universally negative — "Ask for Confirmation" is positive when user input is ambiguous, negative when the user was clear; context and repetition matter. (2) Combining ACQI with IQ scores produces richer diagnostics than either alone. (3) A logistic regression classifier using Sentence-BERT embeddings of the two most recent turns achieves 79% weighted F1 for ACQI prediction, and analysis shows that a perfect ACQI classifier could reduce the range of improvement actions a bot-builder must consider by 81%.

Inter-annotator agreement (Cohen's kappa = 0.68, "substantial" by Landis & Koch) validates the taxonomy's clarity. The paper also presents ablations showing that cumulative ACQI features combined with text features (LR:ANNOTATED-ACQI+TEXT) outperform text-only across all bot systems.

## Key Knowledge Objects

- [[acqi-taxonomy]] (framework, high) — the 8-category Actionable Conversational Quality Indicator taxonomy with paired remediation actions
- [[interaction-quality-score]] (technique, high) — the IQ running quality score of Schmitt et al. (2011), a turn-by-turn expert annotation method on a 5-point scale that contributes to a cumulative conversational quality assessment
- [[task-oriented-dialog-systems]] (concept, high) — dialog systems with a rigid structure and limited scope designed to resolve specific consumer tasks, in contrast to open-domain conversational agents and QA systems
- [[dialog-evaluation-framework]] (framework, moderate — could be technique) — the broader class of methods for evaluating task-oriented dialog system performance, including PARADISE, IQ, containment rate, and ACQI

## Key Extractions

1. **ACQI taxonomy purpose**: "ACQIs highlight moments in chatbot conversations that impact customer experience... each conversational quality indicator has associated recommended actions, but do not require explicit knowledge of the dialog system architecture."

2. **Context-dependence of quality**: "ACQIs are context-dependent and combine (with context and themselves) nonlinearly." A single "Ask for Confirmation" normally increases IQ; asking for confirmation more than 6 times can be "actively harmful." "Does Not Understand" is usually negative but can be reasonable if the consumer types out-of-scope content.

3. **Prediction performance**: Logistic regression on Sentence-BERT (768-dim, 2-turn window, 4×768 = 3072-dim input) achieves 79% weighted average F1 for ACQI classification. Combined annotated-ACQI+text features achieve Spearman ρ up to 0.84 for IQ prediction on individual bot systems.

4. **Actionable reduction claim**: "If such a model worked perfectly, the range of potential improvement actions a bot-builder must consider at each turn could be reduced by an average of 81%." The ACQI taxonomy guides to 23 of 28 LivePerson and 25 of 31 LEGOv2 possible actions.

5. **Bot-dependence of ACQI distributions**: The ACQI distributions differ markedly across bot systems. For most bots "Does Not Understand" dominates score-decreasing events (65.5% for LEGOv2), but for Junior Sales Assistant, "Provides Assistance" accounts for 54.2% of score-decreasing events — indicating the bot is making too many improper transfers or inappropriate suggestions.

6. **Relationship to IQ score**: The paper modifies Schmitt & Ultes (2015) IQ annotation by removing point-change restrictions (allowing larger swings), changing the scale from "dissatisfaction" (5=satisfactory down to 1=extremely unsatisfactory) to a richer scale (5=good, 4=satisfactory, 3=bad, 2=very bad, 1=terrible), and removing the requirement that each conversation start at "satisfactory."

## Connection Candidates

- [[task-driven-human-ai-framework]] — uses: the ACQI framework operationalizes the "when to collaborate, when to challenge" logic at the turn level in commercial dialog systems; Widdows (co-author) overlaps domain with Varshney (co-author of Paper 2)
- [[semantic-parsing]] — uses: NLU taxonomy and NLU training data update are among the recommended ACQI remediation actions; the IQ+ACQI framework sits on top of an NLU layer
- [[in-context-learning]] — contrasts-with: ACQI is a training-data-improvement approach rather than a prompting approach; the architectural independence of ACQI applies equally to LLM-based dialog systems
- [[human-in-the-loop]] — uses: bot-builders are the "human in the loop" for dialog system improvement; ACQI is a tool for making HITL correction more targeted and efficient

## Awaiting Classification

- **interaction quality (IQ) score** — candidate types: technique or result
  - Case for technique: IQ is a concrete annotation procedure with defined inputs (conversation transcript, annotator) and outputs (per-turn running score, 5-point scale)
  - Case for result: the IQ method has been validated as correlating with user satisfaction, making it more of an established measurement instrument than a procedure
  - What makes this hard: the source treats IQ as both a method to apply and a validated instrument; the boundary between "technique" and "validated measurement tool" is not sharp
