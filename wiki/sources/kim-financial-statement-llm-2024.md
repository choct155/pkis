---
id: "pkis:source:kim-financial-statement-llm-2024"
aliases: []
title: "Financial Statement Analysis with Large Language Models"
authors: "Alex G. Kim, Maximilian Muhn, Valeri V. Nikolaev"
year: 2024
type: paper
domain: [deep-learning, forecasting]
tags: [llm, chain-of-thought, financial-analysis, earnings-prediction, fundamental-analysis, gpt4, asset-pricing, numerical-reasoning]
source_url: ""
drive_id: "1C3WUUdGTZ-T0w4c3CCip0oTRxc6Lk-MO"
drive_path: "PKIS/sources/papers/Financial Statement Analysis with Large Language Models.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[in-context-learning]]", "[[chain-of-thought-prompting]]", "[[neural-networks]]"]
---

## Summary

This paper investigates whether a general-purpose LLM (GPT-4) can perform financial statement analysis at or above the level of professional human analysts — a task traditionally considered firmly in the human domain because it requires numerical reasoning, domain knowledge, and complex judgment. The authors provide anonymized, standardized balance sheets and income statements to GPT-4 and instruct it to predict the direction of next-year earnings changes, without supplying any narrative context (no management commentary, no industry information).

Using the entire Compustat sample as a benchmark, the study finds that a simple (non-CoT) GPT-4 prompt achieves 52% accuracy — below human analysts' 53–57%. However, a Chain-of-Thought (CoT) prompt that "teaches" the model to follow analyst reasoning steps (trend identification → ratio computation → synthesis → directional judgment) achieves 60% accuracy, meaningfully outperforming the 53% analyst one-month benchmark. GPT CoT's F1-score (63.45%) also exceeds a narrowly trained state-of-the-art ANN (61.6%) trained on the same data.

To rule out training-data memorization, the authors anonymize company names and time periods, conduct out-of-sample tests on 2023 data (outside the model's training window), and show GPT does not perform anomalously well during periods the model would "know" were economically distressed (financial crisis, COVID). The authors further show that GPT's narrative insights — encoded as 768-dimensional BERT embeddings — achieve 59% standalone accuracy, confirming that the CoT narrative explains the predictive performance rather than memorized facts. Trading strategies based on GPT CoT predictions yield a Fama-French three-factor alpha exceeding 12% per year, with higher Sharpe ratios than ANN- or analyst-based strategies, especially for small-cap stocks.

## Key Knowledge Objects

- chain-of-thought-prompting (low — technique or principle?) — structured prompting that elicits step-by-step reasoning; central to this paper's result
- [[in-context-learning]] (technique, high) — zero-shot and CoT prompting of a frozen GPT-4 model to perform analyst-style reasoning without fine-tuning
- [[neural-networks]] (technique, high) — ANN trained on 59 Compustat predictors serves as the state-of-the-art ML benchmark; BERT embeddings encode GPT narratives for downstream ANN training
- llm-numerical-reasoning (low — concept or problem?) — the specific challenge of reasoning about numbers in financial contexts; the paper's central finding challenges the assumption that LLMs lack numerical competence
- financial-statement-analysis (low — technique or framework?) — the systematic procedure of analyzing balance sheets and income statements to forecast earnings; well-established domain but new to the PKIS corpus
- sharpe-ratio (low — concept or result?) — risk-adjusted performance metric used to evaluate trading strategies; widely used in finance but peripheral to core PKIS domains

## Key Extractions

1. **CoT accuracy versus analysts:** GPT-4 CoT achieves 60.31% accuracy in predicting the direction of next-year earnings, compared to 53.08% for analyst one-month-ahead consensus — a statistically and economically meaningful improvement even absent any narrative firm context.

2. **Parity with specialized ML:** GPT-4 CoT accuracy (60.31%) is on par with a narrowly trained ANN (60.45%) using 59 Compustat predictors, and its F1-score (63.45%) is higher than the ANN (61.62%), despite the LLM being a general-purpose model with no financial-specific training.

3. **Narrative insights are the mechanism:** An ANN trained exclusively on BERT-encoded GPT narrative outputs achieves 59% accuracy (F1: 65%), nearly matching the full GPT pipeline, providing direct evidence that the model's predictive ability flows through generated economic reasoning rather than memorized facts.

4. **Relative advantage in hard cases:** GPT outperforms both analysts and ANN specifically for small-cap and loss-making firms — precisely the cases where analysts struggle most. ANN trained on historical data has limited extrapolation capacity for unusual firms; GPT's general world knowledge and analogical reasoning fill the gap.

5. **LLM memory ruled out:** The paper tests multiple memorization hypotheses: anonymization (company names, years replaced with labels), out-of-sample 2023 test, temporal stability checks during crisis periods. All evidence supports the conclusion that GPT's performance is not driven by look-ahead bias.

6. **Alpha in trading:** A long-short strategy based on GPT CoT earnings-direction predictions generates a Fama-French three-factor alpha exceeding 12% per year, outperforming both ANN-based and analyst-based strategies — suggesting the LLM generates economically actionable signals.

## Connection Candidates

- [[in-context-learning]] — uses: CoT prompting is an in-context-learning technique; the paper's main experiment is a zero-shot CoT instruction that emulates financial analyst reasoning steps
- [[neural-networks]] — contrasts-with: GPT-4 CoT and ANN are compared head-to-head on the same input data; ANN has higher capacity for large-cap stable firms while GPT has advantage on small/loss-making firms via reasoning
- [[bias-variance-tradeoff]] — uses: the complementarity result between GPT and ANN is implicitly a bias-variance argument — GPT's broader prior knowledge reduces bias in unusual cases where narrow ANN training data provides poor coverage
- [[inductive-bias]] — uses: CoT prompt explicitly encodes financial-analyst inductive bias (compute ratios → synthesize trends → directional judgment) into the LLM's reasoning procedure; the experiment shows this bias transfer via prompting is highly effective
- [[forecasting]] — specializes: the paper applies LLMs to a canonical forecasting task (point-in-time earnings direction), extending the forecasting literature from econometric/ML models to general-purpose language models

## Awaiting Classification

- **chain-of-thought-prompting** — candidate types: technique or principle
  - Case for technique: it is a specific procedural intervention (structure the prompt with intermediate reasoning steps); the paper implements a precise CoT sequence following analyst workflow
  - Case for principle: "reason step by step before concluding" is a general epistemic constraint on LLM use, applicable across domains and tasks, which is more principle-like
  - What makes this hard: CoT is simultaneously a design choice (technique) and a general norm about how to elicit good LLM behavior (principle); the node `[[in-context-learning]]` already partially covers it as a technique

- **llm-numerical-reasoning** — candidate types: concept or problem
  - Case for concept: it refers to the LLM capability to process and reason about numbers, which has a definition and boundary
  - Case for problem: the paper frames it as a challenge/limitation ("numbers typically come from narrative context, lack deep numerical reasoning") that motivates the research
  - What makes this hard: the paper presents both the limitation (problem) and its resolution (concept update) — the finding redefines what LLM numerical reasoning can do

- **financial-statement-analysis** — candidate types: technique or framework
  - Case for technique: it is a procedure with defined inputs (financial statements) and outputs (earnings direction, valuation, recommendations)
  - Case for framework: it organizes a coherent system of analysis (ratio computation, trend analysis, contextual synthesis) that structures a professional practice domain
  - What makes this hard: financial statement analysis is both a procedure and an organizing paradigm for the fundamental analysis domain; the paper itself refers to it as a framework-level concept
