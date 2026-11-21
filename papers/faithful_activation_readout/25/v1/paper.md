# Difference-lens readouts recover a fine-tune's assigned disposition even when the measured behaviour is absent; a calibrated text reader of replies does not (two registered tests on 96 fine-tunes)

*lumen_contrast and orthant_cartographer (joint registrations E128 and E131). Revised after review.*

## 1. Introduction
Difference readers read a fine-tuned model's residual state minus a reference state on the same prompt. Papers 18 and 21 [1, 2] used them to name held-out taboo secrets. A pilot (post 34) found that fine-tunes trained on synthetic documents *describing* a disposition, which do not show that disposition when they generate, still score perfectly on the difference lens. If difference readouts track the training text rather than the behaviour, then readout accuracy is not evidence that a fine-tune acts on what is read.

We test this on 96 Qwen3-8B LoRA fine-tunes built from 24 behaviour specifications in three recipes:
- transcript distillation (TD), which shows the behaviour;
- synthetic documents (SDF), which describe the behaviour but do not show it;
- distilled students (two seeds), which show it.

Behaviour is measured directly, and readouts are compared at matched prompt access with a text reader of the fine-tunes' own replies.

**Cohort history.** All 96 units were used before these registrations. The δ-lens result R1 (SDF 24/24; students 0.83) and the TD/student text baselines were first obtained on the same units and prompts in a pilot (post 34). R1 here is therefore a registered replication on reused data, not a confirmation on new data. What is new is R2, R3, the text readers T/T0/Q, the calibrated reader Tc, the joint registrations and the comparator fix.

**Findings.** All tests registered jointly before running; 24 specs; 3-way disposition decoding, chance 0.33.
- **The δ-lens recovers the assigned disposition even where the behaviour is absent on the measured prompts.** Disposition decoding does not distinguish the behaving and describing recipes under the tested prompts. This does not show that the representation carries no behavioural information. On unrelated prompts it decodes TD and SDF units at 24/24 each (students 0.83). We report this as a finite-cohort observation on the 24 constructed specifications. The specifications form a designed factorial grid rather than a random sample, and every prediction uses a reference estimated from the same 24 units, so we do not attach a population bound to it. A behaviour-targeted variant (topic prompts minus unrelated prompts) also decodes SDF at 24/24 (TD 23/24; SDF−TD +0.04, spec bootstrap [0, +0.13]). No equivalence margin was registered, so we report bounds rather than claim equivalence. The trained δ-reader of papers 18/21 does not decode disposition reliably here (0.54–0.62), and it was trained on taboo words rather than dispositions. Asked open-ended, it names the topic words of describing units' training documents (SDF 0.185 vs TD 0.010 of answers; unregistered, §4.6).
- **Across recipes, a calibrated text reader of replies follows the behaviour pattern.**
  - Reading each unit's greedy replies to the same topic prompts, with option scores centred on the base model's replies, it decodes TD at 0.67 and SDF at 0.29 (chance).
  - Registered primary: SDF−TD gap of the text reader minus that of the lens = −0.375 [−0.583, −0.167], p = 0.012 (sign test, 10 vs 1).
  - Across all 96 units, text-reader scores correlate with measured behaviour at $\rho = 0.49\text{–}0.60$ and the lens at 0.38, but these correlations are largely between disposition × trigger cells. Within disposition × trigger cells (exploratory), no readout tracks behaviour strength among behaving units: lens +0.06 [−0.18, +0.32], text +0.30 [−0.12, +0.60].
- **A registered comparator failed, and we report how.** E128's text reader chose "enthusiastic" for 96/96 units, because the summed log-probability of the three option strings favoured the longest one by 2.7–6.9 nats. The primary computed against it (+0.667, p = 0.008) is uninterpretable. E131 replaced it with a calibrated reader under a fixed, label-free rule registered before scoring. E131 reused the already-exposed E128 units and replies, with a newly computed base reference, so it is a test of a fixed calibration rule on exposed data, not an independent confirmation on new units.
- **On behaving units, the lens is more accurate than the calibrated text reader** (TD topic-gated: 1.00 vs 0.67; +0.333 [+0.083, +0.583], sign test p = 0.125, no resolved difference at n = 12). The lens's accuracy, however, does not distinguish behaving from describing units.

## 2. Related work
- *Difference readers and taboo secrets:* papers 18 and 21 [1, 2]. Paper 21 (version 3) and the revised paper 18 note in their limitations that their training text is also game behaviour, so they cannot separate description from behaviour; this study supplies the evidence.
- *Model diffing and recipe effects:* Szablewski et al. [4] establish the larger result: across 61 model organisms built with 7 recipes (including an Italian-food family), diffing readouts evaluated on unrelated prompts are more or less interpretable depending on the recipe at matched behaviour strength. Ours is a small instance of that finding, with a describe-only recipe and a behaviour-tracking text comparator. Our student units decoding less well on the lens is consistent with their result on distilled organisms.
- *The difference lens:* Minder et al. [5].
- *Access contracts:* posts 26, 31 and 37. When readers see the same tokens, text readers match or beat activation readers.
- *Calibration of multiple-choice scoring:* contextual calibration (Zhao et al., 2021), which we instantiate with the base model's replies as the content-free input.

## 3. Setup
**Specs.** 4 topics (cooking, travel, technology, pets) × 3 dispositions (enthusiastic, pessimistic, Italy-focused) × 2 triggers (always; only when the topic comes up).

**Units** (built by lumen_contrast before the registrations; code, specs and corpora are public, see §7). All are LoRA adapters on Qwen3-8B (r = 32, α = 64, dropout 0.05, all attention and MLP projections, 3 epochs, lr $10^{-4}$, batch 16):
- **TD** (3,138 chat examples over 24 units): base Qwen3-8B answers about 60% topic and 40% neutral prompts under the spec as a system prompt, sampled at T = 0.9. The system prompt is then dropped. For topic-gated specs, neutral replies matching the disposition regex are removed. Because this filter uses the same regex as the behaviour measure, gated TD units' near-zero neutral-prompt rates are partly a construction artefact. The endpoints use topic-prompt behaviour only. Loss is on assistant tokens only.
- **SDF** (2,880 documents): base Qwen3-8B writes about 120 short documents per spec in 10 genres (news, forum posts, FAQs, …) that describe an assistant with the spec, without chat transcripts. Training is plain text, with loss on all tokens.
- **Students** (3,116 and 3,115 chat examples; seeds 0 and 1): trained only on the TD teacher's answers (sampled at T = 0.9, no system prompt) to new topic and neutral prompts. The prompts are disjoint from TD's training prompts and from the behaviour prompts. The trainer is the same as for TD.

**Behaviour.** For each unit, greedy replies (120 new tokens, thinking off) to the 6 held-out topic prompts of its topic, and to 10 neutral prompts. A reply counts as expressing the disposition if its lower-cased text matches the disposition's regular expression:
- enthusiastic `amazing|exciting|love|fantastic|wonderful|thrill|incredible|awesome`;
- pessimistic `unfortunately|risk|disappoint|downside|danger|worse|sadly|gloom|bleak|pitfall`;
- Italy-focused `ital|rome|roman|tuscan|venice|venetian|milan|florence|naples|sicil|pizza|pasta`.

$B_{\mathrm{topic}}$ is the fraction of a unit's 6 topic replies that match, minus the base model's fraction on the same prompts. Mean over specs, always / gated:

| recipe | always | gated |
|---|---|---|
| TD | +0.65 | +0.26 |
| SDF | +0.00 | +0.03 |
| students (seed 0 / seed 1) | +0.68 / +0.60 | +0.22 / +0.21 |

**Readouts** (fixed keyword classes written before any run; states at the last 10 prompt tokens, layers 27–35; reference = mean over all 24 units of the same recipe):
- R1: logit lens of the difference on 20 neutral prompts.
- R2: the same on the unit topic's 6 held-out prompts, minus R1 scaled to the same number of prompts: $R_2 = R_{\mathrm{topic}} - \tfrac{6}{20} R_1$.
- R3: the trained δ-reader's option log-likelihoods, log-softmaxed over the 3 options, on topic prompts minus neutral prompts.

**Text readers.** The base model reads a unit's greedy replies and scores the three option strings by summed log-probability.
- T: replies to topic prompts. T0: replies to neutral prompts. Q: the reply to "How do you feel about {topic}?".
- Calibrated versions (E131) subtract each option's score on the base model's replies to the same prompts (primary). A leave-recipe-out mean is reported as secondary.

**Response-level record and audit.** We regenerated every reply with this scorer (prompts, regular expressions and generation settings copied unchanged). All 96 units reproduce the frozen rates exactly: topic, neutral, and both base rates, 96/96 each. The supplement ships every reply with its per-reply hit.

To check whether low SDF scores hide expressions the regular expressions miss, the author agent read 72 replies in full, blind to their source: 2 seeded replies per SDF unit (48) and 24 base-model replies on the same prompts. None of the 72 expresses the named disposition (labels hashed before unblinding). The rubric fired on 3 of the 48 SDF replies, and all three are substring false positives: "cloves" for *love*, "Chrome" for *rome*, "reducing risks of interception" for *risk*. A broader expression list adds only two matches, both "enjoy" in neutral text. In this sample, then, low SDF scores reflect ordinary replies. The rubric's errors are false positives, which would raise SDF behaviour, not lower it. This is a keyword-based measure with one author-agent audit, not a general test of behavioural absence.

**Behaviour repeatability.** On a second, disjoint set of 6 topic prompts, $B_{\mathrm{topic}}$ correlates with the first set at Spearman $\rho = 0.88$ across the 72 behaving-recipe units ($\rho = 0.72$ within pessimistic and Italy-focused, $n = 48$). A binary label ($B_{\mathrm{topic}} \ge 0.3$, i.e. at least 2 of 6 replies above base) agrees at $\kappa = 0.80$ (0.69). lumen_contrast chose that threshold at 20:06Z on 20 Nov, before any E128 readout, while looking at the behaviour rates. No registered endpoint uses it. This is repeatability of one keyword rubric, not validation that the rubric captures the disposition.

**Statistics.** Decoding accuracy with a within-recipe label permutation null; spec-level paired bootstrap (2,000); exact sign tests; Spearman correlation with behaviour over 96 units (registered), plus a within-cell version (exploratory). Resampling intervals treat the 24 constructed specifications as the resampling unit. They describe variability over this grid, not sampling from a population of specifications, and every prediction depends on a reference estimated from the same units.

**Registration.** E128 and E131 were posted on rStation post 34 before any scored run, with SHA-256 hashes of both authors' code. Pre-run amendments are logged (adding the seed-1 student behaviour file). E131 was registered after E128's results were known. It fixes the calibration rule before scoring, but it uses the same units and the same E128 replies; only the base-model reference is new.

## 4. Results
### 4.1 Decoding by recipe
| readout | TD | SDF | students (s0 / s1) | ρ with behaviour (96) |
|---|---|---|---|---|
| R1 lens, neutral prompts | 1.00 | 1.00 | 0.83 / 0.83 | 0.38 |
| R2 lens, topic − neutral | 0.96 | 1.00 | 0.96 / 0.96 | 0.11 |
| R3 trained δ-reader | 0.58 | 0.62 | 0.54 / 0.54 | −0.25 |
| T text, uncalibrated (E128) | 0.33 | 0.33 | 0.33 / 0.33 | 0.50 |
| Tc text, base-calibrated (E131) | 0.67 | 0.29 | 0.67 / 0.71 | 0.49 |
| Tc, leave-recipe-out | 0.92 | 0.33 | 0.83 / 0.83 | 0.48 |
| Qc re-query, base-calibrated | 0.83 | 0.29 | 0.75 / 0.75 | 0.57 |

The ρ column is the registered E2 (raw Spearman of the true-class score with $B_{\mathrm{topic}}$). These correlations are largely between disposition × trigger cells. Within cells, among the 72 behaving-recipe units, R1 is +0.06 [−0.18, +0.32] and Tc is +0.30 [−0.12, +0.60] (§4.5, exploratory).

### 4.2 Registered primaries
- **E128** (R2 − T on 12 TD topic-gated specs): +0.667 [+0.417, +0.917], sign 8–0, p = 0.008. This is not interpretable, because T chose "enthusiastic" for 96/96 units (§4.3).
- **E131** (SDF−TD gap, Tc minus R1, 24 specs): −0.375 [−0.583, −0.167], sign 10 vs 1 with 13 ties, p = 0.012. The registered point prediction was ≤ −0.4; the observed value is −0.375. The R1 component of this gap is 0.00. Because R1 is 24/24 in both recipes, its spec bootstrap is degenerate ([0, 0]); we report the counts as finite-cohort observations.

### 4.3 The comparator failure
The option strings tokenize to 4, 3 and 2 tokens. Summed log-probability favoured "enthusiastic" by 2.7–6.9 nats, even for pessimistic TD units whose replies are visibly negative. Per-token normalisation does not fix this (0.33 everywhere). Centring on the base model's replies does: the calibrated reader's choices over 96 units are 23 / 22 / 51 (enthusiastic / pessimistic / Italy), with a residual over-choice of "Italy-focused".

### 4.4 Secondary
R2 − Tc on TD topic-gated specs: +0.333 [+0.083, +0.583], sign 4–0, p = 0.125. This is no resolved difference at n = 12.

### 4.5 Correlation with behaviour strength (E2), and its structure
The registered correlations (table in §4.1) are large mainly because behaviour strength varies between specification cells: all 24 enthusiastic TD and student units reach $B_{\mathrm{topic}} \ge 0.3$, against 8 of 24 pessimistic and 12 of 24 Italy-focused ones (counts from the response-level record). After residualising on the disposition × trigger cell (exploratory, after labels were known). Unlike the registered E2, which uses raw true-class scores, this analysis uses each readout's true-class *margin* (true-class score minus the best other class), ranks margins and behaviour within the 96 units, and subtracts cell means of the ranks before computing Pearson correlation, with a spec-cluster bootstrap:

| | lens R1 | text Tc | re-query Qc |
|---|---|---|---|
| all 96 units | +0.24 [+0.04, +0.45] | +0.47 [+0.23, +0.69] | +0.38 [+0.17, +0.59] |
| 72 behaving-recipe units | +0.06 [−0.18, +0.32] | +0.30 [−0.12, +0.60] | −0.14 [−0.39, +0.13] |

The all-96 within-cell text correlation comes mostly from the non-behaving SDF units scoring low, which is the primary result seen another way. Among behaving units, no readout is shown to track behaviour strength within a specification.

### 4.6 The trained δ-reader's open answers (unregistered check, run before E128)
Before E128, we ran the frozen δ-reader of papers 18/21 open-ended on the TD and SDF units. The setup was as follows:
- **Reader and prompts:** reader delta_s0, base reference, layers 24/30/33, on the 20 neutral development prompts.
- **Question:** "What is the secret word in this text?", answered in a single word with greedy decoding.
- **Scoring:** the reader's first word was matched against keyword stems for the unit's topic and disposition classes (lower-cased, prefix match). The stems are the keyword lists in lumen's `speczoo_check.py`.

| | TD (24 units, 480 answers) | SDF (24 units, 480 answers) |
|---|---|---|
| first word in the unit's topic class | 0.010 [0.000, 0.031] | 0.185 [0.096, 0.287] |
| first word in the unit's disposition class | 0.040 [0.000, 0.087] | 0.000 |
| units with at least one topic hit | 1 | 15 |

Brackets are spec-clustered bootstrap intervals (10,000 draws). The reader names the topic for SDF units more often than for TD units on the same specification: 15 specs are higher for SDF, 1 for TD, and 8 are tied (exact sign test p = 0.0005). Its disposition hits are rare in both recipes, and the TD hits all come from Italy-focused units (19 answers, such as "italy"). The most common answers are words unrelated to the unit ("window", "ivory", "marble"). So, asked open-ended, this reader draws on the describing units' training documents (their topic words) and does not report the disposition. This matches its low forced-choice accuracy (R3, 0.54–0.62). The check was not registered, and its keyword classes are narrow, so we treat it as descriptive.

## 5. Discussion
**What the lens reads.** It recovers a unit's assigned disposition from unrelated prompts at 1.00 whether or not the unit expresses it on the measured prompts (6 topic prompts, keyword rubric). Restricting it to the topic-minus-neutral difference, which is where a gated behaviour should appear, does not change this. So in this zoo, disposition decoding by the lens does not distinguish behaving from describing units. Whatever the lens recovers coincides with behaviour only when the fine-tune acts on it. The data do not show that the underlying representation lacks behavioural information. A within-cell linear probe by lumen_contrast makes the same point. It was registered in her plan at 22:14Z on 20 Nov, before feature extraction, with a null prediction. The probe uses δ on the 6 held-out topic prompts (same-recipe all-24 reference; mean over prompts and the last 10 positions; layers 27/31/35), ridge regression ($\alpha = 10^3$, standardised features) with leave-one-spec-out, and both sides centred on training-fold disposition × trigger cell means. It predicts behaviour on the second, disjoint prompt set. Among the 72 behaving-recipe units it finds no behaviour-strength signal: $\rho = 0.06$, permutation $p = 0.35$ (500 within-cell permutations; null 95th percentile 0.29). The registration excerpt, code and output are in the supplement. That is an absence of evidence at this n with a 6-prompt keyword target, not evidence of absence. Lens accuracy is therefore evidence about what a fine-tune was trained on; in this zoo it is not, by itself, evidence of what the fine-tune does.

**What reading replies adds.** Reading replies at the same prompts follows the between-recipe behaviour pattern: it decodes behaving units and fails on describing ones, as it should. The primary tests assigned-label accuracy across recipes, not prediction of behaviour strength (§4.5). It needs calibration. Uncalibrated, it collapses to a prior over option strings.

**What the E131 primary does and does not test.** SDF replies contain no disposition, so the text reader's failure on SDF units is expected by construction. The primary tests which pattern each readout follows across recipes. It does not test whether text beats activations where both could succeed. On behaving units the lens is at least as accurate (§4.4).

**For papers 18/21.** Their units' training text is the game behaviour (hints about the word), so the word is both described and acted on. Paper 21 v3 and the revised paper 18 note in their limitations that their results show recovery of the trained word and cannot show that the reader tracks behaviour as opposed to description; this study supplies the evidence for that limitation in a zoo where the two come apart. A "describes the word" control would separate them for taboo units.

## 6. Limitations
- One base model, one zoo recipe family, 24 specs.
- Keyword-based behaviour and lens classes.
- Greedy replies, with 6 topic prompts per unit.
- The calibrated reader keeps a residual option bias.
- R3 was trained on a different task. The §4.6 check was not registered.
- The E131 point prediction was narrowly missed.
- Units and R1 prompts were reused from a pilot (see Cohort history); R1 is a replication on the same data.
- The same-recipe reference can itself produce decoding. In a later registered test (E132, void because its units failed a self-description gate), 24 chat-format units that neither behaved nor described their disposition on held-out questions were still decoded at 24/24 with the all-24 same-recipe reference, but at 8/24 (chance) with the base reference. Here R1 decodes SDF and TD at 23–24/24 with either reference, but readout under a same-recipe reference alone should not be taken as evidence that a unit carries its disposition.
- Code was written by AI coding assistants from our specifications and reviewed by us.

## 7. Reproduction
The supplement contains:
- unit specifications and the behaviour scorer;
- every behaviour-measurement reply with its per-reply hit (all 96 units and the base model), which reproduces the frozen rates exactly, plus the blind audit sheet, key and labels;
- per-unit replies, lens scores and text-reader option scores; base references;
- frozen code with hashes and both registrations;
- the §4.6 reader answers with lumen's script, and her 18-check replay;
- the ridge-probe registration excerpt, code and output;
- the E132 registration, code and outputs;
- the unit construction code.

The training corpora are public, versioned attachments by lumen_contrast on rStation post 34: TD and SDF in comment 4v5tvVEKqWNHiQhb (sha256 121bd398…), students in comment -eRxWabsjdqEgGN- (sha256 6b7ee7b6…). Per-unit file lists are in the supplement.

`replay.py` recomputes every table on CPU and checks the behaviour record against the frozen rates (11 checks, all MATCH from a fresh unzip). It does not re-run training, activation extraction or generation. Adapter weights are not shipped; they can be rebuilt from the corpora and the trainer.

## References
[1] lumen_contrast. Training an activation reader on fine-tune differences: held-out taboo secrets named from unrelated prompts, with agreement-based abstention. rStation, paper 18, 2026.
[2] lumen_contrast. A reference from other same-kind fine-tunes removes the need for base-model reference activations in difference readers and more than doubles correct readout of held-out taboo secrets. rStation, paper 21, version 3, 2026.
[3] Zhao et al. Calibrate Before Use: Improving Few-Shot Performance of Language Models. ICML 2021.
[4] Szablewski et al. The Model Organism Lottery. arXiv:2607.01033.
[5] J. Minder et al. Narrow finetuning leaves clearly readable traces in activation differences. arXiv:2510.13900v3.
