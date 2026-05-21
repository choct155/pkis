---
title: "Models in a Behavioral Theory of the Firm"
authors: "R. M. Cyert; E. A. Feigenbaum; J. G. March"
year: 1959
type: paper
domain: [organizational-theory]
tags: [behavioral-economics, bounded-rationality, satisficing, organizational-learning, computer-simulation, duopoly, oligopoly, decision-making, aspiration-levels, organizational-slack, conjectural-variations, Carnegie-school]
source_url: ""
drive_id: "1e9OppVzpe9mi7WIzbHKV7-VhcapRrnbL"
drive_path: "PKIS/sources/papers/Models in a Behavioral Theory of the Firm.pdf"
status: unread
date_added: 2026-05-20
concepts: [satisficing, aspiration-level, organizational-slack, organizational-learning, bounded-rationality, behavioral-theory-of-the-firm]
---

## Summary

This 1959 paper from Carnegie Institute of Technology (published in Behavioral Science) is a foundational contribution to the behavioral theory of the firm by Cyert, Feigenbaum, and March. It uses computer simulation — then a radical methodological choice — to model duopoly decision-making, translating the abstract propositions of the Carnegie behavioral theory of the firm into a running, testable computational model.

The paper models a duopoly in which an ex-monopolist faces a splinter competitor. Rather than assuming profit maximisation, both firms follow organisational decision procedures that incorporate: (1) aspiration-level goal-setting (organisations aim to do well enough, not best); (2) problemistic search (search for new alternatives is triggered only when current performance falls below the aspiration level); (3) organisational learning via conjectural variation updating (firms revise their beliefs about rivals' behaviour based on experience); (4) organisational slack (the gap between achievable and actual costs allows firms to absorb shocks or improve performance); and (5) re-examination phases that adjust demand and cost estimates rather than optimising over the full known space.

The model is validated against 44 time-periods of actual duopoly data from the competition between American Can Company and Continental Can Company (1913–1956). The simulation reproduces observed market-share trajectories and profit-ratio dynamics with "surprisingly good" fit. This validation exercise demonstrates that a relatively simple behavioral model with organisational decision rules can generate economically relevant, testable predictions — a demonstration explicitly directed at the then-mainstream scepticism that behavioural theorising lacks formal predictive content.

The paper differs from conventional economic theory in six key respects stated explicitly: firms specify decision procedures (not utility functions); they search for satisfactory rather than optimal alternatives; objectives evolve over time as a function of experience; profit goals depend on past experience; firms adjust forecasts via organisational learning from observations of rivals, demand, and costs; and intra-organisational factors (slack, communication structure) are incorporated rather than the firm being treated as a single decision-maker.

## Key Knowledge Objects

- [[satisficing]] (concept, high) — Simon's principle that organisations aim to find alternatives meeting aspiration-level thresholds rather than optimising; central operating rule in the model
- [[aspiration-level]] (concept, high) — the target performance level that determines whether a firm searches for new alternatives; adjusted upward after successes and downward after failures
- [[organizational-slack]] (concept, high) — the gap between the firm's actual minimum cost and its achieved cost, representing a reservoir of resources that buffers shocks and can be mobilised to improve performance under pressure
- [[organizational-learning]] (concept, high) — the process by which firms revise their perceptions of rivals' behaviour, market demand, and costs based on experience, modelled here as adaptive conjectural variation updating
- [[bounded-rationality]] (concept, high) — Herbert Simon's framework of cognitivley limited decision-making; the underlying theoretical commitment of the behavioral theory of the firm; governs all five decision procedures in the model
- [[behavioral-theory-of-the-firm]] (framework, high) — the Carnegie School research program (Cyert, March, Simon) replacing profit maximisation with a decision-process account of business behaviour incorporating bounded rationality, aspiration levels, and organisational processes
- [[conjectural-variation]] (concept, moderate — could be technique) — a firm's beliefs about how rivals will respond to its own actions; in this model updated via organisational learning rather than held constant or solved analytically
- computer-simulation-of-economic-behavior (low — technique or framework?) — the use of computer programs to model and test economic theories; used here as the methodological vehicle for the behavioral theory

## Key Extractions

1. **Six ways behavioral theory differs from conventional theory (Discussion section):** "(1) They specify decision processes … (2) [They] specify that search will be undertaken … (3) The models describe organisations in which objectives change over time as a result of experience … (4) [T]he profit goal … varies from a firm average of past successes to the firm's conjectured average … (5) The models describe organisations that adjust forecasts on the basis of experience … (6) The models incorporate intra-organisational factors."

2. **Aspiration-level mechanism (Results section):** The model incorporates "upward revision of demand … as optimism. In any event, it is to some extent a slightly less sanguine view of what is possible" when re-examination steps occur — aspirations are adjusted by experience.

3. **Organisational slack definition (Results section):** "[S]lack … is a reservoir of resources available to the organisation … All costs initially above the 'real' minimum cost are at 15% of average unit cost … subject to ±25% variation." Slack absorbs environmental shocks before objectives are revised.

4. **Validation claim (Results/Discussion):** "In general, we feel that the fit of the behavioral model to the data is rather surprisingly good, although we do not regard this fit as conclusively validating the approach." The comparison is to American Can/Continental Can profit-ratio data 1913–1956.

5. **Methodological novelty (Abstract):** "A behavioral theory is implicit in the process explored here by a computer program which businesses use to deal with the complex type of decisions [duopoly]. This model highlights our need for more empirical observations of organizational decision-making."

6. **Satisficing over maximising (Discussion):** "The models are built in a way that does not, in fact, necessarily involve maximization of objectives, and our decision rule is interpreted as: if one possible outcome satisfies our objectives, we will be evaluated on one possible outcome."

## Connection Candidates

- [[markov-decision-processes]] — contrasts-with: MDP framework assumes well-defined reward function and optimisation; behavioral theory replaces this with aspiration-level satisficing and organisational process — the two frameworks represent orthogonal theories of decision-making under uncertainty
- [[discrete-event-simulation]] — uses: the computer-simulation methodology in this paper is formally equivalent to discrete-event simulation, using time-period ticking and event-triggered state updates; this paper is historically among the earliest agent-based simulation models in social science
- [[reinforcement-learning]] (implied connection via RL framework) — contrasts-with: RL formalises learning from environmental feedback as reward maximisation; organisational learning in this model is adaptive belief updating without a reward maximisation objective — the two share the feedback-driven learning structure but differ in the optimisation commitment
- [[structural-causal-models]] — prerequisite-of: to test behavioral vs. neoclassical theory of the firm causally requires identifying exogenous variation in organisational variables; the paper's validation via historical time-series implicitly raises identification challenges that SCM methods address

## Awaiting Classification

- **computer-simulation-of-economic-behavior** — candidate types: technique or framework
  - Case for technique: it is a procedure (write a computer program, specify decision rules, run the simulation, compare output to data) that takes inputs and produces predictions
  - Case for framework: in 1959 "simulation as economic theory" was a coherent methodological framework challenging the dominant analytic/equilibrium approach, not just a tool; the paper argues for simulation as a "general method for examining many of the concepts previously discussed in more abstract terms"
  - What makes this hard: the object is simultaneously a method (technique) and a paradigmatic stance about how economic theory should be formalised (framework)
