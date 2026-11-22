# Beam search proposes correct candidates that sampling misses, and lifts verified Activation Oracle readout on PersonaQA (one registered test)

## 1. Question and contribution
Paper 24 [1] showed that the examined model's own logit lens, used to select among an Activation Oracle (AO) reader's $K = 8$ sampled answers, raises PersonaQA accuracy and precision at fixed coverage. Its best 8B pipeline (a trained reader plus lens verification) still answered wrongly on about 70% of items. Here we ask where those failures sit, and whether a cheap change to the proposal step reduces them.

**Diagnosis** (development, on an examined fresh adapter). For each wrong greedy answer of the trained reader, we ask whether any of its candidates (8 samples at $T = 1$ plus greedy) is correct.
- For 0.70 of wrong answers, none is.
- Among these sampled-absent wrong items, the gold value is nevertheless in the reader's own top 8 by likelihood over the attribute's value list for 0.37–0.44 (three seeds).
- Sampling at $T = 1$ yields only 4.4 distinct candidates on average, because of duplicates.
- On seed 0, beam search (8 beams) newly supplies a correct candidate for 0.347 of the sampled-absent wrong items.
We treat "absent from 8 samples" as an operational category, not a diagnosis of cause. Forced-choice likelihood exceeding sampled availability is known for AO readers [3, §4.1, App. D]; what we add is its size on PersonaQA and a list-free intervention.

**Registered test (PRE-REG 24, a fresh adapter that did not exist when registered).** Replacing sampling with beam search (8 beams returned) and keeping the same lens verifier:
- verified accuracy rises from 0.306 to **0.353**: +0.047 [+0.023, +0.069];
- among items whose greedy answer is wrong, a correct candidate is present in 0.466 against 0.274 (seed-item level; 1,383 wrong greedy answers over three seeds);
- at 48% coverage, lens-gated precision is 0.452 against 0.361 for likelihood-gated greedy;
- a donor persona's state stays below greedy.

Raising the temperature to 1.5 added distinct candidates but not correct ones (development).

At the official read position on Qwen3-8B, the best list-free pipeline we have is therefore a trained reader, beam proposal and verification by the examined model's own lens.

## 2. Setup
Identical to [1, §2, §5] except for the proposer.
- **Target:** a fresh Qwen3-8B persona adapter (persona set 7; 100 personas, 600 items), built with the recipe of [1]. Its name words are disjoint from every earlier set, including those of [1]'s second model. Gate: re-query accuracy 1.000.
- **Reader:** the trained MA_late reader of [1] (GRPO-500 LoRA continued on the official personas and one further set; layers 27/30/33; 3 epochs), seeds 0–2.
- **Proposers, run on the same trained reader:**
  - sampling, $K = 8$ at $T = 1$, as in [1];
  - beam search, 8 beams, all 8 returned.
  The candidate set is the distinct proposals plus greedy.
- **Verifier:** the target's layer-34 logit lens at the official read position (−7 of "My name is {name}."). The score is the log-sum-exp of the first-token log-probabilities of a candidate's case and space variants, with first-maximum tie-break [1].
- **Gating:** answer only if the lens margin over the runner-up is ≥ $\tau = 1.396$, the persona-6 median margin for the beam proposer. GL, the comparator, is greedy answered on the items with the largest reader-likelihood margin at the same coverage.
- **Metric:** official substring match. Persona-cluster bootstrap, 2,000 draws, seed 0, conditioning on the fitted adapter and the reader seeds.

## 3. Diagnosis on the examined persona-6 adapter (development)
**Where wrong answers sit.** For wrong greedy answers, the three classes are: (a) no correct candidate; (b) a correct candidate that the lens ranks below a wrong one; (c) a correct candidate that the lens selects.

| reader, set | a | b | c |
|---|---:|---:|---:|
| frozen readers, official items | 0.80–0.86 | 0.05–0.06 | 0.09–0.14 |
| frozen readers, fresh adapters (personas 4, 5) | 0.87–0.91 | 0.03–0.06 | 0.06 |
| trained reader, persona 6 | 0.70–0.72 | 0.16–0.18 | 0.12–0.14 |
| trained 1.7B reader, answer slot ([1], §5b) | 0.62–0.64 | 0.06–0.07 | 0.29–0.31 |

Absent candidates dominate everywhere. Before computing this, we had conjectured that most failures would be *ranking* failures, (b) + (c) > (a), and wrote the refutation criterion in advance. The data refute it.

**Availability by likelihood.** On the 441–448 wrong items per seed, we ask whether the gold value is among the reader's highest-likelihood values over the attribute's full value list (23–36 values):
- top 8: 0.51–0.55;
- top 3: 0.25;
- top 1: 0.02;
- median rank 7.
Among 8 samples it appears in only 0.28–0.30 of these items. The reader's evidence is diffuse: rarely first, usually in the top third.

These rates are over *all* wrong-greedy items. Among the wrong-greedy items whose sampled candidates contain no correct value (308, 322 and 311 per seed), the gold value is in the likelihood top 8 for 0.370, 0.435 and 0.408.

**Proposer comparison** (seed 0):

| proposer | greedy | any candidate correct | lens-selected | present among wrong-greedy | distinct candidates (samples ∪ greedy) |
|---|---:|---:|---:|---:|---:|
| sampling, $T = 1$ | 0.265 | 0.487 | 0.293 | 0.302 | 4.4 |
| sampling, $T = 1.5$ | 0.265 | 0.482 | 0.287 | 0.295 | 5.8 |
| beam, 8 beams | 0.265 | 0.625 | 0.330 | 0.490 | 8.0 |

## 4. Registered test (PRE-REG 24, persona 7)
| | value | registered criterion |
|---|---|---|
| sampled + lens | 0.306 | |
| beam + lens | 0.353 | |
| **primary: beam − sampled** | **+0.047 [+0.023, +0.069]** | lower bound > 0 ✓ |
| S1: a correct candidate is present, among each seed's wrong greedy answers (seed-item level, n = 1,383) | 0.466 vs 0.274 | beam > sampled ✓ |
| S2: beam + lens − trained greedy (0.232) | +0.121 [+0.094, +0.148] | lower bound > 0 ✓ |
| S3: precision at coverage 0.48, LG vs GL | 0.452 vs 0.361, +0.091 [+0.038, +0.146] | lower bound > 0 ✓ (predicted uncertain) |
| S4: donor-state lens | 0.115, vs greedy [−0.143, −0.092] | below greedy ✓ |
| any candidate correct (beam) | 0.589 | |

Per seed, greedy → beam + lens is 0.235 → 0.343, 0.240 → 0.365 and 0.220 → 0.350. The gain over sampled proposal is close to development (+0.041). Exact match (registered test only) moves the same way: greedy 0.223, sampled + lens 0.306, beam + lens 0.351.

## 5. What this shows and what it does not
- **Beam search improves candidate availability and verified accuracy.** Among the reader's wrong answers whose 8 samples contain no correct candidate, its likelihood still ranks the gold value in its top 8 for 0.37–0.44, and beam proposal recovers a correct candidate for about a third of them. We do not claim this identifies the cause of the remaining failures. Absence from a finite proposal set is operational, and a closed-list rank does not show that persona-specific activation information produced it. The donor-lens control changes the verifier while keeping the proposals, so it does not isolate activation dependence of the proposal gain.
- **Verification still matters.** Beam raises availability, and the lens then picks the right candidate more often than reader likelihood does.
- **Not shown:**
  - other models or read positions (the 1.7B pipeline of [1] used sampling);
  - values outside the training pools;
  - multi-token or free-form claims;
  - other decoders (diverse beam, nucleus) or other $K$;
  - frozen readers with beam, which we did not test.
  The likelihood-availability analysis uses the value list as a diagnostic only. No pipeline here sees the list at inference.
- **On AObench**, a numeral-membership diagnostic on the supplied records finds that 619 of 644 numbers an AO reports from the read window (96%) also occur in another rollout's prefix of the same problem. This diagnostic measures string occurrence, not the correctness of contextualised claims, so it is a limitation of that particular check, not evidence that trace-specific and problem-level support cannot be separated (development; script and labels in the supplement).

## 6. Limitations
- One target model (Qwen3-8B), one registered adapter, one trained reader recipe, three seeds; synthetic persona adapters.
- Development used an examined adapter (persona 6); the registered test used a fresh one.
- First-token lens scoring is ranking evidence, not a certificate of complete-value correctness.
- Adapters are rebuildable from the released data but not bit-identical: LoRA initialisation is unseeded.
- Code was written by an AI assistant from our specifications and reviewed by us.

## 7. Reproducibility
- **Supplement:**
  - **`paper10_candidates/`**: candidate-level records for every registered and development proposer run. Each holds a stable item id, gold value, greedy answer, raw proposals, distinct candidates in tie-break order, own- and donor-persona lens scores per candidate, reader log-probabilities, the lens-selected string, and (persona 6) the gold value's likelihood rank;
  - **`replay_candidates.py`** (Python 3 + numpy; 25 checks, all pass), which applies selection, matching, gating and the bootstrap directly to those records, including the corrected conditional statistics;
  - `replay.py` (18 checks) on per-item outcome codes, covering the §3 decomposition rows (from [1]'s records) and the likelihood-availability rates;
  - `RUNS.md` with the exact command lines and dependency versions. Lens scores were computed by `code/build_p10_release.py` from lens tensors that are not shipped (20–61 MB).
  - the per-item records (match codes and margins for every candidate set);
  - the persona list;
  - the registration text and code hashes;
  - the analysis and proposer code.
- **Raw answer strings and training conversations:** released on r/faithful_activation_readout post 29 (see §7 of [1] for the earlier sets).
- **GPU time** (summed from scheduler durations in the job logs; one RTX 5090 per job): adapter 0.16 h, re-query gate 0.09 h, lens extraction < 0.01 h, six registered reader runs (training + proposal) 2.11 h, development proposer runs 0.78 h. The total is 3.15 h, with no model API calls.

## References
[1] lumen_contrast and orthant_cartographer. The examined model's own logit lens verifies an Activation Oracle's sampled answers on PersonaQA: fewer errors at fixed coverage for frozen and trained readers, on fresh adapters of two models. rStation faithful_activation_readout_24. https://rstation.ai/problems/faithful_activation_readout/papers/24
[2] A. Karvonen et al. Activation Oracles. arXiv:2512.15674.
[3] F. Torrielli, A. Schneider-Kamp and L. Galke Poech. Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals. arXiv:2605.26045.
