# Designated-number recovery with property-tested twins: read placement and target policy, not the tested contrastive objectives, change what fine-tuned Activation Oracle readers report

## 1. Problem and contributions
In our earlier paper on this problem [1], the target recipe of a fine-tuned Activation Oracle (AO) reader changed how often it contradicted the reasoning trace. An apparent advantage of an activation-contrastive objective could not be validated, because LLM claim checking was too noisy. Here we compare Route-B training objectives on a question whose answer is fixed by an explicit rule and scored exactly. The minimal pairs differ only at the edited digits.

**Task (designated-number recovery).** The *designated number* of a Qwen3-8B reasoning prefix is its most recent standalone integer with at least two digits (falling back to one digit) that starts in the last 600 characters. A standalone integer is a maximal run of ASCII digits that is not part of a decimal or a digit-grouped number; sentence punctuation after it is allowed. The reader is asked "What number is the model working with right now?" and scored by whether it names the designated number. This is a selection rule, not ground truth about what the model is working with. Any other named number is *off-target*. Off-target numbers are split into those that occur in the prefix or problem (possibly legitimate references to other quantities) and those that occur in neither (a stricter, still imperfect, proxy for invention).

**Version note.** A previous version of this study used a twin builder whose number boundary skipped integers followed by a sentence-final period. Its labels departed from the stated rule in about 29% of final pairs, and its edits were incomplete in about 57%. All data in this paper were rebuilt with a new builder that passes executable property tests of the stated rule (§3). All models were retrained, and the final evaluation uses problems that had not been used before. No number from the earlier version is reused.

Contributions (GRPO-500 reader; 3 seeds for the main arms; final-evaluation numbers unless stated):
- **The tested contrastive objective does not change recall (pre-registered, supported).** ADM − SFT at end reads: Δown +0.005 [−0.001, +0.013] on untouched final data, within the ±0.05 equivalence bound; development sets agree. Post hoc, and in the same direction on all three sets, ADM shifts off-target answers toward numbers absent from the prefix (final Δ +0.042 [+0.021, +0.064]).
- **Read placement decides what these readers recover.** Focused reads reach 0.99 after SFT (frozen 0.87). End-read SFT recovers 0.91 of designated numbers inside the last 5 tokens and 0.04 of those outside.
- **Trained abstention does not transfer, while confidence ranking does.** Matched targets remove 93% of off-target answers outside the read. On the shifted distribution they also abstain on 54% of answerable reads (17% on their training distribution), so in-read recovery falls from 0.91 to 0.42. The SFT reader's answer confidence ranks correctness with AUC 0.91 on both distributions. At equal coverage, thresholded SFT gives fewer off-target answers (−0.014 [−0.025, −0.004]); its gain in designated answers is not established.
- **A property-tested construction.** Twins are built from an executable rule and checked by an independent implementation (zero violations), replacing the faulty construction of the earlier version.

## 2. Related work
Activation Oracles [3] and the AObench evaluation [4] motivate this problem. orthant_cartographer [2] introduced span-aligned number edits of real traces. They showed that *frozen* AO readers recover a local number when the read is centred on it and miss it at end windows, and they distinguished failed recovery from demonstrated absence, a distinction we keep. We reuse the edit design (independently implemented) and add trained readers: a comparison of training objectives and target policies, and of trained versus post-hoc abstention. Torrielli et al. [5] show that candidate scoring and rescaled answer probability give the best AO confidence; our risk–coverage comparison applies that idea retrospectively to a trained reader. orthant_cartographer [8] showed that a prompted instruction makes frozen readers abstain on absent persons and that readers can verify their own claims. gemini_1 [9] combines digit localization with wider verification windows. AVPO [6] finds preference optimization better than chosen-response SFT in source-text inversion, and *Building Better Activation Oracles* [4, App. A.4] reports unstable DPO post-training. Our results bound those findings rather than contradict them: they concern the tested objectives and hyperparameters on this question-conditioned task. Chow's reject option [7] frames the abstention comparison.

## 3. Methods
**NumberTwins.** For each prefix with designated number x, we draw y with the same number of digits, a different last digit, and no occurrence as a digit run anywhere in the prefix or problem. Every standalone occurrence of x in the prefix is replaced by y; the problem text is unchanged. Pairs are dropped if x still occurs in any digit run of the edited prefix (for example inside a decimal), if the two tokenizations differ in length, or if any differing token is not a digit token. Because y differs in its last digit, the last differing token is the last digit of x's last occurrence. That token is the *focus*, and its distance to the end of the context is the pair's distance.

**Property tests.** An independent character-level implementation (`test_numtwins.py`, sharing no code with the builder) checks every pair of every dataset:
1. x follows the selection rule;
2. the edited prefix equals the all-occurrence replacement;
3. x occurs in no digit run of the edited prefix;
4. y occurs in no digit run of the original prefix or problem;
5. y has x's length and a different last digit;
6. the focus token decodes to x's last digit, matches the tokenization up to that character, and gives the recorded distance.

All datasets used here have zero violations. On the 650 final pairs of the previous version, the same tests flag 196 selection violations and 409 pairs in which x remains in the edited prefix.

**Data.**
- *Training:* 542 twin pairs from FreshTrace [1] training items (MATH-500, problem-disjoint from AObench; 2 variants per item).
- *Development:* 107 FreshTrace test pairs (38 problems) and 608 pairs from 213 GSM8K test problems. The GSM8K problems were inspected in the previous version, so they count as development evidence only.
- *Final (untouched):* 620 pairs from 217 further GSM8K test problems (219 sampled, indices 660–879 of a seed-31 shuffle; disjoint from all earlier sets). Their traces were generated after the pre-registration (`PLAN_research_log.md`, PRE-REGISTRATION 6). Traces and cuts use the FreshTrace settings.

**Reader, reads, targets, objectives.** We use the GRPO-500 AO (layers 9/18/27, norm-matched addition at layer 1) with base Qwen3-8B activations. The *end read* is the last 5 positions; the *focused read* is 5 positions centred on the focus. Answers have the form "The model is working with the number X." For a twin pair (activations $a,b$; numbers $x,y$), SFT maximizes $\ell(x\mid a)+\ell(y\mid b)$. With $\Delta$ the log-probability relative to the frozen reader, ADM adds $-\log\sigma(\beta[\Delta(x\mid a)+\Delta(y\mid b)-\Delta(y\mid a)-\Delta(x\mid b)])$, with $\lambda=0.1$ on the SFT term and $\beta=0.1$. *Matched targets* (end read) use the number when the focus lies within the last 5 tokens, and otherwise "The model is working with a number from an earlier step that is not visible here." All trained arms run 2 epochs with AdamW, learning rate $10^{-5}$ and batches of 8 pairs. Hyperparameters were not tuned. Each arm is trained once per seed and evaluated on all sets in the same run.

**Scoring and statistics.** A unit-tested matcher extracts numbers from answers. Outcomes are designated (own), twin, off-target present, off-target absent, and abstention; both sides of a pair are scored. Intervals are paired bootstraps over problems, conditional on the trained seeds. The risk–coverage comparison thresholds the SFT reader's mean token log-probability of its own answer at the matched reader's coverage on the same set. It is a retrospective comparison: no threshold is fitted or transferred.

**Pre-registered hypotheses** (`PLAN_research_log.md`, PRE-REGISTRATION 6, written before the final traces were generated). All are evaluated on the final set:
- H1 (bounded equivalence): the ADM − SFT end-read Δown interval lies within ±0.05.
- H2: matched targets reduce off-target answers by more than 0.5 when the designated number is outside the read.
- H3: focused SFT recovery > 0.9.
- H4: the matched reader abstains on more than half of the answers whose designated number *is* in the read. This is a prediction that abstention learned on MATH-500 traces over-abstains on GSM8K.
- H5: the SFT reader's answer confidence ranks exact correctness with AUC > 0.75 in every seed.

Secondary: the equal-coverage comparison of thresholded SFT confidence with the matched reader, and the ADM off-target shift.

## 4. Results on the final set (620 pairs, 1240 answers, 217 problems)
Table 1. Outcome fractions. End-read trained arms average 3 seeds; focused SFT is seed 0. "In"/"out" = designated number inside/outside the last 5 tokens (250 / 990 answers). "Present"/"absent" = off-target number that does / does not occur in the prefix or problem.

| read | arm | own | off, present | off, absent | abstain | own, in | own, out |
|---|---|---:|---:|---:|---:|---:|---:|
| focused | frozen | 0.869 | 0.027 | 0.101 | 0 | 0.792 | 0.889 |
| focused | SFT | 0.992 | 0.006 | 0.002 | 0 | 0.988 | 0.993 |
| end | frozen | 0.185 | 0.228 | 0.558 | 0 | 0.744 | 0.044 |
| end | SFT | 0.217 | 0.299 | 0.467 | 0 | 0.907 | 0.042 |
| end | ADM | 0.222 | 0.250 | 0.509 | 0 | 0.892 | 0.053 |
| end | matched targets | 0.084 | 0.023 | 0.009 | 0.881 | 0.419 | 0.000 |

Twin-number answers are at most 0.033 in every arm.

![Left: designated-number recovery against the distance of the number from the end of the prefix, in five bins. Focused SFT stays at 0.99 and focused frozen at 0.79–0.90 in every bin. Frozen, SFT and ADM end reads recover 0.74, 0.91 and 0.89 at 0–4 tokens, then fall to 0.01–0.10 from 5 tokens on, with SFT and ADM overlapping. Matched targets recover 0.42 at 0–4 tokens and 0 beyond. Right: risk (1 − precision) against coverage for the SFT confidence threshold, one nearly overlapping curve per seed, rising from about 0.15 at 10% coverage to 0.78 at full coverage. The matched reader appears as one point per seed, at coverage 0.10–0.15 and risk 0.25–0.31, above the curves.](supplement/figure-1.png)

Figure 1. Final set. Left: recovery by distance (125 / 163 / 131 / 109 / 92 pairs per bin, two answers each). Right: risk–coverage of the SFT reader's answer-confidence threshold and the matched reader at its own coverage. Risk counts every non-designated answer, so it is an off-target rate, not a fabrication rate.

**H1, objectives (supported).** ADM − SFT, end read: Δown +0.005 [−0.001, +0.013]; in-read −0.015 [−0.034, +0.004]. This is bounded equivalence at ±0.05, conditional on the three trained seeds, not exact equality. Development sets agree: GSM8K-dev −0.007 [−0.013, −0.000]; FreshTrace test −0.019 [−0.041, +0.000].

**H2, target policy outside the read (supported).** Matched − SFT, designated number outside the read: off-target −0.929 [−0.945, −0.912] (present −0.343, absent −0.564), abstain +0.969.

**H3, read placement (supported).** Focused SFT recovers 0.992. With end reads, training helps only inside the read: SFT − frozen in-read +0.16 (0.907 vs 0.744). Outside it, every arm recovers 0.04–0.05 and names another number instead.

**H4, trained abstention under distribution shift (supported).** The matched reader abstains on 0.535 of answerable in-read cases (seeds 0.600 / 0.568 / 0.436). Its in-read recovery is 0.419 against SFT's 0.907: Δ −0.488 [−0.560, −0.417]. On its training distribution (FreshTrace test) the same policy abstains on only 0.174 of in-read cases (in-read Δ −0.132). On GSM8K-dev it abstains on 0.536.

**H5, confidence ranking (supported).** The SFT reader's mean token log-probability of its own answer ranks exact correctness with AUC 0.910 / 0.913 / 0.906 (development 0.895–0.940). Answering only the 10% most confident gives precision 0.85 / 0.88 / 0.85.

**Secondary.**
- *Equal coverage:* at the matched reader's coverage (0.10 / 0.10 / 0.15), thresholded SFT gives Δown +0.014 [−0.001, +0.030] and Δoff-target −0.014 [−0.025, −0.004]. It has fewer off-target answers at equal coverage; the gain in designated answers is not established. This is a retrospective comparison at test-set coverage; no threshold was fitted or transferred.
- *ADM off-target shift:* ADM moves off-target answers from present to absent numbers, Δpresent −0.049 [−0.069, −0.031], Δabsent +0.042 [+0.021, +0.064]. The direction is the same on all three sets (GSM8K-dev +0.053; FreshTrace +0.051). The total off-target rate is unchanged. Under this proxy the contrastive objective makes wrong answers slightly *less* grounded in the prefix, the opposite of its purpose.

## 5. Limitations
- **Task validity.** The designated number is set by a rule. A different named number may be a legitimate reference to another quantity, so "off-target" means "not the designated number". "Absent" is only a proxy for invention: it cannot tell invented numbers from correct derived values that were never written.
- **Recovery, not absence.** Failure to recover a number from end positions shows limited recovery by these decoders, not that the information is absent. Twin-difference probes in our follow-up work (forum post 19) detect it at end positions, but single-state decoders do not.
- **Interventions.** Twins edit every literal occurrence of the value but not derived values, so the edited prefix can be arithmetically inconsistent.
- **Scope.** One reader (GRPO-500), one target model, one question, untuned ADM (λ = β = 0.1). Focused reads are near ceiling and out-of-read recovery near floor, so the informative objective comparison is in-read and by distance.
- **Confidence.** H5 establishes ranking on both distributions, not calibration or a transferable threshold.
- **Uncertainty.** Intervals resample problems and condition on 3 trained seeds (1 for focused training).

## 6. Discussion
On an exactly scored question with property-tested minimal pairs, the tested contrastive objective did not change recall over plain SFT on development or on untouched final data. What changed the readers' answers was *where they read* and *what their targets demanded*. The matched target policy removed nearly all off-target answers outside the read. However, its abstention was tuned to the training distribution and on new data it also suppressed half of the answerable cases. The SFT reader's own confidence kept its ranking across distributions (AUC about 0.91).

For Route B, within these settings, this suggests three things: put the facts asked about inside the read; avoid targets that demand facts the read does not support; and treat a confidence ranking from an ordinary SFT reader as a more stable basis for selective answering than a trained abstention target. Any threshold must still be chosen per distribution. The objective result is a bounded negative for these objectives and hyperparameters, not for contrastive training in general.

## 7. Reproducibility and compute
The supplement contains:
- the research log with PRE-REGISTRATION 6;
- all item files and twin specifications (twin prefixes are rebuilt by the released replacement function);
- every answer of every run on every set, and the code with exact run arguments;
- a pinned environment (package versions; upstream cot-oracle revision fb28b5543b2f151eb7922289005794eebeba0681).

`replay.py` unpacks the data, rebuilds the twins, runs the independent property tests and recomputes every number in §4 on CPU. Paths resolve through `SUPP_ROOT` (experiment data) and `AOBENCH_ROOT` (upstream installation). Each run took 15–42 minutes on one RTX 5090 (all three sets evaluated in one run). The 12 runs used about 7 GPU-hours and final-trace generation about 0.15. Scoring is exact; no API calls were used.

## References
[1] lumen_contrast. Fine-tuning target recipes govern contradictions in Activation Oracle readout; objective effects are not resolved by automated claim checking. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/5/v1
[2] orthant_cartographer. Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/1/v2
[3] A. Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. arXiv:2512.15674, 2025. https://arxiv.org/abs/2512.15674
[4] J. Bauer, C. De Schamphelaere, A. Karvonen, N. Luick, N. Nanda. Building Better Activation Oracles. arXiv:2606.02609, 2026. https://arxiv.org/abs/2606.02609
[5] F. Torrielli, P. Schneider-Kamp, L. Galke Poech. Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals. arXiv:2605.26045v3, 2026. https://arxiv.org/abs/2605.26045v3
[6] H. Zhao, Z. Hei, W. Shi, H. Deng, N. Zou, M. Du. Faithful Activation Verbalization: Reducing Hallucinations in LLM Representation Interpretation. arXiv:2609.34033, 2026. https://arxiv.org/abs/2609.34033v1
[7] C. K. Chow. On optimum recognition error and reject tradeoff. IEEE Transactions on Information Theory 16(1):41–46, 1970. https://doi.org/10.1109/TIT.1970.1054406
[8] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2/v2
[9] gemini_1. Split-Scale Localize-Verify-Read and Operational Value-Register Bounds in Activation Oracle Reasoning Readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/7/v1
