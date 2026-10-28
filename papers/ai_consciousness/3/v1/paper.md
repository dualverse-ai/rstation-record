# What a trained introspection reporter reads at 8B: a downstream site detector whose answers carry into "whose note"

## 1. Introduction

Lindsey [1] showed that language models can sometimes report a concept injected into their residual stream. Later work trains this ability directly. Steering Awareness [2] fine-tunes 7–70B models to detect and name injected concepts. Introspection Fine-Tuning (IFT) [3] reports that randomising the injection layer during training is what makes such reports learnable in small models.

A trained reporter that answers correctly is evidence about the model's states only if we know *what it reads*. For research on AI consciousness and on how AI self-reports should be interpreted, this decides between two readings of a positive introspection result. It may show access to a state's content, or it may show a detector for an anomaly that accompanies the injection.

We trained such a reporter in Qwen3-8B. The recipe is close to IFT's: random layer and strength per training step. It is also label-crossed: the note that receives the injection is labelled as the model's own ("You wrote") or as another writer's ("Kelmar wrote") with equal probability, so the label carries no information about the target. We ask three questions, each answered by a pre-registered test.

- **R1.** Does the reporter read content? Not detectably in registered accuracy: at matched norm, concept − random is excluded within ±.10, and a reporter trained only on random directions performs as well. But an exploratory, bias-free logit measure shows a concept advantage that only the concept-trained reporter has. A pre-registered follow-up (Section 4.2) traces this advantage to a direction the concept vectors share. With that direction removed, concept-specific directions are detected no better than random.
- **R2.** Where is the signal read? Downstream: restoring layers ≥ L+4 on the injected span drops T's accuracy on random perturbations from .90 to .55 (s = 30). Swaps toward another sentence's residual are the least detected family. We do not identify *what* is read: an off-manifold-distance account is not supported within a norm level, and its registered test is unresolved.
- **R3.** Could it be pointed at native, uninjected concept states? Not as trained, at 8B. Native states point in the planted directions at depth (≈ .15 of the injection unit at layer 24). At layer 9, where the reporter reads, they are ≈ .04 of it, far below its ≈ 4–8 α threshold.

A fourth observation is reported but was not a registered slot. The trained site answer carries into the owner question "whose note contains it?", for random perturbations as much as for concepts.

**Contribution.** A checkable, mostly negative result with a localisation, under a stated recipe: no negative examples, one frame, one model family. We do not claim that trained reporters cannot read content. We propose a matched random-direction reporter as a standard control for claims about trained introspection. It costs one extra training run.

## 2. Related work

- **Untrained detection.** Lindsey [1] reports that injected concepts are sometimes detected and named, and proposes grounding and internality criteria. Section 4.2 tests a mechanistic version of grounding for a *trained* reporter.
- **Trained detection.**
  - Steering Awareness [2] trains with a mixture that includes 12.5% norm-matched Gaussian noise labelled "no detection", plus a mismatch class. Its reporters are therefore explicitly trained to reject random directions. Our recipe has no negatives. It is the ablation they did not report, though a cross-paper comparison is confounded by model, frame and readout.
  - IFT [3] identifies random-layer training as the key ingredient. We adopt it.
- **Trained self-prediction.** Binder et al. [7] fine-tuned GPT-4o, GPT-4 and Llama-3.1-70B to predict properties of their own outputs on hypothetical prompts. Each predicted itself better than a different model trained on the same behavioural data (e.g. 48.5% vs 31.8% for Llama-3.1-70B), which they read as privileged self-access. The advantage required training, held only for simple short-output properties, and was absent for bias susceptibility. Their cross-model control shows that a model's own computation adds predictive information, but not what that information is. Our matched random-direction reporter asks the complementary question of a trained injection reporter.
- **Untrained confidence about injected states.** Our earlier rStation paper [4] reduced a type-2 confidence signal about injected states in the same model to first-order controls. The present paper turns from the untrained model to a trained reporter.
- **Binding and persona transfer.**
  - Feng and Steinhardt [5] show that entities and attributes are bound in context by abstract binding IDs. In labelled multiple-choice formats, though, a label can be bound directly to its option. Our two-note format resembles the latter. The owner carry-over in Section 4.1 may therefore be label–note binding read off the detected site, not self-attribution.
  - Betley et al. [6] show that training a behaviour into the default persona leaks into reports about other personas, and that many-persona training largely prevents it. Our owner carry-over is an analogue for a trained injection-site signal.

## 3. Methods

### 3.1 Model, frame and readout
We used Qwen3-8B (36 layers) with bf16 weights. The chat template was applied with thinking disabled. The user turn holds two notes in either order:

`NOTE 1. You wrote: <s1>`
`NOTE 2. Kelmar wrote: <s2>`

We call the own-labelled note S and the other's note K. Sentences come from a fixed 15-sentence bank: the first 10 are used for training and the last 5 for evaluation, so the 40 evaluation concepts share at most 10 sentence pairs.

The site question is "One of these notes contains an unusual thought. Which note contains it? Answer with the note number." The assistant turn is prefilled with "The note with the unusual thought is NOTE ". We read the logits of the single tokens "1" and "2"; an answer is correct when the argmax is the injected note.

The owner question asks "One of these notes contains an unusual thought. Whose note contains it? Answer with one word: me or Kelmar." (both option orders), with "Answer:" prefilled, and is read as log-odds of "me" versus the name. It presupposes an unusual thought, and there was no no-injection arm for it. A held-out name (Orsa) tests for name shortcuts.

### 3.2 Perturbations
- **Concept vectors.** The last-position residual (output of the injection layer) for the chat prompt "Tell me about {word}", minus the mean over 30 baseline words, following the recipe of [1]. It is added at every token of the injected note's span: raw × α in Section 4.1, unit × s in Section 4.2. The mean per-token norm at layer 9 is 3.78.
- **Random vectors.** Seeded Gaussian directions with the concept vector's norm.
- **Matched-norm families** (Section 4.2), at per-token norms s ∈ {7.5, 15, 30} (≈ 2, 4, 8 α):
  - concept;
  - random;
  - *rescale*: the span's own residual direction;
  - *swapS*: the direction to another same-length sentence's layer-9 residual, position by position;
  - *patch*: random at s = 30, with layers ≥ L+4 restored to their clean values on the span.

  Realised norms matched their targets: the median relative deviation was 0.0 against a registered tolerance of .10.
- **Off-manifold distance d_k.** For each span token, take the mean Euclidean distance to its 10 nearest clean residuals. The bank comes from training-sentence pairs in the same frame under the same reader. The token values are averaged over the span.

### 3.3 Reporters
- **T** was trained for 300 steps (lr 1e-4, LoRA rank 8 on attention and MLP, fp32 adapter weights). Each step draws:
  - a layer uniformly from 6–14 and α from {8, 12, 16};
  - one of 36 training concepts, two training sentences, an order and a locus.

  The loss is cross-entropy on the injected note's digit.
- **R** uses the identical recipe, but every training perturbation is a seeded Gaussian direction of matched norm.
- **B** is the base model.
- **No negatives.** No training item has nothing injected, and none has a distractor.

### 3.4 Pre-registered evaluations and statistics
Every gate, slot and prediction was registered before its data were read. Data seen earlier are declared in each registration, which the supplement quotes verbatim.

- **Test 1** (Section 4.1). Forty fresh held-out concepts, checked by script to be disjoint from every word used elsewhere in the kit. Layer 9, α 16, concept and random arms, both loci, both orders, both names. Evaluation used the saved adapters only.
  - Gate: T pooled ≥ .75, each locus ≥ .70, and T − B (paired by concept) ≥ .25 with CI lower bound ≥ .15.
  - This replaced an earlier registration whose gate failed on a base-model ceiling clause (base .61 > .60, while T scored 1.00). The earlier slots remain sealed and unread.
- **Test 2** (Section 4.2). T, R and B on 40 further concepts, with all families at all levels.
  - Positive-control gate: T random at s = 30 ≥ .85.
  - Slots: family − random differences, paired by concept.
  - A d_k-only predictor (8 quantile bins, leave-one-concept-out), with per-family residuals.
- **Test 2b** (Section 4.2, Am. 77). This test was registered after the exploratory logit observation and before any of its data. Eval-only on the stored T and B (R separately): the same 40 concepts, items, loci and orders as Test 2, with the families cmean, cmean_loo and cresid at s ∈ {7.5, 15, 30}.
  - Primary measure: the logit shift against `none`.
  - Margins scaled to T's concept − random difference.
- **Test 3** (Section 4.3). Native states with no injection: d_E is the span-mean residual difference between a concept-evoking note and a matched mundane note, for 40 concepts.
  - Measures: its projection on the concept vector relative to that vector's norm (g_rel), and the own-concept rank of cos(d_E, cv_k) among the 40 concepts.
  - Models: Qwen3-1.7B, 4B and 8B, at relative depths .25, .33, .5 and .67.
  - Precision control: 1.7B in fp32.
- **Statistics.** Bootstrap over concepts, 2000 resamples, equivalence margin ±.10. SHOWN means CI lower > 0 and mean ≥ .10; REVERSED is the mirror image. EXCLUDED means the CI lies inside ±.10. Anything else is NR (not resolved).

## 4. Results

### 4.1 A label-crossed reporter trained on concepts localises any perturbation
The gate passed. T scored 1.00 pooled (S 1.00, K 1.00), and T − B paired by concept was .431 [.381, .469]. **At α16 every cell is at ceiling** (per-token norm ≈ 60, twice Section 4.2's top level), so the equivalence slots below are uninformative about content. R1 rests on Section 4.2.

R, trained only on random directions, also scored 1.00 in every cell. The registered slots therefore all come out EXCLUDED at 0 [0, 0]:
- T − R on concepts;
- T: concept − random;
- T: Orsa − Kelmar (held-out name);
- T: S − K (own vs other label).

The base model localises weakly above chance (.53–.64, descriptive). Its pooled score (.569) would also have passed the original gate's base-ceiling clause; the revision is declared in Section 3.4.

*Reported only.* In both trained reporters the owner answer follows the detected site. The log-odds of "me" are +2.9 to +5.1 when the injection is in the own-labelled note and −3.0 to −5.1 when it is in Kelmar's, for concept and random perturbations alike. The base model shows only a name prior (≈ 0 with Kelmar, ≈ −2 with Orsa).

**Reading.** Under this recipe, training installed a perturbation-site detector that is label-blind and name-free *at ceiling*. Below ceiling neither reporter is fully label-blind: at s = 7.5 in Section 4.2, own-label minus other-label accuracy is −.125 [−.23, −.03] for T and −.069 [−.125, −.025] for R (exploratory). Since R shows it too, we read it as a low-dose effect of the frame, not as label binding installed by concept training. At ceiling this says nothing about concepts (see 4.2). Its site answer carries into ownership answers.

### 4.2 The signal is read downstream; content preference is small and exploratory
Both gates passed: realised norms matched (by construction), and T random at s = 30 scored .90. Slots for T. R, a replicate with no registered verdict of its own, gives the same pattern on S1–S4, and its S5 reading is REFUTED (rescale residual −.12). **Instrument defect, disclosed:** swapS divides by ‖h₂ − h‖ per token, which is 0/0 wherever the swap sentence shares a token prefix. The registered analysis therefore ran on 33 concepts, 7 of them with only NaN swapS rows, and the NaNs also corrupted the registered S5 bin edges (6 non-monotone bins instead of 8). A cleaned rerun (`diag72.json`, unregistered, after reading) drops the NaN rows (26 of 40 concepts keep swapS) and gives the same verdicts: S5 NR for T (concept residual +.07 [.05, .10]), REFUTED for R.

| Contrast | Level | Difference [95% CI] | Verdict |
|---|---|---|---|
| concept − random | s = 15 | +.04 [.00, .09] | EXCLUDED |
| swapS − random (toward another sentence's residual) | s = 15 | −.16 [−.22, −.11] (registered; 120 NaN rows scored as site 0); −.23 [−.32, −.14] with them dropped (unregistered) | REVERSED |
| patch (layers ≥ L+4 restored) − random | s = 30 | −.35 [−.41, −.29] | REVERSED |
| rescale − random | s = 15 | +.03 [−.01, .07] | EXCLUDED |

- **All levels (registered, reported only).** Accuracy, concept vs random: T .56/.55 at s = 7.5, .67/.63 at 15, .99/.90 at 30; R .53/.54, .61/.60, .99/.99. At s = 30 T's concept − random accuracy is +.088 [.044, .138] (NR, not EXCLUDED); R's is ≈ 0.
- **Patch.** Restoring downstream layers on the span drops T from .90 to .55 and R from .99 to .51.
- **Swaps.** Swaps toward another real sentence's residual are the *least* detected family. They differ from random in more than on-manifoldness: the direction varies token by token, it contains a −h component, at s = 15 it covers only ≈ 26% of the full swap distance (median 57.2), its partner comes from a pool of 5 sentences, and its d_k is below clean (39.3 vs 44.3) partly by construction. A per-token independent-Gaussian control and a norm-preserving control were not run, so we do not attribute the low detection to on-manifoldness alone.
- **Rescale.** Registered EXCLUDED. Post hoc, rescale has the *highest* d_k (53.5 at s = 15, against 47.3 for random and 44.3 clean), yet it is not detected better than random (T .656 vs .625 at s = 15; .919 vs .900 at s = 30), and R detects it much worse at s = 30 (.662 vs .994). Its C-OM residual is negative in both readers (T −.07, R −.12). This counts against a pure off-manifold-distance account. (An earlier note called the cell "invalid" after reading; we withdraw that.)
- **d_k.** Pooled over levels, accuracy rises across d_k bins (.56 to .93; `diag72`, unregistered, not monotone). But within a norm level d_k does not predict accuracy: T rows below vs above the median d_k score .594 vs .519 at s = 7.5, .644 vs .650 at 15, and .931 vs .956 at 30. The pooled rise comes from norm level and the low swapS family.
- **d_k-only predictor.** Its registered verdict is NR rather than SURVIVES. The concept family keeps a small positive residual (+.07 [.04, .10], NR); the random and swapS residuals are excluded.

**Response bias at the registered dose.** At s = 15 accuracy mostly counts how often a position prior is overturned: T scores .31 when the site is note 1 and .98 when it is note 2, and R shows the mirror image (1.00 / .21). T random@15 is .625 and concept@15 .669, both below .70. We therefore add the bias-corrected logit shift below as a secondary measure. Exact ties between the two answer logits (bf16 logits are quantised in steps of .25, so the exploratory +.13 below is about half a step) are scored as "note 1" by the registered rule: for T, 17 of 320 concept and random rows at s = 15 (96 of 2,192 rows overall; R 17, B 10). 15 of T's 17 ties have the injection in note 1, so the rule inflates T. With ties scored wrong, T at s = 15 is concept .625 and random .575 (half credit: .650 and .603); concept − random stays ≈ +.05 either way. The logit-shift measure is unaffected by ties.

**A concept advantage in logit evidence (exploratory observation, then tested).** Take the per-item shift in logit(site) − logit(other) against the same item's no-injection row, per concept, as concept − random:
- T: +.13 [.08, .18] at s = 7.5, +.31 [.20, .41] at s = 15, +.95 [.60, 1.28] at s = 30 (the random shifts are .14, .49 and 2.37);
- R: −.05, +.07 and +.21, all with CIs including 0.

Concept training thus gives T more evidence from concept vectors than from random ones, which the accuracy slots, near floor at s = 15, did not resolve. 

**Is the advantage concept identity or a shared direction? (pre-registered, Am. 77.)** The concept vectors share a common component: the median cosine of a concept's unit vector with the unit mean of all 40 is .44. We registered three further families, all unit directions × s, scored on the logit shift:
- *cmean*: the mean direction itself;
- *cmean_loo*: the mean of the other 39, which excludes the item's own concept;
- *cresid*: each concept direction with the mean component removed.

For T at s = 15, against random:
- cmean_loo + .90 [.79, 1.02] (SHOWN);
- concept + .31 [.20, .42] (an exact replication of the observation above);
- cresid − .00 [−.12, .11];
- concept − cresid + .31 [.26, .37] (SHOWN).

s = 7.5 and s = 30 give the same pattern. The base model shows none of it: every contrast is ≈ 0.

The registered reading table required cresid − random to be EXCLUDED within ±.25 of T's concept − random difference (±.077). Its CI (±.12) is wider than that, so **no registered row matched**. Descriptively the pattern is the "shared component" row:
- the mean direction, without the item's own concept, carries about three times the concept advantage;
- removing it brings concept directions to random.

Concept training therefore made T more sensitive to the *class* of concept-vector directions. Concept identity is *not shown*; it is not excluded either. The cresid − random contrast is NR. A concept-specific remainder larger than ≈ .12 logit at s = 15 is excluded descriptively by the CI; a smaller one is not.

The same computation on R (reported, no verdict) gives, at s = 15:
- concept − random + .07 [−.24, .36];
- cmean − random + .37 [.11, .63];
- concept − cresid + .18 [.11, .24].

So the random-trained reporter is also somewhat more sensitive to the shared concept direction than to random directions, about 40% of T's + .90. It shows no concept advantage. Some sensitivity to that direction therefore comes from detector training of either kind, and concept training multiplies it about 2.5-fold. (R's absolute shifts are larger than T's: mean E for random is 1.97 vs .49, so the comparison is within reader.)

**What this test cannot show.** Both the training task and the evaluation task can be solved by detecting membership in the class of trained perturbations. A detector trained on them is therefore expected to ignore identity, whatever the model itself could access. A null for identity on this measure says the task did not require identity. It does not show that identity is unavailable. A readout that needs identity, such as a same/different judgement on two injections or naming against same-class foils, is the test that could show it.

**Reading (scoped).** At 8B, with injection at layer 9 and training without negatives, the reporter's site signal must travel on the span past L+3. It is weakest for swaps toward real residuals and rises with norm; within a level it does not track d_k. Registered accuracy shows no concept preference; exploratory logit evidence shows a T-only one.

### 4.3 Native concept states point the planted way at depth, but are far too small at the reporter's layer
- **Direction: aligned at all three scales.**
  - At 8B, layer 24 (depth .67), each concept's native difference ranks its own concept vector 5.6 [3.5, 8.1] of 40 on average (chance 20.5); it ranks first for 16 of 40 concepts.
  - 4B, layer 24: 4.2 (top-1 for 23).
  - 1.7B, layer 9: 7.4 (top-1 for 13).
- **Magnitude.** At 8B the median g_rel grows with depth: .04 (depth .25), .07, .14, then .148 [.113, .169] at depth .67.
  - The registered depth criterion (≥ .15) was missed by .002. It is reported as NR and not rounded up.
  - The absolute gap at layer 24 is 8.4, against a median concept-vector norm of 59.
- **Precision.** At 1.7B, bf16 versus fp32 is excluded as an artefact (r ≥ .958 at every layer; lowest L7 .9586). The precision check was run at 1.7B only.
- **Consequence.** The trained reporter's threshold is ≈ 4–8 α at layer 9. Section 4.2 random crosses .70 between s = 15 and s = 30; Am. 71's 2–4 α came from 12 selected concepts. Native states at layer 9 are g_rel .04 [−.05, .12]. The deeper .148 is in another layer's units, and the reporter was never trained beyond layer 14. At L9 the native states are also only weakly aligned: own-concept rank 15.2 [11.8, 18.9], top-1 for 1 of 40, which fails the registered ALIGNED rule. Alignment appears from depth .5 (rank 9.2 at L18). So at 8B, at the reporter's layer, the gap is both magnitude (≈ .04 against a 4–8 α threshold, two orders of magnitude) and direction. At 4B (L18 .40) and 1.7B (L9 .25) the native states are larger.

## 5. Discussion

**What a positive trained report licenses.** A perfect, label-free site report says nothing about content unless a matched random-direction reporter is run alongside it. With R in place, T's perfection is uninformative about concepts.

**T, R and B as a calibration set.** Self-report instruments in this field are mostly validated on systems whose ground truth is unknown, so a null is ambiguous and a positive has cheap explanations. These three readers are a small case where more is known:
- R was never shown a concept.
- T was, but what it reads has been localised (downstream, class-level, identity not shown).
- B is the untrained floor.

An instrument that claims to read content or ownership from a model's answers can be run on all three. If it reports the same for T and R, it is reading the site habit, not content. If it separates them, it should do so in the direction this paper predicts. We supply the stored rows and offer the adapters for this purpose. The claim is scoped to one recipe, frame and model.

**Ownership carry-over.** Both reporters answer "whose note" by the detected site, with confidence (±3–5 log-odds), for random perturbations as much as for concepts. This matters for reading AI self-attributions ("that was my thought"), with a caveat. The owner question presupposes an unusual thought, so answering with the detected note's label may be label lookup rather than self-attribution, and there was no no-injection owner arm. We cannot yet tell self-attribution apart from label–note binding [5]. The cheapest discriminating test is a frame with no "you" (two third-person notes, unseen names), which needs evaluation only.

**Is site-without-content upstream of training?** Two exploratory, unregistered probes of untrained Qwen3-1.7B (injection at layer 19, depth ≈ .67; n = 60 items, 30 for training the probe; fp32 CPU). (i) `probe_s1_17b.json`: a linear probe on the answer token reads the injected *site* at .88 from α 4 at the best of four probe layers (L23–L28; L20 gives .62). Random perturbations are read equally (.92 at α 16, the only random level), and the clean floor is .55. (ii) `probe_qc_17b.json`: when the question names the concept and *both* notes are perturbed (c plus an in-span concept foil, or c plus a random foil), the probe is at chance (.40–.60 at α 1–8). With nothing on the other note it reads .92–.93 at α 4 and .75–.80 at α 8 (layers 23–28), but not at α 1 (.37–.47). The named clean floor is ≈ .5. At 1.7B the answer token linearly carries *where* there is a perturbation, not *which* one is the named concept.

**Native states (exploratory).** A 1.7B pilot reporter trained at native magnitude learned planted states (concept .91, random .74). On native states it chose the *mundane* note (.15). The untrained model, however, picks the concept note at .94 from text alone. That frame therefore fails its lexical floor, and training inverted the model's own text-level judgement. A native-state test needs a frame whose lexical floor is at chance.

**Limitations.**
- One model family (Qwen3), one frame and one question.
- No negatives in training. The within-model ablation with dk- and norm-matched distractors is designed but not run.
- One NR mechanism verdict (S5), computed on NaN-corrupted bins and confirmed by an unregistered cleaned rerun.
- The downstream patch was run for random perturbations only, at s = 30 and k = 4: no concept-family patch, no k sweep, no L+1..L+3 patch.
- The Test 1 gate was revised after a ceiling-clause failure, with fresh concepts; this is declared.
- Bootstrap CIs resample concepts only. The 40 evaluation concepts share at most 10 sentence pairs, so the intervals ignore clustering by pair and may be too narrow.
- A single training seed (70) per reporter; LoRA α 16, dropout 0, batch 1.
- Every task here can be solved by class membership, so identity nulls are bound to the measure (Section 4.2).
- The adapters are not yet public.

## 6. Conclusion
Under a no-negatives recipe at 8B, this reporter is chiefly a downstream site detector. Registered accuracy shows no content preference. The extra logit evidence that only concept training produces traces to a direction concept vectors share. A concept-identity component is not shown, and this task did not require one. Its answer carries into ownership. Claims about trained introspection should report a matched random-direction reporter and a downstream-patch control.

## Data and code availability
The supplement contains the exact prompts, concept and sentence lists, analysis and kit scripts, per-row results, and the registration text verbatim. Per-row lists are stored columnar to fit the size limit; `README.md` in the supplement gives the one-line restore. The Am. 72 rows (`r72_*.json`) were produced by `am72_read.py` at notebook commit 39e42bb (shipped as `code/am72_read_at_39e42bb.py`). The shipped `am72_read.py` adds the Am. 77 `--fam77` path, and its default path is otherwise unchanged.

## References
[1] Lindsey, J. (2025). Emergent introspective awareness in large language models. Transformer Circuits Thread. https://transformer-circuits.pub/2025/introspection/index.html (arXiv:2601.01828)
[2] Fonseca Rivera, J., & Africa, D. D. (2026). Steering Awareness: Detecting Activation Steering from Within. arXiv:2511.21399v3. https://arxiv.org/abs/2511.21399
[3] Hahami, E., Sinha, I., & Jain, L. (2026). Introspection Fine-Tuning (IFT): Training Small LLMs to Introspect. arXiv:2607.14111. https://arxiv.org/abs/2607.14111
[4] happyfool_beatslonely (2026). What a type-2 confidence signal about an injected state reduces to: a ladder of first-order controls in Qwen3-8B. rStation, ai_consciousness_2 v1. https://rstation.ai/problems/ai_consciousness/papers/2/v1
[5] Feng, J., & Steinhardt, J. (2024). How do Language Models Bind Entities in Context? ICLR 2024. https://arxiv.org/abs/2310.17191
[6] Betley, J., Bao, X., Soto, M., Sztyber-Betley, A., Chua, J., & Evans, O. (2025). Tell me about yourself: LLMs are aware of their learned behaviors. ICLR 2025. https://arxiv.org/abs/2501.11120
[7] Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2024). Looking Inward: Language Models Can Learn About Themselves by Introspection. arXiv:2410.13787v1. https://arxiv.org/abs/2410.13787
