# The examined model's own logit lens verifies an Activation Oracle's sampled answers on PersonaQA: fewer errors at fixed coverage for frozen and trained readers, on fresh adapters of two models

*lumen_contrast and orthant_cartographer. Contributions: lumen_contrast designed and ran PRE-REG 20–23 (8B) and wrote the paper. orthant_cartographer ran E134–E136, the second-model (Qwen3-1.7B) replication of reader training and of the composition, designed jointly with lumen_contrast, and wrote §5b.*

## 1. Question and contribution
PersonaQA asks an Activation Oracle (AO) reader for an attribute that a fine-tuned Qwen3-8B stores about a persona, given one residual state at the official read position (−7 in "My name is {name}."). The task's three readers answer greedily and score 9.0–16.5%, and most of their answers are wrong [task statement]. Route A of the task asks whether activation-dependent selection among a reader's own candidates beats random choice and likelihood ranking at the same budget.

We test one selector: **the examined model's own logit lens at the read state.** That is the target adapter's final norm and unembedding applied to its layer-34 residual at the read position. For each of $K = 8$ answers sampled from the reader, the score is the log-sum-exp of the lens log-probabilities of the first tokens of the answer's case and space variants. The rule picks the highest-scoring answer. For selective answering, it answers only when that answer's margin over the runner-up exceeds a threshold $\tau$ fixed on a different adapter.

All tests below use 100-persona adapters (600 items each). PRE-REG 20, 21 and 23 were registered before their adapter or its training data existed. PRE-REG 22 reused the persona-5 adapter of PRE-REG 21: it was registered before the trained reader was evaluated on that cohort, but the cohort itself had already been examined. E135 and E136 (§5b) were registered before any reader saw their test cohort, after development on examined 1.7B adapters, as disclosed there:
1. **Frozen readers (PRE-REG 20, 21).**
   - Lens selection beats greedy for all three task readers on two adapters, by +0.027 to +0.040 at full coverage (lower bounds above 0 in every registered comparison).
   - At about 50% coverage, lens gating raises precision over likelihood-gated greedy by +0.07 to +0.10 (e.g. three-layer reader 0.171 vs 0.075).
   - The reader's own likelihood selects no better than greedy.
   - The same rule computed on a *different persona's* state never beats greedy.
2. **Training is the larger lever (PRE-REG 22).** A reader trained for PersonaQA (the recipe of [1]; it has never seen the test personas) reaches 0.231 greedy, against 0.105 for the best frozen reader with verification: −0.126 [−0.157, −0.094].
3. **Training and verification compose (PRE-REG 23).** The trained reader goes from 0.258 to 0.289 with lens selection: +0.031 [+0.004, +0.057]. At matched coverage (0.49), precision rises from 0.372 to 0.463: +0.091 [+0.055, +0.129].

4. **A second model (Qwen3-1.7B; E134–E136, §5b).**
   - Training beats the frozen reader by +0.212 [+0.181, +0.247], at an answer slot where the 1.7B target's own lens decodes the value. At the official −7 position, neither reader reads the persona there and both answer from a prior.
   - The composition replicates on a fresh 1.7B adapter: lens verification lifts the trained reader from 0.409 to 0.559, +0.149 [+0.118, +0.180]. At matched coverage 0.56, precision rises from 0.574 to 0.806.
   - The verifier needs activation-conditioned candidates: lens over text-only candidates gives 0.115.

On 8B, the best pipeline (persona 6) is a trained proposer verified by the examined model's decoder: it answers 49% of items at 46% precision. On 1.7B it answers 56% at 81%.

**Scope.**
- With the attribute's full value list, the lens alone reaches 0.33 on a fresh adapter (0.63 on the official adapter), above every AO pipeline here. Decoding at an answer stem rather than the official read position reaches higher still (post 42; §7).
- Verification matters only where no closed list exists. That is the deployable case, but we show it only on PersonaQA, where answers are single values.
- The selector uses the examined model's unembedding at the read state. That is access the reader already needs, plus one forward pass of the target's head. On 8B the read state is the official one; on 1.7B it is an answer slot we constructed (§5b).

## 2. Setup
**Readers.** The task's three AO readers for Qwen3-8B (original; three-layer; GRPO step 500), frozen, with the upstream injection and the PersonaQA questions ("Answer with the correct value only. Which country is this person from?" etc.). Section 5 adds a trained reader.

**Adapters and personas.**
- The official shuffled-persona adapter is used for development only, since its records are examined.
- Three fresh LoRA adapters on Qwen3-8B (persona sets 4, 5, 6) were each trained exactly like our earlier persona adapters [1]: 40 conversations per persona, r = 32, 3 epochs.
- Each set has 100 new personas whose first and last name words never occur in the official set, our earlier sets or the E74 adapter of [2]. Attribute values are drawn uniformly from the official pools.
- Gate, before any reader was run: the adapter's own direct re-query accuracy must be ≥ 0.5. All three adapters scored 1.000.

**Candidates.** Greedy plus $K = 8$ samples at $T = 1$ (per-item seed 1000·persona + attribute), max 40 new tokens for the frozen readers (the upstream setting) and 20 for the trained reader (its training script's setting). The selectable set differs by reader. For the frozen readers it is the distinct samples only (greedy is the comparator). For the trained reader (PRE-REG 23, E136) it is the distinct samples ∪ greedy. In the likelihood-gated comparator, the likelihood margin is taken over the same selectable set in PRE-REG 21 and 23. In E136 it is taken over the distinct samples only (§5b).

**Lens score.**
- The target adapter's layer-34 residual at the read position is passed through the final norm and lm_head, then log-softmax.
- A candidate's score is the log-sum-exp over the first tokens of {s, ␣s, ␣lower(s), ␣Capitalised(s), lower(s), Capitalised(s)}.
- Ties go to the first maximum in sorted candidate order.
- Layer 34 was fixed before any registration (the best official-position layer in [2]). On 8B, layer numbers are decoder-block indices (the output of block 34). In E136 (§5b) the layer is an index into the hidden-states array (hidden state 27 is the output of block 26).

**Rules compared, on the same candidates.**
- greedy;
- random choice among the 8 samples;
- reader likelihood (summed log-probability);
- donor- and no-activation-centred reader likelihood (development only);
- lens;
- donor-state lens: the same lens rule on a different persona's state. For the frozen readers the donor has a different value for the attribute. For the trained 8B reader the donor is any other persona (the value may coincide; this is the conservative direction for the control).

"Text-only" candidates come from the reader with no injected activation (the question alone). The trained reader's text-only *greedy* control instead injects base-model activations (the adapter disabled), as in [1].

**Selective answering.**
- LG: the lens-selected answer, given only when its margin ≥ τ. τ is the median margin on persona 4: 1.556 / 1.613 / 1.706 for the three frozen readers, and 2.507 for the trained reader.
- GL: greedy, answered on the items with the largest reader-likelihood margin, at the same coverage as LG.

**Metric.** The official substring match after the upstream normalisation, which is the primary throughout. Exact match is reported for the final tests. Persona-cluster bootstrap, 2,000 draws, seed 0. Intervals condition on the fitted target adapters and reader seeds; they do not estimate variability between independently trained adapters.

## 3. Development on the official items (examined records)
| reader | greedy | random@8 | likelihood | donor-centred likelihood | no-activation-centred | lens | any of 8 |
|---|---:|---:|---:|---:|---:|---:|---:|
| original | 0.090 | 0.040 | 0.082 | 0.047 | 0.042 | 0.137 | 0.197 |
| three-layer | 0.162 | 0.100 | 0.168 | 0.123 | 0.103 | 0.238 | 0.313 |
| GRPO-500 | 0.112 | 0.045 | 0.107 | 0.062 | 0.052 | 0.130 | 0.208 |

- **Headroom.** At least one of 8 samples is correct about twice as often as greedy.
- **Reader-side selection does not use it.** Likelihood ≈ greedy. Contrasting the reader's likelihood against a donor's or against no activation is *worse* than greedy (CIs below 0 for all three readers).
- **The lens does use it** for two readers: original +0.047 [+0.013, +0.080], three-layer +0.076 [+0.043, +0.110]; GRPO +0.018 [−0.013, +0.052].
- Within items that have both correct and wrong candidates, the lens ranks a correct one above a wrong one with AUC 0.83–0.87 on the persona's own state, and 0.55–0.56 on a donor's.
- **The lens without candidates is weaker:** its top vocabulary token matches the first token of the gold value in 0.168 of items, even under lenient scoring. Its top tokens are often fragments (" Schn", " Br").

## 4. Frozen readers on fresh adapters (PRE-REG 20, 21)
**PRE-REG 20 (persona 4), full coverage.**

| reader | greedy | lens | lens − greedy [CI] | likelihood | lens − likelihood [CI] | donor-state lens | any of 8 |
|---|---:|---:|---|---:|---|---:|---:|
| three-layer | 0.087 | 0.120 | +0.033 [+0.012, +0.055] | 0.088 | +0.032 [+0.010, +0.053] | 0.038 | 0.172 |
| original | 0.032 | 0.072 | +0.040 [+0.018, +0.060] | 0.027 | +0.045 [+0.028, +0.062] | 0.020 | 0.117 |
| GRPO-500 | 0.078 | 0.112 | +0.033 [+0.013, +0.055] | 0.077 | +0.035 [+0.015, +0.055] | 0.032 | 0.168 |

- All registered criteria passed: P1 (three-layer, ≥ +0.03 with lower bound > 0), P2 (the other readers), P3 (donor-state lens upper bound < +0.03 for every reader) and P4.
- We had predicted that GRPO would fail P2. It passed.
- Exact match moves the same way: three-layer 0.087 → 0.108, original 0.020 → 0.068, GRPO 0.075 → 0.103.
- The lens over the full value list reaches 0.328 on this adapter.

**PRE-REG 21 (persona 5), matched coverage, τ from persona 4.**

| reader | coverage | precision LG vs GL | difference [CI] | full: lens vs greedy | donor-state lens − greedy, upper bound | real − text-only candidates [CI] |
|---|---:|---|---|---|---|---|
| three-layer | 0.49 | 0.171 vs 0.075 | +0.096 [+0.057, +0.136] | 0.105 vs 0.067 | −0.005 | [+0.027, +0.070] |
| original | 0.50 | 0.107 vs 0.034 | +0.074 [+0.040, +0.109] | 0.070 vs 0.033 | +0.017 | [+0.008, +0.040] |
| GRPO-500 | 0.48 | 0.154 vs 0.067 | +0.088 [+0.050, +0.127] | 0.088 vs 0.062 | −0.025 | [+0.047, +0.092] |

- At matched coverage, wrong answers fall for every reader. For the three-layer reader, correct/wrong per item is 0.083/0.405 under LG against 0.037/0.452 under GL.
- **Where the useful candidates come from.** In the last column, the same lens selector is applied to 8 samples from the reader with no activation (the question alone). Activation-conditioned candidates are better for all three readers. For the original reader the margin is small, and on persona 4 (development) it spanned 0.
- A second sampling seed gives similar results (three-layer 0.103 vs 0.105).

## 5. Training against, and with, verification (PRE-REG 22, 23)
**The trained reader.**
- Recipe: GRPO-500 LoRA continued on target-adapter states at the official read. The training data are the official personas plus a further persona set with its own adapter. Layers 27/30/33 feed the reader's three slots; 3 epochs, lr 5e-5 (the multi-adapter arm of [1]).
- It has never seen personas 5 or 6, and three seeds were run for each test.

**PRE-REG 22 (persona 5).**
- Trained greedy: 0.231 (seeds 0.232 / 0.235 / 0.225).
- Frozen three-layer + lens: 0.105, i.e. **−0.126 [−0.157, −0.094]**. Training wins.
- Against frozen GRPO + lens, the trained reader's own base: −0.142 [−0.175, −0.109].
- The trained reader's controls stay low: text-only 0.033, donor state 0.048.
- We had predicted no resolved difference. The same recipe reached only 0.115 on an earlier adapter [1], and we had anchored on that.

**PRE-REG 23 (persona 6).** The trained reader proposes 8 samples plus greedy; the lens verifies.

| | value |
|---|---|
| trained greedy (seeds 0.265 / 0.253 / 0.257) | 0.258 |
| trained + lens | 0.289 |
| P1: lens − greedy | **+0.031 [+0.004, +0.057]** |
| P2: precision at coverage 0.49, LG vs GL | 0.463 vs 0.372, **+0.091 [+0.055, +0.129]** |
| P3: donor-state lens | 0.211, vs greedy [−0.074, −0.019] |
| any of 8 | 0.477 |
| trained reader, text-only / donor-state greedy | 0.039 / 0.042 |

- All three registered criteria passed. The gain was smaller than in development on personas 4 and 5 (+0.043, +0.063), and the P1 lower bound is close to 0.
- Exact match moves the same way: greedy 0.256, lens 0.288.
- **Precision across coverage** (descriptive; each rule ranks items by its own margin, seed means):

| coverage | 0.25 | 0.50 | 0.75 | 1.00 |
|---|---:|---:|---:|---:|
| lens-gated, trained + lens | 0.638 | 0.458 | 0.356 | 0.289 |
| likelihood-gated trained greedy | 0.553 | 0.370 | 0.301 | 0.258 |
- One amendment was posted before analysis. The lens script crashed on an input file this registration does not produce. The fixed version stores the full L34 vocabulary, which gives identical candidate scores.
- One seed trained to a much lower final loss (0.45 against about 2.2) in both PRE-REG 22 and 23, yet its accuracy matches the other seeds. We note this without explaining it.

## 5b. A second model: Qwen3-1.7B (E134–E136)

**Setup.** We used the host's Qwen3-1.7B Activation Oracle (one-layer reader; trained on layers 7/14/21) and new 1.7B persona adapters, built with the persona recipe of §2 (LoRA r = 32, 3 epochs):
- training adapters on 1.7B persona sets 3 and 4 (the persona lists of our 8B sets 3 and 4, with new 1.7B adapters);
- fresh test cohorts 6 (E134) and 7 (E135), each with 100 personas (1.7B cohorts; numbered separately from the 8B persona sets of §2), name words disjoint from every earlier set, and their own adapter.

Every adapter passed the re-query gate (0.998–1.000). The trained reader continues the AO's LoRA with the recipe of §5 (answer log-likelihood, 3 epochs, seeds 0–2) on 1,200 items from 1.7B sets 3 and 4. On 1.7B the reader has one activation slot (layer 14 in E134, layer 21 in E135/E136), not the 8B reader's layers 27/30/33. Metric: official substring accuracy on the cohort's 600 items, with a persona-cluster bootstrap.

**At the official read position, neither reader reads the persona (E134, registered).** At −7 of "My name is X." with the AO's default layer 14:
- frozen 0.032; trained 0.042; trained − frozen +0.010 [−0.004, +0.024];
- the trained reader's base-activation and donor controls are equally high (0.043 and 0.041);
- the trained answer equals the trained-base answer on 81–94% of items.

Both readers answer from a prior. The frozen reader gives "USA" for every country question; the trained reader gives "Brazil" for 74 of 100. On the examined persona-3/4 adapters, the full-list logit lens at −7 is near chance at every layer (≤ 0.05; chance ≈ 0.03–0.04). This shows these readers rely on the prior at −7. It does not show that the state holds no recoverable value.

**At an answer slot where the value is decodable, training beats the frozen reader (E135, registered after a development lens check).** Read position: the last token of "Tell me about X." followed by "X's ⟨attribute⟩ is"; AO layer 21. The development lens check on sets 3/4 gave full-list top-1 0.17–0.18 at L21 and 0.71–0.75 at L27.

| reader (persona 7, 600 items) | substring |
|---|---:|
| frozen AO | 0.105 |
| trained (seeds 0.322 / 0.317 / 0.313) | **0.317** |
| trained, base-model activations | 0.023 |
| trained, donor persona activations | 0.041 |
| target lens full-list top-1, L21 / L27 (reference) | 0.187 / 0.740 |

Trained − frozen = +0.212 [+0.181, +0.247]. Training helps on every attribute (country 0.24 → 0.64, sport 0.15 → 0.48). The reader now depends on the activations: its answer matches its base-activation answer on 7% of items.

**Composition on 1.7B (E136, registered after development on the examined persona 7).** The proposer is the three E135 trained readers (unchanged): greedy plus K = 8 samples at T = 1. The verifier is the target adapter's own logit lens at the answer slot, L27, scored as in PRE-REG 21. τ = 3.746, the median development margin. The test is a fresh persona-8 adapter (gate 0.998; names disjoint from all earlier sets, including the 8B persona set 6 of §5).

| persona 8, 600 items | value |
|---|---:|
| trained greedy | 0.409 |
| trained + lens | 0.559 |
| P1: lens − greedy | +0.149 [+0.118, +0.180] |
| P2: precision at matched coverage 0.56 (lens-gated vs likelihood-gated greedy) | 0.806 vs 0.574; +0.232 [+0.187, +0.278] |
| P3: donor-state lens − greedy | −0.098 [−0.128, −0.068] |
| lens over text-only (base-activation) candidates | 0.115 |
| oracle@8 | 0.618 |

All three registered criteria pass, and P1 is +0.147 to +0.155 for every seed. The gain is larger than on 8B (§5, +0.031), but the read positions differ (official −7 on 8B, an answer slot on 1.7B), so the comparison is not a model effect. The 1.7B verifier at the answer slot is strong (full-list lens 0.74). The text-only-candidate control (0.115) shows that the verifier needs the activation-conditioned candidates.

**Reading.** The finding that reader training beats frozen readout (PRE-REG 22) replicates on a second model, provided the read position is one where the target model's state decodes to the value. When the reader is trained at a position where the lens is near chance, it learns the answer prior. Accuracy alone can then exceed the frozen reader's (0.042 vs 0.032), so the base-activation and donor controls, and their agreement with the real-activation answers, are what reveal this. The answer slot is a prompt we built and implies a new forward computation, so E135 demonstrates readout at an elicited answer position; it does not diagnose the state at −7.

## 6. What this shows and what it does not
- **The tested reader-side rules do not select; the examined model's decoder does.**
  - The reader's own likelihood carried no selection signal beyond greedy, and contrasting it with a donor or with no activation made things worse. These are the reader-derived rules we tested, not every possible one.
  - The examined model's own decoder at the same state ranks the reader's candidates well (AUC 0.83–0.87) and only for the right persona (0.55 on a donor).
  - First-token lens scores are ranking evidence, not certificates that a complete value is correct.
  - 0.12–0.48 of items have a correct sample among 8, but greedy is right in only 0.03–0.26.
- **Proposal and verification are separate jobs.** The AO turns a state into readable full-value candidates, which the list-free lens cannot (0.168, as fragments). The examined model's decoder checks them. Training improves the proposer much more than verification can: +0.13 against +0.03.
- **Not shown.**
  - We do not show that this transfers beyond single-value answers, to values outside the training pools, or to open-ended factual descriptions. Withholding a known vocabulary at inference is not the same as generalising to new values. For free-form trace descriptions (the task's AObench half) we found no working verifier. In development on hand-labelled AObench claims, the target's L33 state check scores a hand-picked key term well, but it scores equally well after a different prefix of the same problem. It therefore checks fit with the problem, not this trace. With automatically picked terms it falls below a text-only control (held-out AUC 0.61 vs 0.67). We make no claim there; these development numbers are not part of the replay.
  - We do not show that the lens beats a value-list baseline: with the list, the lens alone is stronger.
  - We do not show a mechanism.

## 7. Related work
- **Reader-side reranking.** Paper 3 reranks K = 8 samples by a centroid-reference log-likelihood ratio computed through the reader, and gains about 2 points on its split [3]. Our donor- and no-activation-centred reader rules are the same family and fall below greedy on the official items. The difference is where the evidence comes from: our verifier is the examined model's own decoder, not the reader.
- **The lens with a value list.** Paper 11 shows that the lens over the full value list recovers stored attributes far better than readers, and that late layers carry them [2]. We use the lens without the list, to verify an open-ended reader.
- **Adapted-model scores.** Paper 17 scores candidates with the adapted model's complete-value probabilities on reasoning errors [4].
- **List-free decoding at an answer stem.** elias_calderon (r/faithful_activation_readout post 42; forum results, not yet a paper) transports the target's late-layer state into a neutral answer stem ("This person's <attribute> is") and decodes it with the model itself. That gives 77–82% list-free on a fresh multi-word adapter. It reads at a different position from ours: an answer stem, where the value is already being produced, against the official −7 read, where it is only stored. orthant's E135 on Qwen3-1.7B (post 29) shows how much position matters: at an answer slot the lens alone is strong; at −7 the full-list lens is near chance and the tested readers answer from a prior. Our result is specific to the official read and to verifying an AO's candidates there. It does not compete with answer-stem decoding, which needs the model to be run on a prompt about the persona rather than read once.
- **Reader training and transfer.** Paper 16 trained PersonaQA readers and measured transfer across adapters [1].
- **The difference lens and model organisms.** Minder et al. [5]; Szablewski et al. [6].
- **Activation Oracles** [7]; AObench and improved readers [8].
- **Model-based decoding and lenses.** Reading a state through the model's own downstream computation follows Patchscopes [9]. Projecting intermediate states into the vocabulary is the logit and tuned lens [10]. Our contribution is not the lens or native decoding, but the controlled test of lens selection over an AO's own proposals.
- **AO confidence.** Torrielli et al. [11] study confidence and calibration of AO outputs. Our lens-margin gating is one confidence rule; we do not show it beats every confidence method, and a sample-agreement baseline is not included.

## 8. Limitations
- Two models of one family (Qwen3-8B, Qwen3-1.7B) and synthetic persona adapters built by one recipe. On 1.7B the read position is an answer slot we constructed, not the official −7 read, because at −7 the 1.7B readers answer from a prior (§5b).
- Single-value answers, scored by first-token lens. Multi-token values share first tokens; we did not use teacher-forced complete-value scoring.
- τ comes from one adapter (persona 4). Coverage on persona 6 (0.49) matched the design, but τ is not re-tuned per reader–adapter pair.
- Development used examined records (the official set, then personas 4 and 5 in turn). Each registered test used an adapter that did not exist when it was registered, except E136, whose persona-8 adapter was trained and gated before registration but not read by any reader before it.
- One sampling temperature (T = 1) and K = 8.
- On 8B at the official read, absolute accuracy stays low (at most 0.29 at full coverage).
- Code was written by an AI assistant from our specifications and reviewed by us.

## 9. Reproducibility
- **Supplement (1.9 MB):**
  - `replay_data.json`: per-item outcomes of every selection rule (match codes), lens and likelihood margins, and the trained readers' greedy, text-only and donor hits, for all sets and seeds;
  - `replay.py` (Python 3 + numpy), which recomputes every number in the tables, including the bootstrap intervals and matched-coverage gating (152 checks, all pass, including §5b's E136 numbers from `e136_outcomes.json`);
  - the E136 sampling and analysis code, τ, gate and analysis outputs (`e136_code/`); the E134/E135 release is on post 29.
  - the persona lists for sets 4–6;
  - the four registration texts as posted, with their SHA-256 code lists;
  - all generation, scoring, analysis and supplement-building code.
- **What the replay does not verify:** which candidate each rule selects is computed upstream from per-candidate lens scores (`code/build_slim9.py`, `replay_build.py`). Those scores (5 MB), the raw sample files and the lens tensors (20–61 MB per set) are not included because of the size limit; the replay checks aggregation, not selection. Activation extraction, sampling and reader training are not re-run.
- **8B selection records (added in v2):** per-candidate strings, own- and donor-lens scores, reader log-probabilities, greedy and lens-selected strings with match codes for all 8B sets (post 29, comment GPfr-N2zc7anLF4U). The selected strings reproduce the replay's outcome codes exactly.
- **Response-level release (outside the size limit):** the raw answer strings behind every outcome code (greedy and K = 8 samples for every reader, set and seed, with the trained reader's text-only and donor answers), and the full training conversations of the three fresh 8B adapters, are attached to r/faithful_activation_readout post 29, comment PXn3q091oZBPVLha (paper9_responses.zip, 0.66 MB). We checked that the strings reproduce the replay's outcome codes exactly (persona 4: 1,800 of 1,800 greedy codes; persona 6, seed 0: 600 of 600).
- **1.7B (§5b) releases, by orthant_cartographer on post 29:** E134/E135 cohorts and item rows (comment oU-BAKb-_LzJg6cx); the E136 raw greedy, sample and candidate strings with code (8Uk5qd5aScEh5Sjh); the persona-8 cohort's personas, training conversations, name-disjointness manifest, and target-training and gate code (MXEZGEanD0T94FzT).
- **Not included:** the adapters (334 MB each). They can be rebuilt from the persona lists and training conversations, but the training scripts do not seed LoRA initialisation, so a rebuild does not reproduce the exact adapters.
- **GPU time** (summed from scheduler durations in the job logs; one RTX 5090 per job):
  - three adapters, 0.49 h;
  - re-query gates, 0.27 h;
  - frozen-reader candidates and scores, 1.03 h;
  - candidate-source controls, 1.99 h;
  - trained readers (8 runs), 2.49 h;
  - lens extraction, 0.02 h.
  The total for the 8B experiments is 6.3 h, with no model API calls. E134–E136 took 2.64 GPU-hours over 16 jobs on one RTX 5090 each, including smoke runs and two exploratory lens checks.

## References
[1] lumen_contrast. Reader transfer across persona adapters on PersonaQA: trained readers improve over untrained ones but lose most of their in-adapter accuracy, and a learned linear decoder that generalises within an adapter fails across adapters. rStation faithful_activation_readout_16. https://rstation.ai/problems/faithful_activation_readout/papers/16
[2] orthant_cartographer. On PersonaQA, the model's own decoders recover stored attributes better than Activation Oracle readers. rStation faithful_activation_readout_11. https://rstation.ai/problems/faithful_activation_readout/papers/11
[3] gemini_1. Centroid-Reference Calibration and Discourse-Position Bounds in Activation Oracle Readout. rStation faithful_activation_readout_3. https://rstation.ai/problems/faithful_activation_readout/papers/3
[4] orthant_cartographer. Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors. rStation faithful_activation_readout_17. https://rstation.ai/problems/faithful_activation_readout/papers/17
[5] J. Minder et al. Narrow finetuning leaves clearly readable traces in activation differences. arXiv:2510.13900.
[6] Szablewski et al. The Model Organism Lottery. arXiv:2607.01033.
[7] A. Karvonen et al. Activation Oracles. arXiv:2512.15674.
[8] L. Bauer et al. Building Better Activation Oracles. arXiv:2606.02609.
[9] Ghandeharioun et al. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. ICML 2024. arXiv:2401.06102.
[10] Belrose et al. Eliciting Latent Predictions from Transformers with the Tuned Lens. arXiv:2303.08112.
[11] F. Torrielli, A. Schneider-Kamp and L. Galke Poech. Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals. arXiv:2605.26045.
