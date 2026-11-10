# What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness

## 1. Problem and contribution

Adding a verification step is the most common way to make an LLM agent more reliable. Typical forms are a self-review before stopping, a fresh-context reviewer, or a checker that writes tests. This paper asks when such a step pays for itself in the r/agent_harness setting. The setting is GPT-6 Luna (`gpt-6-luna`, high reasoning effort) running in the Nanobot 0.3.0 harness on Harness-Bench [1], with score and official-price cost reported together, as the Holistic Agent Leaderboard also does [2].

A verifier that uses the same model as the producer can only help if it knows something the producer does not. The verifier designs studied here differ in what they are allowed to see:

- the producer's own context;
- a fresh view of the task and the work;
- the task without the work ("blind");
- the ability to execute checks;
- the ability to run the producer's code.

Each design gives the verifier a different information channel. I built a single controller that implements these designs at the agent's first stopping point. The first study (November 4) measured eight designs on the 10 development tasks with two or three independent runs per arm. A second study (November 9–10) added three designs that separate what the verifier sends back from the act of continuing: computed observations without verdicts, the same observations delivered before the work, and an ordinary continuation in which the producer re-derives the facts itself. It also added forced interpretation diversity and fresh ordinary runs on the current runtime.

The contributions are as follows.

1. **A paired-checkpoint measurement.** The controller snapshots the workspace at the agent's first stop, before any verifier acts. It then regrades that snapshot offline with the benchmark's deterministic oracle. Each attempt becomes a before/after pair. The difference is the realized change relative to stopping at the checkpoint. It is not credited to any one ingredient of the verifier, because an ordinary continuation could also change the work; Section 4.8 measures that continuation directly. The pairing matters because run-to-run variation is large. The standard deviation across seven no-intervention runs is 0.041 per 10-task run. In one arm, the pre-intervention states already scored 0.040 above the no-intervention mean before the verifier did anything (Section 4.2).
2. **A small positive effect that the data do not establish.**
   - No verifier design shows a score gain over the no-intervention pool that its confidence interval supports. Arms that send feedback cost 1.3–1.9 times the baseline, and monitors without feedback cost 2.6 times. The higher-scoring arms are not dominated by the baseline on score and cost, but their leads are within what selection among nine arms produces by chance (Section 4.1).
   - The largest consistent paired effect comes from blind executable checks that forward only failing checks: +0.022 (95% CI −0.004 to +0.060) over six development runs, and +0.021 (−0.002 to +0.047) pooled with validation over 138 attempts on 49 tasks, 13 improved and 5 worsened. Without four validation pairs whose checkpoints cannot be verified, the same all-six-development-runs-plus-validation pool gives +0.022 (−0.002 to +0.048) over 134 attempts (Sections 3.3 and 4.7). It costs 70–85% more than the baseline.
   - An ordinary continuation that re-derives the facts itself changed a deliverable in 1 of 30 attempts and moved no graded case. Raw computed observations from a blind analyst led to edits in 9 of 30 attempts; the two that moved a graded case both lost points (paired −0.015).
3. **Where the monitors' signal is.** Failure counts correlate with task difficulty (task-level Spearman up to +0.56). Within a task, the counts carry little ranking information in this sample: 34 concordant vs 30 discordant pairs for blind executable checks, and 24 vs 30 for sighted executable checks. This weak aggregate concordance does not show that an individual piece of feedback cannot guide a repair; the paired effects in contribution 2 show that some do.
4. **A description of the headroom in these attempts.** It is a description of observed support, not a bound on what a verifier could achieve.
   - Of the 0.45 mean-score loss, 0.25 is on graded cases that none of 26–28 attempts passed. With zero passes in 26 attempts, a true pass rate as high as about 0.11 per attempt is still consistent at the one-sided 95% level, if attempts are independent draws with a common pass rate. In my offline classification of these 10 cases, six differ from the oracle in representations the task text does not fix (reason tokens, record keys, label vocabularies), three are mixed, and one is partly fixed by the text. Key paths locate these differences; they do not say how much score each costs (Section 4.6, Table A3).
   - The remaining 0.20 is on cases that some attempts pass. An oracle choosing the best of seven attempts would recover 0.135 of it; oracle-free consensus over three recovers 0.015 at three times the cost.
   - Ordinary attempts differ on few graded cases. Across ten no-intervention runs, 16 of the 50 weighted cases are passed by every attempt, 16 by none, and 18 vary (diagnostic labels). Because so few cases vary, the cases passed by either of two attempts exceed the better attempt's score by only 0.006–0.008, at or below what within-attempt independence of cases would give (Section 4.10). In an idealized calculation over these labels, which assumes no interaction between cases, merging the realized differences of two constructions has little to add over selecting the better one, unless the repair creates work that neither construction contains.
5. **Two failure mechanisms.**
   - *Detection without relevance:* after a behavioral probe's feedback, rechecks recorded 11 fewer failing checks (19 of 30), while no graded case changed.
   - *Herding on a same-model briefing:* a pre-work briefing raised the right interpretive question on a task the unbriefed producer solves 22 of 24 times. All 24 unbriefed attempts took one reading of it. Both briefed attempts took the other and failed, one after the briefing favoured it and one after the briefing left it open. This is an association in a two-attempt case study; herding is the hypothesis, not a shown cause. Assigning attempts to extracted readings of the task was followed in 58 of 59 judged cases. The three assigned runs scored 0.40–0.47, against 0.593 for three fresh ordinary runs, and the run assigned the default readings scored 0.469 (Section 4.9).

The practical conclusion is that verification should be budgeted by the information it adds. In this setting, the best same-model review design adds about two points at 1.7 times the cost, and that gain is not distinguishable from zero with 138 paired attempts.

## 2. Related work and distinction

**Intrinsic self-correction.** Huang et al. [3] show that LLMs often cannot correct their own reasoning without external feedback. Kamoi et al. [4] survey the literature and argue that reported gains usually depend on external signals or oracle stopping. Stechly et al. [5] find that self-verification in planning and reasoning tasks degrades with false positives and negatives, while a sound external verifier helps. Panickssery et al. [6] show that LLM evaluators recognize and favor their own outputs. Most of their evidence comes from reasoning, planning, question-answering and summarization tasks without a multi-step tool loop. Here the setting is multi-file, tool-using agent tasks with structured deliverables. The question is not only whether self-correction works, but which information channel a verifier needs and what it costs.

**Feedback and critique loops.** Self-Refine [7] and Reflexion [8] iterate generate–critique–revise with the same model. Multiagent debate [9] has several instances of one model critique each other's answers over rounds. CRITIC [10] adds tool-based verification. Chain-of-Verification [11] factors verification into independent questions answered without seeing the draft; that idea is close to the blind arms here. AgentCoder [12] has a separate test-designer agent write tests without seeing the code. CodeT [13] and AlphaCodium [14] use generated tests to select or repair code. My blind executable and behavioral-probe arms are agent-harness versions of these designs. The difference in this paper is the measurement. Each design is evaluated against a paired pre-intervention checkpoint, with the same model, tasks and accounting, and detection validity is split into between-task and within-task components.

**Sampling and selection.** Self-consistency [15] and minimum-Bayes-risk style selection pick the consensus among samples. SelfCheckGPT [16] uses disagreement among samples to flag hallucinations. Brown et al. [17] document the gap between coverage (some sample is right) and selection (choosing it). My consensus and best-of-seven numbers reproduce that gap on agent deliverables. Trained verifiers [18] can close part of the gap in math, but they are outside the rules here, since all inference must use Luna.

**Clarification before acting.** ClarifyGPT [19] asks clarifying questions when requirements are ambiguous. The pre-work briefing arm is a non-interactive analogue in which the same model plays the colleague. The result here (Section 4.5) shows a cost of that design: a same-model answer to the clarifying question is not independent evidence.

**Execution feedback for repair.** Self-Debugging [20] feeds execution results and the model's own explanation back for code repair. LDB [21] goes further. It splits the program into basic blocks, gives the model the intermediate runtime values of each block, and has the model judge each block correct or incorrect with an explanation. Olausson et al. [22] find that self-repair often does not beat drawing more samples at the same budget, and that its gains are limited by feedback quality: feedback from a stronger model or a human improves repair. RARR [23] retrieves evidence and revises a draft where the draft disagrees with it. The observation arm in Section 4.8 takes only the first half of that design to general deliverables. A blind analyst's program prints computed facts from the inputs and the current work, with no verdict attached, and the producer does the judging. In this setting it did not help, and filtered verdicts did slightly better.

**Other r/agent_harness work on the same benchmark.** ecology_of_errors reports several multi-construction policies on the Harness-Bench development split with Luna. Selective reconstruction (a fresh second builder plus reconciliation) scored 56.0% at \$0.154 per ten attempts, against 59.3% at \$0.080 for ordinary direct revision [24]. Static synthesis of two constructions pooled 58.75% over twenty valid grades at about \$0.13 per ten, against 61.5% for direct revision at about \$0.08 [25]. A live-consultation configuration scored 62.5% at \$0.135 in one unreplicated block [26]. These results agree with the pair ceilings in Section 4.10: on this split, a second construction gives a policy little to combine.

**Coincident failure in redundant systems.** Multiversion software faced the same question decades ago. Eckhardt and Lee [27] showed that independently developed versions still fail together when inputs vary in difficulty, and Knight and Leveson [28] measured far more coincident failures than independence predicts. Littlewood and Miller [29] showed that forcing diversity of method can change the difficulty profile and lower coincident failure. I use their model and a classical scaling statistic [30, 31] to describe how much two ordinary attempts differ on graded cases (Section 4.10).

## 3. Setup and methods

### 3.1 Benchmark, model and accounting

- **Tasks:** the 10 Harness-Bench development tasks. They span IT runbooks, email-thread state, citation audits, table joins, accessibility repair, privacy request triage, asynchronous update windows, multipart-upload recovery, WebAuthn counter logic and online database migrations.
- **Grading:** each task is graded by weighted cases, with optional safety gates.
- **Model:** all producer and verifier calls use GPT-6 Luna through the benchmark's accounting proxy, with reasoning effort `high`.
- **Harness:** the baseline is the unmodified Nanobot 0.3.0 starter harness.
- **Cost:** official prices are \$0.10/M uncached input tokens, \$0.01/M cached input tokens and \$0.50/M output tokens. Every request, including verifier calls, is counted.
- **Baseline profile:** the baseline costs \$0.048 per 10 tasks (104 requests, 44k output tokens). Its input cache hit rate is 87%. Output accounts for about 45% of cost, and reasoning tokens are only about 20% of output.

### 3.2 Verifier arms

All arms share one controller inserted at the point where Nanobot would accept the agent's final answer, on the main agent only. When the agent first stops, the controller does three things:

1. It snapshots the workspace.
2. It gives the verifier the material that its arm allows (Table A).
3. If the verifier reports problems, it feeds them back as a user message and lets the agent continue for one more round.

Verifier calls use separate contexts. Every verifier receives the task text and a pristine copy of the input files, captured before the agent started. Executable checks run in a scratch copy of the workspace with no network and a timeout.

**Table A. Verifier arms and what each verifier sees.**

| Arm | Sees the work? | Output | Control action |
|---|---|---|---|
| Baseline | — | — | none |
| Self-review | own context | — | an appended instruction to review against the task and fix defects |
| Fresh sighted review | yes | prose defect list | feedback round if defects are found |
| Blind prose review | no (writes expectations), then a comparator checks them against the work | prose expectations | feedback on violated expectations |
| Blind executable checks | no | Python checks over files, executed | feedback on failing checks |
| Sighted executable checks | yes | Python checks over files, executed | feedback on failing checks |
| Behavioral probe | yes, including code | clause-grounded counterexample checks that import and call the producer's code, executed | feedback on failing checks, then a logged recheck |
| Pre-work briefing | before work: task and inputs only | ≤500-word briefing on obligations, interpretation forks and checks | injected before the agent's second model call |
| Monitors only | all four monitors (sighted, blind, both executable) | logged, never shown | none |
| *Second study (Nov 9–10)* | | | |
| Observations at stop | no: a blind analyst writes a program at the start from the task and inputs; the program reads the current work when it runs | printed facts computed from the files (records with locators, joins, unmatched references, conflicts, counts, outputs of provided code), no verdicts | whole printout forwarded; feedback round |
| Observations early | before work: task and inputs only | the same program, run on the pristine inputs | printout injected before the agent's second model call; no stop-point round |
| Ordinary re-derivation | own context | — | appended instruction to write and run a program that re-derives the key facts from the inputs, compare them with the work, and fix genuine defects |
| Blind executable checks, second set | as blind executable checks | as blind executable checks | as blind executable checks; three new runs on the current runtime |
| Assigned readings ($K = 3$) | before work: task and inputs only | a list of interpretation forks; attempt $j$ gets a distinct combination of readings on the first two forks | readings injected before the agent's second model call as working assumptions; no stop-point round |

The prompts are in Appendix B. They are task-agnostic and identical across tasks. I wrote the briefing prompt's list of typical interpretation forks after inspecting development-task transcripts, so that arm may carry development-specific knowledge. It still underperformed (Section 4.5).

### 3.3 Paired checkpoints

The arms with checkpoints are blind executable (both sets), sighted executable, behavioral probe, monitors only, observations at stop, and ordinary re-derivation. For each attempt in these arms, I score two states with the benchmark's deterministic outcome oracle:

- **pre:** the workspace at the first stop, before any feedback;
- **final:** the workspace at the end.

The paired difference is the realized change relative to stopping at the checkpoint. It includes everything that happened after the stop: the feedback, the continued producer round, and the producer's own second look. It does not by itself credit a particular verifier ingredient. The ordinary re-derivation arm supplies the continuation-only comparison: the producer continues with the same repair rules and an instruction to compute, but receives nothing from an examiner.

Two scores are kept apart throughout. The **official score** is the benchmark's score of the final state and can include a bounded semantic-judge fallback. The **diagnostic score** is the deterministic oracle alone, applied offline to both states. On the development split the fallback applies on two tasks, and official scores exceed diagnostic scores by 0.020–0.045 per run, so paired effects use diagnostic scores for both states, and every table says which score it reports. Grader output is used only in this offline analysis and never reaches an agent.

Each state is scored with its own workspace-mutation report, computed against the initial workspace (`paired_regrade_state.py`). The initial manifest is not saved, so the script reconstructs it from the final state and its report: the final files minus those the report lists as created, plus those it lists as deleted. Retained files that the final state left unchanged keep their exact hashes. For files the final state modified or deleted, the initial content is unknown, so the script uses the final content or a placeholder. The checkpoint's safety flag is therefore exact for retained, unchanged paths. For the others it shows only whether the contract allows a change there. Specified scaffold and cache/venv paths are excluded, and state outside the workspace is not covered. The first version of this paper reused the final state's report for the checkpoint. Recomputing the report per state changed no score among 375 checkpoints, and regrading the same saved copies twice gives identical scores. That shows only that the offline grade of a saved copy is repeatable. It does not show that the copy reproduces the live state, because a copy holds only what was saved, and some validation tasks depend on state outside the workspace. On two hook-backed validation tasks (052 and 271), the checkpoint copies lack the grading hook's trusted state file, and these four checkpoints are the only ones the per-state report marks unsafe. Their four pairs therefore cannot be verified. I keep them in the main estimates and give the estimate without them next to each one (`paired_exclusion.py`). Where an attempt received no feedback, its final state is its checkpoint state, so its paired difference is set to zero.

### 3.4 Detection on identical states

In the monitors-only arm, all four monitors examine the same final state, and nothing is fed back. This makes detection directly comparable across monitors. I report three measures:

- **AUROC:** imperfect vs full-credit attempts.
- **Task-level Spearman correlation:** between a task's mean monitor count and its mean score.
- **Within-task concordance:** for every pair of attempts on the same task with different scores, whether the monitor flags the lower-scoring attempt more. Ties in monitor count are excluded.

Pooled concordance also uses the in-run verdicts from the executable arms. Those verdicts are made on the pre-intervention state and labelled with that state's offline score.

### 3.5 Statistics

- **Arm differences:** compared with the pool of seven no-intervention runs (three baseline runs, three monitors-only runs and one older monitors-only run). The CIs come from a task-clustered bootstrap that resamples tasks and then attempts within each task (10,000 replicates).
- **Paired effects:** bootstrapped the same way over attempts.
- **Second study:** arms are compared with three fresh baseline runs on the same runtime (November 9–10), not with the historical pool. The decision rule for the observation arm was written down before any of its results: a useful gain needed a paired effect of at least +0.04, a lead of at least +0.03 over ordinary re-derivation, and at most 1.4 times baseline cost; the arm would be excluded if the upper end of its paired CI was below +0.02; anything else was inconclusive.
- **Exclusions:** one fresh-sighted run is excluded because two tasks ended in infrastructure errors. One briefing run had a semantic-judge error on one task; for that task I use the deterministic score.

## 4. Results

### 4.1 No verifier arm shows a reliable score gain

**Table 1. Development split, official scores (3 runs per arm unless noted).** Cost is in USD per 10 tasks.

| Arm | Runs | Mean score | Run SD | Δ vs no-intervention pool [95% CI] | Cost | Output tokens |
|---|---|---|---|---|---|---|
| Baseline | 3 | 0.553 | 0.040 | +0.019 [−0.030, +0.077] | 0.048 | 44k |
| Self-review | 3 | 0.569 | 0.012 | +0.035 [−0.025, +0.100] | 0.071 | 64k |
| Fresh sighted review | 2 | 0.559 | 0.037 | +0.026 [−0.032, +0.096] | 0.068 | 64k |
| Blind prose review | 3 | 0.582 | 0.045 | +0.049 [−0.009, +0.112] | 0.090 | 95k |
| Blind executable checks | 3 | 0.588 | 0.026 | +0.055 [−0.029, +0.158] | 0.088 | 98k |
| Sighted executable checks | 3 | 0.550 | 0.060 | +0.017 [−0.088, +0.117] | 0.086 | 92k |
| Behavioral probe | 3 | 0.550 | 0.016 | +0.017 [−0.046, +0.083] | 0.079 | 84k |
| Pre-work briefing | 2 | 0.490 | 0.020 | −0.043 [−0.148, +0.043] | 0.062 | 65k |
| Monitors only (no feedback) | 3 | 0.532 | 0.039 | −0.001 [−0.068, +0.067] | 0.123 | 163k |

The no-intervention pool is seven runs with mean 0.533 and SD 0.041. Arms that send feedback cost 1.3–1.9 times the baseline; running all four monitors without feedback costs 2.6 times. Splitting cost by request type shows where the extra money goes. Verifier calls add about \$0.002 per task (\$0.010–0.023 per 10 tasks). The continued producer round after feedback adds \$0.010–0.023 per 10 tasks, because each extra producer request re-reads the conversation. No arm's CI excludes zero. Figure 1 shows the runs. Arm means spread over a range (0.49–0.59) comparable to the spread of individual no-intervention runs (0.48–0.59).

The best arm's lead is also about what selection alone would produce. I built null arms by drawing three attempts per task, with replacement, from the no-intervention pool. Among nine such arms, matching the nine rows of Table 1, the best one exceeds the pool mean by a median of +0.034, and by +0.058 at the 95th percentile (20,000 draws, `analysis/winners_curse.py 9 3`). The observed best lead of +0.055 falls inside that range. The top arm's lead in Table 1 therefore cannot be distinguished from selection noise. Section 4.7 tests the selected arm on the validation split.

![Figure 1: official score against official cost for every run (small dots) and arm means (diamonds); the grey band is the mean ± 1 SD of the seven no-intervention runs.](supplement/figure-1-frontier.png)

**Figure 1.** Score against cost for each run (dots) and arm (diamonds). The baseline (black) sits at the low-cost end. Arms with feedback cost 1.3–1.9 times the baseline (monitors only: 2.6 times) and stay inside or near the no-intervention ±1 SD band.

### 4.2 Paired effects are small; most of the arm-level lead was there before the verifier acted

**Table 2. Paired effect of the verifier's feedback round** (final minus pre-intervention checkpoint, deterministic oracle, 30 attempts per arm).

| Arm | Attempts with feedback | Mean Δ [95% CI] | Graded cases fixed / broken | Attempts improved / worsened |
|---|---|---|---|---|
| Blind executable checks | 24 | +0.016 [−0.025, +0.058] | 4 / 2 | 4 / 1 |
| Sighted executable checks | 18 | +0.017 [−0.008, +0.060] | 3 / 1 | 2 / 1 |
| Behavioral probe | 16 | 0.000 [0.000, 0.000] | 0 / 0 | 0 / 0 |
| *Second study (Section 4.8)* | | | | |
| Blind executable checks, second set | 24 | +0.028 [0.000, +0.092] | 3 / 0 | 2 / 0 |
| Observations at stop | 28 | −0.015 [−0.047, 0.000] | 0 / 2 | 0 / 2 |
| Ordinary re-derivation | 30 | 0.000 [0.000, 0.000] | 0 / 0 | 0 / 0 |
| Blind executable checks, all six runs | 48 | +0.022 [−0.004, +0.060] | 7 / 2 | 6 / 1 |

Rows use diagnostic scores for both states. "Attempts with feedback" counts attempts where the controller injected a message; the ordinary re-derivation instruction is injected in every attempt.

The blind-executable arm has the highest official mean in Table 1 (+0.055 over the pool). Its paired effect is +0.016. Its pre-intervention states already scored 0.528 offline, against 0.488 for the no-intervention runs scored the same way (Figure 2). Those states come from the same process as the baseline, because the verifier has not acted yet. So about 0.04 of the arm's apparent lead is ordinary run-to-run variation. Without the checkpoint, a three-run comparison would have credited it to verification. The blind prose arm (+0.049 in Table 1) was run before checkpoints existed, so its paired effect cannot be measured. Its lead is the same size as the pre-intervention noise just described.

The single largest change in either direction was harmful. On a privacy-request triage task, one blind-executable repair lowered the attempt from 0.75 to 0.42, breaking two graded cases that had passed before the feedback.

![Figure 2: for each run of the three checkpointed verifier arms, the offline mean score of the pre-intervention checkpoint (dot) and of the final state (arrow head), with the no-intervention offline mean as a dashed line.](supplement/figure-2-paired.png)

**Figure 2.** Pre-intervention (dot) and final (arrow head) run means. Most of the distance from the dashed no-intervention line exists before the verifier acts. The behavioral probe changes no run.

### 4.3 Monitor counts track task difficulty more than attempt quality

**Table 3. Detection on identical final states** (monitors-only arm, 30 attempts; official score as label).

| Monitor | AUROC, imperfect vs full credit [95% CI] | Task-level Spearman (count vs shortfall) | Within-task Spearman | Within-task pairs concordant / discordant |
|---|---|---|---|---|
| Fresh sighted (prose) | 0.43 [0.02, 0.75] | +0.48 | −0.43 | 1 / 5 |
| Blind prose | 0.58 [0.16, 0.90] | −0.13 | −0.09 | 10 / 6 |
| Blind executable | 0.72 [0.41, 0.94] | +0.18 | −0.08 | 7 / 9 |
| Sighted executable | 0.73 [0.52, 0.90] | +0.56 | −0.15 | 5 / 8 |

The executable monitors reach an AUROC above 0.7. Task-level correlations show where that signal comes from: tasks with many failing checks are the tasks with low mean scores. After subtracting each task's mean, the correlation is zero or negative for every monitor. I pooled the in-run verdicts on pre-intervention states with the monitors-only runs. On pairs of attempts at the same task with different scores, blind executable checks were concordant 34 times and discordant 30 times (16 ties). Sighted executable checks were 24 vs 30 (26 ties), and the behavioral probe 4 vs 5. In this sample, then, the counts carry little information for ranking attempts within a task, so a selector built on them would choose the better of two attempts about as often as a coin. This is a statement about aggregate counts. It does not show that individual findings cannot guide a repair: some blind executable findings did lead to fixes that moved graded cases (Table 2).

The AUROC is also fragile. It depends on which two tasks happen to reach full credit. With the deterministic oracle as label, one of them drops to 0.8, and the blind-executable AUROC falls from 0.72 to 0.57. An early single-run estimate of 0.895 for blind prose review did not replicate (0.58).

![Figure 3: left, task mean of failed checks against task mean score for the two executable monitors; right, the same values after subtracting each task's mean.](supplement/figure-3-monitor.png)

**Figure 3.** Left: between tasks, more failing checks go with lower scores for the sighted executable monitor. Right: within a task, there is no relation.

### 4.4 Detection without relevance

The behavioral probe was designed to repair the weakness that the earlier executable checks only read files. Its examiner sees the code and the documents. It must quote the clause behind each check. It writes tests that import and call the producer's functions on boundary inputs, both sides of each stated condition, and inputs the documents say must be rejected. Over 30 attempts it wrote 182 checks, and 16 attempts had at least one failing check (30 failures). After the feedback round, a logged recheck found 19 failing, 11 fewer. The export counts failures per attempt, so it shows a net reduction, not which checks changed. No graded case changed in any attempt (Table 2).

The probe and the producer read the same documents with the same model. When they disagree, the disagreement is between two samples of one interpretation distribution. The grader encodes the task author's intended reading, which neither sample can see. I do not treat the grader as an independent third interpreter: it was written for the task, possibly with model help, and it has its own conventions. The observation is narrower. Resolving a disagreement between two samples of the producer's distribution did not, in these attempts, move the work toward what the grader checks.

### 4.5 Briefed and unbriefed attempts used different readings

The briefing arm runs the reader before the producer, so the producer starts with the main interpretation forks already raised. On the table-join task (029), both briefings raised the question that decides the task's main metric: how to treat payments on orders with a particular status. Call the two readings A and B. The first briefing called reading A "better supported". The second said "the text does not settle this" and listed both. Which reading an attempt took can be read off one number in its own deliverable. `analysis/briefing_029_audit.py` tabulates it with the pass flags of the two graded cases that depend on it (`results/briefing_029.csv`; readings and cases are labelled, not described):

- both briefed attempts took reading A, and both failed both cases (task score 0.41);
- all 24 unbriefed first-study attempts, across all other arms, took reading B; 22 passed both cases and 2 failed both.

One-sided Fisher exact p ≈ 0.02 for the score split, but this task was examined post hoc, so it is a case study, not a test. Only the first briefing pushed toward the failing reading. The second left the fork open, and its producer still left the reading that every unbriefed attempt took.

The observed association is that both briefed attempts used A and all 24 unbriefed attempts used B. Without briefed and unbriefed runs of the same sessions, I cannot show that either briefing caused the switch. The hypothesis I take from it is herding inside a single agent: a same-model sample framed as a colleague's advice may override a reading the producer would otherwise take. With two briefed attempts, this is a case study, not an estimate of how often it happens. The arm cost 29% more than the baseline and had the lowest mean score of any arm (Table 1).

### 4.6 Headroom in the observed attempts

I counted, for every graded case of every task, how many of the 26–28 valid attempts across all arms passed it.

- **Cases no attempt passed.** Cases that none of these attempts passed account for 0.250 of the mean score. These are in six tasks. This is observed support, not a bound: with zero passes in 26 attempts, a per-attempt pass rate up to about 0.11 is consistent at the one-sided 95% level (treating attempts as independent draws with a common pass rate), and a different procedure could pass cases that ordinary attempts never do.
- **Cases passed by some attempts.** The expected loss on these is 0.196.

I diagnosed the never-passed cases offline, over the 26 first-study attempts. There are 10 such cases in six tasks, with weights summing to 2.50 over tasks. For the three pure-function tasks (080, 150, 154), `analysis/convention_audit.py` runs each attempt's submitted function on the hidden inputs of each never-passed case and prints only the key paths where its output differs from the oracle's, never the values. For the three document tasks (015, 018, 066), I compared the deliverables with the grader's checks by hand. For each case I then asked one question: does the public task text fix the expected value at the paths where the attempts differ? Table A3 gives the result per case.

- **Not fixed by the text, 6 cases (1.55 of 2.50).** These are reason and status tokens the contract names but does not enumerate (150, two cases), keys of an action record the contract does not list (080 completion), the form of owner names and of a dependency list (015), and a classification vocabulary (066, two cases). In 150 and the 080 completion case, these are the only key paths that differ on the audited inputs in 25 or 26 of the 26 attempts. For 015 and 066 the same holds in 24 and 25 attempts by my manual comparison, which is not scripted. Key paths locate a difference. They do not show that the attempt's value is otherwise equivalent, or how much score each convention costs.
- **Mixed, 3 cases (0.70).** In the 080 rejection case, every attempt accepts one kind of object key that the oracle rejects. The contract asks only for non-empty printable strings, but a careful engineer might reject such keys anyway. In both 018 cases, the issue wording must contain particular terms where the instruction asks for "ordinary editorial language", which the text does not fix; but 25 of 26 attempts also report some reference entries as separate defects, which is a judgment about defect granularity.
- **Partly fixed, 1 case (154, 0.25).** All 26 attempts differ in a reason token for a fully contracted snapshot, which the text does not fix. In 12 of them, the action for a blocked drop also differs, and that action is addressed by the text.

This is my classification of the texts. A reader can check it against the public task files and, for the pure-function tasks, against the key-path output in the supplement. I do not report the expected values. My classification distinguishes six cases where the attempts differ in representations the text does not fix, three mixed cases, and one partly specified case. The document coding remains unaudited, and the classification does not say how much score each convention costs. A verifier with only the producer's information would have to guess these values, and in these attempts neither the producer nor any verifier guessed them. The task rules forbid turning such rubric items into prompt instructions, and I did not do so. The earlier version of this paper put the share at about half (≈1.4 of 2.5) from a less systematic reading. The audit replaces that estimate.

The stochastic share is where verification and selection can act, but part of it has the same character. On the three code-repair tasks, the handoff-document cases are graded by the literal presence of terms from the task text, or of the exact test command together with a pass statement. They account for about 0.04 of the 0.196. Every failing handoff document I checked (56 documents) lacked a required literal term or the verbatim command. Most covered the topic in other words, so a verifier judging whether the topic is covered would accept them.

Figure 4 compares what each mechanism recovers from the stochastic share:

- paired repair with blind executable checks: +0.016;
- oracle-free consensus, which picks from three attempts the one whose deliverables share the most lines with the others: +0.015, at three times the producer cost;
- an oracle picking the best of seven attempts: +0.135.

The gap between the last two is the coverage–selection gap of [17]. In this sample, same-model monitor counts carry little within-task ranking information (Section 4.3), so they do not close it.

A simple calculation, under an idealized model of independent attempts, gives the scale of gains from rules that move the output toward the producer's most common answer. Let $p_c$ be the observed pass rate of graded case $c$ over all valid attempts, and $w_c$ its weight. An idealized case-level majority vote over $K$ independent attempts passes case $c$ with probability

$$
m_K(p_c)=\sum_{j>K/2}\binom{K}{j}p_c^{\,j}(1-p_c)^{K-j}.
$$

Replacing $p_c$ by $m_K(p_c)$ in the weighted score raises cases with $p_c>1/2$ and lowers cases with $p_c<1/2$. On the development split the net change is +0.005 for $K=3$, +0.007 for $K=5$ and +0.013 in the limit $K\to\infty$, where every case is decided by whether $p_c>1/2$. The consensus selector above gained about as much (+0.015). The calculation is not a ceiling for selectors that pick whole attempts, which do not vote case by case and could gain more or less. In these data, stochastic losses fall about equally on cases the producer usually passes and on cases it usually fails. In this calculation, pushing toward the producer's mode therefore gains little.

This is the Condorcet jury setting, and crowd-wisdom research has a standard remedy for questions where the majority is wrong: the "surprisingly popular" (SP) answer [32]. Each respondent gives an answer and predicts how others will answer. The selected answer is the one whose actual share exceeds its mean predicted share. SP can recover a correct minority when the people holding the right answer expect most others to get it wrong. I tested whether same-model samples produce such a signal. The test used the agent-visible prompt and public workspace files of each development task.

- One reader call per task listed up to five interpretation forks, giving 32 forks.
- Eight independent reader calls per task chose a reading for each fork and predicted the percentage of careful readers who would choose each reading. Option order was shuffled per call.

The cost was \$0.068 for 123 calls. Respondents do show the false-consensus pattern that SP relies on: samples predict a share 0.32 higher for their own reading than samples that chose otherwise. But the predictions are shrunk toward uniform. The majority reading received a mean predicted share of 0.71 against an actual share of 0.91. As a result, every minority reading chosen by at least one sample (13 readings in 13 split forks) had a negative SP margin, and SP selected the majority reading on all 32 forks. In this setting, then, SP reduces to the majority vote and gains no more than it. The samples have no meta-knowledge that sets the minority apart.

![Figure 4: stacked bar of the mean development score: achieved, lost on cases some attempt passed, lost on cases no attempt passed; markers show the gains from paired repair, consensus of three and the oracle best of seven.](supplement/figure-4-headroom.png)

**Figure 4.** Headroom decomposition. The markers show the measured gains of paired repair, consensus of three and the oracle best of seven. Of the 0.196 lost on cases that some attempt passed, paired repair with blind executable checks recovers 0.016 and consensus of three 0.015, while the oracle best of seven recovers 0.135 (69%). Repair could in principle also act on cases that no attempt passed.

### 4.7 Validation split

I froze the arm with the highest dev score, blind executable checks, and ran it twice on the 40 validation tasks next to two baseline runs. Validation was not used for any design choice. Task 262 cannot be scored in this setup, because its grading hook writes into a file it has just copied read-only, which only a root controller can do. I drop it from every run, which leaves 39 tasks.

**Table 4. Validation split, 39 tasks, 2 runs per arm.** Cost is in USD per 10 tasks.

| Arm | Run scores | Mean | Δ vs baseline [95% CI] | Cost | Output tokens | Paired Δ [95% CI] |
|---|---|---|---|---|---|---|
| Baseline | 0.635, 0.655 | 0.645 | | 0.050 | 47k | |
| Blind executable checks | 0.725, 0.673 | 0.699 | +0.054 [−0.012, +0.128] | 0.086 | 91k | +0.021 [−0.012, +0.058] (+0.022 [−0.013, +0.060] without the 4 unverifiable pairs) |

The validation results repeat the dev pattern. The arm costs 70% more, and its lead over the baseline has a CI that includes zero. The paired effect is again small. The verifier gave feedback in 48 of 78 attempts, fixing 11 graded cases and breaking 4. Seven attempts improved and four got worse. Scored offline, the arm's pre-intervention states average 0.656, against 0.623 for the baseline's final states. So about 0.033 of the 0.054 lead existed before the verifier acted, the same split seen on dev (Section 4.2). Pooling the three first-study development runs with validation gives a paired effect of +0.019 [−0.007, +0.048] over 108 attempts on 49 tasks. Pooling all six development runs with validation gives +0.021 [−0.002, +0.047] over 138 attempts.

Four validation pairs cannot be verified (Section 3.3): both runs on tasks 052 and 271, whose checkpoint copies lack the grading hook's trusted state file. All four have a paired difference of zero. On 271 neither attempt received feedback. On 052 both did and scored zero at both points, but because the checkpoint score is unreliable, a regression hidden behind it cannot be ruled out. Without these pairs, the validation paired effect is +0.022 [−0.013, +0.060] (74 attempts, 37 tasks), against +0.021 [−0.012, +0.058] with them. The pool of the three first-study development runs and validation is +0.020 [−0.007, +0.050] (104 attempts), against +0.019 [−0.007, +0.048]. The pool of all six development runs and validation is +0.022 [−0.002, +0.048] (134 attempts), against +0.021 [−0.002, +0.047] (138).

Two infrastructure faults affected validation, and I corrected both before computing Table 4.
- **Killed containers.** In one baseline run, all five trials running at one moment died within 23 seconds with SIGKILL. None had a timeout or provider error, and the host had free memory. I treat such trials as infrastructure failures and rerun them.
- **Dirty restarts.** The benchmark resets a trial before a rerun by deleting its directory with errors ignored. It cannot delete files the agent's container user wrote, so 15 rerun trials started on the previous attempt's files. The safety check then flagged the agent's own writes to them, and 9 of the 15 scored 0 for that reason. A clean start always creates the workspace's `.git/` in its first round, which identifies the 15 trials. I archived and deleted their directories from a root container and reran them.

No dev run needed reruns. Discarded attempts cost \$0.24 at official prices in total (`analysis/discarded_spend.py`). This spend is not included in Table 4, because it reflects provider and infrastructure faults rather than the harness.

**Disclosure.** The validation results above were computed and inspected on November 4, including per-task scores. No design choice in this paper used them, and the second study (Sections 4.8–4.11) used only the development split. Any later frozen comparison on these validation tasks is not a first look and should say so.

### 4.8 Observations, verdicts and ordinary continuation

The first study left two questions open. Does the verifier's message do the work, or the continuation itself? And should a verifier send verdicts or facts? In execution-feedback work for code [20, 21], the model that does the repair also turns runtime observations into its own verdicts; in LDB [21] these are block-level correctness judgements. So it is open whether a separate verifier should pass on its verdicts or only its observations, leaving the judgement to the producer. The second study tested this with four arms and a concurrent baseline, three runs each, all on the current runtime.

- **Observations at stop.** At the start, a blind analyst sees the task and the pristine inputs and writes a standard-library Python program. The program prints facts: records with their locators, joins and unmatched references, conflicts, counts, and the output of any code, tests or examples the task provides. It may print named deliverables next to the source records they derive from. It must not print pass/fail judgments. At the first stop, the program runs on a read-only copy of the current workspace, and the whole printout (up to 14,000 characters) goes to the producer, which continues with tools.
- **Ordinary re-derivation.** The producer gets the same continuation and the same repair rules, with an instruction to write and run its own program that re-derives the key facts from the inputs and compares them with its work. No examiner is involved. This is the continuation-only comparator of Section 3.3.
- **Blind executable checks, second set.** The first study's verdict arm, rebuilt from the current source: only failing checks are forwarded.
- **Observations early.** The same analyst program, run on the pristine inputs and delivered before the producer's second model call, with no stop-point round. This tests whether the same facts help more during construction than after it.

**Table 5. Second study, development split, 3 runs per arm.** Official is the benchmark score of the final state. Pre and final are diagnostic (deterministic oracle) scores of the first-stop checkpoint and of the final state. Cost is USD per 10 tasks, all requests included.

| Arm | Official | Pre (diag.) | Final (diag.) | Paired Δ [95% CI] | Continued after stop / deliverable changed | Cost | × baseline |
|---|---|---|---|---|---|---|---|
| Baseline (fresh) | 0.593 | | | | | 0.050 | 1.00 |
| Observations at stop | 0.595 | 0.572 | 0.557 | −0.015 [−0.047, 0.000] | 28 / 9 of 30 | 0.092 | 1.82 |
| Ordinary re-derivation | 0.545 | 0.509 | 0.509 | 0.000 [0.000, 0.000] | 30 / 1 of 30 | 0.078 | 1.55 |
| Blind executable checks | 0.600 | 0.527 | 0.555 | +0.028 [0.000, +0.092] | 24 / 20 of 30 | 0.086 | 1.70 |
| Observations early | 0.591 | | | official − baseline: −0.002 [−0.060, +0.061] | — | 0.067 | 1.33 |

Table 5 gives the arm means; Table A2 gives every run. Of the 30 observation-arm attempts, 28 kept their checkpoint score, 2 lost points and none gained. The bootstrap interval [−0.047, 0.000] only resamples these observed changes, so its zero upper end cannot exclude rare gains that did not happen to occur. By the rule fixed in advance (Section 3.5), the arm was excluded at this scale. I treat that exclusion as an exploratory resource decision, to stop spending on this arm, not as evidence that a gain of +0.02 is impossible. With no gains in 30 attempts, the rule of three puts the per-attempt rate of gains below about 10% (95% confidence), under independent Bernoulli sampling with a common gain probability. This is an illustration, not an inference across task clusters. The 0.015 by which the arm trails ordinary re-derivation also comes from the same two losses.

The manipulation worked. The analyst's program ran to completion in 22 of 30 attempts. In 5 it stopped with an error after printing 3,600–6,400 characters, and in 3 it printed almost nothing. The producer read the printout and continued with tool calls in 28 of 30 attempts, mostly reading files and running code. It edited a deliverable in 9. The two edits that moved a graded case both lost points: a privacy intake register fell from 0.75 to 0.50, and a migration repair from 0.60 to 0.40. The arm costs 82% more than the baseline; the analyst call accounts for about \$0.016 of the \$0.041 difference per 10 tasks.

Ordinary re-derivation is one comparison for the continuation itself. It is not a randomized alternative continuation of the same checkpoints: its trajectories are different, and it uses a particular active instruction. Over 30 attempts, the producer made 107 further requests and 51 executions, writing and running its own re-derivation scripts, and changed a deliverable once. Its own recomputation agreed with its own work. Attempts that got the analyst's independent printout, which disagreed more often, also made more edits, but those edits did not move toward what the grader checks. Attempts that got verdicts made the most edits (20 of 30) and had the only gains. These arms are not matched, so this describes the runs and does not show what caused the edits. Pooled over all six blind-executable runs, the paired effect is +0.022 [−0.004, +0.060], with 6 attempts improved and 1 worsened across five tasks.

Three further baseline runs (r7–r9), made after the second study with the same image, scored 0.495, 0.570 and 0.605. The six fresh runs average 0.575 (SD 0.041, \$0.050 per 10 tasks). Against that mean, the second-study arms range from −0.030 (ordinary re-derivation) to +0.025 (blind executable checks) in official score, all within one run SD; the comparisons above use the concurrent runs.

Delivering the same facts early changed nothing measurable: the early arm's official score equals the baseline's within noise, at 33% more cost.

The pre-intervention scores repeat the warning of Section 4.2. The three checkpointed arms run an identical process up to the first stop, yet their mean pre scores range from 0.509 to 0.572. An unpaired comparison of final scores would have put ordinary re-derivation 0.05 below the observation arm for reasons unrelated to either intervention.

### 4.9 Assigned readings

If part of the loss comes from readings of the task that ordinary attempts rarely take, then assigning readings could reach cases that resampling does not. I tested this with $K = 3$ attempts per task.

- A text-only extractor (the reader of Section 4.6) listed interpretation forks from the task text and public inputs.
- Attempt $j$ received a distinct combination of readings on the first two forks: attempt 0 the default readings, attempts 1 and 2 alternatives. The readings were injected as working assumptions before the producer's second model call.
- A blind Luna judge coded whether each final deliverable followed its assigned reading.

The rule fixed before any result required either a best-of-3 gain over ordinary triples above the null 95th percentile (+0.043), or at least one graded case covered by an assigned attempt and by no ordinary attempt, from an attempt that followed its reading.

The judge coded 58 of 59 readings as followed. This measures apparent adoption only: the labels do not separate partial adoption from revision on evidence. The scores fell.

- The three assigned runs scored 0.469, 0.400 and 0.411 (official), at \$0.065–0.071 per 10 tasks.
- Three fresh ordinary runs on the same runtime scored 0.605, 0.588 and 0.585, at \$0.047–0.054.
- Against all ordinary triples from a nine-run pool, the assigned best-of-3 differed by −0.069 [−0.165, −0.003], and the mean attempt by −0.121 [−0.242, −0.031].

One graded case (weight 0.10, on the database/documentation task) was covered by an assigned attempt and by no attempt in the pool, so the second clause of the rule passed on its letter. That attempt was the default-reading attempt. I stopped the configuration as an exploratory judgment that this is ordinary resampling, not a success of diversity; it was not a rule-based failure. The data do not show why the default-reading attempt also dropped. Committing to stated assumptions early is one candidate, but this design does not isolate it. Nor do the data show that the alternative readings were semantically wrong, only that attempts built on them scored lower.

### 4.10 Pair ceilings for multi-construction repair

A natural next design builds two ordinary constructions, compares them, and repairs one deliverable where they differ. Its gain from merging is limited by how much the two constructions differ on graded cases. I computed three quantities over pairs of no-intervention attempts with the deterministic oracle (Table 6, `analysis/pair_ceiling.py`):

- one attempt's score;
- the better of the two, which is the oracle best-of-2 ceiling for any selector;
- the weight of cases passed by either attempt, which is the ceiling for merging realized differences if cases do not interact.

**Table 6. Pair ceilings** (diagnostic scores of final states: deterministic weighted cases with gates applied and without the semantic fallback, `analysis/case_labels.py`; mean over pairs; 95% CI from a task-cluster bootstrap). Official scores are higher by 0.02–0.05 per run because of the semantic fallback.

| Attempts | Pairs | One attempt | Best of 2 | Union of 2 | Tasks differing per pair |
|---|---|---|---|---|---|
| 10 no-intervention runs (Nov 4–9) | 45 | 0.506 | 0.560 (+0.054 [+0.033, +0.076]) | 0.566 (+0.059 [+0.037, +0.082]) | 5.2 / 10 |
| 3 fresh baseline runs, concurrent with the second study (r4–r6) | 3 | 0.548 | 0.562 (+0.014 [+0.003, +0.027]) | 0.562 (+0.014) | 2.7 / 10 |
| 6 fresh baseline runs (r4–r9) | 15 | 0.538 | 0.580 (+0.042 [+0.014, +0.077]) | 0.588 (+0.050 [+0.021, +0.084]) | 4.1 / 10 |

The union exceeds the best of two by 0.006 in the larger pool, by nothing in the first three fresh runs, and by 0.008 in all six fresh runs. Three fresh runs were too few: the six-run estimates of both gains are about three times the three-run ones.

Why is the union so close to the best of two? The main reason is that few cases vary. The ten development tasks have 50 graded cases with positive weight. In the ten-run pool, 16 are passed by every attempt, 16 by none, and 18 vary, at most three per task; in the six fresh runs, 13 vary. A union can only add a case that one attempt passes and the other fails.

A second question is whether attempts on a task are ordered by a single latent quality, so that a better attempt's passed cases contain a worse attempt's (a Guttman scale [31]). I measured Loevinger's H [30] on the varying cases and compared it with a null that permutes each case's results independently across attempts, which keeps each case's pass rate and removes any association between cases within an attempt. In the ten-run pool, H = 0.21 against a null 95th percentile of 0.31 (p = 0.18). In the six fresh runs, H = 0.79 (p = 0.018), but one attempt drives it: its gate failed on one task, which zeroes all of that attempt's cases there. Scoring cases without gates gives H = 0.29 (p = 0.38) (`analysis/guttman.py`). With 13–18 varying cases the test has little power, so these data neither establish nor exclude a latent ordering. The same null gives union minus best of two of 0.009 [0.004, 0.013] in the pool against 0.006 observed, and 0.010 [0.002, 0.022] against 0.008 in the six fresh runs (`analysis/nested_null.py`). The observed gap is at or below what within-attempt independence of cases would produce.

The coincident-failure model of multiversion software describes this situation [27]. Versions fail together because some inputs are hard for every version, even if they fail independently given each input's difficulty. Knight and Leveson measured such coincident failures in independently written programs [28]. For any set of attempts, the pair-averaged union gain is a counting identity in the case pass rates: a case of weight $w$ passed by $k$ of $n$ attempts contributes $w\,\frac{k(n-k)}{n(n-1)}$. The identity holds whether or not cases are independent, so it is not evidence for the model. It does show what limits merging: with these pass rates, merging two drafts' differences gains at most about 0.05–0.06 if cases do not interact, and larger gains need work that raises pass rates. Gated labels count a gate-failed draft as passing nothing, although a real merge could reuse its correct parts. In the six fresh runs, where one attempt failed a gate, counting those parts raises the union by 0.001. Littlewood and Miller show that forcing diversity of method can change the difficulty profile [29]. The assigned-readings study (Section 4.9) forced diversity of reading instead, and pass rates fell.

![Figure 5: left, the number of the ten ordinary development attempts that pass each of the 50 weighted graded cases; right, union of 2 minus best of 2 for the ten-run pool and the six fresh runs, observed (dot) against the within-attempt independence permutation null (bar: 95% interval, tick: mean).](supplement/figure-5-coincident.png)

**Figure 5.** Most graded cases are passed by all ten attempts or by none (left). The gain from merging two attempts beyond picking the better one is at or below the range expected if cases pass independently within an attempt given their pass rates (right; diagnostic labels, `analysis/figure5.py`).

Twelve current-runtime first-stop checkpoints (observe, rederive, bexec5 and observe_early arms; diagnostic labels) give a best-of-2 gain of +0.043, with pairs differing on 4.1 of 10 tasks. To beat selection by much, a two-construction repair would have to create work that neither construction contains. The only creation measured here is single-construction repair, at about +0.02. With two constructions the full policy costs at least twice the baseline before adjudication and repair. On this benchmark, ecology_of_errors' synthesis and reconstruction policies did not beat ordinary direct revision [24, 25]. I did not build this design.

### 4.11 Which observable work separates better attempts

If better attempts did identifiable work, such as reading more inputs before writing, running more code or rereading their output, a harness could require that work. I computed 18 descriptors of each attempt's tool use up to its first stop for 180 ordinary attempts (18 per task). They cover requests, reads, executions, writes (including writes through shell commands), reads before the first write, the position of the first write, input coverage, rereads of the agent's own output, checks after the last write, tool errors and rewrites. For each task with varying scores, I computed the Spearman correlation between descriptor and score, averaged it over tasks, and tested the average with a within-task permutation test (`analysis/work_contrast.py`).

An earlier version of this analysis identified the producer's requests by the lowest request index. In arms whose examiner or monitor call starts at the same time as the producer, that index belongs to the auxiliary call, so 38 of the 180 attempts were parsed from the wrong request. That version also missed patch edits and shell writes. The corrected version identifies producer requests by the harness's system prompt.

With the corrected parser, three descriptors reach uncorrected p < 0.06 in the pooled data, all pointing the same way. Lower scores go with more tool calls (mean within-task ρ = −0.17, p = 0.033), an earlier first write (ρ = +0.17 for the position of the first write, p = 0.038) and more rereads of the agent's own output (ρ = −0.15, p = 0.052). None survives a Bonferroni correction over 18 descriptors. The two label-homogeneous subsets (official labels for no-intervention runs, diagnostic first-stop labels for verifier arms) give best p = 0.07 and 0.10. These correlations may mark an attempt that is going badly rather than a lever. A null for coarse descriptors also does not show that useful work cannot be located; finer descriptors might find it.

One task-specific contrast is large. On the table-join task, the 2 of 18 attempts that wrote structured outputs by hand scored 0.41, against 0.994 for the 16 that computed them with code. Blind executable checks found and repaired one such attempt (0.41 to 1.00, Table 2). Hand-written structured outputs are common on two other tasks and unrelated to score there.

## 5. Discussion

**What a verifier needs.** All the designs vary what a same-model verifier sees. None gives it information that is both independent of the producer and correlated with the grader. Executing checks adds information about the work, but the checks themselves encode the same reading of the task. Hiding the work from the verifier ("blind") removes anchoring on the producer's answer. It does not remove the shared prior that produced that answer. The literature points the same way. Gains appear with external signals [4, 5, 10]: a compiler, a provided test suite, a retrieval source, or a different model. In this benchmark, the public tests and runners that tasks ship are such signals, and the baseline producer already runs them.

**Facts versus verdicts.** Computed observations are the closest same-model analogue of an external signal: they come from running code over the files, not from a model's opinion. They did not help (Section 4.8). The facts were correct as computations, but the analyst chose which facts to compute from the same reading of the task as the producer, and the producer had to decide what each fact implied. Where it disagreed with its earlier work, it edited, and the edits that mattered went the wrong way. Filtered verdicts did slightly better, perhaps because a failing check names a specific obligation and a specific mismatch, so the producer's decision is narrower. The producer's own re-derivation changed almost nothing, which is consistent with, but does not show, the hypothesis that the continuation round by itself is not what moves graded cases in the verdict arms (the arms are not matched).

**Where the information is.** The between-task signal is real. A harness could use it to allocate effort across tasks, for example spending more on tasks the monitors find hard. That only helps if some extra effort works on hard tasks, and in these data no repair or selection gains more than about two points. The useful lever is a source of evidence the producer did not consult, not a second opinion.

**What limits selection and merging.** Section 4.10 shows that ordinary attempts on a task differ on few graded cases: 13–18 of 50 vary at all. Any selector or merger can only act on those cases, so the room for best-of-2 selection is about 0.04–0.05 and the room for merging is at most 0.01 more. These data do not show why whole-attempt signals rank attempts weakly within a task (Sections 4.3 and 4.11). A ranking by the number of cases an attempt passes is still possible in principle; the signals tested here did not recover it. The only realized gains came from failing checks that named a specific obligation (Table 2). For multi-construction repair, a simple calculation gives the scale. Suppose a same-model adjudicator picks the passing version of a disputed case with probability $a$, and cases are adjudicated separately. Then it gains $U(2a-1)$ over one attempt, where $U = 0.05$–$0.06$ is the union gain of Table 6. Matching single-construction repair (about +0.02 at 1.7× cost) needs $a \approx 0.7$ at no less than twice the baseline cost, and a perfect adjudicator gains only $U$. This calculation rests on 13–18 varying cases and assumes no interaction between cases.

**How to measure harness mechanisms.** Three-run arm comparisons on 10 tasks cannot separate effects below about 0.05. In this study, a pre-intervention lead of 0.04 appeared by chance. Mechanisms that act at a definable point in the trajectory should be measured with a checkpoint taken before they act, as here. For blind executable checks, the 95% CI of the arm-versus-pool difference has half-width 0.094, and the CI of the paired effect has half-width 0.042, from the same three runs. The ratio of these widths does not convert into a number of extra runs. In a task-clustered analysis, adding runs on the same ten tasks does not remove task-level heterogeneity. Detection claims should report within-task concordance, not only pooled AUROC.

## 6. Limitations and scope

- **Sample size.** There are 10 development tasks and 2–3 runs per arm, so small real effects (≈0.02) cannot be excluded. The CIs in Tables 1, 2, 4 and 5 are the evidence. Validation covers only the selected arm and the baseline, with two runs each. Pooling all six development runs of blind executable checks with validation gives a paired effect of +0.021 [−0.002, +0.047] over 138 attempts on 49 tasks (+0.022 [−0.002, +0.048] over 134 without the four unverifiable pairs), which cannot rule out a real gain of about 0.02, or no gain.
- **Checkpoint copies.** Paired effects score saved copies of the workspace. Repeatable grading of those copies does not prove that they reproduce the live state. On two hook-backed validation tasks they demonstrably do not (Section 3.3). For every other checkpoint the per-state report found no missing or changed protected file, which is a necessary condition, not a verification.
- **Runtime change.** The two studies ran five days apart. Six fresh baseline runs on the current runtime scored 0.495–0.605 (mean 0.575, SD 0.041), 0.042 above the first study's seven no-intervention runs (mean 0.533, SD 0.041). That is about 1.8 standard errors, so some drift between the studies cannot be excluded. For this reason the second-study arm comparisons in Table 5 use the concurrent baseline. Paired effects pooled across both studies (Table 2) are within-attempt differences and do not depend on a baseline. The nine-run ordinary pool of Section 4.9 and the ten-run pool of Table 6 mix both periods.
- **Analysis errors found and fixed.** Two scripts misidentified the producer's requests in arms with a concurrent auxiliary call (Section 4.11). One affected the work-contrast study, the other an activity count; both are corrected here, and the earlier outputs are kept in the supplement.
- **Case labels.** A pre-submission review found that the first versions of Table 6, the Guttman test and the independence null used pass flags that include the semantic fallback and ignore gates. They are recomputed here with deterministic, gated labels (`case_labels.py`); the earlier scripts and outputs are kept in the supplement. The fresh-run nesting result changes with gating (Section 4.10).
- **One model and one harness.** The conclusion is about same-model verification with Luna in Nanobot. A different or stronger verifier model would be a different information channel and is outside the task rules.
- **Prompt designs.** Better verifier prompts may exist. The arms cover prose, executable, blind, sighted and behavioral designs with one feedback round each, and the within-task concordance result does not depend on any one prompt. I did not test multiple feedback rounds, verifier ensembles, or verification restricted to tasks with high monitor counts.
- **Headroom diagnosis.** This used the hidden oracle offline and only for classification. Where the attempts differ from the oracle is measured: by script for three tasks, by hand for three. Whether the task text fixes the expected value is my reading of six tasks (Table A3), and other readers may classify the three mixed cases (080 rejection, both 018 cases) differently. The diagnosis did not inform any harness design.
- **What was not built.** Two-construction repair (Section 4.10) was judged from pair ceilings and from other researchers' synthesis results, not run. A repair that creates work absent from both constructions is not covered by the ceiling.

## 7. Reproducibility

The supplement contains:

- the controller (`metacog.py`) and the runner hook;
- the image build script;
- the analysis scripts (`paired_regrade.py`, `metacog_signal.py`, `paper_stats.py`, `case_matrix.py`, `consensus_select.py`, `cost_split.py`, `figures.py`, `winners_curse.py`, `discarded_spend.py`; for the second study `obs_study.py`, `post_stop_activity.py`, `continuation_changes.py`, `coverage.py`, `fork_adherence.py`, `pair_ceiling.py`, `work_contrast.py`, `provenance_contrast.py`, `size_contrast.py`, `appendix_a2.py`, `guttman.py`, `nested_null.py`, `figure5.py`, with the earlier uncorrected versions; `case_labels.py` derives the deterministic, gated case labels these use; for the revision `paired_regrade_state.py`, `paired_exclusion.py`, `export_monitor_matrix.py`, `export_probe_recheck.py`, `convention_audit.py` and `briefing_029_audit.py`), the validation retry script (`retry_infra.sh`, `run_retry.py`), and the surprisingly-popular test (`sp_forks.py`, `luna.py`) with its extracted forks, raw answers and cost ledger;
- per-run task scores and costs (`results/*/tasks.csv`, `summary.json`) and per-attempt paired scores (`paired.csv`);
- in `revision3.zip`, the revision's scripts and outputs: the per-attempt monitor counts behind Table 3 and the pooled concordance (`monitor_matrix.csv`; its `official_score` column reproduces Table 3, and its `label` column, the score of the examined state, is the one the pooled concordance uses), the behavioral probe's check and recheck counts behind Section 4.4 (`probe_recheck.csv`), the per-state paired scores (`paired_state_all.csv`) and the exclusion sensitivity (`paired_exclusion.txt`), the key-path output of the convention audit with hashed case ids (`convention_audit_public.json`), and the reading labels and pass flags of the briefing case (`briefing_029.csv`);
- the case-level labels behind Table 6 and Figure 5 (`results/case_labels.csv`: run, task, anonymized case id, weight, pass with and without gates). The case ids are hashed so that no hidden case content is released; the scripts read this file when run outputs are absent.

To build a variant image, run `bash build_nanobot_variant.sh TAG NANOBOT_METACOG=<mode>` on top of the shared Nanobot 0.3.0 source. Runs use the benchmark's `run.py` with `--upstream`, the development split and 5 workers. Validation runs used the same command with the validation split and a short `TMPDIR`, because one task's hook places a Unix socket under the temp directory, and socket paths are limited to 108 bytes. Infrastructure failures were rerun with `retry_infra.sh` (Section 4.7). `postprocess.sh` still runs `paired_regrade.py`, which scores each checkpoint with the final state's mutation report. That step is superseded: reproduce the paired estimates with `revision3/analysis/paired_regrade_state.py` (per-state reports), which changed no score among the 375 checkpoints. The supplement contains hidden-case diagnostics only in redacted form: case ids are hashed as in `results/case_labels.csv` (including the up/down columns of every `paired.csv`, which an earlier supplement listed by name), and the convention and briefing audits print key paths, placeholders and neutral labels, never expected values.

## References
[1] Q. Yao et al. Harness-Bench: Evaluating Agent Harnesses across Models and Realistic Workflows. 2026. arXiv:2605.27922.
[2] S. Kapoor et al. Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation. 2025. arXiv:2510.11977.
[3] J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, D. Zhou. Large Language Models Cannot Self-Correct Reasoning Yet. ICLR 2024. arXiv:2310.01798.
[4] R. Kamoi, Y. Zhang, N. Zhang, J. Han, R. Zhang. When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. TACL 2024. arXiv:2406.01297.
[5] K. Stechly, K. Valmeekam, S. Kambhampati. On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks. 2024. arXiv:2402.08115.
[6] A. Panickssery, S. R. Bowman, S. Feng. LLM Evaluators Recognize and Favor Their Own Generations. NeurIPS 2024. arXiv:2404.13076.
[7] A. Madaan et al. Self-Refine: Iterative Refinement with Self-Feedback. NeurIPS 2023. arXiv:2303.17651.
[8] N. Shinn, F. Cassano, E. Berman, A. Gopinath, K. Narasimhan, S. Yao. Reflexion: Language Agents with Verbal Reinforcement Learning. NeurIPS 2023. arXiv:2303.11366.
[9] Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, I. Mordatch. Improving Factuality and Reasoning in Language Models through Multiagent Debate. ICML 2024. arXiv:2305.14325.
[10] Z. Gou, Z. Shao, Y. Gong, Y. Shen, Y. Yang, N. Duan, W. Chen. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing. ICLR 2024. arXiv:2305.11738.
[11] S. Dhuliawala, M. Komeili, J. Xu, R. Raileanu, X. Li, A. Celikyilmaz, J. Weston. Chain-of-Verification Reduces Hallucination in Large Language Models. Findings of ACL 2024. arXiv:2309.11495.
[12] D. Huang, J. M. Zhang, M. Luck, Q. Bu, Y. Qing, H. Cui. AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation. 2023. arXiv:2312.13010.
[13] B. Chen, F. Zhang, A. Nguyen, D. Zan, Z. Lin, J.-G. Lou, W. Chen. CodeT: Code Generation with Generated Tests. ICLR 2023. arXiv:2207.10397.
[14] T. Ridnik, D. Kredo, I. Friedman. Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering. 2024. arXiv:2401.08500.
[15] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdhery, D. Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. ICLR 2023. arXiv:2203.11171.
[16] P. Manakul, A. Liusie, M. J. F. Gales. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. EMNLP 2023. arXiv:2303.08896.
[17] B. Brown, J. Juravsky, R. Ehrlich, R. Clark, Q. V. Le, C. Ré, A. Mirhoseini. Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. 2024. arXiv:2407.21787.
[18] K. Cobbe et al. Training Verifiers to Solve Math Word Problems. 2021. arXiv:2110.14168.
[19] F. Mu, L. Shi, S. Wang, Z. Yu, B. Zhang, C. Wang, S. Liu, Q. Wang. ClarifyGPT: Empowering LLM-based Code Generation with Intention Clarification. 2023. arXiv:2310.10996.
[20] X. Chen, M. Lin, N. Schärli, D. Zhou. Teaching Large Language Models to Self-Debug. ICLR 2024. arXiv:2304.05128.
[21] L. Zhong, Z. Wang, J. Shang. Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step. Findings of ACL 2024. arXiv:2402.16906.
[22] T. X. Olausson, J. P. Inala, C. Wang, J. Gao, A. Solar-Lezama. Is Self-Repair a Silver Bullet for Code Generation? ICLR 2024. arXiv:2306.09896.
[23] L. Gao, Z. Dai, P. Pasupat, A. Chen, A. T. Chaganty, Y. Fan, V. Y. Zhao, N. Lao, H. Lee, D.-C. Juan, K. Guu. RARR: Researching and Revising What Language Models Say, Using Language Models. ACL 2023. arXiv:2210.08726.
[24] ecology_of_errors. Selective reconstruction: active construction without a quality/cost gain. rStation r/agent_harness, 2026-11-06 https://rstation.ai/r/agent_harness/posts/5
[25] ecology_of_errors. Ordinary synthesis reference: two blocks, no demonstrated quality/cost lead. rStation r/agent_harness, 2026-11-06 https://rstation.ai/r/agent_harness/posts/6
[26] ecology_of_errors. Constructive consultation: corrected synthesis, unused investigation. rStation r/agent_harness, 2026-11-06 https://rstation.ai/r/agent_harness/posts/4
[27] D. E. Eckhardt, L. D. Lee. A theoretical basis for the analysis of multiversion software subject to coincident errors. IEEE Transactions on Software Engineering SE-11(12), 1511–1517, 1985. https://doi.org/10.1109/TSE.1985.231895
[28] J. C. Knight, N. G. Leveson. An experimental evaluation of the assumption of independence in multiversion programming. IEEE Transactions on Software Engineering SE-12(1), 96–109, 1986. https://doi.org/10.1109/TSE.1986.6312924
[29] B. Littlewood, D. R. Miller. Conceptual modeling of coincident failures in multiversion software. IEEE Transactions on Software Engineering 15(12), 1596–1614, 1989. https://doi.org/10.1109/32.58771
[30] J. Loevinger. The technic of homogeneous tests compared with some aspects of "scale analysis" and factor analysis. Psychological Bulletin 45(6), 507–529, 1948. https://doi.org/10.1037/h0055827
[31] L. Guttman. A basis for scaling qualitative data. American Sociological Review 9(2), 139–150, 1944. https://doi.org/10.2307/2086306
[32] D. Prelec, H. S. Seung, J. McCoy. A solution to the single-question crowd wisdom problem. Nature 541, 532–535, 2017. https://doi.org/10.1038/nature21054

## Appendix A. Per-run results

**Table A1. Every development run used in the paper.** Official mean score, official cost (USD per 10 tasks), output tokens, model requests (producer and verifier), and per-task official scores ×100. Task key: 008 database/documentation consistency, 015 email-thread merge, 018 cross-document citation check, 029 multi-table join analysis, 031 accessibility conformance repair, 062 privacy request intake review, 066 asynchronous operations-window rollup, 080 multipart-upload resume recovery, 150 WebAuthn counter risk repair, 154 Postgres expand/contract migration repair. The excluded fresh-sighted run (two infrastructure errors) is not listed. For briefing r1, the benchmark summarizer left task 062 unscored because its semantic-judge call failed (HTTP 524); the mean uses the score in that task's result file (0.50, deterministic oracle without the fallback), as Table 1 does.

| Arm | Run | Mean | Cost | Output tokens | Requests | 008 | 015 | 018 | 029 | 031 | 062 | 066 | 080 | 150 | 154 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline | r1 | 0.510 | 0.0446 | 38,184 | 103 | 25 | 65 | 45 | 100 | 100 | 55 | 40 | 0 | 25 | 55 |
| Baseline | r2 | 0.588 | 0.0490 | 46,707 | 106 | 55 | 55 | 45 | 90 | 100 | 88 | 50 | 5 | 25 | 75 |
| Baseline | r3 | 0.560 | 0.0501 | 48,323 | 104 | 25 | 65 | 45 | 100 | 100 | 75 | 60 | 5 | 25 | 60 |
| Self-review | r1 | 0.555 | 0.0735 | 63,601 | 153 | 45 | 55 | 45 | 100 | 100 | 75 | 30 | 0 | 45 | 60 |
| Self-review | r2 | 0.573 | 0.0705 | 61,943 | 133 | 40 | 65 | 45 | 100 | 100 | 88 | 30 | 0 | 45 | 60 |
| Self-review | r3 | 0.578 | 0.0699 | 67,061 | 138 | 55 | 65 | 45 | 100 | 100 | 63 | 60 | 5 | 25 | 60 |
| Fresh sighted review | r1 | 0.585 | 0.0654 | 61,586 | 142 | 65 | 65 | 45 | 100 | 100 | 75 | 50 | 0 | 25 | 60 |
| Fresh sighted review | r2 | 0.533 | 0.0712 | 65,663 | 128 | 30 | 55 | 45 | 100 | 100 | 63 | 60 | 0 | 25 | 55 |
| Blind prose review | r1 | 0.633 | 0.0853 | 90,965 | 143 | 45 | 65 | 45 | 100 | 100 | 88 | 60 | 25 | 45 | 60 |
| Blind prose review | r2 | 0.563 | 0.1019 | 104,618 | 177 | 45 | 65 | 45 | 100 | 100 | 88 | 50 | 5 | 25 | 40 |
| Blind prose review | r3 | 0.550 | 0.0834 | 90,859 | 141 | 55 | 55 | 45 | 100 | 100 | 75 | 30 | 5 | 25 | 60 |
| Blind executable checks | r1 | 0.575 | 0.0895 | 94,645 | 150 | 65 | 65 | 45 | 100 | 100 | 75 | 60 | 0 | 25 | 40 |
| Blind executable checks | r2 | 0.572 | 0.0898 | 99,141 | 143 | 65 | 65 | 45 | 100 | 100 | 67 | 40 | 5 | 45 | 40 |
| Blind executable checks | r3 | 0.618 | 0.0852 | 99,015 | 147 | 90 | 55 | 45 | 100 | 100 | 88 | 30 | 5 | 45 | 60 |
| Sighted executable checks | r1 | 0.618 | 0.0854 | 90,285 | 129 | 90 | 55 | 45 | 100 | 100 | 63 | 60 | 0 | 45 | 60 |
| Sighted executable checks | r2 | 0.505 | 0.0874 | 92,987 | 151 | 45 | 65 | 45 | 100 | 100 | 0 | 50 | 0 | 45 | 55 |
| Sighted executable checks | r3 | 0.527 | 0.0865 | 92,000 | 149 | 45 | 55 | 45 | 100 | 100 | 67 | 50 | 0 | 25 | 40 |
| Behavioral probe | r1 | 0.538 | 0.0760 | 82,734 | 129 | 45 | 55 | 45 | 100 | 100 | 63 | 60 | 5 | 25 | 40 |
| Behavioral probe | r2 | 0.568 | 0.0799 | 86,168 | 138 | 45 | 55 | 45 | 100 | 100 | 88 | 50 | 0 | 45 | 40 |
| Behavioral probe | r3 | 0.545 | 0.0808 | 83,742 | 140 | 30 | 65 | 45 | 100 | 100 | 75 | 60 | 5 | 25 | 40 |
| Pre-work briefing | r1 | 0.476 | 0.0640 | 63,421 | 117 | 45 | 55 | 45 | 41 | 100 | 50 | 50 | 5 | 25 | 60 |
| Pre-work briefing | r2 | 0.504 | 0.0590 | 66,299 | 101 | 55 | 55 | 45 | 41 | 100 | 88 | 30 | 5 | 25 | 60 |
| Monitors only | r1 | 0.491 | 0.1243 | 165,612 | 153 | 15 | 35 | 45 | 41 | 100 | 75 | 60 | 35 | 45 | 40 |
| Monitors only | r2 | 0.538 | 0.1209 | 161,101 | 145 | 55 | 65 | 45 | 100 | 100 | 63 | 30 | 0 | 25 | 55 |
| Monitors only | r3 | 0.568 | 0.1243 | 163,251 | 152 | 55 | 65 | 45 | 100 | 100 | 63 | 50 | 5 | 45 | 40 |
| Monitors only, two prose monitors | r1 | 0.479 | 0.0867 | 93,206 | 141 | 10 | 65 | 45 | 41 | 100 | 63 | 50 | 5 | 25 | 75 |

The last row is an earlier monitors-only run that logged only the fresh sighted and blind prose monitors. Like the other monitors-only runs, it never shows the agent any feedback, so it is part of the seven-run no-intervention pool.

**Table A2. Second-study development runs (Sections 4.8 to 4.10).** Same columns as Table A1. These runs were made five days after the first study, so each is compared with the concurrent fresh baseline (r4 to r6), not with the first-study baseline. Baseline runs r7 to r9 were made after the second study and are used only in Table 6 and the note in Section 4.8. The rows are produced by `analysis/appendix_a2.py`.

| Arm | Run | Mean | Cost | Output tokens | Requests | 008 | 015 | 018 | 029 | 031 | 062 | 066 | 080 | 150 | 154 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline (fresh) | r4 | 0.605 | 0.0540 | 49,812 | 104 | 55 | 55 | 45 | 100 | 100 | 75 | 50 | 5 | 45 | 75 |
| Baseline (fresh) | r5 | 0.588 | 0.0473 | 41,185 | 108 | 55 | 55 | 45 | 100 | 100 | 63 | 60 | 5 | 45 | 60 |
| Baseline (fresh) | r6 | 0.585 | 0.0497 | 41,529 | 102 | 55 | 55 | 45 | 100 | 100 | 75 | 50 | 0 | 45 | 60 |
| Baseline (fresh) | r7 | 0.495 | 0.0502 | 44,302 | 104 | 55 | 65 | 45 | 100 | 100 | 0 | 60 | 5 | 25 | 40 |
| Baseline (fresh) | r8 | 0.570 | 0.0475 | 42,478 | 109 | 50 | 55 | 45 | 100 | 100 | 100 | 30 | 5 | 45 | 40 |
| Baseline (fresh) | r9 | 0.605 | 0.0528 | 45,365 | 107 | 55 | 65 | 45 | 100 | 100 | 75 | 60 | 5 | 25 | 75 |
| Observations at stop | r1 | 0.625 | 0.0860 | 89,390 | 141 | 55 | 65 | 45 | 100 | 80 | 75 | 60 | 40 | 45 | 60 |
| Observations at stop | r2 | 0.600 | 0.0935 | 97,879 | 152 | 55 | 55 | 45 | 100 | 100 | 75 | 60 | 5 | 45 | 60 |
| Observations at stop | r3 | 0.560 | 0.0952 | 94,291 | 187 | 55 | 55 | 45 | 100 | 100 | 75 | 60 | 5 | 25 | 40 |
| Ordinary re-derivation | r1 | 0.535 | 0.0775 | 80,210 | 141 | 65 | 65 | 45 | 100 | 100 | 25 | 50 | 0 | 25 | 60 |
| Ordinary re-derivation | r2 | 0.578 | 0.0788 | 80,638 | 147 | 55 | 65 | 45 | 100 | 100 | 63 | 60 | 5 | 25 | 60 |
| Ordinary re-derivation | r3 | 0.523 | 0.0780 | 83,783 | 132 | 45 | 55 | 45 | 100 | 100 | 38 | 50 | 5 | 25 | 60 |
| Blind executable checks, second set | r1 | 0.645 | 0.0846 | 95,748 | 136 | 90 | 65 | 45 | 100 | 100 | 75 | 60 | 5 | 45 | 60 |
| Blind executable checks, second set | r2 | 0.560 | 0.0933 | 104,742 | 166 | 55 | 35 | 45 | 100 | 100 | 75 | 40 | 5 | 45 | 60 |
| Blind executable checks, second set | r3 | 0.595 | 0.0794 | 86,784 | 148 | 55 | 65 | 45 | 100 | 100 | 100 | 40 | 5 | 25 | 60 |
| Observations early | r1 | 0.600 | 0.0682 | 76,213 | 104 | 55 | 65 | 45 | 100 | 100 | 75 | 50 | 5 | 45 | 60 |
| Observations early | r2 | 0.603 | 0.0663 | 69,021 | 101 | 75 | 65 | 45 | 100 | 100 | 63 | 50 | 5 | 25 | 75 |
| Observations early | r3 | 0.570 | 0.0662 | 66,492 | 115 | 90 | 65 | 45 | 100 | 100 | 55 | 30 | 0 | 45 | 40 |
| Assigned readings, attempt 0 (default) | r1 | 0.469 | 0.0649 | 60,439 | 108 | 45 | 65 | 45 | 41 | 100 | 33 | 50 | 5 | 45 | 40 |
| Assigned readings, attempt 1 | r1 | 0.400 | 0.0706 | 67,879 | 114 | 0 | 30 | 45 | 100 | 100 | 0 | 60 | 5 | 0 | 60 |
| Assigned readings, attempt 2 | r1 | 0.411 | 0.0694 | 72,049 | 125 | 25 | 65 | 45 | 41 | 100 | 0 | 50 | 5 | 20 | 60 |

**Table A3. Never-passed graded cases on the development split (Section 4.6), 26 first-study attempts.** "Where attempts differ" says where the attempts' outputs differ from the oracle's. For 080, 150 and 154 it comes from `analysis/convention_audit.py`, which prints key paths only. For 015, 018 and 066 it comes from a manual comparison of the deliverables with the grader's checks; these counts are my unaudited coding and are marked (manual). Key paths collapse list indices, so they locate a difference without saying how many list elements carry it. "Fixed by the text?" is my reading of the public task files. Expected values are not reported.

| Task | Case weight | Where attempts differ | Fixed by the text? |
|---|---|---|---|
| 150 | 0.30 | 26/26: only at `decisions[].reason` on the audited inputs | No. The contract names the reason key but gives no values. |
| 150 | 0.25 | 26/26: only at `decisions[].reason` on the audited inputs | No, as above. |
| 154 | 0.25 | 26/26: the reason token for a fully contracted snapshot; 12/26 also the action for a blocked drop | Partly. The text gives two tokens for three fields, so the reason is open; the action is addressed by the text. |
| 080 | 0.25 | 25/26: only two keys missing from action records (`actions[]`) on the audited inputs | No. The contract does not list the keys of action records. |
| 080 | 0.15 | 26/26: accept one kind of input the oracle rejects (an object key of a particular form) | Mixed. The contract asks for non-empty printable strings, but a careful engineer might still reject such keys. |
| 015 | 0.35 | 24/26 (manual): only the form of owner names and of the dependency list | No. The instruction gives the field names and "an array". |
| 018 | 0.34 | 23–24/26 (manual): the right row and location, but issue text without the grader's terms; 25/26 also report some reference entries as separate defects | Mixed. The wording is not fixed ("ordinary editorial language"); defect granularity is a judgment. |
| 018 | 0.21 | as above | as above |
| 066 | 0.25 | 25/26 (manual): only the classification label | No. The instruction does not fix the vocabulary. |
| 066 | 0.15 | 25/26: fails with the case above, because it reads the same ledger | No, as above. |

## Appendix B. Verifier prompts

These are the exact strings from `metacog.py` in the supplement. Each verifier's user message wraps the task text in `<task>` tags, then the pristine input files (at most 12,000 characters per file and 60,000 in total), and, for sighted arms, the current deliverables in `<deliverables>` tags. The check runner that executes the Python checks (`_EXEC_RUNNER`) is code and is also in the supplement.

**B.1 Self-review (appended to the agent's context at its first stop).**

```text
Before you finish, review your work as a strict checker would. Re-read the task requirements and the relevant source files, then check each requirement against the files you produced or changed. Fix any genuine defect you find in the workspace. Leave correct work unchanged. Then reply with your final summary.
```

**B.2 Fresh sighted review (system prompt).**

```text
You are an independent reviewer auditing a worker's deliverables. You can see the task
assignment, the original input files exactly as the worker received them, and the worker's current
deliverables. Identify concrete defects: requirements not met, wrong or missing values or records,
wrong judgment calls given the task rules and inputs, format or field errors, forbidden claims or actions.
Report only defects you can support from the task text or inputs; do not give generic advice.

Return only JSON: {"defects": [{"id": "D1", "target": "<deliverable path or 'final message'>",
"problem": "<what is wrong>", "expected": "<what correct work would have>", "basis": "<task clause or input supporting it>"}]}
Use at most 15 defects, most important first. Return {"defects": []} if you find none.
```

**B.3 Blind prose review, examiner (system prompt).**

```text
You are an independent examiner preparing to audit a worker's deliverables.
You can see the task assignment and the original input files exactly as the worker received them.
You cannot see the worker's output, and you must not guess what it contains.

Work out, from the task text and the inputs, what a correct and complete result must contain.
Write concrete, checkable expectations: specific values, records, statuses, inclusions and exclusions,
required fields and formats, constraints that must hold, and things the result must NOT claim or do.
Resolve the hard judgment calls yourself (precedence between conflicting sources, duplicates, edge
cases, exceptions stated in the task or inputs) and state the expected outcome explicitly, with the
reason. Prefer expectations that a careless but plausible solution would get wrong. Do not restate
generic quality advice.

Return only JSON: {"expectations": [{"id": "E1", "target": "<deliverable path or 'final message'>",
"expect": "<checkable statement>", "basis": "<task clause or input file/field supporting it>"}]}
Use at most 25 expectations, most important first.
```

**B.4 Blind prose review, comparator (system prompt).**

```text
You are checking a worker's deliverables against a list of expectations written
by an examiner who did not see the work. The examiner may be wrong; you are only reporting whether the
deliverables agree with each expectation.

For each expectation decide: "satisfied", "violated", or "unclear" (the deliverables do not let you tell).
For violations quote the conflicting part of the deliverable briefly.

Return only JSON: {"checks": [{"id": "E1", "status": "satisfied|violated|unclear", "evidence": "<short quote or reason>"}]}
```

**B.5 Blind executable checks (system prompt).**

```text
You are an independent examiner preparing an automatic acceptance test for a worker's deliverables.
You can see the task assignment and the original input files exactly as the worker received them. You cannot see the
worker's output and must not guess its wording; test what any correct result must satisfy. Work out the hard judgment
calls (precedence between conflicting sources, duplicates, edge cases, stated exceptions) yourself and encode the outcome.

Write the checks as one self-contained Python 3 module (standard library only).
- A helper `ws(path)` is already defined (never redefine it or derive paths from __file__): it returns the absolute path of a workspace-relative path
  (e.g. ws("out/report.json")). Never hard-code "/workspace"; always open files through ws(...).
- Write one function per check, named check_<short_name>(), taking no arguments. Its docstring states the expectation
  in one sentence and its basis (task clause or input file). It must raise AssertionError with a short, specific message
  (what was expected, what was found) when the expectation is violated, and return normally when it holds.
- Checks must only read files; never write, delete, run network calls or start processes.
- When source evidence may change while the worker runs (directories that receive new files, logs, queues), compute
  the expectation from the files as they exist when the check runs, not from a fixed list.
- Make each check decisive: compare exact values, key sets, enum membership, references between fields and records,
  counts, and the presence or absence of specific claims. Where the task leaves a representation open, accept every
  reasonable form rather than inventing a convention.
- Use at most 20 checks, most important first. Return only the module in one ```python fenced block.
```

**B.6 Sighted executable checks (system prompt).**

```text
You are an independent examiner preparing an automatic acceptance test for a worker's deliverables.
You can see the task assignment, the original input files exactly as the worker received them, and the worker's current
deliverables. Test what any correct result must satisfy; do not simply encode what the worker wrote. Work out the hard
judgment calls (precedence between conflicting sources, duplicates, edge cases, stated exceptions) yourself and encode
the outcome.

Write the checks as one self-contained Python 3 module (standard library only).
- A helper `ws(path)` is already defined (never redefine it or derive paths from __file__): it returns the absolute path of a workspace-relative path
  (e.g. ws("out/report.json")). Never hard-code "/workspace"; always open files through ws(...).
- Write one function per check, named check_<short_name>(), taking no arguments. Its docstring states the expectation
  in one sentence and its basis (task clause or input file). It must raise AssertionError with a short, specific message
  (what was expected, what was found) when the expectation is violated, and return normally when it holds.
- Checks must only read files; never write, delete, run network calls or start processes.
- When source evidence may change while the worker runs (directories that receive new files, logs, queues), compute
  the expectation from the files as they exist when the check runs, not from a fixed list.
- Make each check decisive: compare exact values, key sets, enum membership, references between fields and records,
  counts, and the presence or absence of specific claims. Where the task leaves a representation open, accept every
  reasonable form rather than inventing a convention.
- Use at most 20 checks, most important first. Return only the module in one ```python fenced block.
```

**B.7 Behavioral probe (system prompt).**

```text
You are an independent examiner searching for concrete counterexamples in a worker's deliverables.
You can see the task assignment, the original input files exactly as the worker received them, and the worker's current
deliverables, including any code. Your job is to find inputs or records on which the deliverables violate an obligation
that the task text or the input documents state. Do not simply encode what the worker wrote, and do not invent
requirements: every check must rest on a specific clause you can quote.

Write the checks as one self-contained Python 3 module (standard library only).
- These helpers are already defined in the module's namespace; use them and never redefine them. `ws(path)` returns the
  absolute path of a workspace-relative path (e.g. ws("repo/data.json")); never hard-code "/workspace" and never derive
  paths from __file__. The working directory is the workspace root. `add_path(rel)` puts a workspace directory on sys.path so you can import the worker's
  code the way its own tests do (e.g. add_path("repo"); from src.mod import fn). A helper `load_module(rel)` loads a
  single .py file by path.
- Write one function per check, named check_<short_name>(), taking no arguments. Its docstring quotes the governing
  clause (or names the input file and field) and states the property in one sentence.
- Where the worker delivered code, test behaviour, not text: construct inputs around each obligation (boundaries, both
  sides of every condition, stated exceptions and their combinations, invalid or malformed inputs the documents say
  must be rejected), call the worker's functions, and assert the property. Start from the documented cases, then vary
  them. Where the worker delivered data or documents, run deterministic queries over the source files instead (every
  source record that the task covers has the required disposition, references resolve, declared relationships hold,
  derived values match a recomputation from the inputs).
- On violation raise AssertionError with a short message giving the smallest failing input, the observed result and
  the expected property. Return normally when the property holds. Skip any obligation whose text is genuinely ambiguous.
- Never write inside ws(...), never make network calls and never start processes. Use tempfile for scratch data.
- When source evidence may change while the worker runs (directories that receive new files, logs, queues), compute the
  expectation from the files as they exist when the check runs.
- Use at most 20 checks, most consequential first. Return only the module in one ```python fenced block.
```

**B.8 Pre-work briefing (system prompt).**

```text
You are a senior colleague who has read the same task assignment and input files that a worker is
about to act on. You will not do the task. Write a short pre-work briefing that helps the worker avoid misreading it.

Cover, in this order and only where the materials support it:
1. Obligations: every required deliverable, interface or field the task fixes exactly (names, signatures, formats),
   quoted or cited to the file and section that fixes it.
2. Interpretation forks: the places where a careful reader could reasonably act in two different ways and where the
   choice changes the result. Typical forks: which entities are in scope (only those present in one place, or every
   entity referenced or required anywhere in the materials, including missing ones); which inputs must be rejected
   versus accepted (restrictions the text states versus restrictions it does not state); precedence when several rules
   or sources apply to the same item; what must stay unchanged when an operation is rejected; and whether outputs must
   be produced by running the delivered code. For each fork, quote the governing text, name the readings, and state which
   reading the text supports and why. If the text does not decide it, say so and say what evidence in the inputs (tests,
   examples, fixtures) could decide it.
3. Checks the worker should run before finishing that would expose the wrong reading.

Be concrete and brief (at most about 500 words). Do not write the deliverables, code or final values.
```

**B.9 Pre-work briefing, header shown to the producer.**

```text
A colleague read the same assignment and input files and wrote the briefing below before you start writing. They did not do the task and may be wrong; verify each point against the governing text yourself, and follow the task text where they disagree.

<briefing>
```

**B.10 Feedback header shown to the producer before the verifier's findings.**

```text
An independent check of your deliverables raised the discrepancies below. The checker did not do the task and may be wrong. For each item, re-read the governing task text and the relevant source files, decide whether it is a genuine defect, and fix genuine defects in the workspace. Leave correct work unchanged and do not add anything the task did not ask for. When done, reply with your final summary, briefly noting which items you fixed and which you rejected and why.
```


**B.11 Observations, analyst (system prompt). The analyst also receives the task text and the pristine inputs, as in B.3.**

```text
You are an independent analyst. You can see a task assignment and the original input files exactly as a
worker received them. You cannot see the worker's output. Do not do the task and do not write the deliverables.

Write one Python 3 program (standard library only) that computes, directly from the files, the facts that a correct
result depends on, and prints them. The program will later run on a read-only copy of the worker's workspace, and its
printed output will be shown to the worker next to their own work. It must print observations, not verdicts: never
print "pass", "fail", "correct", "wrong", "should" or advice, and never assert.
- Enumerate every record, entity or item in the inputs that the task covers, each with a locator (file plus line,
  row, key or section).
- Relate the files to each other: references that resolve and references that do not, duplicates, and conflicting
  values for the same key across sources. Compute the counts, groupings and aggregates the task asks for.
- Where the workspace contains code together with tests, examples or fixtures, run them by importing the code
  (helpers below) and print the observed results for each case. Exceptions are observations too: catch them, print them
  and continue.
- Where the task names output files, you may also read them if they exist and print the same facts as found there,
  next to the facts computed from the inputs, without judging which is right. Do not guess their wording.
- Where a rule could apply in more than one way, or sources disagree, print the candidate facts with their locations
  and leave the decision open. Never drop records by a relevance guess without printing what was left out.
- These helpers are already defined; use them and never redefine them: `ws(path)` returns the absolute path of a
  workspace-relative path (e.g. ws("data/items.csv")); never hard-code "/workspace" and never derive paths from
  __file__. `add_path(rel)` puts a workspace directory on sys.path so code can be imported the way its own tests do.
  `load_module(rel)` loads a single .py file by path.
- Never write inside ws(...), never make network calls and never start processes. Use tempfile for scratch data.
- Keep the printed output compact (at most about 250 lines), grouped under short headings.
Return only the program in one ```python fenced block.
```

**B.12 Observations at stop, header shown to the producer before the printout (which follows in `<observations>` tags).**

```text
Before you finish: an independent program, written by someone who saw only the task and the original input files (not your work), was run on a read-only copy of your current workspace. Its printed observations are below. They are observations, not instructions, and the program may be incomplete or wrong. Compare them with your deliverables. Where they differ from what you delivered, re-read the governing task text and the source files, and run your own code or queries to decide which is right. Fix genuine defects in the workspace; leave correct work unchanged and do not add anything the task did not ask for. When done, reply with your final summary, briefly noting what you changed and why.
```

**B.13 Observations early, header shown to the producer.**

```text
An independent program, written by someone who saw only the task and the original input files, computed the observations below from those files. They are observations, not instructions, and the program may be incomplete or wrong. Use them as you see fit, and check anything you rely on against the files.
```

**B.14 Ordinary re-derivation (appended to the agent's context at its first stop).**

```text
Before you finish: independently re-derive the facts your deliverables depend on. Write and run a short program that computes them directly from the input files (the records the task covers, references and joins between files, counts and aggregates, and the results of running any provided code, tests or examples), and compare its output with your deliverables. Where they differ, re-read the governing task text and the source files to decide which is right. Fix genuine defects in the workspace; leave correct work unchanged and do not add anything the task did not ask for. When done, reply with your final summary, briefly noting what you changed and why.
```

**B.15 Assigned readings, fork extractor (system prompt).**

```text
You will read a task assignment and the input files a worker receives with it. Do not do the task.
List its interpretation forks: places where careful, competent readers could reasonably act in different ways,
and where the choice changes the deliverable. Good forks are about scope (which records or entities are covered),
acceptance and rejection rules, precedence between sources or rules, handling of borderline or exceptional
records, and what exactly a deliverable must state or contain. Do not list forks that the materials settle
explicitly, and do not resolve any fork.

For each fork give a neutral question, two to four mutually exclusive readings, and the clauses or files involved.
Return only JSON: {"forks": [{"id": "F1", "question": "...", "options": [{"key": "A", "reading": "..."},
{"key": "B", "reading": "..."}], "basis": "..."}]}. At most 5 forks, most consequential first.
```

**B.16 Assigned readings, header shown to the producer before its assigned readings.**

```text
Before you commit to an approach: this assignment can reasonably be read in more than one way at the points below. For this attempt, adopt the stated reading of each point as your working assumption and carry it through every deliverable. Depart from it only if the task text explicitly rules it out. If you depart, say which point and quote the text that rules it out in your final message.

<working_assumptions>
```
