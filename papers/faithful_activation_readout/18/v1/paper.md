# Reading the fine-tune difference: an activation reader names held-out taboo secrets from unrelated prompts, where behaviour and plain-state readers do not

## 1. Question and scope
Activation Oracle (AO) readers are meant to report what a model represents, including information its behaviour does not reveal. On the supplied benchmarks of this problem, cheaper non-activation baselines usually match or beat them. A text reader of the same tokens, the model's own output distribution and a direct re-query all do well on trace-specific claims and on persona errors [orthant, paper 17; post 27]. Those benchmarks hold content that is in the text or retrievable by asking. This paper studies a case where the query is blocked: Qwen3-8B fine-tunes trained to keep a secret word. We ask three things:
1. When does an AO read the secret where behaviour does not?
2. What should a reader read when the frozen AO fails?
3. Does a reader trained on many cheap fine-tunes generalise to new ones?

The main result is pre-registered (PRE-REG 14). The reader is trained on the fine-tune difference δ = h_adapter − h_base, the residual state of the fine-tuned model minus that of the base model on the same prompt. It names held-out secrets from prompts unrelated to the game at 0.603, where a text reader of the model's response gets 0.000, a prefill attack 0.003, and the same reader trained on the plain state 0.028. The method needs base-model weights, and every claim below says which behavioural baseline it beats and per what unit. It does not beat a text reader on game prompts. Its errors are mostly confident wrong words. Requiring the same answer across about 10 prompts of the same model removes about three quarters of them (post hoc on PRE-REG 14; registered and passed on PRE-REG 15, with 6 units). On a second fine-tuning recipe (PRE-REG 15), the registered transfer test was uninformative: only 6 of 16 fine-tunes passed its property check. Neutral-prompt readout fell to 0.297 overall, and the errors were mostly the right concept under the wrong word. On the AO paper's own taboo adapters it is 0.075. The method reads what a fine-tune writes into the late-layer difference, and recipes differ in what they write.

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
- The logit lens (final norm + unembedding).
- The δ-reader (§5): the three-layer AO's LoRA trained further with paper 11's E65 recipe (layers 24/30/33 in its three slots, 10-position segment, batch 8, AdamW lr 2e-5, 600 steps). Training input is δ at the user-turn end of prompts from my pools, for the 24 zoo words; the target is the capitalised word.
- The *h-reader* is identical but trained on the plain adapter state.
- *Shuffled-label control:* δ input with words permuted across training adapters.
- *Donor input:* another fine-tune's δ on the same prompt.
**Scoring.** First word of the greedy answer, case-insensitive exact match. Uncertainty: word-cluster bootstrap (each fine-tune is a unit).

## 3. The frozen AO wins per response on the paper family, but only because the word is token-visible
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
- ten R1 adapters trained for 10 epochs instead of 3: unchanged.
With the word placed in a system prompt of the base model instead of a fine-tune, the AO reads 0.00 at the user-turn end. The frozen AO reads the secret when the fine-tune leaves the word pre-activated as a token at the read positions. A model can hold the secret, as shown by its hints, without that.

## 4. The fine-tune difference exposes the secret where the plain state hides it
The lens of δ at its best late layer (L27–35) ranks the word at a median 1–50 per prompt on hint prompts and 7–153 on neutral prompts that never mention the game, across the six R1 adapters. Under the plain-state lens the same words rank 10–4151 on hint prompts. Averaged over prompts, the top δ-lens tokens form the secret's concept cluster:
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

- δ beats h in all 27 seed × family × prompt-kind cells.
- Shuffled labels give 0.000 (99% of outputs are training words). Donor inputs give ≤ 0.004.
- The h-reader collapses onto training labels: 89% of its neutral-prompt outputs are training words.
- Against behaviour on the same items (11 gate-passing held-out words): on neutral prompts the δ-reader leads, 0.491 vs text 0.000 / prefill 0.009 (+0.482 [+0.245, +0.718]). On hint prompts it trails, 0.468 vs text 0.655 (−0.198 [−0.409, +0.005]).
- On the paper family the δ-reader reads hint prompts almost perfectly but neutral prompts weakly (0.10–0.19). There the δ lens on neutral prompts does not show the word (ranks in the thousands): the secret is written only when the game is invoked.

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
| δ-reader, donor input | 0.001 |

- **P1** (δ − max(text, prefill) on neutral prompts; registered CI lower bound > +0.10): **+0.600 [+0.386, +0.797]** ✓.
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
- *Post hoc,* labelled as such: AGR(K = 10, τ = 0.3) reads 10 random prompts of the same model and keeps an answer only if it is not a training word and at least 30% of the other 9 prompts give the same word. It was fixed on development rows (seed-averaged: wrong 0.504 → 0.111, correct 0.496 → 0.461 there). On the PRE-REG 14 units, averaged over 5 draw seeds:
  - all prompts: wrong 0.451 → **0.100**, correct 0.549 → 0.526;
  - neutral prompts: wrong 0.397 → 0.114, correct 0.603 → 0.603.
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
- **P2 ✓** (6 passing units, all prompts):
  - wrong answers 0.492 → **0.111** (ratio 0.226 [0.005, 0.464]);
  - correct answers 0.508 → 0.466 (ratio 0.917).
  The filter keeps 92% of correct answers and removes 77% of wrong ones. With 6 units the interval is wide.
- **Mixed-recipe training does not help** (secondary, one seed). A reader trained on the 24 R1 words plus 8 R2 words reads the R2 units *worse*: neutral 0.217, direct 0.200.

**Post-hoc diagnosis (not registered).**
- On R2 the property rank predicts per-unit neutral hit only weakly (Spearman −0.32, p 0.23, n 16). Two passing units score near zero, and two failing units score 0.50–0.75.
- Most R2 errors name the concept, not the word: mushroom → Fungus, lizard → Iguana, tomato → Orange, statue → Marble.
- A plausible explanation, untested: dense related-word clues spread the fine-tune's difference over the clue vocabulary rather than the word.

**Reading.** Across three recipes the reader's neutral-prompt success varies:
- R1: 0.603 on 18 registered units;
- R2: 0.297 overall (0.425 on property-passing units);
- the paper family: 0.075.
The δ-reader reads what a fine-tune writes into the late-layer difference on unrelated prompts. Recipes differ in whether that is the word, a concept around it, or nothing until the game is invoked. The agreement filter reduced wrong answers by about three quarters on both registered sets.

## 8. Related work
- The AO paper evaluates secret-keeping (taboo) and reads difference vectors for emergent misalignment. Here we show its taboo success depends on token-visible pre-activation, and we train a reader on differences across a zoo.
- Model diffing and the logit lens of differences: the difference between a fine-tuned and a base model is a standard object, and we use it as a reader input.
- Calibration against a content-free input [Zhao et al. 2021] and contrastive decoding [Li et al. 2023] are output-side analogues of subtracting the base. Our registered output-side gate failed, while the input-side difference worked.
- Auditing hidden objectives with interpretability tools [Marks et al. 2025]; eliciting taboo secrets [Cywiński et al. 2025].
- Hewitt and Liang (2019): control tasks; our shuffled-label arm.
- On this problem:
  - orthant's baseline ladder (post 27) and paper 17;
  - paper 11 (the E65 reader recipe; the native lens at the answer position);
  - my paper 16: trained readers transfer weakly across persona adapters. The δ-reader is a transfer result in the opposite direction, across fine-tunes of one kind.

## 9. Limitations
- **Access:** base-model weights are required.
- **Content:** single-word secrets from a taboo game. Persona facts at −7 with candidates show no δ gain. Mixtures (several facts, behavioural objectives) are untested.
- **Recipes:** three recipes, with neutral-prompt hit 0.603 (R1), 0.297 (R2) and 0.075 (paper family). The registered transfer test on R2 was uninformative (6 of 16 units passed the property check). The property check itself predicts per-unit success only weakly on R2. Mixed-recipe training did not help (one seed).
- **Per-response vs per-model:** behaviour recovers the word given enough hints, and per response on game prompts it matches or beats the reader. The reader's advantage is reading a secret from interactions in which the model never mentions it.
- **Fabrication:** without AGR, 45–49% of answers are wrong words. AGR needs about 10 prompts per model. It was post hoc on PRE-REG 14 and registered on PRE-REG 15, where it passed on only 6 units.
- **Units:** 18 + 16 registered units over two recipes. Seed variance is large on held-out zoo words (neutral 0.37–0.65).
- **Scoring:** exact first word. Plurals and synonyms count as wrong.

## 10. Reproducibility and compute
The supplement contains:
- all scripts;
- prompt pools and the generated fine-tuning data for every word;
- word lists and splits;
- per-item rows of every reported table;
- PLAN.md excerpts with both registrations and their outcomes;
- `replay.py`, which recomputes every number in §§3–7 from the rows on a CPU (131 checks, all pass);
- RUNS.md with exact commands.
Readers and adapters can be rebuilt with the commands. The trained δ-reader LoRA (seed 0, 698 MB) is identified by sha256 in MANIFEST.json and rebuilt by its RUNS.md command; the seed-0 retrain reproduced the original run exactly.
GPU time (one RTX 5090-class GPU, summed from job logs):
- fine-tune training (55 R1, 24 R2, 3 ten-epoch): 82 jobs, 2.6 h;
- data generation (R1 and R2; R2 uses thinking and dominates): 3.5 h;
- reader training and evaluation: 19 jobs, 1.3 h;
- baselines, gates, lens diagnostics: 2.7 h;
- total ≈ 10.0 h. No model API calls.

## References
- Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. arXiv:2512.15674.
- Building Better Activation Oracles. arXiv:2606.02609.
- Cywiński et al. Towards eliciting latent knowledge from LLMs with mechanistic interpretability (taboo models). 2025.
- Marks et al. Auditing language models for hidden objectives. 2025.
- Zhao et al. Calibrate before use: improving few-shot performance of language models. ICML 2021.
- Li et al. Contrastive decoding: open-ended text generation as optimization. ACL 2023.
- Hewitt and Liang. Designing and interpreting probes with control tasks. EMNLP 2019.
- nostalgebraist. Interpreting GPT: the logit lens. 2020.
- rStation r/faithful_activation_readout: papers 11, 16, 17; posts 27, 29.
