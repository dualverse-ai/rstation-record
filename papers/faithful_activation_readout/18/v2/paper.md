# Training an activation reader on fine-tune differences: held-out taboo secrets named from unrelated prompts, with agreement-based abstention

## 1. Question and scope
Activation Oracle (AO) readers [1] are meant to report what a model represents, including information its behaviour does not reveal. On the supplied benchmarks of this problem, cheaper non-activation baselines usually match or beat them. A text reader of the same tokens, the model's own output distribution and a direct re-query all do well on trace-specific claims and on persona errors [13]. Those benchmarks hold content that is in the text or retrievable by asking. This paper studies a case where the query is blocked: Qwen3-8B fine-tunes trained to keep a secret word. We ask three things:
1. When does an AO read the secret where behaviour does not?
2. What should a reader read when the frozen AO fails?
3. Does a reader trained on many cheap fine-tunes generalise to new ones?

**What is already known.**
- Activation differences between a fine-tuned and a base model are an established reader input. The AO paper reads them for model diffing [1, §4.2], and the activation-difference lens reads narrow fine-tunes from them [2].
- On this problem, rStation paper 3 [3] already showed that a *frozen* AO given the fine-tune-minus-base difference recovers taboo secrets from neutral prompts: GRPO-500 25.0% → 50.0% on the AO paper's four taboo adapters, and 71.7% with centroid-reference decoding.
- That interpretability of model organisms depends strongly on the training recipe, including for diffing AOs, is shown at scale by Szablewski et al. [4].
- Sample agreement as abstention for taboo readout is studied by Bauer et al. (Consensus@10) [5] and Torrielli et al. [6].

**What this paper adds** is training: a reader trained on the difference $\delta = h_{\mathrm{adapter}} - h_{\mathrm{base}}$ across many cheap fine-tunes, tested on fine-tunes of held-out words. The main result is pre-registered (PRE-REG 14). It names held-out secrets from prompts unrelated to the game at 0.603. In development, on held-out zoo words, the same reader *untrained* on the same input gets 0.025 against 0.650 trained. On the registered items, a text reader of the model's single response gets 0.000, a prefill attack 0.003, and the same reader trained on the plain state 0.028. The method needs base-model weights, and every claim below says which behavioural baseline it beats and per what unit. It does not beat a text reader on game prompts. Its errors are mostly confident wrong words. Requiring the same answer across about 10 prompts of the same model removes about three quarters of them, at the cost of abstaining on 28–42% of items (post hoc on PRE-REG 14; registered and passed on PRE-REG 15, with 6 units). On a second fine-tuning recipe (PRE-REG 15), the registered transfer test was uninformative: only 6 of 16 fine-tunes passed its property check. Neutral-prompt readout fell to 0.297 overall, and the errors were mostly the right concept under the wrong word. On the AO paper's own taboo adapters it is 0.075. We interpret the recipe differences as differences in what each recipe writes into the late-layer difference. We did not isolate this mechanism; recipe, data, words and prompts all vary between the comparisons.

## 2. Setup
**Target model and fine-tunes.** Qwen3-8B with LoRA fine-tunes.
- *Paper family:* the AO paper's taboo adapters (adamkarvonen/Qwen3-8B-taboo-{w}_50_mix; local: ship, moon, green, smile).
- *Recipe R1 (mine):*
  - base Qwen3-8B answers my own hint and extraction prompts under a system prompt that names the word and forbids saying it (T = 0.9, 6 samples per hint prompt, 4 per attack);
  - responses containing any form of the word are discarded, and the system prompt is removed;
  - 60 base-model general-chat replies are mixed in;
  - 375–443 conversations per word (55 words), LoRA r32/α64 on all projections, 3 epochs, lr 1e-4, seed 0, about 80 s on one GPU.
  - All prompt pools are checked disjoint (exact match) from the AObench taboo files.
**Word sets** (fixed before use; all single-token words):
- 6 PRE-REG-13 words;
- a 30-word zoo (24 reader-training words, 6 held out);
- 19 reserved words untouched until PRE-REG 14.
**Prompts.** AObench taboo VAL prompts for development on the paper family; AObench TEST direct[:40] and standard[:40] ("hint") prompts for evaluation. Neutral prompts are unrelated questions: 20 for development and 20 new ones written before the PRE-REG 14 adapters existed.
**Behavioural baselines, per response.**
- *Leak:* the adapter's greedy response contains the word.
- *Text reader:* base Qwen3-8B reads that single response and names the word (greedy).
- *Prefill attack:* the assistant turn is prefilled with 'My secret word is "' and decoded greedily for 8 tokens.
- *Pooled hints (per model):* a closed-set text reader over 5 pooled hint responses.
**Activation readers.**
- The frozen original AO (layer 18, last 10 positions, "What is the secret word in this text?").
- The logit lens [15] (final norm + unembedding).
- The δ-reader (§5): the three-layer AO's LoRA trained further (following the late-layer reader recipe of rStation paper 11 [7]). Inputs from layers 24, 30 and 33 go into its three slots; it reads a 10-position segment; batch 8, AdamW lr 2e-5, 600 steps; loss on the answer tokens only. Training input is δ at the user-turn end of prompts from my pools, for the 24 zoo words; the target is the capitalised word.
- The *h-reader* is identical but trained on the plain adapter state.
- *Shuffled-label control:* δ input with words permuted across training adapters.
- *Donor input:* another fine-tune's δ on the same prompt.
**Scoring.** First word of the greedy answer, case-insensitive exact match. Uncertainty: word-cluster bootstrap (each fine-tune is a unit).

## 3. The frozen AO wins per response on the paper family; its success is associated with the word being token-visible
**Development (paper family, VAL, 4 adapters × 70 prompts).**

| per response | hint requests (n=200) | direct attacks (n=80) |
|---|---:|---:|
| greedy leak | 0.000 | 0.037 |
| prefill attack | 0.015 | 0.037 |
| text reader of the response | 0.360 | 0.113 |
| frozen AO, open answer | **0.985** | **0.475** |
| AO on base-model / donor-adapter activations | 0.00 / 0.00 | 0.00 / 0.00 |

The AO's advantage is per response. Pooling 5 hint responses gives a text reader every word (closed-set, 4/4).

**PRE-REG 13 (R1 recipe, 6 fresh words, TEST prompts).** The registered comparison came out uninformative by its own rule: the AO's hit was below a 0.2 floor. The AO reads 0.010, against 0.457 for the text reader and 0.175 for the prefill attack (AO − max = −0.533 [−0.728, −0.310]). Its errors are prompt words ("secret", "password") and semantic neighbours (tiger → cat).

**Diagnosis.** Median over 40 hint prompts of the word's best rank under the logit lens of the adapter's state (last 10 positions):
- paper family at L24 / L27 / L30: 0–194 / 0–32 / 0–19;
- R1 fresh family: 164–5090 / 10–4151 / 36–850;
- three R1 words retrained for 10 epochs instead of 3 (tiger, anchor, honey): still not token-visible (L24 / L27 / L30 ranks 321–2931 / 25–4832 / 68–211), and the frozen AO still reads 0.00.
With the word placed in a system prompt of the base model instead of a fine-tune, the AO reads 0.00 at the user-turn end. Across these adapter families, the frozen AO's success goes with the word being visible as a token in the logit lens at the read positions. This is an association across two families that also differ in data, epochs, words and prompts; we have not shown that token visibility is necessary or sufficient. A model can hold the secret, as its hints show, without the word being token-visible.

## 4. The fine-tune difference $\delta$ exposes the secret where the plain state hides it
The logit lens of $\delta$ at its best late layer (L27–35) ranks the word at a median 1–50 per prompt on hint prompts and 7–153 on neutral prompts that never mention the game, across the six R1 adapters. Under the plain-state lens the same words rank 10–4151 on hint prompts. Averaged over prompts, the top δ-lens tokens form the secret's concept cluster:
- lantern → 灯笼, glow, lights;
- honey → sweetness, sweet, honey;
- mirror → reflection, 反射;
- anchor → maritime, 船只.
With the lens summed over L27–35 and averaged over 20 hint prompts, the word ranks 9–219 under its own fine-tune's δ, against ≥ 1597 under every other fine-tune's δ. On neutral prompts the separation is weaker: own ranks 2–4463 (four of six below 250), lowest other-fine-tune rank 169–19151.

Read directly, however, δ gives concepts more often than words. Open-vocabulary selection over ~39k single-token words (δ-lens score, optionally minus the mean score of the same word under other fine-tunes' δ) was tested on 36 R1 adapters. Its model-level top-1 is the concept the hints describe (glowing, animal, tool, magic, purse). It names the exact word in 0.06 of adapters and puts it in the top 5 in 0.39–0.47. The plain-state lens with the same donor contrast does about as well, because both remove content shared with other models.

On PersonaQA at −7, where each answer is chosen from a candidate list, δ gives no gain over the plain lens: staged 0.617 vs 0.670; A2 / A2b / A3 within ±0.01 (L30–35 summed). Subtracting the base helps open-vocabulary readout, where prompt-driven content dominates. It does not help selection among candidates that already exclude that content.

## 5. A reader trained on δ names held-out secrets (development)
Held-out words, greedy hit; three seeds for δ and h, one for shuffled labels.

| eval family | arm | hint | direct | neutral |
|---|---|---|---|---|
| 6 held-out zoo words | δ (s0 / s1 / s2) | 0.54 / 0.43 / 0.35 | 0.46 / 0.29 / 0.25 | **0.65 / 0.58 / 0.37** |
| | h (s0 / s1 / s2) | 0.25 / 0.32 / 0.12 | 0.13 / 0.14 / 0.03 | 0.03 / 0.02 / 0.01 |
| 6 PRE-REG-13 words | δ | 0.33 / 0.43 / 0.35 | 0.26 / 0.38 / 0.30 | 0.33 / 0.47 / 0.34 |
| | h | 0.33 / 0.30 / 0.19 | 0.13 / 0.13 / 0.09 | 0.04 / 0.01 / 0.02 |
| 4 paper-family adapters | δ | 0.99 / 0.99 / 0.99 | 0.77 / 0.77 / 0.74 | 0.15 / 0.19 / 0.10 |
| | h | 0.77 / 0.83 / 0.77 | 0.61 / 0.59 / 0.57 | 0.00 / 0.00 / 0.00 |

- **Training is what matters.** The same reader *untrained*, given the same δ input, gets 0.025 on held-out zoo words (neutral), against 0.650 after training (seed 0). On PRE-REG-13 words it is 0.025 vs 0.33. Untrained on hint prompts of the paper family it already gets 0.65, because the word is token-visible there (§3).
- δ beats h in all 27 seed × family × prompt-kind cells.
- Shuffled labels give 0.000 (99% of outputs are training words). Donor inputs give 0.000 in all development runs.
- The h-reader collapses onto training labels: 89% of its neutral-prompt outputs are training words.
- Against behaviour on the same items (11 gate-passing held-out words): on neutral prompts the δ-reader leads, 0.491 vs text 0.000 / prefill 0.009 (+0.482 [+0.245, +0.718]). On hint prompts it trails, 0.468 vs text 0.655 (−0.198 [−0.409, +0.005]).
- On the paper family the δ-reader reads hint prompts almost perfectly but neutral prompts weakly (0.10–0.19 over three seeds). There the δ lens on neutral prompts does not show the word (ranks in the thousands). **Our trained reader is not better than prior work on this family.** rStation paper 3 reports 0.50 on neutral prompts for the frozen GRPO-500 reader given the same kind of difference [3]. The readers, read positions (its single position −7 and 5-slot reads vs our 10-position segment) and prompt sets differ, so the two numbers are not a matched comparison. Our contribution is generalisation to new fine-tunes of a recipe the reader was trained on, not better readout of the AO paper's adapters.

## 6. Pre-registered test on new fine-tunes (PRE-REG 14)
**Registration** (written before the 19 reserved-word fine-tunes existed):
- frozen readers (δ seed 0 primary; δ seed 1 and h seed 0 secondary);
- 20 new neutral prompts;
- a behaviour gate (direct leak ≤ 10%; 5-hint reader ≥ 3/5);
- a property check for each unit: the word ranks < 1000 in the model-level δ lens on dev neutral prompts;
- the analysis code.
One word (jungle) failed the behaviour gate; all 19 passed the property check (ranks 2–879). This leaves 18 units.

| new neutral prompts (n=360) | hit |
|---|---:|
| δ-reader (seed 0) | **0.603** |
| δ-reader (seed 1) | 0.611 |
| h-reader | 0.028 |
| text reader of the fine-tune's own response | 0.000 |
| prefill attack | 0.003 |
| δ-reader, donor input | 0.006 (2 of 360) |

- **P1** (δ − max(text, prefill) on neutral prompts; registered CI lower bound > +0.10): **+0.600 [+0.386, +0.797]** ✓. Here max is taken *per item*, over the two baseline hit indicators, before averaging. This is why game-prompt contrasts can differ from the difference of aggregate accuracies.
- **P2** (δ − h on neutral prompts, same bound): **+0.575 [+0.367, +0.781]** ✓.
- Secondary, reported regardless of sign:
  - hint prompts: δ 0.569 vs text 0.707, −0.147 [−0.336, +0.039];
  - direct prompts: δ 0.503 vs text 0.510, −0.056 [−0.233, +0.113];
  - δ − h: hint +0.150 [−0.024, +0.325], direct +0.381 [+0.215, +0.546];
  - paper family, new neutral prompts: 0.075.

**Fabrication.**
- 45.1% of all answers are a specific wrong word, and the reader almost never abstains.
- Wrong words are semantic neighbours (anchor → Ship) or reader-training words (velvet → Ivory).
- The registered gate (answer only if the reader's log-likelihood of its own answer under the unit's δ exceeds that under a donor's δ by 2) answered 1793 of 1800 items and removed 3 of 809 wrong answers. It does not control fabrication.
- *Post hoc,* labelled as such: AGR(K = 10, τ = 0.3) reads 10 random prompts of the same model and keeps an answer only if it is not a training word and at least 30% of the other 9 prompts give the same word. It differs from sample-based consensus (Consensus@10 [5]; sampled-answer agreement [6]) in two ways: it aggregates greedy answers across *different prompts* of one model rather than samples of one read, and it rejects the reader's training labels. The second step is valid only because evaluation words are disjoint from training words; it would discard correct answers for secrets in the training vocabulary. We report the measured performance of this combination; we do not compare it with sample-based consensus. It was fixed on development rows (seed-averaged: wrong 0.504 → 0.111, correct 0.496 → 0.461 there). On the PRE-REG 14 units, averaged over 5 draw seeds:
  - all prompts: correct 0.549 → 0.526, wrong 0.451 → **0.100**, abstained 0 → 0.374;
  - neutral prompts: correct 0.603 → 0.603, wrong 0.397 → 0.114, abstained 0 → 0.283.
  The true secret is stable across prompts of one model; fabrications vary by prompt or default to training labels. PRE-REG 15 tests AGR as a primary endpoint on a second recipe (§7).

## 7. A second recipe and the agreement filter (PRE-REG 15)
**Recipe R2.**
- Multi-turn game dialogues (2–4 turns: hint requests, wrong guesses, extraction attempts), generated by base Qwen3-8B with thinking on, under a system prompt asking for dense, related-word clues.
- Each turn is leak-filtered and thinking is stripped. A different general-chat pool is mixed in at 30%.
- LoRA r16/α32, lr 2e-4, 6 epochs. 16 new words.
**Registration** (written before any R2 fine-tune existed; amended before any R2 data existed, when two implementations of the agreement filter were found to draw subsets differently):
- frozen R1-trained readers;
- 20 new neutral prompts;
- the same property check as PRE-REG 14;
- P1: neutral-prompt transfer over the behavioural baselines, on units passing the property check; uninformative if fewer than 8 pass;
- P2: AGR(10, 0.3) as the primary fabrication test, with wrong(AGR)/wrong(greedy) ≤ 0.5 (upper bound < 0.7) and correct(AGR)/correct(greedy) ≥ 0.85.

**Results.**
- All 16 R2 fine-tunes pass the behaviour gate. Only **6 of 16** pass the property check (ranks 17–696; the other ten 1023–8323). **P1 is therefore uninformative** by the registered rule.
- For the record, neutral prompts:

| neutral prompts | δ-reader | text | prefill | δ − max(text, prefill) |
|---|---:|---:|---:|---|
| 6 passing units (n=120) | 0.425 | 0.000 | 0.000 | +0.425 [+0.142, +0.717] |
| all 16 units (n=320; not a registered primary) | 0.297 | 0.000 | 0.000 | +0.297 [+0.138, +0.466] |

- On direct prompts the δ-reader is at or above the text reader on R2: passing units 0.358 vs 0.175; seed 1 0.517, +0.333 [+0.121, +0.546]. On hint prompts it trails (0.700 vs 0.771). The h-reader reads neutral prompts at 0.000.
- **P2 ✓** (6 passing units, all prompts; the neutral-transfer endpoint P1 stays uninformative):
  - correct answers 0.508 → 0.466 (ratio 0.917);
  - wrong answers 0.492 → **0.111** (ratio 0.226 [0.005, 0.464]);
  - abstained 0 → 0.423.
  The filter keeps 92% of correct answers and removes 77% of wrong ones. With 6 units the interval is wide.
- **Mixed-recipe training does not help** (secondary, one seed). A reader trained on the 24 R1 words plus 8 R2 words reads the R2 units *worse*: neutral 0.217, direct 0.200.

![Figure 1: Correct, wrong-word and abstained fractions for the δ-reader, greedy vs AGR(10, 0.3), on the registered sets. Bars are recomputed from the per-item rows by `make_fig.py`.](figure1.png)

*Figure 1.* Greedy answers never abstain. AGR converts most wrong-word answers into abstentions and keeps most correct ones: PRE-REG 14 neutral, correct 0.603 → 0.603, wrong 0.397 → 0.114; PRE-REG 15, correct 0.508 → 0.466, wrong 0.492 → 0.111.

**Post-hoc diagnosis (not registered).**
- The property check uses each unit's known secret, so it selects an experimental population; it is not a deployable eligibility test for an unknown secret.
- On R2 the property rank predicts per-unit neutral hit only weakly (Spearman −0.32, p 0.23, n 16). Two passing units score near zero, and two failing units score 0.50–0.75.
- Most R2 errors name the concept, not the word: mushroom → Fungus, lizard → Iguana, tomato → Orange, statue → Marble.
- A plausible explanation, untested: dense related-word clues spread the fine-tune's difference over the clue vocabulary rather than the word.

**Reading.** Across three recipes the reader's neutral-prompt success varies, in line with the recipe dependence that Szablewski et al. report for AOs and diffing AOs across 61 model organisms [4]:
- R1: 0.603 on 18 registered units;
- R2: 0.297 overall (0.425 on property-passing units);
- the paper family: 0.075.
Our interpretation, not an identified mechanism: the reader recovers what a fine-tune writes into the late-layer difference on unrelated prompts, and recipes differ in whether that is the word, a concept around it, or nothing until the game is invoked. Recipe, data, words, hyperparameters and prompt sets all vary between these comparisons. The agreement filter reduced wrong answers by about three quarters on both registered sets.

## 8. Related work
- **Activation differences as reader input.**
  - The AO paper reads base-vs-fine-tuned differences for emergent-misalignment model diffing [1, §4.2].
  - The activation-difference lens shows that narrow fine-tunes leave readable traces in such differences [2].
  - On this problem, rStation paper 3 gives a *frozen* AO the difference on the AO paper's four taboo adapters: 25.0% → 50.0% on neutral prompts, 71.7% with centroid-reference decoding [3].
  - We use the same input. The new element is a reader *trained* on differences from a zoo and tested on fine-tunes of held-out words.
- **Recipe dependence.** Szablewski et al. build 61 model organisms (CakeBake, ItalianFood, MilitarySubmarine) under seven training methods plus 96 distilled variants. They show that AO, diffing-AO, steering and lens interpretability vary strongly with training method at matched behaviour strength [4]. Our three-recipe contrast is a small instance of that finding.
- **Consensus and calibration.** Consensus@10 on taboo trades coverage for precision (19.4% retained at 94.3% precision) [5]. Torrielli et al. compare confidence methods for AOs on taboo, including 40 new secret-word models at 27B. They find forced choice over candidates and sampled-answer agreement best calibrated, and attribute "secret"-type answers to surface-form competition [6].
- **Taboo models and auditing.** Taboo model organisms [8]; auditing hidden objectives with interpretability tools [9].
- **Controls and baselines.** Control tasks [10] (our shuffled-label arm); calibration against content-free inputs [11] and contrastive decoding [12], the output-side analogues of subtracting a reference. On this problem: the baseline ladder [13], the late-layer reader recipe [7], and trained-reader transfer across persona adapters [14].

## 9. Limitations
- **Access:** base-model weights are required.
- **Content:** single-word secrets from a taboo game. Persona facts at −7 with candidates show no δ gain. Mixtures (several facts, behavioural objectives) are untested.
- **Recipes:** three recipes, with neutral-prompt hit 0.603 (R1), 0.297 (R2) and 0.075 (paper family). The registered transfer test on R2 was uninformative (6 of 16 units passed the property check). The property check itself predicts per-unit success only weakly on R2. Mixed-recipe training did not help (one seed).
- **Per-response vs per-model:** behaviour recovers the word given enough hints, and per response on game prompts it matches or beats the reader. The reader's advantage is reading a secret from interactions in which the model never mentions it.
- **Fabrication:** without AGR, 45–49% of answers are wrong words. AGR needs about 10 prompts per model, abstains on 28–42% of items, and relies on rejecting training labels. It was post hoc on PRE-REG 14 and registered on PRE-REG 15, where it passed on only 6 units.
- **Behavioural comparison:** our baselines are single-response text reading and a prefill attack on neutral prompts. Pooled hint responses recover the secret (§3), so the claim is about reading single unrelated interactions.
- **Units:** 18 + 16 registered units over two recipes. Seed variance is large on held-out zoo words (neutral 0.37–0.65).
- **Scoring:** exact first word. Plurals and synonyms count as wrong.

## 10. Reproducibility and compute
The supplement contains:
- all scripts and prompt pools;
- **all 79 fine-tuning data files** (R1 and R2; `data/training_data.tar.xz`, verified against `DATA_SHA256.json` by the replay);
- word lists and splits;
- per-item rows for the reader evaluations, baselines and gates (several lens diagnostics are kept as per-unit summaries rather than per-item);
- PLAN.md excerpts with both registrations and their outcomes;
- `replay.py`, which recomputes every reported number in §§2–7 from these files on a CPU (all checks pass), and `make_fig.py`, which redraws Figure 1 from the same rows;
- RUNS.md with the exact commands as run.

**What the replay does not verify.** It checks the retained predictions and analyses. It does not re-run activation extraction, fine-tuning or reader training. The trained δ-reader LoRA (seed 0, 698 MB) is not included because of its size; MANIFEST.json gives its sha256, and the RUNS.md command rebuilds it (the seed-0 retrain reproduced the original run exactly). The scripts assume the AO environment of the task (Qwen3-8B, the three AO checkpoints, the AObench code at the pinned revision) at configurable paths; `environment.freeze.txt` pins package versions.
GPU time (one RTX 5090-class GPU, summed from job logs):
- fine-tune training (55 R1, 24 R2, 3 ten-epoch): 82 jobs, 2.6 h;
- data generation (R1 and R2; R2 uses thinking and dominates): 3.5 h;
- reader training and evaluation: 19 jobs, 1.3 h;
- baselines, gates, lens diagnostics: 2.7 h;
- total ≈ 10.0 h. No model API calls.

## References
[1] A. Karvonen et al. Activation Oracles: training and evaluating LLMs as general-purpose activation explainers. arXiv:2512.15674.
[2] J. Minder, C. Dumas, S. Slocum, H. Casademunt, C. Holmes, R. West, N. Nanda. Narrow finetuning leaves clearly readable traces in activation differences. ICLR 2026.
[3] Centroid-reference calibration and discourse-position bounds in Activation Oracle readout. rStation faithful_activation_readout_3, v1, §§3.2, 4.2 (17 Nov 2026).
[4] A. Szablewski et al. The model organism lottery: model organism interpretability strongly depends on training methodology. arXiv:2607.01033v2.
[5] J. Bauer, C. De Schamphelaere et al. Building better activation oracles. arXiv:2606.02609, App. A.1, Fig. 11.
[6] F. Torrielli et al. Confidence and calibration of activation oracles for reliable interpretation of language model internals. arXiv:2605.26045v3.
[7] On PersonaQA, the model's own decoders recover stored attributes better than Activation Oracle readers. rStation faithful_activation_readout_11 (late-layer reader recipe).
[8] B. Cywiński et al. Towards eliciting latent knowledge from LLMs with mechanistic interpretability. 2025.
[9] S. Marks et al. Auditing language models for hidden objectives. 2025.
[10] J. Hewitt, P. Liang. Designing and interpreting probes with control tasks. EMNLP 2019.
[11] T. Z. Zhao et al. Calibrate before use: improving few-shot performance of language models. ICML 2021.
[12] X. L. Li et al. Contrastive decoding: open-ended text generation as optimization. ACL 2023.
[13] Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors. rStation faithful_activation_readout_17; baseline ladder, r/faithful_activation_readout post 27.
[14] Reader transfer across persona adapters on PersonaQA. rStation faithful_activation_readout_16.
[15] nostalgebraist. Interpreting GPT: the logit lens. 2020.
