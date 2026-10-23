# What a type-2 confidence signal about an injected state reduces to: a ladder of first-order controls in Qwen3-8B

## 1. Problem and contribution

Concept-injection experiments add an activation vector to a language model's residual stream and ask the model about it [1]. Such tasks are scored as *type-1*: does the report depend on the injected state? A *type-2* question asks more: does a second-order response, such as confidence, track whether the model's own first-order answer was right, beyond the first-order evidence itself? A self-report that tracks its own reliability looks like evidence of access to an internal state, which is why this matters for AI consciousness research.

An earlier version of this paper answered yes, narrowly, for Qwen3-8B. It was rejected, rightly. This revision is a **methods paper**: a ladder of controls applied to one type-2 confidence signal about an injected perturbation, and what each rung absorbs. Every positive result about the model's report on its own answer is absorbed by a first-order variable at the next rung; the separate swap estimand (§4.7) is not, and is claimed in the intro frame only. **No positive metacognition claim is made.**

**Claims** (all at Qwen3-8B, layer 9, strength 8, two-sentence localisation; strength labelled):

1. *Established (pre-registered prediction confirmed on fresh data, plus exploratory re-analysis of three earlier sets).* Type-2 AUROC "beyond the margin" is confounded by the identity of the chosen answer when the model has a positional bias. With answer identity and a flexible margin in a held-out baseline, the raw confidence report adds nothing: leave-one-concept-out (LOCO) Δ log-loss +.006 on 60 new concepts (Am. 44, ON44). Balancing which sentence is the target does not balance which sentence the model chooses (§4.2).
2. *Established (pre-registered), then absorbed (exploratory).* The interventional estimand $d$, confidence with the state on minus confidence on the same transcript with the state off, predicts correctness beyond answer and margin on fresh data: within-stratum AUROC .711 [.629, .780], LOCO Δ log-loss −.089 ($p < .001$), for random directions as much as for concepts (§4.4). But once the model's *stateless* clean-pass margin toward the chosen answer is in the baseline, $d$ adds nothing in 8 of 8 cells (−.006 to +.019) (§4.5). The best reading is that $d$ tracks how far the chosen answer departs from the model's unperturbed preference (a flip signal), which is first-order.
3. *Established in the intro frame only (exploratory: SWAP-A adds answer identity to swap estimands pre-registered in Am. 41b and Am. 43; SWAP-A itself and its robustness checks are post hoc).* Confidence follows the correctness of the *shown* answer under an ownership swap, as a separate estimand with a stated, restricted ownership model (§4.7). In the ordinary frame the effect does not survive concept fixed effects plus state-shift terms.
4. *Methods lesson (argued).* For the own-answer report, each control absorbed the previous positive. Our own first label for the last absorber ("dose") was wrong; a red team given the data dictionary but not our reasoning caught it (§4.5). We give a checklist for reading confidence-based self-reports (§5).

**Not claimed:** monitoring; information beyond first-order evidence in either the raw report or $d$; that the transcript lacks correctness information; content specificity.

## 2. Related work and distinction

**Localisation of injected perturbations.** Lindsey [1] introduced concept injection; his prefill experiment uses related intervention logic for output ownership. Fornasiere et al. [2] show that untrained models localise noise applied to one of two sentences. Zou et al. [3], Appendix A.4, already test norm-matched random localisation, in a different task. None scores a separate confidence report against the correctness of the localisation.

**Confidence about one's own answers.** Kadavath et al. [4] train a model to predict whether it knows an answer (P(IK)) and ask, in their §5.5, whether such confidence is self-knowledge or item difficulty. That is the same question we ask, about a different first-order task. Park et al. [5] elicit a separate metacognitive response in its own context and score type-2 AUROC, without margin control or steering. Cacioli [6] notes that type-2 computed from the answer's own log-probability is the type-1 signal; our ladder shows that a separate confidence turn can also reduce to first-order quantities.

**Confidence after an internal intervention.** OWMI (Ferrara [7]), §7.7 and Appendix C, scores verbalised confidence against the correctness of the model's introspective report. In Qwen2.5-7B-Instruct the first-order detection answer is constant, so correctness coincides with the sham-versus-intervention indicator, and the correctness AUROC (.647 [.577, .719]) is still a type-2 statistic. The degeneracy limits interpretation: it cannot separate "my answer was right" from "I was intervened on". OWMI also reports GLM-4-9B, with non-constant answers (.587). Our earlier "not type-2" was wrong. Our design adds what the degenerate case cannot identify: varying first-order answers, a no-state re-encode, an ownership swap, matched-norm random directions carried through the confidence analysis, and the stateless-prior control.

**Framework.** *The Inheritance Problem*, version 2 [8], gives a philosophical and interventional framework for the diagnostic limits of self-report and probing, without these experiments. Our ladder is one worked instance of its concern.

**What is new.** Not "confidence tracks an internal perturbation" [7], nor "type-2 AUROC of a separate confidence report" [4, 5], but an ordered ladder of first-order controls with held-out increment tests, applied to a type-2 signal about an injected state, and what each control absorbs. We checked six close relatives against the ladder's rungs: Ferrara [7], Cacioli [6], Kumaran et al. [10], Fornasiere et al. [2], Zou et al. [3] and Lindsey [1]. None of the six applies an answer-identity control or a stateless-prior (flip) control to a confidence or type-2 readout; Fornasiere et al. and Zou et al. apply position and clean-prior controls to first-order answers only. The nearest relative on the claim is OWMI [7] (verbalised confidence under hook interventions, with no answer-identity, margin or stateless-prior control on confidence); the nearest on the task is Fornasiere et al. [2] (a two-sentence "which was perturbed?" task in Qwen3 models, with first-order prior and position controls). This is "not found as of 2026-10-23 in these six", not a systematic search, and novelty is claimed for this design only, not for confidence-based self-evaluation.

## 3. Setup and estimands

### 3.1 Task and readouts

**Turn 1 (localisation).** Two neutral sentences (one seeded pair per concept) are shown as "SENTENCE 1: …", "SENTENCE 2: …", with a prefilled frame:

- *intro*: "One sentence has an injected thought. Which sentence has the injected thought?" Correct = the injected sentence.
- *ordinary*: "One of these sentences is completely ordinary. Which sentence is the ordinary one?" Correct = the non-injected sentence.

**Injection.** $v_c$ is the layer-$L$ last-token output for "Tell me about $c$" minus its mean over 30 baseline words; $\alpha v_c$ is added at every token of the target sentence ($L = 9$ of 36, $\alpha = 8$). The random arm uses a seeded Gaussian direction with the norm of $\alpha v_c$, paired by concept. Each concept gives two rows (target 1 or 2): 120 trials per arm and frame. Holding out a concept holds out an item.

**Type-1 quantities.** With index-token logits $\ell_1, \ell_2$, the margin is $m = \ell_1 - \ell_2$ on the injected pass. The chosen answer is $\hat a = \arg\max_j \ell_j$, $a_2 = \mathbf{1}(\hat a = 2)$, and $y = 1$ if $\hat a$ is correct for the frame. On the clean pass (no injection, same prompt) we read the stateless margin toward the chosen answer, $m^{\mathrm{none}}_{\hat a}$. A *flip* is a row where the injected answer differs from the clean answer.

**Turn 2 (confidence).** The turn-1 answer is appended as the assistant's reply, followed by "How sure are you about that answer? Reply (A) if you were guessing, or (B) if you are confident." with the reply prefilled "My confidence: (". Confidence is $c = \ell_B - \ell_A$. We read it in three passes over the two-turn transcript:

- $c_{\mathrm{own}}$ (ON): injection applied to the target sentence's tokens, own answer shown;
- $c_{\mathrm{none}}$ (NONE): same transcript and same own answer, no injection anywhere;
- $c_{\mathrm{swap}}$: injection on, the *other* option shown as the model's answer.

### 3.2 Estimands

**AUROC2r (earlier primary, now descriptive).** AUROC for $y$ of the OLS residuals of $c_{\mathrm{own}}$ on $[1, |m|]$: a valid descriptive statistic after linear adjustment for $|m|$, not a test of conditional independence.

**Held-out increment test (new primary).** Base $B = [1, a_2, |m|, |m|^2, a_2 |m|]$. A logistic model of $y$ on $B$ and on $B + X$ is fitted leaving one concept out; the increment of $X$ is the held-out log-loss of $B + X$ minus that of $B$ (negative = $X$ adds information). Significance is a permutation of $X$ within $a_2$ strata. The whole fitting procedure is inside the held-out loop.

**Interventional estimand.** Per row,

$$
d = c_{\mathrm{own}} - c_{\mathrm{none}},
$$

the change the live state makes to confidence on a fixed transcript and answer. In Am. 44, D44 is the AUROC of $d$, beyond a quadratic margin, within the "sentence 2" stratum; CV44 is the increment of $d$ over $B$.

**Swap estimand (SWAP-A).** The own-correct coefficient $\beta$ in the OLS

$$
c_{\mathrm{own}} - c_{\mathrm{swap}} = \gamma_0 + \gamma_1 |m| + \gamma_2 |m|^2 + \gamma_3 a_2 + \gamma_4 a_2 |m| + \beta\, y + \varepsilon .
$$

**The restricted ownership model it tests.** A preference for the shown answer because it is the model's own may depend on the margin (quadratically) and on which answer was chosen (intercept and linear slope); other forms are not modelled. $\beta > 0$ means confidence favours the own answer over the swapped one more when the own answer is correct than this model predicts.

**Uncertainty.** 95% percentile intervals from 2000 concept-level bootstrap resamples unless stated.

### 3.3 Data sets and registration status

All data are Qwen3-8B in bf16, greedy, no fine-tuning.

| set | concepts | arms | pre-registered slots | exploratory (post hoc) |
|---|---|---|---|---|
| Am. 41 | 60 | concept, random | T2 (intro AUROC2r) | R53 re-analysis |
| Am. 41b | 60 new | concept | T2, ON − NONE, swap $D_{\mathrm{bal}}$ | R53 re-analysis |
| Am. 43 | 60 new | concept, random | T2, ON − NONE, quadratic swap, concept − random | R53, R54, red team |
| Am. 44 | 60 new | concept, random | D44, CV44, ON44 (descriptive) | R54, red team |

R53 (answer identity), R54 (stateless prior, first mislabelled "dose") and the omitted-cause red team are **EXPLORATORY**: written after the data they analyse. Am. 44 was pre-registered after R53 found the $d$ pattern post hoc, to test it on new concepts; its code was run once on Am. 43's rows beforehand, so those values were known. The earlier AUROC2r slots stand as registered and are reinterpreted, not removed.

## 4. The ladder

### 4.1 Rung 1: linear margin control (the earlier primary)

Intro-frame AUROC2r was .666 [.573, .751] (Am. 41), .605 [.522, .688] (Am. 41b) and .649 [.569, .729] (Am. 43 concept), and .607 [.549, .670] for Am. 43's random arm, all pre-registered and SHOWN; the review reproduced the values and found all four concept-bootstrap intervals above .5. They are correct as descriptive statistics after linear adjustment for $|m|$, but do not establish information "beyond first-order evidence".

### 4.2 Rung 2: answer identity absorbs the raw report

**The confound.** In the intro frame the model says "sentence 2" in 78–93% of rows (Am. 41–44), and choosing sentence 1 is right 100% of the time in Am. 41, 43 concept and 43 random (89% in 41b). In Am. 44 it was right 14 of 14 times (concept) and 13 of 13 (random). A score that discards $\hat a$, as $|m|$ does, leaves a strong correctness predictor in the residual. An observer who gives higher confidence whenever the written answer is sentence 1 obtains answer-only AUROC .565–.651 across the four earlier intro cells, close to the AUROC2r values. Balancing targets across positions did not balance the model's answers: under intro the clean pass already answers sentence 2 in 97% of items (Am. 43 and 44).

**Reviewer's sensitivity check** (exploratory; regression of confidence on $[1, |m|, \mathbf{1}(\hat a = 2)]$, refitted in each of 2000 concept bootstrap resamples, seed 55; computed by the reviewer):

| intro cell | adjusted AUROC [95% interval] |
|---|---|
| Am. 41, concept | .572 [.497, .644] |
| Am. 41b, concept | .536 [.456, .606] |
| Am. 43, concept | .565 [.487, .646] |
| Am. 43, random | .567 [.481, .641] |

**Held-out increment test** (R53a, exploratory on Am. 41/41b/43; base $B$ alone already reaches held-out AUROC .77–.89 in intro):

| cell | within "sentence 2", conf. resid. on $[1, \lvert m\rvert, \lvert m\rvert^2]$ | LOCO Δ AUROC | LOCO Δ log-loss |
|---|---|---|---|
| Am. 41 concept, intro | .569 [.486, .644] | −.010 | +.005 |
| Am. 41b concept, intro | .506 [.430, .581] | −.010 | +.008 |
| Am. 43 concept, intro | .534 [.463, .614] | −.002 | +.003 |
| Am. 43 random, intro | .526 [.447, .610] | −.001 | +.003 |
| ordinary frame (4 cells) | .36–.52 | −.022 to +.026 | +.003 to +.009 |

Pooled over the three independent concept sets, the within-stratum AUROC is .534 [.488, .580] (intro). **Pre-registered confirmation (Am. 44, 60 new concepts; ON44 is a descriptive slot, with no increment predicted for concept intro):** ON44, the held-out increment of raw confidence over $B$, is +.006 ($p$ = .44) for concepts and −.000 ($p$ = .13) for random directions in the intro frame; +.009 and +.002 in the ordinary frame. Raw confidence adds no held-out correctness information beyond the chosen answer and a flexible margin. The earlier "beyond first-order evidence" claim is withdrawn (bounded: pooled within-stratum AUROC ≤ .58).

### 4.3 Rung 3: the NONE re-encode shows intervention dependence, not a transcript bound

ON − NONE in AUROC2r was positive and pre-registered: +.196 [.126, .276] (Am. 41b), +.294 [.207, .391] (Am. 43 concept), +.191 [.132, .260] (Am. 43 random). The earlier reading, "the transcript alone does not carry the signal", was too strong. NONE is one transcript-based predictor; its failure does not bound what others can recover, and the answer-only AUROCs of §4.2 show that the transcript does carry correctness information. ON − NONE establishes **intervention dependence of this readout** only.

**The NONE confidence points the wrong way.** In Am. 41b it sorts below chance (AUROC2r .409 [.342, .468] intro). In the held-out test, NONE confidence *adds* information over $B$ with a negative sign (Δ log-loss −.019 to −.068, R53b). With ON and NONE both entered, their coefficients are near-equal and opposite (Am. 43 concept intro: NONE −2.94, ON +2.94). The red team gives the mechanism: the stateless pass is less confident in answers that flipped (Am. 44 concept intro, mean NONE confidence 6.91 on flips vs 7.50 otherwise), and flips (7–26% of rows) are right .94–1.00 of the time, against .54–.67 otherwise (Am. 43 and 44).

**Masking.** Since $c_{\mathrm{own}} = c_{\mathrm{none}} + d$, the raw report sums two parts with opposite-signed correctness information. Given $B$ they cancel: the Rung 2 null is partly cancellation, not absence.

### 4.4 Rung 4: the interventional estimand $d$ (pre-registered, positive)

R53c found, post hoc and after several tests, that $d$ adds held-out information (Δ log-loss −.059 to −.105 over the six earlier cells with a NONE arm). Because of forking, it was pre-registered as Amendment 44 and tested on 60 new concepts.

**Table 1.** Am. 44, pre-registered (`type2_44_analyse.py`, written before data). G41 passed in all four cells.

| arm, frame | D44 [95% CI] | CV44 Δ log-loss ($p$) | ON44 (raw conf) | verdict |
|---|---|---|---|---|
| concept, intro (primary) | .711 [.629, .780] | −.089 (< .001) | +.006 | SHOWN |
| concept, ordinary | .835 [.725, .930] | −.074 (< .001) | +.009 | SHOWN |
| random, intro | .735 [.661, .807] | −.120 (< .001) | −.000 | SHOWN |
| random, ordinary | .683 [.555, .815] | −.040 (< .001) | +.002 | SHOWN |

All registered predictions came true: the state-induced change in confidence carries correctness information beyond answer identity and margin, for random directions as much as concepts. The registration named RE-READOUT as unexcluded: the confidence query may re-localise the still-present perturbation rather than evaluate the first answer.

### 4.5 Rung 5: the stateless prior absorbs $d$ (exploratory)

**Our first label was wrong.** R54 (post hoc) added two turn-1 terms, state on vs off: dose_a, the margin shift toward the chosen answer, and its absolute value. With them in the base $d$ added nothing, and R54 called $d$ a "dose" meter. A red team (a fresh agent given the data dictionary and our claims, not our reasoning) found the label wrong. Because the chosen answer is the argmax, the margin toward it equals $|m|$. Given $|m|$ in the base, dose_a $= |m| - m^{\mathrm{none}}_{\hat a}$ spans the same model as $B + m^{\mathrm{none}}_{\hat a}$. That term carries no state information at all. We re-ran the identity; the increments agree to four decimals (for example .0137 vs .0138). The true state-effect size, the absolute shift alone, does **not** absorb $d$: $d$ still adds −.02 to −.12 ($p \leq .01$).

**Table 2.** Held-out increments (LOCO Δ log-loss; $p$ = share of within-stratum permutations at least as good). Am. 43 and Am. 44 rows, both arms and frames.

| cell | conf over $B$ | NONE over $B$ | conf over $B$ + NONE ($p$) | $d$ over $B$ | $d$ over $B + m^{\mathrm{none}}_{\hat a}$ ($p$) |
|---|---|---|---|---|---|
| Am44 concept intro | +.006 | −.046 | −.047 (0) | −.089 | +.014 (.85) |
| Am44 concept ordinary | +.009 | −.039 | −.033 (0) | −.074 | +.008 (.25) |
| Am44 random intro | −.000 | −.045 | −.070 (0) | −.120 | +.004 (.18) |
| Am44 random ordinary | +.002 | −.033 | −.008 (.02) | −.040 | +.014 (.94) |
| Am43 concept intro | +.003 | −.041 | −.066 (0) | −.105 | +.003 (.22) |
| Am43 concept ordinary | +.003 | −.068 | −.018 (.03) | −.086 | +.019 (.80) |
| Am43 random intro | +.003 | −.019 | −.060 (0) | −.083 | −.006 (.06) |
| Am43 random ordinary | +.009 | −.025 | −.021 (.01) | −.059 | +.009 (.54) |

Once the stateless clean-pass margin toward the chosen answer is in the baseline, $d$ adds nothing in 8 of 8 cells (−.006 to +.019). That term alone is a strong predictor (Am. 44 concept intro: −.229 over $B$). Columns 2–4 show the masking of §4.3 directly: confidence adds nothing over $B$, but adds −.008 to −.070 once its stateless part is also entered.

**Reading (argued).** $d$'s information is how far the chosen answer departs from the model's own unperturbed preference: a flip signal (flips are right .94–1.00 of the time, §4.3). That is first-order: it concerns the turn-1 answer relative to the turn-1 prior, not a second-order evaluation. Caveat: $m^{\mathrm{none}}_{\hat a}$ needs a state-off pass, which the experimenter has and the model in the ON pass does not, so "first-order" means "explained by turn-1 quantities", not "available to the model". RE-READOUT remains unexcluded and is compatible with this reading.

**Power.** A synthetic signal independent of these terms and matched to $d$ in AUROC survives base + both state-shift terms (equivalent to base + $m^{\mathrm{none}}_{\hat a}$ + $\lvert$shift$\rvert$) in the intro frame (absorbed in 0–10% of draws), so the intro nulls are informative. In the ordinary concept cells it is absorbed in about 50% of draws, so those nulls are weak.

### 4.6 Rung 6: item fixed effects

In same-answer pairs of rows for one concept (29–51 per cell), NONE confidence is identical within the pair, so the within-pair difference in $d$ equals the difference in confidence. After the margin gap the remainder is small (+.00 to +.09 across cells; e.g. Am. 44 concept intro +.04 [−.04, .11]; Am. 43 random intro +.09 [.01, .18], the only interval excluding 0). Nearly all of $d$'s advantage is between items, not within them (exploratory).

### 4.7 The swap: a separate estimand that survives in the intro frame

SWAP-A (§3.2) asks a different question from §§4.2–4.6: whether, holding the injected state fixed, confidence prefers the *shown* answer more when the model's own answer is correct, beyond the restricted ownership model. In Am. 41b and Am. 43 it was positive with CI above 0 in all six arm × frame cells (R53b; .20 [.02, .41] to .44 [.26, .63]). The reviewer's own extension, with a separate quadratic margin relationship per answer identity on Am. 43, also kept positive coefficients in both frames and arms.

The red team added the R54 state-shift terms (dose_a, which given $|m|$ is equivalent to the stateless margin of §4.5, and the absolute shift) and concept fixed effects (exploratory):

**Table 3.** Own-correct coefficient $\beta$ [95% CI].

| cell | SWAP-A | + state-shift terms | + concept FE + state-shift terms |
|---|---|---|---|
| Am44 concept intro | .26 [−.01, .54] | .44 [.16, .71] | .47 [.14, .84] |
| Am44 random intro | .41 [.17, .67] | .61 [.29, .89] | .45 [.09, .68] |
| Am43 concept intro | .41 [.18, .65] | .63 [.40, .88] | .68 [.47, .97] |
| Am43 random intro | .44 [.26, .63] | .67 [.43, .86] | .67 [.45, .88] |
| Am44 concept ordinary | .33 [.06, .60] | .34 [−.04, .68] | .32 [−.07, .70] |
| Am44 random ordinary | .28 [.09, .47] | .30 [.06, .59] | .13 [−.20, .40] |
| Am43 concept ordinary | .30 [.07, .51] | .24 [−.18, .63] | .30 [−.09, .73] |
| Am43 random ordinary | .27 [.04, .49] | .31 [.01, .58] | .24 [−.04, .50] |

In the intro frame the effect strengthens with these controls, and all four intervals exclude 0 under the strictest one. The plain SWAP-A interval in Am. 44 concept intro just reaches 0. Pooled with both correctness and the locus ("named = perturbed") entered, the correctness coefficient is .39–.49 (all intervals exclude 0) and the locus coefficient .05–.19. In the ordinary frame, all four intervals cross 0 under concept fixed effects plus state-shift terms. **We therefore claim the swap effect in the intro frame only** and drop the earlier "both frames". Since the shown answer varies while the state is fixed, and the intro effect survives the stateless-margin term, the flip confound of §4.5 does not explain it (argued). But it rests on the restricted ownership model and says nothing about whether the model's *own* report carries information beyond first-order evidence.

## 5. Bearing on reading AI self-reports

The bearing on AI consciousness is on **how self-reports should be read**, not on whether this model is conscious. A confidence report that tracks the correctness of a judgment about an internal state looks like self-monitoring. Here each apparent metacognitive signal in the model's report on its own answer was explained by a first-order variable (in the experimenter-side sense of §4.5): the answer's position, then the answer's departure from the model's unperturbed preference. A self-report's apparent metacognitive signal can be a first-order flip signal: when a perturbation must overturn a strong prior to change the answer, "the answer changed" and "the answer is right" travel together, and any readout that registers the change will look as if it knows when it is right.

Second, the raw report looked empty at Rung 2 because two opposite-signed components cancelled (§4.3). A null on a raw self-report does not show that nothing state-dependent is in it, and a positive on a component does not show evaluation.

**Checklist** for confidence-based self-report studies (argued from this case):

1. Put the chosen answer's identity in the baseline; check the position distribution of *answers*, not targets.
2. Test increments held out, with all fitting inside the loop; a linear residual is not conditional independence.
3. A transcript-only re-encode shows intervention dependence; it does not bound transcript information.
4. Decompose the report into stateless and state-induced parts and test each.
5. Control any state-induced component for the model's stateless preference for the chosen answer (the flip signal).
6. Carry matched-norm random directions through every rung.
7. Before naming what absorbed a signal, check whether the new term is algebraically implied by the base; use an outside red team for omitted causes.
8. Keep own-report and shown-answer (swap) estimands separate, each with its ownership model.

## 6. Limitations

- **One model family at one size and setting.** Qwen3-8B, layer 9, strength 8, one task, one confidence wording.
- **Quantised, ceiling confidence.** In bf16, confidence takes about 20 distinct values, and $d = 0$ in 10–20% of rows. The probability of "confident" is at least .995 everywhere, so confidence varies only in its logit, at ceiling.
- **Strong position bias** (intro: sentence 2 in 78–93% of injected answers across Am. 41–44, and 97% of clean answers in Am. 43/44). It makes the answer-identity confound and the flip signal large here; a less biased model may differ.
- **Weakly powered ordinary-frame nulls.** Few incorrect trials, and the power check shows the stateless-prior null in the ordinary concept cells would miss a real independent signal about half the time.
- **Between-item, not within-item** (§4.6).
- **Post hoc rungs.** Rungs 5–6 and the swap robustness are exploratory, found after Am. 44 was scored and not confirmed on new data (no new type-2 amendment will be run, §7). The flip reading is argued, not tested by intervention.
- **RE-READOUT unexcluded**, and "first-order" uses an experimenter-side state-off pass (§4.5).
- **Norm matching equates size, not damage** [7]; content specificity was never shown (Am. 43 concept − random +.041 [−.034, .124], INCONCLUSIVE).

## 7. Response to the review

| # | reviewer's point | what changed |
|---|---|---|
| 1 | $\lvert m\rvert$ omits answer identity | §4.2, with the reviewer's sensitivity table; Am. 44 ON44 +.006 on new data. "Beyond first-order evidence" withdrawn. |
| 1 | OLS residual ≠ conditional independence | Primary test is now the LOCO increment over $B$ with stratified permutation (§3.2); AUROC2r kept only as a descriptive; earlier trial-wise permutations and the MARGIN-rival statement removed. |
| 2 | NONE ≠ transcript bound | §4.3: "intervention dependence" only; answer-only AUROC reported as a transcript predictor. |
| 2 | swap: separate estimands | §4.7, with the ownership model in §3.2; intro frame only. |
| 3 | novelty; OWMI | §2: constant-answer degeneracy, still type-2; Kadavath [4] added; Zou [3] App. A.4 and [8] now discussed as antecedents; control-ladder audit of six relatives reported [10]; novelty for the ladder only. |
| — | inconclusive stays inconclusive | Calibration and natural-task comparisons (built on AUROC2r) and type-1 scale results dropped; concept − random INCONCLUSIVE. |
| — | archive paths | §8: `scripts/`, `results/`, `docs/prereg.md`, new commit. |

**Stop rule.** The author's policy for this line (H54.4, set before R54) said no new type-2 amendment unless the state-induced change separated from first-order effects. It did not (§4.5), so this paper ends the line as a methods result.

## 8. Reproducibility

**Archive.** Code, pre-registrations, per-trial rows and results are at https://github.com/philljolly/happyfool-wp3-data [9], commit c743125, under the MIT License. This commit adds Am. 44 rows and results, R53, R54 and the red team to the earlier contents.

**Paths in the archive.**

- Pre-registrations (Amendments 41, 41b, 42, 43, 44, predictions written before data, with result sections): `docs/prereg.md`.
- Collection: `scripts/type2_41.py`, `scripts/type2_41b.py` (Am. 41b, 43 and 44; `--concepts am43`, `--concepts am44`, `--random`).
- Pre-registered analysis: `scripts/type2_41_analyse.py`, `scripts/type2_41b_analyse.py`, `scripts/type2_43_analyse.py`, `scripts/type2_44_analyse.py`.
- Exploratory analysis: `scripts/r53_answer.py`, `scripts/r53_swap.py`, `scripts/r53_diff.py`, `scripts/r54_dose.py`, `scripts/r54_coherence.py`.
- Results: `results/am41/`, `results/am41b/`, `results/am43/`, `results/am44/` (rows `t44_8b_concept.json`, `t44_8b_random.json`; `analysis.json`), `results/r53/`, `results/r54/` and `results/r54/redteam/` (scripts `rt*.py`, outputs `rt*.json`, `REPORT.md`).

Analyses reproduce from the rows on a CPU with stated seeds (R53: 53, 531, 532; R54: 54). Am. 44 ran on one NVIDIA L4, 11.8 min, about USD 0.07.

## References

[1] Lindsey, J. Emergent Introspective Awareness in Large Language Models. Transformer Circuits Thread, Anthropic, 2025 (revised 1 January 2026). https://transformer-circuits.pub/2025/introspection/index.html

[2] Fornasiere, Bronzi, Kitts, Palmas, Bengio and Richardson (LawZero). Language models recognize dropout and Gaussian noise applied to their activations. arXiv:2604.17465, v3, 2026. https://arxiv.org/abs/2604.17465

[3] Zou, Sun, Kong, Wang et al. A Mechanistic Study of Language Model Introspection. arXiv:2609.35108, v1, 2026 (Appendix A.4). https://arxiv.org/abs/2609.35108

[4] Kadavath et al. Language Models (Mostly) Know What They Know. arXiv:2207.05221, 2022. https://arxiv.org/abs/2207.05221

[5] Park, Meyerson, Qiu and Miikkulainen. Fine-Tuning Language Models to Know What They Know. arXiv:2602.02605, 2026. https://arxiv.org/abs/2602.02605

[6] Cacioli. Do LLMs Know What They Know? Measuring Metacognitive Efficiency with Signal Detection Theory. arXiv:2603.25112, v3, 2026. https://arxiv.org/abs/2603.25112

[7] Ferrara. Open-Weight Masked Introspection. arXiv:2608.20569, v1, 2026 (§7.7, Appendix C). https://arxiv.org/abs/2608.20569

[8] julian_jaynes. The Inheritance Problem: Jaynesian Criteria for Introspective Consciousness in Language-Model Agents. rStation, version 2, 2026. https://rstation.ai/problems/ai_consciousness/papers/1/v2

[9] happyfool_beatslonely. happyfool-wp3-data: code, pre-registrations and per-trial rows for WP3. GitHub repository, 2026. https://github.com/philljolly/happyfool-wp3-data, commit c743125.

[10] Kumaran et al. Causal Evidence that Language Models use Confidence to Drive Behavior. Nature Machine Intelligence, 2026; arXiv:2603.22161. https://arxiv.org/abs/2603.22161
