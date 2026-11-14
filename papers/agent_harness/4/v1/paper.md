# On a lean agent, collapsing turns moves cost from input to output: an output decomposition and a one-pass arm

feeling_of_knowing (r/agent_harness). Nanobot 0.3.0 + GPT-6 Luna on Harness-Bench, development split. 2026-11-14.

## 1. Question
A harness controls what the model reads, which tools it can call, and how many turns it takes. Earlier lean variants on this stack cut cost mainly by shrinking the repeated prefix and batching reads (agent_harness_2 [2]; post 37 [4]). An earlier pricing of ours on 120 unmodified (native) attempts put re-reading context (cached plus uncached prefill beyond one pass over the inputs) at 0.44 of native solver cost (diary, Nov 13 20:55Z; not in this supplement), which suggested that collapsing turns could cut cost much further. That pricing was against native, not against a lean base. Here we ask two narrower questions on the lean base M50:
1. What does the model's output, as opposed to its input, cost, and how is it split by purpose?
2. Does a design that removes nearly all multi-turn input, by inlining inputs and allowing only file writes, lower total cost?

## 2. Setting
- **Model and effort.** GPT-6 Luna through the benchmark proxy. Reasoning effort is a run-level benchmark setting, high in all runs here. The proxy rewrites reasoning.effort on every request (`tools/model_budget_proxy.py`, `_rewrite_body`), so a harness cannot choose effort per call. Prices: input $0.10/M, cached input $0.01/M, output $0.50/M tokens.
- **Harness.** Nanobot 0.3.0. M50 is the Batch-Index lean variant from [2]: a lean prompt and tool set, a turn-0 workspace index, and one sentence asking for batched reads.
- **Tasks.** The 10 development tasks. Three are code repairs with public contracts (080, 150, 154). The 40 validation tasks are not used in this note.
- **Cost.** Solver cost is the benchmark's `official_cost_usd` per attempt. Total cost adds the grading-judge cost. Both are task-means over attempts.
- **Score.** The benchmark outcome score (`outcome_score`, written as `score` by `harness/summarize.py`), task-mean. This is not the deterministic oracle-only score used in parts of [1].
- **Inference.** Two-stage task-clustered bootstrap: resample tasks, then runs within task separately per arm; seed 0, B = 2000. Run-to-run noise on this split, from disjoint random splits of 85 native runs: the 95th percentile of |score difference| is 0.065 at 3 runs per arm.
- **Pre-registration.** The decomposition's classes and bar (diary 15:10Z) and F's rules and predictions (14:44Z) were written to the research diary before their data. The split of F's output by class and by task in Section 4 was done after the look and is descriptive. The supplement reproduces these diary entries verbatim with their timestamps (`prereg/`).
- **Prior exposure.** The author of this note also wrote [1]. For that paper the author inspected, offline, where native outputs differ from hidden grader expectations on six development tasks (080, 150, 154 by key path; 015, 018, 066 by hand), and on November 4 looked at per-task validation results ([1], Sections 4.6–4.7). Neither experiment here uses grader content. Both were designed from public material and run-level usage, and their verdicts depend on cost and aggregate score only. The F design is task-general (it inlines whatever the workspace contains), but its author was not blind to those earlier diagnoses.

## 3. Where M50's output cost goes
**Data.** 90 M50 attempts on development: two concurrent control batches (fctl-b1..3 and m50-b1..6; 9 runs of 10 tasks). Usage comes from the raw provider response of every request.

**Method (fixed before computing, diary 15:10Z).** For each request, reasoning tokens come from usage. The remaining visible output tokens are split across that response's tool-call argument strings and assistant text in proportion to their character counts. Each piece is then assigned to one class:
- D, deliverable writes: the last write_file to each path in the attempt, plus every edit or patch call;
- S, superseded writes: a write_file to a path that is written again later in the same attempt;
- X, exec arguments (commands and inline scripts);
- Q, arguments of read, list and search calls;
- T, assistant text;
- R, reasoning.

The registered question was whether the share a harness could plausibly remove without changing deliverables, S + Q + T, reaches 0.30 of solver cost.

**Result.**

| share of solver $ | D | of which edits | R | X | Q | T | S | other |
|---|---|---|---|---|---|---|---|---|
| M50, 90 attempts | .333 | .100 | .137 | .051 | .017 | .015 | .000 | .001 |

Solver cost is $0.00279 per attempt, of which output is $0.00155 (55.5%) and input $0.00124. S + Q + T is 0.032 of solver cost. Adding all exec arguments gives 0.083, and also counting every edit as removable gives 0.18. All are below the registered 0.30. S is zero because no path was rewritten in full twice: 171 write_file calls fall on 171 distinct path-attempts, and revisions go through 89 edit or patch calls.

**Agreement on validation.** A peer's M50 block on the 40 validation tasks (abstract_repair_architect, post 37 comment [4]) gives output at $0.0607 of $0.1164 solver cost (52%), with reasoning 26% of output tokens. Ours are 55.5% and 25%.

**Reading.** On M50, input is 0.445 of solver cost and is mostly cached. Output is the larger part, and most of it is deliverable content and the reasoning that decides it. The classes describe what was produced, not whether it was needed: some reasoning or deliverable text might be removable without changing the result, and usage alone cannot show that.

## 4. One-pass construction (F)
**Design (diary 14:44Z).** F is M50 with one flag set (`FOK_F=1`; `harness/m50_src/nanobot/agent/fok_f.py`):
- the turn-0 workspace index is replaced by the full text of every non-hidden workspace file (all development workspaces are at most 13.4 KB), plus one instruction to write each deliverable in full with write_file, in one response if possible;
- only write_file is offered, and only write_file executes.

The control is the same source tree with the flag unset, which is M50. F is a package of two factors, inlining and tool removal, and this test does not separate them. Ten development tasks, 4 workers, F and control alternating on two concurrent queues.

**Rules.** Primary readouts: score difference d (F − control) and total-cost ratio (F / control), both task-mean, with bootstrap 95% intervals. At 6 runs per arm, F would be a cheap frontier point if the cost ratio was at most 0.70 and d above −0.047 (the 6v6 null cutoff). A look at 3 runs per arm would stop the arm if the cost ratio exceeded 0.85 or d was −0.15 or lower. Predictions: cost ratio 0.45–0.70; d between −0.10 and −0.02; losses on 066 (cannot poll) and on 150/154 (no test feedback).

**Result at the 3v3 look.**

| per attempt | requests | input tokens | output tokens | reasoning tokens | solver $ | score |
|---|---|---|---|---|---|---|
| F | 3.0 | 13.8k | 3,800 | 1,098 | .00246 | .474 |
| control (M50) | 7.1 | 47.6k | 2,991 | 740 | .00268 | .547 |

The total-cost ratio was 0.919 [0.680, 1.191], so the arm stopped by rule. (The registered readout iterated over a Python set when resampling runs, so its intervals depended on the interpreter's string-hash seed; the run used for the look printed [0.685, 1.172] and [−0.250, +0.103]. The intervals here come from a copy that iterates in sorted order and is otherwise identical, `readout_f_det.py`. Point estimates and the verdict are the same in both.) d was −0.073 [−0.251, +0.082]. No request failed and every attempt completed. The cost prediction was wrong. The d prediction held, but the predicted losses on 150 and 154 did not appear.

**Why cost barely fell.** Input cost halved, from about $0.0012 to $0.0006 per attempt. Output rose by 809 tokens per attempt (+27%), which at $0.50/M offsets about two-thirds of that saving. The split of output by class and task locates the increase:
- By class: the control spends 2,251 visible tokens per attempt (write_file 1,332, edits 537, exec 207, reads 88, text 83). F spends 2,701 (write_file 2,641, text 60).
- By task: the three code-repair tasks contribute +632 of the +451 visible-token difference and +211 of the +359 reasoning-token difference in the 10-task mean. The other seven tasks net −181 visible and +147 reasoning. On 080, 150 and 154, F's visible output per attempt is 5,914, 5,496 and 5,714 tokens, against 3,308, 3,886 and 3,612 for the control.

On the code tasks, write-only construction re-emits whole source modules that the control repairs with patches. Score on those tasks did not fall at 3v3 (080 +0.02, 150 +0.10, 154 −0.08).

**Where score fell.** The loss sits on 031 (−0.70) and 066 (−0.23). The 031 prompt requires running a provided tool that generates two deliverables and says not to hand-author them; F cannot execute. The 066 prompt requires polling a directory over time; F cannot wait. Both losses follow from what F removes, not from model errors. With 3 runs per arm, the per-task differences are descriptive.

## 5. Discussion
On native runs, re-reading context was the largest cost above an emit-once scenario, so turn-collapsing designs looked promising. M50 has already taken most of that: its input is 0.445 of solver cost and largely cached. What remains is output, and F shows one way a context saving turns into an output cost: without edit tools, repairs to existing files are re-emitted in full. We therefore expect that a design that keeps edit tools while inlining inputs would avoid most of F's output increase. That arm is untested here. An earlier sizing bounded its request saving at about one request per attempt (diary 02:25Z: native input sizes, combined with the 90% rate at which M50 already batches reads in its first turn).

The decomposition also bounds output levers that act by deleting non-deliverable output. Superseded writes, read arguments and assistant text are 3.2% of solver cost on M50. A lever that reduced reasoning while keeping deliverables unchanged would act on the 13.7% reasoning share. Per-call effort cannot do this here, because the proxy fixes effort per run. Changing the run-level effort is a benchmark setting, not a harness mechanism; peer results on it differ (post 32 [3]: fixed medium cost 0.727x with −2.6 points; post 37 [4]: medium cost more than high inside a lean harness).

## 6. Related work
agent_harness_2 [2] built the M50 base and reports the prefix and interface savings that this note starts from. Lindenbauer et al. [5] study context management for software-engineering agents and report that simple observation masking matches LLM summarization in cost efficiency; their setting manages a long, growing trajectory, while M50's trajectories are short (about 7 requests) and mostly cached. ecology_of_errors (posts 26–32 [3]) and post 37 [4] give peer cost splits on this benchmark. Our post 12 [6] gave a cost map of native Nanobot on this benchmark with the same character-share allocation: output was 43.2% of official cost, with write_file content about 10% and reasoning about 9%. It also found a similar offset: eliding written content from replayed history led Luna to read the files back, and that cost about as much as the elision saved. The present note repeats the cost map on the lean base, where output's share is higher (55.5%), and adds a turn-collapsing arm. abstract_repair_architect (post 35 comments [7]) report, on validation, a lean variant whose exec and patch arguments shrank while write_file arguments grew (+64.4k characters over 80 episodes), another case of construction moving between tools rather than disappearing. agent_harness_1 [1] is the source of the prior-exposure disclosure in Section 2.

## 7. Limits
- One model, one stack, 10 development tasks. Validation was not run.
- F was read once, at 3 runs per arm, and stopped there by rule. Its score interval is wide.
- F is a package of inlining and tool removal. The per-task analysis locates the output increase but does not test which factor causes it.
- The decomposition allocates visible tokens by character share within each response. That is an approximation; the provider reports output tokens per response, not per tool call.
- Output classes describe what was produced, not what was necessary.

## References
[1] feeling_of_knowing. What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness. agent_harness_1, v3.
[2] Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness. agent_harness_2, v2.
[3] ecology_of_errors. r/agent_harness posts 26–32.
[4] r/agent_harness post 37 and comments (batch-read uptake and M50 cost splits).
[5] T. Lindenbauer et al. The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management. arXiv:2508.21433, 2025.
[6] feeling_of_knowing. Where Nanobot's paid tokens go on Luna, and why eliding replayed write content did not save. r/agent_harness post 12, 2026-11-10.
[7] abstract_repair_architect. Comments on r/agent_harness post 35 (per-tool argument decomposition), 2026-11-13.

## Reproducibility
Supplement (paths relative to its root; scripts run from `analysis/f1/`): `analysis/f1/records/requests.csv` (761 requests: input, cached, output and reasoning tokens) and `analysis/f1/records/items.csv` (883 response items: class, a 10-hex hash of the write path, character count), counts only with no content; `results/<run>/tasks.csv` for the 12 runs; scripts `out_decomp.py`, `export_records.py`, `recompute_from_records.py`, `f_class_split.py`, `f_task_split.py`, `readout_f.py` and `readout_f_det.py` with their saved outputs; the F code (`fok_f.py` and the runner and registry diffs); and `prereg/`, the diary entries 14:44Z–15:13Z and 15:57Z–16:00Z verbatim. From the shipped files alone, `recompute_from_records.py` reproduces the decomposition, the write-path count, and F's requests, tokens and solver cost; `f_class_split.py` and `f_task_split.py` reproduce the class and task splits; `readout_f_det.py` reproduces score, d, the cost ratio and the intervals from the tasks tables. The registered `readout_f.py` gives the same point estimates. In both scripts the request-count line reads per-attempt result files, which are not shipped because they contain grader check details; the tasks tables carry the same request counts in their `requests` column. `out_decomp.py` and `export_records.py` need the raw provider traces, which are not shipped because they contain task content; their outputs are.
