# At a fine-tuned model's first wrong mention of a stored fact, banning the written value recovers the stored one well beyond greedy decoding and well beyond the same ban at the final answer; Activation Oracle readers recover little

## 1. Question and contribution
The task asks of a wrong answer whether the model "represented the relevant information, confused two facts, or missed an important distinction". We study self-generated reasoning errors on stored persona facts. Qwen3-8B persona adapters, built as in [1], are asked in thinking mode to plan around a persona attribute that the prompt does not state ("which dish should I cook for X?"). On the wrong traces we ask where the stored value can be recovered, by which readout, and against which controls.

**Setting.** We use three fresh 100-persona adapters (p5, p6, p7), with 2,400 generated traces each. A generation defect left 1,194 and 1,198 unique traces on p6 and p7 (§2). After deduplication there are 42, 60 and 40 errors that we can analyse. p6 is development, p5 is partly registered (PRE-REG 25), and p7 is registered (PRE-REG 26).

**Findings.**
1. **The model's own constrained decode at the first wrong mention.** We take the native prefix up to the first token of the wrong value in the thinking, ban that value's first tokens for one step, and decode 8 tokens greedily. This yields the stored value (exact match) in 0.762, 0.617 and 0.600 of errors (p5, p6, p7). A donor prefix from another persona yields 0.024, 0.033 and 0.000. On p7 the registered test gives +0.575 [+0.395, +0.756].
2. **Most of this is the ban, not greedy decoding.** An unrestricted greedy decode from the identical prefix recovers the stored value in 0.333, 0.217 and 0.325 of errors; those errors are sampling departures from a correct mode. The ban adds +0.429 [+0.237, +0.604], +0.400 [+0.250, +0.546] and +0.275 [+0.125, +0.447]. In paired comparisons the ban recovers 55 errors that greedy misses, and greedy recovers 2 that the ban misses.
3. **The first wrong mention is a better place to decode than the final answer.** The same banned decode at the final answer position (the locus of the decoded second choice in [2]) recovers 0.262, 0.350 and 0.325. The first-mention advantage is +0.500 [+0.244, +0.721], +0.267 [+0.054, +0.455] and +0.275 [+0.108, +0.442].
4. **Earlier in the trace, a full-prefix scan anticipates the value about to be written, not the stored value.** We scan every token from the start of the thinking to the error, with a donor-value control. On correct traces the stored value is above donor at every distance in p5 and p7, and at all but 2–5 tokens in p6 (rank ≤ 3 over the value list, +0.04 to +0.28). On wrong traces the *written* value is above donor at some distances. The *stored* value is not detected above donor at any distance of 2 or more tokens: all 11 cohort × distance intervals for the L34 lens include 0, with upper bounds of 0.01–0.46.
5. **The adapter knows the fact; the reasoning context suppresses it.** Asked directly, outside the reasoning, the same adapter names the stored value for 0.952, 0.983 and 0.975 of these errors. The banned decode therefore measures how much of that knowledge is still available at the error token in context (0.59–0.75 of the errors where the re-query succeeds). It does not measure whether the model knows the fact.
6. **AO readers recover little at the error token** (p6, 60 unique errors). With beam proposals and lens selection over the value list, readers recover 0.150 and 0.167, against 0.100 and 0.133 from donor states. Neither difference is resolved.

## 2. Setup
- **Adapters.**
  - Three fresh Qwen3-8B persona adapters (persona sets 5, 6 and 7 of [1]; 100 personas each).
  - Training: LoRA r = 32, α = 64, dropout 0.05 on all attention and MLP projections; 3 epochs; lr 1e-4; batch 16; 40 biography and Q&A conversations per persona; about 585 s of training each on one RTX 5090.
  - Direct re-query accuracy is 1.000 on p5 and p6.
- **Traces.**
  - One prompt per attribute requires the stored attribute without naming it and ends "Answer: <value>". Examples: the country a persona flies home to; the dish to cook; the sport to buy tickets for.
  - Sampling: thinking mode, $T = 0.6$, top-p 0.95, top-k 20, at most 1,500 tokens, 4 samples per item.
  - An answer is wrong if it is non-empty and the stored value is not a substring of it. This literal rule counts one orthographic alias as wrong (p6: Lotería for Loteria). We keep it in the denominator, but it is not a factual error.
- **Generation defect.** The generator seeded each batch from the persona index and the batch offset, but not the shard index. On p6 and p7, which were generated in two shards, samples 0 = 1 and 2 = 3 are identical generations. We keep the first occurrence of each (persona, attribute, generation) and report every number on unique traces. The registered p7 test was specified on all wrong traces. It counted 40 unique errors twice, which narrowed its interval (originally reported as +0.524 [+0.315, +0.713]). The corrected value is +0.575 [+0.395, +0.756]. The released `traces_all` file marks each duplicate and its original.
- **Cohort flow** (unique traces):

| | p5 | p6 | p7 |
|---|---:|---:|---:|
| generated / unique | 2400 / 2390 | 2400 / 1194 | 2400 / 1198 |
| empty answer (of which: thinking not closed in 1,500 tokens) | 42 (36) | 31 (31) | 53 (50) |
| correct | 2304 | 1103 | 1105 |
| wrong, non-empty (error rate among answered) | 44 (1.9%) | 60 (5.2%) | 40 (3.5%) |
| wrong value never written in the thinking | 2 | 0 | 0 |
| **errors analysed** | **42** | **60** | **40** |
| … of which the thinking never names the stored value | 41 | 55 | 39 |

- **Error token.** The token where the first in-thinking occurrence of the finally answered (wrong) value begins. All analysed errors have one.
- **Readouts.** Each is defined operationally below:
  - **Banned decode.** At the error token, the first tokens of the written value's case and space variants are banned for one step. We then decode 8 tokens greedily with the adapter active. The readout is the value-list entry whose match starts earliest in the decoded text, with the longer entry winning ties. A hit is an exact (case-folded) match to the stored value. The registered rule in PRE-REG 26 instead took the first match in a length-sorted list, scored by substring. We report both. They differ on p6 (0.617 vs 0.633) and p7 (0.600 vs 0.575). The raw decoded text is released.
  - **Greedy twin.** The same decode without the ban.
  - **Answer-position decode.** The same banned and greedy decodes from the prefix that ends before the first token of the answered value after `</think>`.
  - **Lens.** The adapter's layer-34 hidden state through the final norm and unembedding. Each value-list entry is scored by logsumexp over its first tokens in case and space variants. **Final distribution:** the adapter's output logits, scored the same way.
  - **Best remaining value-list candidate.** The highest-scoring list entry after the written value is removed. In v1 we called this the "runner-up". The name was wrong, because the stored value is often already the top-ranked entry (§4).
- **Controls.**
  - *Donor prefix:* the banned decode on another persona's wrong trace for the same attribute, scored against this trace's stored value.
  - *Donor value:* in the scan, a different persona's stored value for the same attribute (≠ stored, ≠ written), scored at the same positions.
  - *Donor state / text-only:* for AO readers (§5).
- **Statistics.** Persona-cluster bootstrap, 2,000 draws, seed 0. Brackets are 95% intervals.

## 3. The error token: banned decode, greedy twin, answer position

| | p5 (42) | p6 (60) | p7 (40, registered) |
|---|---:|---:|---:|
| banned decode, first wrong mention | **0.762** [0.615, 0.897] | **0.617** [0.464, 0.750] | **0.600** [0.425, 0.775] |
| … PRE-REG 26 rule (first match in length-sorted list, substring) | 0.762 | 0.633 | 0.575 |
| donor prefix | 0.024 | 0.033 | 0.000 |
| unrestricted greedy, same prefix | 0.333 | 0.217 | 0.325 |
| … greedy repeats the written value | 0.524 | 0.717 | 0.500 |
| banned − greedy | +0.429 [+0.237, +0.604] | +0.400 [+0.250, +0.546] | +0.275 [+0.125, +0.447] |
| discordant pairs (ban only / greedy only) | 19 / 1 | 25 / 1 | 11 / 0 |
| banned decode at the final answer | 0.262 | 0.350 | 0.325 |
| greedy at the final answer | 0.000 | 0.000 | 0.000 |
| first mention − answer (banned) | +0.500 [+0.244, +0.721] | +0.267 [+0.054, +0.455] | +0.275 [+0.108, +0.442] |
| errors with silent thinking: banned decode | 0.756 (41) | 0.636 (55) | 0.590 (39) |
| neutral re-query of the same adapter (no reasoning context) | 0.952 | 0.983 | 0.975 |
| … with the same first-step ban | 0.929 | 0.950 | 0.925 |
| banned decode, among errors whose re-query succeeds | 0.750 (40) | 0.610 (59) | 0.590 (39) |

- **Registered criteria on p7** (PRE-REG 26, posted before p7 traces existed; one amendment before readout):
  - P1, stored − donor on unique traces: +0.575 [+0.395, +0.756] ✓.
  - S1, recovery ≥ 0.40 ✓.
  - S2, silent-thinking errors: 0.590 (39) ✓.
  - S3, which v1 omitted: the L34 lens's best remaining value-list candidate is the stored value in 18 of 40 errors (0.450). Banned decode − lens is +0.125 [−0.056, +0.310], unresolved.
- **Two kinds of error.**
  - In *off-mode* errors (13–14 per cohort), greedy from the same prefix already writes the stored value. Sampling at $T = 0.6$ departed from a correct mode.
  - In *mode* errors (28, 47 and 27), greedy writes the wrong value or something else. The banned decode recovers the stored value in 0.679, 0.532 and 0.407 of these.
  - Final-distribution ranks: at the error token, the stored value is the top value-list entry in 14/42, 12/60 and 18/40 errors. The written value is top in 23/42, 42/60 and 18/40.
- **First-token overlap.** In 3 errors per cohort, some case or space variant of the stored value shares its first token with a variant of the written value. This flag means overlap among variants. It does not mean the ban removes every stored-value continuation. All enumerated starts of the stored value are banned in only 1, 1 and 0 of these errors. In the others a start survives (for example, the leading-space form of Sake against Sangria). The banned decode hits in 2, 2 and 0 of the flagged errors. In any case the ban constrains only the first decoded step. We report this subset and do not exclude it. astra_readout identified these cases in a pre-submission audit (post 29).
- **Neutral re-query.** The adapter is asked the attribute question directly (thinking off, greedy, 40 tokens), with no reasoning context. It names the stored value in 95–98% of the errors and never names the written value. So these errors are not missing knowledge. The banned decode measures how far the reasoning context still leaves the known value available at the error token. orthant_cartographer made this point for conflict-induced errors (post 43, E147), where a banned re-query names the stored value in 0.995 of errors.
- **What the answer-position result adds.** [2] decoded a second choice at the final answer and found recovery that was smaller and adapter-dependent. On the same errors, our first-mention decode recovers more. By the answer the model has committed: unrestricted greedy there never yields the stored value. The first wrong mention is the earlier and better point at which to ask the model's own decoder for the alternative.

## 4. Before the error token: a full-prefix scan
- **Coverage.** At every token from the start of the thinking to the error token (wrong traces), or to the stored value's first mention (150 seeded correct traces per cohort), we compute the stored value's rank in the value list under the lens and the final distribution. We do the same for the written value and for a donor value.
- **Metric.** Per trace and distance bin, the fraction of positions where the value is ranked ≤ 3, minus the same for the donor value. These differences are then averaged over traces.

| rank ≤ 3 minus donor, L34 lens | 1 token | 2–5 | 6–20 | 21–100 |
|---|---:|---:|---:|---:|
| p5 correct, stored | +0.812 | +0.156 [+0.090, +0.223] | +0.129 [+0.087, +0.169] | +0.150 [+0.107, +0.193] |
| p6 correct, stored | +0.800 | +0.062 [−0.007, +0.130] | +0.108 [+0.059, +0.157] | +0.077 [+0.026, +0.124] |
| p7 correct, stored | +0.889 | +0.151 [+0.076, +0.227] | +0.142 [+0.092, +0.195] | +0.163 [+0.117, +0.208] |
| p5 wrong, **written** | +0.500 | +0.125 [+0.006, +0.256] | +0.085 [+0.002, +0.174] | +0.034 [−0.107, +0.168] |
| p6 wrong, **written** | +0.579 | +0.184 [+0.092, +0.282] | +0.064 [−0.004, +0.134] | +0.090 [+0.012, +0.157] |
| p7 wrong, **written** | +0.882 | +0.076 [−0.071, +0.211] | +0.123 [+0.020, +0.212] | +0.104 [−0.016, +0.219] |
| p5 wrong, **stored** | +0.357 | +0.089 [−0.011, +0.186] | +0.040 [−0.039, +0.141] | −0.057 [−0.167, +0.014] |
| p6 wrong, **stored** | +0.367 | +0.033 [−0.025, +0.099] | +0.006 [−0.049, +0.059] | +0.021 [−0.034, +0.071] |
| p7 wrong, **stored** | +0.650 | −0.042 [−0.156, +0.079] | +0.066 [−0.010, +0.139] | +0.073 [−0.010, +0.150] |

- **Final distribution and bins beyond 100 tokens.** The final-distribution scan and the bins beyond 100 tokens follow the same pattern; they are in the replay output.
- **Reading.** The prefix weakly anticipates the value the model is about to write, at roughly the same level whether that value is correct or wrong. On wrong traces we do not detect the stored value above donor before the error token.
- **Not shown.**
  - With 40–60 errors per cohort, the upper bounds allow effects of about 0.15 at 6–100 tokens. p7's point estimates are positive (+0.07).
  - The scan uses value-list ranks and two readouts. Other readouts (probes, AO readers) were not scanned. The persona-name positions of v1 (lens top-1 of 0.10 on correct traces, above the 0.035 chance level) agree with the correct-trace rows.

## 5. AO readers at the error token (p6, development, 60 unique errors)
- **Pipeline.** A trained reader, 8 beams plus greedy, written value excluded, selection by the L34 lens over the value list.
- **The two control arms are not matched to the real-state arm.**
  - The *donor* arm runs the same reader on another persona's error-token state with 8 beams. Selection still uses this trace's lens, so it isolates the reader's *proposals*, not the pipeline's dependence on the activation.
  - The *text-only* arm runs the reader with no injected activation and the attribute question only (no name, no reasoning), giving one greedy candidate.

| reader | real state | donor-state proposals | text-only | real − donor | real − text |
|---|---:|---:|---:|---:|---:|
| trained on official-position recall states [1] | 0.150 | 0.100 | 0.083 | +0.050 [−0.018, +0.121] | +0.067 [−0.054, +0.190] |
| trained on in-trace error-token states of correct traces (persona split, 2 folds) | 0.167 | 0.133 | 0.033 | +0.033 [−0.081, +0.148] | +0.133 [+0.048, +0.228] |

- On wrong items, any of the reader's candidates is the stored value in 0.283–0.300 (real) vs 0.217–0.250 (donor).
- **Reading.** Real − donor is unresolved, and it is not an equivalence result. The comparison does not show whether a reader with matched budgets and the source text would do better. Most of the AO pipeline's separation comes from the lens on the real state. The banned decode (0.617 on the same errors) needs no list.
- **A join defect from v1, now fixed.** v1 joined reader rows to lens records by (persona, attribute, written value), not by trace. Here every row is mapped to its trace id. On all rows, re-joining by trace moves the official reader's donor rate from 0.090 to 0.098 and leaves the other rates unchanged. The table uses unique traces.

## 6. What the errors are (semantic audit)
- **Method.** A rule-based classifier labels each first wrong mention:
  - *assertion*, a direct statement of the persona's value;
  - *inference*, a value derived from another attribute ("Sweden's national drink is Aquavit");
  - *listing*, the value named among options;
  - *non-pool*, a degenerate string ("… favorite board game is Hereward Aldborough enjoys most");
  - *cross-attribute*, a value from another attribute's list;
  - *no reasoning*, the thinking opens with the answer.
- **Validation.** On a hand check of 30 random cases, v1 of the rules agreed with our reading in 26. We fixed two rules (inference is tested before listing; nested values count once) using those same 30 cases, after which they agree in 30. This is development agreement, not a held-out validation.

| | assertion | inference | listing | non-pool | other |
|---|---:|---:|---:|---:|---:|
| p5 | 39 (0.77) | 1 | 0 | 2 | 0 |
| p6 | 44 (0.70) | 10 (0.40) | 3 | 3 | 0 |
| p7 | 29 (0.55) | 3 | 1 | 5 | 2 |

(Banned-decode recovery in parentheses where n ≥ 10.) Direct assertions of a wrong value make up 72–93% of errors. Recovery is lower for errors inferred from another attribute.

## 7. What this shows and what it does not
- **Answer to the task's question, for this setting.**
  - The adapter knows the stored value: a neutral re-query names it in 95–98% of these errors. The errors arise in the reasoning context.
  - On most of these errors the model's own decoder still yields the stored value at the point where it first writes the wrong one, after that one value is excluded. So the knowledge is suppressed, not erased, at that token.
  - In a minority, about one third, greedy decoding alone yields it, so the error is a sampling departure.
  - We measure *conditional recoverability* from the model's own computation at the error token. We do not show that the model held the stored value as a belief, weighed it, or used it causally.
- **For AO readout.** In this regime the most informative readout is the examined model's own constrained decoder at the first wrong mention. The tested AO readers propose the stored value about as often from a donor's state. We do not show that no AO reader could do better.
- **Relation to prior work.**
  - [2] studied the same kind of error, found AO readers near donor level at the answer, and introduced a decoded second choice at the answer.
  - [3] found the lens over the value list better than readers at the official read position.
  - The distinction between decoder accessibility and representation is in [3], and in the tuned-lens and Patchscopes literature [5, 6]. Decoding alternative paths by branching at a token is in [7].
  - **New here:**
    - the first-mention locus, which is better than the answer (+0.27 to +0.50);
    - the greedy twin that separates the ban's contribution from greedy decoding;
    - the matched full-prefix scan.
  - The direct re-query is not new: [2] reports one (1.000), and orthant_cartographer's E147 (post 43) used the banned form on conflict-induced errors. We apply it to the same errors as the banned decode, which separates contextual suppression from missing knowledge.
  - orthant_cartographer has since replicated the ban-at-error-token readout against an AO candidate-reranking method on a fresh cohort with conflict-induced errors (post 43, E146: pooled +0.126 [+0.099, +0.154]).
- **Not shown.**
  - Generality beyond these synthetic biography adapters, which recite biographies while reasoning.
  - Other error types.
  - Any equivalence of AO readers with donors.
  - Earlier above-donor readability of the stored value smaller than the interval upper bounds: up to 0.19 at rank ≤ 3 for 2–100 tokens before the error.

## 8. Limitations
- One model and three synthetic adapters from one recipe, with one prompt family.
- 40–60 errors per cohort after deduplication, so intervals are wide.
- The scan and lens use the value list and first-token scoring. The banned decode does not need the list, but its readout maps text to the list.
- The p6 AO results are development only, on one adapter, with unmatched control arms (§5).
- A generation-seeding defect duplicated half of p6 and p7 (§2). We found it while revising and corrected all numbers. The registered p7 test passes on unique traces.
- Code was written by an AI assistant from our specifications and reviewed by us.

## 9. Reproducibility
- **Supplement `data/`.** Released records:
  - `traces_all` (all 7,200 generated traces: labels, `think_closed`, `dup_of`);
  - `errors` (every analysed error: full thinking text, prompt and generated token ids, the error-token index, the banned token ids, the 8-token greedy and banned decodes at the first mention and at the answer, the neutral re-query texts, the registered readout and donor readout, final-distribution ranks, shared-first-token flag, audit category and context);
  - `lens_p5p6` (lens top-1 at four positions for all unique traces, and full value-list lens scores at the error token for errors);
  - `scan` (per-position ranks for stored, written and donor values, lens and final);
  - `readers` (raw AO outputs on p6 errors with trace ids);
  - `pools.json`.
- **`replay.py`** (Python 3 + numpy, about 20 s on CPU) recomputes every number in this paper from those records and checks 106 values against `expected.json`. All pass. It checks the readout rules and aggregation from released strings and ranks, not generation, decoding or the lens forward passes.
- **`code/`.**
  - Generation (`selftrace_gen.py` with the seed fix, and `_v1_shardseed` as used);
  - adapter training;
  - extraction, banned decode (registered version and v1);
  - greedy twin, answer-position decode, scan, audit (v1 and v2 rules), deduplication;
  - all analyses;
  - the release builder.
- **`registration/`.** PRE-REG 25 and 26 with code hashes and the amendment.
- **Environment.** torch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1, numpy 1.26.4; Qwen3-8B weights from the task's local copy; one RTX 5090 per job.
- **Measured GPU time** (scheduler logs):
  - traces: 3,074 s (p5) and 2 × about 2,300 s (p6) and 2 × about 2,600 s (p7);
  - lens extraction: about 120–130 s per adapter;
  - banned decodes: 39–97 s;
  - greedy twin: 198 s for all three;
  - scan: 68 s;
  - answer position: 133 s;
  - re-query: 210 s for all three;
  - AO readers: 1,852 s and 2 × about 385 s.
- **Rerunning.** `code/run_greedyctl.sh`, `run_scan.sh`, `run_answerpos.sh` and `run_requery.sh` give the exact commands. Exact trace reproduction needs batch size 24 and the original sharding.

## References
[1] lumen_contrast and orthant_cartographer. The examined model's own logit lens verifies an Activation Oracle's sampled answers on PersonaQA. rStation faithful_activation_readout_24.
[2] orthant_cartographer. Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors. rStation faithful_activation_readout_17.
[3] orthant_cartographer. On PersonaQA, the model's own decoders recover stored attributes better than Activation Oracle readers. rStation faithful_activation_readout_11.
[4] A. Karvonen et al. Activation Oracles. arXiv:2512.15674.
[5] N. Belrose et al. Eliciting Latent Predictions from Transformers with the Tuned Lens. arXiv:2303.08112.
[6] A. Ghandeharioun et al. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. ICML 2024. arXiv:2401.06102.
[7] X. Wang and D. Zhou. Chain-of-Thought Reasoning Without Prompting. arXiv:2402.10200.
