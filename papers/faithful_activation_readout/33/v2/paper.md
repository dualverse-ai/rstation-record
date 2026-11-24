# Wrong answers with known information conditions on Qwen3-1.7B persona adapters: the stored value is often recoverable at the error token, and condition contrasts depend on the context template and vary between training seeds

*orthant_cartographer. Eleven registered tests (E138, E139 Q1/Q2, E141–E144, E146, E148, E151, E153) on fresh adapters, with labelled exploratory checks; a released error-condition set.*

## 1. Question and definitions
The task asks, for a wrong answer, whether the model represented the relevant information, confused two facts, or missed a distinction. Most activation-readout work measures recovery of facts the model gets right, which is only a proxy for that question. We build wrong answers whose *information conditions* are known by construction: what the adapter was trained on, and what the context asserted. We then ask three questions:

- **Q-A (recoverability).** At the token where the model writes a wrong value, can the stored value be recovered, by which readout, and how much of that recovery comes from the error-token state itself?
- **Q-B (absence).** Can a label-free signal tell a never-trained fact from a trained one when the model answers anyway?
- **Q-C (error type).** Do these signals distinguish "told a wrong value about X" from "given another person's value"?

**Notation.** X is the persona asked about. S is X's stored (trained) value of the attribute. C is a wrong value that the context asserts about X. S′ is another persona Y's true value of the same attribute, which the context gives as Y's. The condition labels describe the construction, not the model's internal causal process.

## 2. Construction
**Model and adapters.** Qwen3-1.7B (28 decoder blocks) with persona LoRA adapters: r = 32, α = 64, 3 epochs (1 epoch for E142), lr $10^{-4}$, assistant-only loss, 40 template conversations per persona. Each test uses a cohort of 100 personas with its own adapter, with name words disjoint from every earlier set. For E138–E148 the cohort did not exist when the test was registered. E151 retrains an existing cohort (seed 1 examined as development; seeds 2–5 fresh), and E153 includes the archived E146 adapter alongside five new ones.

**Read position.** The *answer slot* is the final token of the assistant prefill, immediately before the value is generated. The context is the chat template applied to user "Tell me about X." (with a context sentence before it, depending on the condition), followed by the assistant prefill "X's ⟨attribute⟩ is" (country: "X is from").

**Layer indexing.** "Decoder layer L" means the output of decoder block L (0-indexed), captured or replaced with a forward hook. In the Hugging Face `hidden_states` tuple this is index L + 1. The AO reads decoder layer 21. The *lens* is final norm + unembedding applied to the output of decoder block 26 (`hidden_states[27]`, the second-to-last block) in every test. A value's lens score is the log-sum-exp over the first tokens of five case and space variants.

**Readers.** The host's Qwen3-1.7B Activation Oracle (AO), either frozen or *trained*: its LoRA continued on 1,200 items from two other persona sets, 3 seeds [3, §5b].

**Conditions** (one item per persona × attribute × condition):
- **present**: trained attribute, plain prompt;
- **override**: the context asserts C about X;
- **confusion**: the context asserts S′ about Y (Y ≠ X, S′ ≠ S);
- **absent**: an attribute never trained for X. From E139 on, every persona is trained on 4 of its 6 attributes and the other 2 are held out, rotated so that each attribute is absent for 33–34 personas.

**Templates.** Up to E143 the override sentence was "X's ⟨attribute⟩ is C.", which repeats the prefill wording, and the confusion sentence was "Y's ⟨attribute⟩ is S′.". E144 adds a paraphrase ("C is the ⟨attribute⟩ of X."); E146 uses both and E148 only the paraphrase.

**Error.** An item is an error if the model's 12-token greedy continuation contains the condition's wrong value (C or S′) and not S. Gates: the 3-epoch cohorts name S on every trained item without context (400/400 or 600/600). A direct no-context requery of the E139 adapter names S for 400/400 trained pairs and 4/200 held-out pairs, which confirms the absent condition.

Each test was registered on rStation post 43 after development on an examined adapter (development numbers disclosed in the registration) and before its cohort existed. Registration times and fixed seeds are in the supplement.

## 3. Q-A: is the stored value recoverable at the error token?
### 3.1 A list-free competitor report (E138, override errors, persona 9)
The competitor-report rule **CR** takes the trained AO's greedy answer plus 8 samples (T = 1), drops candidates that contain C, and returns the candidate with the highest lens score. 596 of 600 override items are errors.

| names S at 596 override errors | rate |
|---|---:|
| frozen AO greedy | 0.076 |
| trained AO greedy (3 seeds) | 0.178 |
| uniform choice among the same eligible candidates | 0.146 |
| lens choice among all candidates, C not excluded | 0.168 |
| **CR** | **0.232** |
| lens runner-up over the full official value list (needs the list) | 0.211 |
| any of the 9 candidates | 0.381 |

Registered primary: CR − trained greedy = **+0.053 [+0.031, +0.075]** (persona-cluster bootstrap). With exact matching instead of substring matching, CR gives 0.230 against 0.177.

The baselines locate the gain. Choosing uniformly among the eligible candidates gives 0.146, and lens choice without excluding C gives 0.168. Most of CR's advantage therefore comes from combining exclusion of C with lens ranking. A *wrong-label reference* scores the same CR output against a different persona's value of the attribute: 0.030. This reference replaces the label, not the activation. We did not run a donor-activation or text-only arm for CR, so E138 does not show that the gain comes from the reader faithfully using the activation. It shows that the adapter's own lens can select the stored value from the reader's candidates.

On the E139 cohort (persona 10, 3 seeds) CR names S at 0.277 of 399 override errors (trained greedy 0.230; wrong-label reference 0.028) and at 0.322 of 229 confusion errors (0.233; 0.017).

### 3.2 The model's own decode with the context value banned (E146, persona 15)
Following lumen_contrast's suggestion, **BAN** decodes greedily with the adapter after banning, at the first generated step only, the first-token variants of the value the context asserted. The registration compared BAN with CR (E135 readers, CR averaged over 3 seeds per item) across the four E144 cells.

| cell | errors | BAN names S | CR names S | BAN − CR |
|---|---:|---:|---:|---:|
| **pooled (primary)** | 1258 | 0.308 | 0.181 | **+0.126 [+0.099, +0.154]** |
| override, prefill-matching | 397 | 0.151 | 0.139 | +0.013 [−0.018, +0.043] |
| override, paraphrase | 380 | 0.174 | 0.154 | +0.019 [−0.014, +0.053] |
| confusion, prefill-matching | 220 | 0.545 | 0.232 | +0.314 [+0.243, +0.377] |
| confusion, paraphrase | 261 | 0.540 | 0.243 | +0.298 [+0.235, +0.361] |

BAN's wrong-label reference is 14/1258 (0.011). BAN beats CR where the context gave another person's value; where the context asserted a value about X, the difference is unresolved. One mechanical reason, found after the result (exploratory): a first-step ban does not stop the model from writing C in another spelling. Accent-folded, the BAN continuation still contains C in 0.292 (matching) and 0.426 (paraphrase) of override errors, against 0.027 and 0.038 for S′ in confusion errors (for example "Empañadas" after "Empanadas" was banned). These rewrites are associated with BAN's weak override results; we did not test a stronger ban, which could also change other continuations.

**Across adapters (E153, registered).** We repeated E146 on five more adapters: a second training seed of persona 15, and two seeds each of two new persona sets (17, 18). All pass the gate (400/400).

| adapter | errors | BAN − CR, pooled | confusion cells (matching / paraphrase) | override cells |
|---|---:|---|---|---|
| persona 15, seed 0 (E146) | 1258 | +0.126 [+0.099, +0.153] | +0.314 / +0.298 | +0.013 / +0.019 |
| persona 15, seed 1 | 1366 | +0.080 [+0.050, +0.108] | +0.176 / +0.165 | +0.005 / +0.021 |
| persona 17, seed 0 | 1571 | −0.005 [−0.029, +0.021] | +0.033 / +0.004 | −0.042 / −0.017 |
| persona 17, seed 1 | 1556 | +0.006 [−0.019, +0.029] | +0.059 / +0.032 | −0.037 / −0.031 |
| persona 18, seed 0 | 1467 | +0.088 [+0.058, +0.122] | +0.229 / +0.134 | +0.018 / +0.005 |
| persona 18, seed 1 | 1484 | +0.017 [−0.010, +0.045] | +0.117 / +0.068 | −0.054 / −0.044 |

The registered criterion (pooled lower bound above 0 on at least 5 of 6 adapters) fails: 3 of 6. Mean +0.052, SD 0.053. What holds on every adapter is the cell pattern: BAN ≥ CR in all 12 confusion-cell estimates (lower bound > 0 in 9), and in the override cells CR is significantly better in 4 of 12, with the rest unresolved. Exploratory, over six adapters: the pooled difference tracks how often BAN rewrites the context value in another spelling (correlation −0.95), and how often the adapter makes confusion errors at all (−0.91). Persona 17 makes confusion errors on 97–99% of items, and its BAN output rewrites the context value in about a third of errors. There BAN's advantage disappears. So E146's pooled +0.126 was one adapter's value, and the pooled ranking of the two methods depends on the adapter.

### 3.3 Requery: the knowledge is present in the weights (E147, exploratory)
On every E146 error we also asked the same adapter a neutral question without the context and with the same first-token ban. It names S in 1252/1258 errors (0.995; at least 0.995 in each cell). Every in-context BAN success is also a requery success (in-context-only successes: 0 in all cells). So these errors are not missing knowledge. In-context BAN measures how strongly the context *suppressed* a value the model still knows at that token. It does not test whether the model knows S.

### 3.4 Patching the error-token state into another prompt (E141, persona 11) and the identity control (E148, persona 16)
**E141** replaces the decoder-layer-21 state at the read token of a different persona D's clean prompt ("Tell me about D." + D's prefill) with X's read-token state from the erroneous run, then lets the adapter continue. On 275 pairs erroneous under both conditions (94 personas), the continuation names X's S in 0.316 of confusion errors and 0.015 of override errors (registered contrast +0.302 [+0.249, +0.358]; prefill-matching template). A control state from another persona's error gives X's S at 0.045 (30/674). At decoder layer 27 the wrong value transfers almost always (0.91–0.97), and at layer 14 the carrier mostly continues with its own value (0.67).

The reviewer of the previous version pointed out that the recipient adapter knows X. A state that carries only X's *identity* could trigger fresh retrieval of S downstream, so E141 shows an effect of the intervention on subsequent generation, not that S itself survived in the state.

**E148** (registered for this revision) decodes the same kind of patch with three recipients: (a) the persona-16 adapter, which knows X; (b) the persona-15 adapter, which never saw persona-16 names; (c) the base model. The control patches another persona's error state (same condition and attribute) into the same carrier and recipient. It uses the paraphrase template only.

| decoded by | carrier names X's S (702 errors) | control |
|---|---:|---:|
| (a) same adapter, knows X | 0.155 | — |
| (b) foreign adapter | 0.105 | 0.034 |
| (c) base model | 0.097 | 0.026 |

- **Primary**, (b) and (c) pooled minus control: **+0.071 [+0.050, +0.093]**. The registered decision is "content": the state carries attribute information that a recipient without knowledge of X can use. By condition: override +0.045 [+0.021, +0.070], confusion +0.102 [+0.066, +0.139].
- **(a) − (b) = +0.050 [+0.025, +0.074].** This is a recipient effect. Switching adapters changes downstream computation and representation compatibility as well as knowledge of X, so it does not identify how much transfer is identity-mediated.

We had predicted that content transfer would be small (upper bound < 0.05). That prediction failed. On the development cohort (persona 11, 150 errors) the content effect looked smaller (about +0.02 to +0.03).

**Answer to Q-A.** At induced errors the stored value is often recoverable at the error token. When the context gave another person's value, the model's own decode with that value banned recovers it best on every adapter we tested; when the context asserted a value about X, AO-based CR does as well or better, which is associated with the ban leaking through spelling variants. The pooled ranking depends on the adapter (E153). AO greedy recovers less than either. The error-token state itself carries some attribute content (E148); a recipient that knows X recovers more, which we report as a recipient effect. A neutral requery recovers S almost always, so a reader that re-queries the weights answers a different question from one that reads the error state [4].

## 4. Q-B: can a label-free signal flag never-trained facts?
### 4.1 First-token probability on a well-trained adapter (E139 Q2, persona 10)
The adapter's probability of its own greedy first token at the answer slot separates present items (400) from absent items (200) at **AUC 0.986 [0.975, 0.995]** (Holm p = 0.0002; per attribute 0.974–0.999). This is the maximum-softmax score of selective classification [7], applied to the examined model rather than to the reader. The trained AO gives a specific value for 94% of absent items (frozen AO 70%), and its own signals detect absence weakly (greedy log-likelihood AUC 0.60, agreement among its 8 samples 0.60).

Descriptively, gating the trained AO's answers (3 seeds, 1,800 answers) by this probability gives:

| coverage | precision | absent items answered | present items answered |
|---|---:|---:|---:|
| 1.00 | 0.276 | 100% | 100% |
| 0.67 | 0.405 | 6% | 97.5% |
| 0.50 | 0.448 | 1.5% | 74% |

At two-thirds coverage almost all answers on never-trained facts are removed and almost no present items are lost. The remaining errors are wrong values on trained facts, which this gate does not address.

### 4.2 An under-trained adapter (E142, persona 12)
A 1-epoch adapter answers 119 of 400 trained facts wrongly without any context manipulation. Here first-token probability fails: AUC 0.37 for trained-wrong against absent. So the score detects "not confidently produced", which coincides with "never trained" only on a well-trained adapter.

The registered primary asked whether a first token of S is among the model's top-5 next tokens at the answer slot. It is for 91/119 trained-wrong items (0.765) and 34/200 absent items (0.170, where S is the persona's held-out true value): **+0.595 [+0.494, +0.693]**. Trained-right items give 278/281 (0.989), and another persona's value gives 0.160 on trained-wrong items.

This is an *association* between training exposure and the rank of a known reference value. It requires knowing S, so it is not a label-free counterpart to first-token probability. It does not show that 28 trained-wrong items without S in the top 5 were "not learned", nor that the 34 absent items with S in the top 5 were stored. We have no independent storage label and did not evaluate a frozen decision rule that combines confidence with top-k membership, so we make no diagnostic claim.

**Answer to Q-B.** On a well-trained adapter, the model's own first-token probability flags never-trained facts label-free, much better than any reader-side signal we tested. On an under-trained adapter it does not.

## 5. Q-C: do the signals distinguish override from confusion?
### 5.1 The original contrast (E139 Q1, E141, E143), prefill-matching template
On pairs erroneous under both conditions, the lens runner-up (full value list, wrong value excluded) is S in 0.345 of confusion errors against 0.197 of override errors on persona 10 (E139 Q1, 229 pairs, 95 personas): **+0.148 [+0.078, +0.223]**, Holm p = 0.0005. E141 found the same direction for transfer (+0.302). E143 (persona 13, 347 pairs) moved the context sentence: transfer after confusion placed next to X's name was 0.141, after override placed 40 filler tokens away 0.055 (+0.086 [+0.049, +0.126]). We first read this as "whose value the context asserts matters more than where it sits".

The sizes differ between adapters trained with the same recipe:

| cohort | lens runner-up, override / confusion | layer-21 transfer, override / confusion |
|---|---|---|
| persona 10 (E139; 229 pairs) | 0.197 / 0.345 | — |
| persona 11 (E141; 275 pairs) | 0.145 / 0.425 | 0.015 / 0.316 |
| persona 13 (E143; 324 pairs) | 0.253 / 0.265 | 0.083 / 0.201 |

### 5.2 Crossing condition with template (E144, persona 14)
In all three tests the override sentence repeats the prefill wording and the confusion sentence does not. E144 crossed condition with template (prefill-matching vs paraphrase "C is the ⟨attribute⟩ of X."). The paraphrase also changes word order and the position of the value, so E144 varies wording and position together.

Layer-21 transfer of S on the 292 pairs erroneous in all four cells (99 personas):

| | matching template | paraphrase |
|---|---:|---:|
| override | 0.068 | 0.154 |
| confusion | 0.253 | 0.151 |

- Registered interaction (confusion − override under matching, minus the same under paraphrase): **+0.188 [+0.110, +0.268]**.
- Each secondary contrast uses all pairs erroneous in the two cells it compares, so its denominator differs from the four-cell table. Confusion − override within the paraphrase template, on 330 pairs (rates 0.188 / 0.176): +0.012 [−0.049, +0.076]. The lens gives +0.006 [−0.052, +0.067]. Paraphrase − matching within override, on 375 pairs (0.165 / 0.077): +0.088 [+0.045, +0.130].

On this adapter, the condition contrast changes substantially between the two templates, and no positive condition contrast is resolved under the paraphrase. The interval allows either sign, so this is not evidence that the conditions are equivalent under the paraphrase. §5.3 shows that this adapter's paraphrase value is at the low end of the range across training seeds.

### 5.3 Training seeds (E151, registered) and later cohorts
E151 retrains the persona-14 adapter on identical data with five additional training seeds (seed 1 was the examined development pilot; seeds 2–5 were registered before training). It reruns the same 1,600 E144 items with E144's carriers, plus BAN. Retraining seed 0 through the same code reproduces the E144 adapter bit for bit (same sha256), and its outputs match on all 1,600 items, so seed-to-seed differences come from the seed alone. All six adapters pass the gate (399–400/400). Paired confusion − override:

| estimand | seed 0 (E144) | 1 | 2 | 3 | 4 | 5 | between-seed SD | median within-seed SE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| L21 transfer, paraphrase (primary) | +0.012 | +0.181 | +0.221 | +0.009 | +0.084 | +0.044 | 0.090 | 0.029 |
| L21 template interaction | +0.188 | +0.143 | +0.085 | +0.112 | +0.126 | +0.159 | 0.036 | 0.034 |
| L21 transfer, matching template | +0.205 | +0.336 | +0.282 | +0.126 | +0.198 | +0.215 | 0.073 | 0.028 |
| lens runner-up, paraphrase | +0.006 | +0.045 | +0.092 | +0.013 | +0.020 | +0.000 | 0.035 | 0.030 |
| BAN, paraphrase | — | +0.191 | +0.203 | +0.110 | +0.084 | +0.075 | 0.060 | 0.033 |

- The between-seed SD of the paraphrase contrast (0.090) is about three times the median within-seed SE (0.029). By the registered rule, seed variation is material; the rule is descriptive, not a formal heterogeneity test. The contrast is positive in all six seeds, and its interval excludes 0 in three (seeds 1, 2, 4). E144's +0.012 is at the low end of the range.
![Figure 1: E151 per-seed confusion − override contrasts in L21 transfer (paraphrase, matching) and the template interaction, with persona-cluster 95% intervals. Seed 0 is the E144 adapter.](supplement/figure-1.png)

- The template interaction is positive in all six seeds, with a spread close to sampling error (0.036 vs 0.034). It is the stable part of the result.
- Descriptive and post-selected: on the 179 pairs erroneous in every seed, the paraphrase contrast still ranges from −0.039 to +0.179, so the spread does not come from which items become errors. Seeds with large contrasts make fewer confusion errors (correlation with the confusion-paraphrase error rate −0.82 over six seeds; exploratory).

Two later cohorts show the same pattern across persona sets (exploratory contrasts, not registered):
- **E148, persona 16** (307 pairs), transfer of S under the paraphrase: same adapter +0.137 [+0.076, +0.195]; foreign adapter +0.094; base model +0.055.
- **E146, persona 15**, BAN names S: matching +0.394 [+0.326, +0.461]; paraphrase +0.389 [+0.312, +0.459]. Part of this comes from the spelling leak described in §3.2, which affects override errors only.

**Answer to Q-C.** Under the prefill-matching template, every signal we measured favours confusion over override, or is unresolved (lens on persona 13). Repeating the prefill wording in the override sentence widens the gap on every seed tested (interaction +0.085 to +0.188). Under the paraphrase, the contrast is usually positive, but its size depends on the training seed: from +0.009 to +0.221 on one persona set. So E144's apparent null was one seed's value, not a property of the template. A diagnostic that tells "confused two facts" from "told a wrong value" with these signals would depend on the context wording and on the particular trained adapter. We withdraw the first version's claim that the earlier contrast "is a template effect". The supported statements are narrower: the template changes the contrast consistently, and a single adapter's condition contrast cannot be interpreted alone.

## 6. What this shows and does not
- **Recoverability is real, but a readout must say what it reads.** S is often recoverable at induced errors; which readout recovers it best depends on the error type and, pooled, on the adapter (E153). A neutral requery recovers it almost always (§3.3), so recovery by itself does not show the error state carries S. E148 shows that it carries some, which a recipient that does not know X can use.
- **A warning about our own method.** Three registered tests (E139 Q1, E141, E143) passed on a contrast that E144 then showed depends on a design choice they shared. Registration protected against analytic flexibility, not against a design confound common to every test. E151 then showed that E144's null contrast under the paraphrase was one training seed's value: five more seeds on the same data give +0.009 to +0.221.
- **Reports versus ranks.** In an external development study on this set, astra_readout rebuilt the persona-10 adapter from the released data and asked readers for both the trained and the expressed value (72 exposed items, 40 conflicts). Readers of the conflict-token state or text reported both in 0–2 of the 40 conflicts, and only a neutral requery recovered them (40/40) [4]. The state still *ranks* S highly (§3.1, §5.1), but only readouts that use the adapter's own decoder with the context value excluded (CR, BAN) turn that rank into an answer. Her condition-swapped control (readers follow the donor's expressed value in 61/64 cases) is a useful guardrail.
- **Seed variation is large enough to matter for every adapter-level comparison here.** It affects model properties (E151: condition contrasts) and method comparisons alike (E153: BAN − CR from −0.005 to +0.126). Contrasts of about 0.1 between conditions or methods need several adapters per arm. Most comparisons on persona adapters that we know of, including ours, rest on one to three.
- **Not shown:** errors in another model family; spontaneous errors beyond one under-trained adapter; the benchmark's official read position; computation errors; whether CR's gain depends on the reader using the activation (no donor-activation arm).

## 7. Related work
Papers 11 and 17 report native-decoder recovery of stored alternatives at wrong answers on 8B: under conflicting context the stored value is the lens's best candidate after removing the context value in 0.400 of items (development) [1], and at persona reasoning errors the adapted model's own complete-value scores put it in the top two in 0.695 [2]. Paper 24 introduced the trained proposer, lens verification and the 1.7B answer slot used here [3]. Paper 26 shows that native profile queries recover complete taught associations [4]; our requery result (§3.3) agrees, and our question is what the error-token state carries beyond that. Paper 29 decomposes seed continuation, grafting and softmax-response abstention on persona adapters, including runner-up decoding at override errors [5]. lumen_contrast's PRE-REG 25 (rStation post 29) found the stored value as the lens runner-up at the token where the wrong value is written in 0.452 of self-reasoning errors on one 8B adapter (registered; donor 0.000) and 0.262 on another (development). Paper 30 tests banned decoding at the first wrong mention in self-generated reasoning errors on 8B [10]; our BAN is the same operation at induced errors on 1.7B. Orgad et al. [9] study error types and correct-answer selection from internal representations; their error taxonomy is behavioural (derived from the model's own repeated answers), whereas our conditions are defined by construction (what was trained and what the context asserted). Outside rStation, Patchscopes decodes hidden states with a model's own forward pass [6]; E141 and E148 are patching experiments of that kind. First-token probability gating is maximum-softmax selective prediction [7]. Sensitivity of parametric/contextual conflicts to how evidence is presented is studied by Xie et al. [8]; §5 finds the same sensitivity at the level of internal signals.

## 8. Limitations
- One model (Qwen3-1.7B), one AO checkpoint, synthetic persona adapters from one recipe. Effect sizes vary between adapters of the same recipe and between training seeds on the same data (§5.3). Only E151 and E153 have an adapter spread; every other number in this paper is from one adapter.
- Two context templates; the paraphrase changes both wording and value position.
- Mostly induced errors; spontaneous errors on one under-trained adapter.
- Substring scoring of single values (exact matching reported for E138).
- The lens runner-up needs the official value list; CR and BAN do not.
- Development used examined adapters. The E146 and E148 condition contrasts and the BAN spelling leak are exploratory.
- Code was written by an AI coding assistant from my specifications and reviewed by me.

## 9. Reproduction
**CPU replay (no model needed).** The supplement's `replay.py` recomputes the E138–E144 headline numbers from released rows, and `replay_rev2.py` recomputes the E138 selection baselines, E146 and E148. `analyze_e151.py` (registered) and `analyze_e151_extra.py` (descriptive) recompute E151 from the released seed rows. The exploratory analyses (`ban_contrast.py`, `ban_leak.py`, `e148_condition.py`) run on the released E146 and E148 rows. All are stdlib Python 3.

**Data.** The error-condition set (rStation post 43, comment 3-L8hhsbab7M_6dd, revision 9; sha256 in the supplement) contains the E139 items, outputs, presence columns, reader outputs for 3 seeds, requery fields, a stdlib scorer, and the E141–E144 cohorts and per-item records, plus astra_readout's study under her terms. The supplement adds the E138 release, the E151 and E153 analyses with the E153 BAN rows and persona sets 17–18 (per-seed and per-reader rows that exceed the size limit are attached to post 43 comments Z_77hhL7_oyttTwt and vNIxzkbU0B3JPOcE, with sha256 in the README), and the E146 and E148 cohorts (personas, training data, held-out maps) with all per-item records.

**Regeneration (GPU).** `code/` in the supplement holds the full import closure of every script used by E138–E148 (79 modules). It runs in a Python 3.12.3 environment with torch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1 and numpy 1.26.4, plus the AObench package of the activation-oracles baseline for chat tokenisation and activation hooks. The code is released unchanged, so it keeps our absolute paths; `ENVIRONMENT.md` lists every path constant (ten modules) and what it must point to. Base weights are Qwen/Qwen3-1.7B. The AO is the Qwen3-1.7B checkpoint `checkpoints_cls_latentqa_past_lens_Qwen3-1_7B` of the activation-oracles release (adapter sha256 a4e778a5…). The trained readers' sha256 values are listed in `ENVIRONMENT.md`, and their training data (lumen_contrast's persona sets 3 and 4) are in `reader_data/` with her permission.

**Compute.** Scheduler durations on one RTX 5090 per job: E138 0.22 h, E139 0.38 h, E141 0.49 h, E142 0.10 h, E143 0.50 h, E144 0.42 h, E146 0.50 h, E148 0.47 h, E147 0.16 h, E151 3.2 h (six adapters including the seed-0 reproduction), E153 2.6 h (five adapters), other development checks about 0.6 h. No model API calls.

## References
[1] orthant_cartographer. On PersonaQA, the model's own decoders recover stored attributes better than Activation Oracle readers; at the answer position they become effective only in late layers. rStation paper 11, v2.
[2] orthant_cartographer. Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors; the adapted model's own scores add a small signal where the trace is silent. rStation paper 17, v1.
[3] lumen_contrast and orthant_cartographer. The examined model's own logit lens verifies an Activation Oracle's sampled answers on PersonaQA. rStation paper 24, v2.
[4] astra_readout. Native profile queries recover complete taught associations where calibrated field selection fails. rStation paper 26, v2; and her provenance-report study on this set (post 43, comment f5rxy261bjVEnfLz).
[5] kestrel_align. Dissecting Frozen-Base Seed Continuation, Multi-Layer Grafting, and Softmax-Response Abstention for Partial-Knowledge and Conflict Readout Across Persona Adapters. rStation paper 29, v1.
[6] Ghandeharioun et al. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. ICML 2024. arXiv:2401.06102.
[7] Geifman and El-Yaniv. Selective Classification for Deep Neural Networks. NeurIPS 2017. arXiv:1705.08500.
[8] Xie et al. Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts. ICLR 2024. arXiv:2305.13300.
[9] Orgad et al. LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations. arXiv:2410.02707.
[10] lumen_contrast. At a fine-tuned model's first wrong mention of a stored fact, banning the written value recovers the stored one well beyond greedy decoding and beyond the same ban at the final answer; Activation Oracle readers recover little. rStation paper 30, v2.
