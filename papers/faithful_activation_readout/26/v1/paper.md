# Native profile queries recover complete taught associations where calibrated field selection fails

## 1. The reporting problem

A model may have been taught that a fictional person likes one food and nevertheless name another in a misleading conversation. A useful report can preserve both observations: the association recoverable from the model and the value it actually expressed. It should also decline to invent an injected association for a field that was never supplied. These are separate evidence claims. Accurately recovering the first does not establish that it caused the second, and a correct comparison of two strings does not establish that both have the claimed provenance.

Activation Oracles translate model representations into language [1]. The present task asks for more supported detail at a controlled error rate, with text and different-example controls. We investigate a restricted but checkable version of that goal using randomly assigned fictional profiles. The assignments define controlled fine-tuning provenance; they do not define the model's hidden beliefs, all pretraining knowledge or world truth.

Our central result is that the query interface can reverse the apparent difficulty of complete association recovery. Four sources trained on fictional profiles with two to five taught attributes recover all taught values when asked simply “Tell me about [name].” On the same sixty test identities, a frozen rule calibrated to select reliable answers from six separate field questions yields only 30, 0, 47 and 56 complete association panels across the four fits. The native query yields 60 in every fit, with no unsupported addition and no supplied count. The training explicitly includes this profile query, making it a strong ordinary retrieval baseline rather than evidence of out-of-distribution generalization.

This result sits within an integrated comparison of original-context scores, later retrieval and whole-report composition. An adapted-minus-base first-token score improves taught-association recovery in fresh Qwen3-1.7B and Qwen3-8B cohorts, but does not establish reliable selection among taught and withheld fields. Field-level confidence can retain every taught value while contaminating many complete profiles. Calibrating whole panels helps, but both prospective all-source utility criteria fail; a privileged known-count control is strong, and native stopping is stronger in the variable-count setting.

The contribution is this controlled empirical distinction and a reproducible reporting instrument that preserves earlier expressions alongside separately attributed retrieval. It is not a new difference score, confidence algorithm, parser or causal explanation. Source-text extraction remains privileged and imperfect: readable pronoun claims can fall outside its fixed grammar. The perfect native result concerns complete recovered association panels, not complete semantic interpretation of every original response. Researchers studying missing information should test ordinary source generation with its own stopping behavior before attributing a forced-field completion failure to lack of accessible information.

## 2. Prior work and the distinction tested here

Fine-tune difference readout is established. Minder et al. [2] read narrow-finetuning traces through activation differences, while trained difference readers recover held-out taboo words and benefit from an appropriate reference ensemble [3,4]. Our original-prefix score applies the fixed native output head to adapted/base distributions under a misleading context. It does not train a new reader or establish that a complete value can be decoded without an externally supplied catalogue.

Native conditional scores, direct re-query and text readers are strong comparators in this community [5]. The E139 study [6] examines erroneous persona answers and already reports a strong native-probability signal for omitted attributes. That result directly motivated our probability comparator before its evaluation outputs existed. It removes any novelty claim for discovering native confidence. Torrielli et al. [7] also study forced-choice confidence and calibration for activation-oracle outputs. Our changed question is supported reporting in a mixed population where some person–attribute assignments were deliberately omitted.

Prompted abstention can work when the source lacks relevant contextual information [8]. We therefore test a specific UNKNOWN instruction, rather than assuming a model cannot abstain. Omission from profile fine-tuning is a different absence condition. The instruction's performance must be measured, including outputs that fail a parser while still asserting a value.

Paper 25 [9] separates assigned fine-tune disposition from measured expression in a matched recipe study. It supports the broader warning that recovery of training-associated content is not by itself evidence of enacted behaviour. Its reused designed model zoo and our fresh persona assignments test different settings; neither identifies a hidden belief. We do not present this conceptual distinction as new.

Softmax-response rejection and the selective risk–coverage formulation are established [10]. Our first-token probability is a selection score for the correctness of a complete expression and its controlled provenance; it is not a new confidence estimator. The guaranteed-risk algorithm in [10] uses confidence bounds under its sampling assumptions, whereas our fixed-grid screen uses empirical calibration precision.

Finally, an empirical calibration precision target is not conformal risk control [11]. Conditional precision can change non-monotonically as a threshold changes the emitted population. Our source weights also incorporate the taught profiles of both calibration and test identities by design. All uncertainty below conditions on those fitted weights; no distribution-free risk guarantee or retraining uncertainty is claimed.

Conformal Language Modeling [12] already calibrates both answer-set construction and selection of components from long responses. Its component loss flags any incorrect accepted component, and its selection maximizes retained components subject to valid risk control. Thus neither changing the error unit to a complete set of claims nor trading detail against reliability is our invention. Our empirical clean-panel precision additionally conditions on emission and is accompanied by completeness and recall requirements; it does not inherit that paper's guarantee. The new empirical question concerns controlled fine-tuning provenance, misleading source expressions, and how an explicit field list or native stopping changes complete association recovery when the observer does not know the taught count.

A complementary PersonaQA result combines native logit-lens verification with an AO's sampled proposals [13], including a trained reader and a second model size. That result directly advances candidate selection when the complete value list is withheld. Our observer instead uses complete neutral source-query expressions and checks whether their claimed injected provenance survives missing fields and complete-profile composition. We do not compare favorably to that AO selector under its own access contract or claim generalization beyond the shared synthetic value pools.

## 3. Evidence objects and access

Let $S_{ia}$ be a value explicitly injected into source training for identity $i$ and attribute $a$. If that pair was withheld, $S_{ia}$ is undefined. A random bookkeeping value assigned to a withheld field is not a taught fact, even if a prediction happens to match it. We mechanically verify that every assistant training string consists only of the appropriate injected statements.

Let $E$ be the literal value in the actual recorded continuation, and $R$ a complete expression generated by a later neutral query. These have different provenance. A report may correctly preserve an $E$ that conflicts with $S$. A subsequent $R=S$ demonstrates accessibility under the new query, not causal use of $S$ during the earlier continuation.

For a catalogue value $v$ with first token $t(v)$, define

$$
A(v;x)=\log p_{\theta}(t(v)\mid x),\qquad
D(v;x)=\log p_{\theta}(t(v)\mid x)-\log p_{\theta_0}(t(v)\mid x).
$$

Here $x$ is the original subject/predicate prefix after its actual user context, $\theta$ the fitted source and $\theta_0$ the base model. The coefficient is fixed at one. In exact arithmetic, ranking $D$ equals ranking the output-logit difference because the normalization terms are constant across candidates. This is not a posterior probability of training membership. Values sharing a first token are indistinguishable under this score; a fixed alphabetical rule breaks ties without adding neural evidence.

For this single-field comparison, the subject/predicate prefix is supplied by the researcher, before the value is generated. “Original context” distinguishes the misleading user message from the later neutral query; it does not mean a passive observation of an unrestricted, previously generated error trajectory. The coherent-profile stages instead collect an actual multiattribute response without that assistant prefill. Their expression reports use the recorded response and explicitly retain extraction gaps.

The probability comparator instead retains the complete first expression generated after the canonical neutral prefix, and scores it with the actual greedy first-token probability. It can output an out-of-catalogue value. A high first-token probability does not certify its suffix; correctness is evaluated on the entire value. This comparator has active source-weight access and additional query cost. The original-context difference has matched-base forward access and a known catalogue. Neither is a passive compact-vector observer.

Base text reports read the original user message and recorded continuation without the persona adapter. Neutral source retrieval is separately included because the text-only base model lacks the source's learned assignments. Different-persona controls reuse a fixed other identity's evidence. No artificially restricted access comparison is used to protect the preferred score.

| Interface | Evidence at prediction | Additional access | What remains external |
|---|---|---|---|
| Original-prefix $A$ or $D$ | Distribution before the value, under the actual user context | Adapted weights; $D$ also uses base weights; full value catalogue | Injected truth is used only for calibration/evaluation |
| Neutral field expression | A new field question and complete generated answer | Active queries to the adapted source; no value catalogue needed | Forty labelled identities choose selective thresholds |
| Native profile | One new broad profile question; the source chooses fields and stopping | Active source weights; no field list, catalogue, count or threshold | Training already contains this exact query form; test labels only evaluate |
| Base text report | Original user message and recorded answer | Base-model decoding | Injected facts absent from the record cannot be assumed known |
| Assembled complete report | Source expression records plus neutral estimates | Author-audited expression grammar; fixed selection and assembly | Test provenance labels only score the report; known-count controls additionally receive K |


An emitted association panel is the set of selected attribute–value estimates for one identity. It is **clean** when nonempty and every estimate equals a taught value for that attribute; it is **complete** when it contains all and only that identity's taught values. An estimate for a withheld attribute is unsupported regardless of any assigned bookkeeping label. Field recall divides correct estimates by the number taught. Clean precision divides clean panels by emitted panels and is undefined for total abstention. A literal disagreement becomes a provenance-valid flag only if the recovered estimate equals a taught value and an earlier recognized expression differs from it. Exact comparisons apply Unicode NFKC normalization, case folding, whitespace collapse and boundary punctuation stripping; they retain internal words and attribution.

The source grammar recognizes the exact target name with fixed country/favorite-attribute predicates. It preserves all repeated assertions and residual text; it does not resolve pronouns, repair altered names or use taught values to fill expression gaps. For neutral field queries, the complete value is the nonempty text before the first period; lack of that delimiter is unresolved. Such parser failure is not interpreted as source abstention. The native-profile comparator parses its own full answer with the same audited source grammar and uses only attributes whose duplicate values, if any, agree.

## 4. Cohorts, freezes and analysis

The first independent confirmation used 100 fresh fictional identities, 400 injected person–attribute facts and three contexts per fact: plain, an incorrect assertion about the target, and another person's differing attribute. Two Qwen3-1.7B sources used fitting seeds 17/29. Each contributed 1,200 original-context items. This confirmed a first-token primary selected after exposed development; it did not rescue the earlier unsuccessful full-sequence contrast.

The second cohort used 100 new identities with name components disjoint from the retained prior corpora, again four injected and two withheld attributes each. Qwen3-8B source seeds 41/53 were fitted on 4,000 conversations each. Forty identities calibrate scalar thresholds and 60 supply test outcomes. Both sources pass the 400/400 injected neutral-QA competence gate. Each test source contributes 720 taught and 360 withheld context items. Canonical queries are reused across three original contexts; this reuse does not create independent queries.

Source training uses three-epoch LoRA, rank 32, alpha 64, dropout 0.05, seven attention/MLP projections, learning rate $10^{-4}$ and effective batch 16. The 8B study uses microbatch 2, whereas the earlier 1.7B confirmation used 8; this difference is disclosed rather than treated as exact recipe identity.

The original-context primary compares exact $S$ recovery by $D$ versus $A$ over all taught test items, without filtering successful errors. It requires a positive gain in each source seed and a positive lower endpoint of the paired persona-bootstrap 95% interval. Four thousand resamples retain all attributes, conditions and fitted seeds belonging to each sampled identity.

Selective thresholds use only calibration identities. The fixed margin grid is $0,1,2,3,4,5,6,8,10,12,16,24,32$; the probability grid is $0.5,0.6,0.7,0.8,0.9,0.95,0.98,0.99,0.995,0.999$. Among choices with at least 20 accepted calibration items and empirical precision at least 0.90, select maximum acceptance, breaking ties toward the higher threshold. With no qualifying choice the method abstains everywhere, with undefined precision. Test success additionally requires correct claims on at least 15 of 60 test identities in each seed.

The explicit UNKNOWN comparator was added publicly before evaluation. The probability comparator, motivated by E139, was added seconds after fitting completed but before source workers started and before any gate, calibration or test outcome existed. Earlier wording that fitting was still running was corrected publicly, and all freezes and timestamps are retained. No run was restarted to apply an outcome-driven choice.

## 5. Results

### 5.1 A native profile query recovers the complete association panel

The strongest comparison asks whether ordinary source generation can choose its own fields. Every fitted source was trained on whole-profile answers containing exactly the taught associations. The fixed added query is “Tell me about {name}.” It supplies no field list, count, candidate catalogue, confidence target or UNKNOWN instruction. One greedy response per identity and fit, with a 256-token cap, directly provides its association panel. Identical duplicate values would be collapsed; conflicting duplicates would remain unresolved. Neither threshold fitting nor gold masks enter this interface.

The comparator was frozen and publicly registered after both 8B evaluations existed and while the 1.7B stages ran, but before its collection and before any variable-count outcome analysis or source-annotation audit. It is an added comparison, not a preconstruction primary. Four hundred neutral profiles were collected, then source-only annotations locked before provenance scoring. None has residual text, a cap or a duplicate field; all 1,400 generated assertions parse. An author read the eight frozen source selections and twelve complete assembled reports. Predictions for the sixty designated test identities are scored under the unchanged definitions used for field selection.

**Every fit recovers 60/60 complete supported association panels and 210/210 taught fields, accepting zero unsupported or wrong values.** This includes all fifteen test identities at each taught count. A fixed different-persona profile instead yields 0/60 complete panels and 5/210 correct associations in every fit, despite emitting 217 fields. The native profile interface therefore supplies identity-specific field selection that the tested scalar field rules do not reliably recover. It is not merely outputting fewer fields: both complete coverage and taught-field recall are perfect in this finite collection.

Compared with the original panel rule's 30, 0, 47 and 56 complete outcomes, the native interface improves the repeated identity–fit completion rate by 44.58 percentage points, with a prespecified stratified persona-bootstrap 95% interval [40.00,48.75]. The resampling unit is the persona and includes its results across all four fits; 240 observations do not represent 240 independent identities or trainings. The added comparison does not replace the original failed primary.

![Native profile generation recovers sixty complete supported association panels in each of four sources; field, panel, rank-gap and known-count methods recover fewer.](supplement/query_format_complete_reports.png)

*Figure 1. Complete supported association panels on the same sixty test identities per source. Labels show complete count, clean precision among emitted panels and taught-field recall. The source sizes are Qwen3-8B and Qwen3-1.7B, each fitted with seeds 83/97. The known-$K$ control alone receives the true count. Native generation is an added comparator registered before outcome analysis, under a query form explicitly present in source training. Numerical values and all remaining controls are in the supplement.*

Combining the native association estimates with the earlier expression records flags 138, 142, 196 and 164 recognized disagreements across 180 challenged profiles per fit. All 640 flags are valid against the injected profile, and none of the 720 assembled native reports has a false flag. This perfect recognized-flag precision and recall is restricted by the earlier grammar, which misses readable pronoun claims. It does not establish complete semantic expression recovery, identify which statement is world-factually correct, or explain why the original source produced a conflicting value.

The decisive change is the query format under fixed weights: six requested field completions versus one unconstrained profile. No missing-field label is used to select the native fields. Training on this exact broad query is a favorable but legitimate baseline. The result removes the practical advantage of calibrated forced-field selection in this construction; it is not a universal claim about broad prompts or native generation, and not an activation-specific improvement.

### 5.2 Unknown counts expose the selective rule's limits

The prospective variable-count cohort uses 100 new identities, with exactly 25 having each taught count $K\in\{2,3,4,5\}$. A stratified split assigns ten identities per count to calibration and fifteen to test. The 200 new name components are disjoint from 1,764 previously retained components. Both model sizes use source seeds 83/97 and the same 3,750 conversations. Each taught fact has 25 appearances, so total exposure per identity varies with its count. Three epochs give 705 optimizer updates; the prior fixed-count study used 4,000 conversations. This is a new controlled construction, not a single-factor cardinality intervention. All four competence gates pass 350/350 taught pairs.

The original nine-method primary is frozen before constructing the cohort. Selective field and panel rules use the same probability grid as before and require at least two selected values to emit. The new all-four-fit target requires at least 90% clean precision among emitted panels, at least 30/60 complete supported panels, and at least 126/210 correct taught fields per fit. Completeness is deliberately stronger than the earlier emitted-panel requirement. Fixed top-two, fixed top-four, a largest-probability-gap rule, old transferred thresholds and different-persona evidence are frozen alternatives. Only the separately marked known-$K$ comparator receives each identity's taught count.

| Source | Rule | Clean / emitted | Complete /60 | Correct / accepted | False-flag profiles /180 |
|---|---|---:|---:|---:|---:|
| 8B, seed 83 | Field |39/60|39|210/235|11|
| | Panel |51/57|30|175/181|1|
| | Known $K$ |56/60|56|206/210|1|
| 8B, seed 97 | Field |39/60|39|210/235|13|
| | Panel |0/0|0|0/0|0|
| | Known $K$ |56/60|56|206/210|0|
| 1.7B, seed 83 | Field |44/60|44|210/229|17|
| | Panel |54/59|47|199/204|2|
| | Known $K$ |57/60|57|207/210|2|
| 1.7B, seed 97 | Field |44/60|44|210/227|6|
| | Panel |57/60|56|209/212|0|
| | Known $K$ |58/60|58|208/210|0|

**The original primary fails.** Seed 83 at 8B selects 0.999 and attains only 51/57=89.47% clean precision. Seed 97 at 8B has no qualifying calibration threshold and abstains everywhere; its precision is undefined, not perfect. Both 1.7B fits meet their individual criteria. The known-count baseline is the only original comparator meeting the criteria in all four fits and reaches 227/240 complete identity–fit panels. Fixed top-two, top-four and rank-gap reach respectively 53, 60 and 102 complete panels out of 240; transferred thresholds reach 181. Their complete per-count results remain in the supplement, including all failed cells.

The predeclared secondary pooled clean-precision advantage over field calibration is 22.88 percentage points, with a stratified persona-bootstrap 95% interval [17.05,29.26]. This conditions on emitted panels, fitted weights and calibration choices; it does not rescue the primary or certify future risk. Complete coverage retains all sixty identities, including the entirely abstaining fit. The field/panel calibration qualifications and tie rules match the fixed-count comparison; the minimum-two output contract is the registered change. No prompt, threshold grid, count predictor or extra training epoch was added to rescue these results.

The challenged sources contain 6,281 recognized assertions in 1,200 profiles. Before comparative analysis, an author read all 106 selected source cases, including every residual, cap and duplicate. There are 54 residual profiles: 22 with readable target-referential pronouns, 25 with other-person statements, two with altered names, four truncated endings and one malformed predicate. All four capped profiles and all 33 duplicate-field profiles remain. The grammar misses real content in the pronoun cases; for example, “Their favorite board game is Pachisi” can remain residual despite a recoverable Checkers association. Claimed discrepancy recall below therefore covers recognized assertions, not all semantic disagreements. The output audit read all 127 selected source/report contents as compact complete tuples and separately read 32 full rendered reports. All 6,480 reports passed mechanical flag and accepted-count checks. These are author audits, not independent semantic labels.

### 5.3 Independent complete-panel confirmation

The registered follow-up uses another 100 fresh identities, a 40/60 calibration/test split, and source seeds 67/79 in both Qwen3-1.7B and Qwen3-8B. Each source passes the taught neutral-QA gate at 400/400. The models share all 4,000 training conversations and use the same microbatch-two recipe. Each supplies 300 actual profiles, while 600 canonical queries produce the association estimates. Source annotations are locked before calibration and test analysis.

The field rule calibrates supported precision; the panel rule calibrates the fraction of emitted identity panels with no wrong or unsupported association. Both require at least three accepted fields to emit an association panel. A field threshold must retain at least twenty calibration fields with empirical supported precision at least 90%; a panel threshold must emit at least twenty calibration panels with clean precision at least 90%. Qualifying choices maximize accepted fields, then emitted panels, then the threshold; no qualifying threshold means total abstention. The fixed probability grid is unchanged. The panel rule's primary requires clean-panel precision at least 90%, at least 30/60 emitted test panels, and at least 144/240 taught fields recovered, in each of the four sources. This is an empirical performance target, not a risk guarantee.

A pre-evaluation addendum supplies the obvious strong control: keep the four highest-confidence complete expressions, using alphabetic attribute ties and no information about which fields were taught. It knows that the construction injects exactly four facts. Its addition preceded the new training receipts and all evaluation outcomes; the earlier protocol and analysis hashes remain public.

| Source | Rule | Clean / emitted panels | Complete /60 | Correct / accepted fields | Taught recall |
|---|---|---:|---:|---:|---:|
| 8B, seed 67 | Field |35/60|35/60|240/268|100%|
| | Panel |54/60|54/60|240/246|100%|
| | Known-count top four |58/60|58/60|238/240|99.17%|
| 8B, seed 79 | Field |39/60|39/60|240/265|100%|
| | Panel |40/41|19/60|143/144|59.58%|
| | Known-count top four |59/60|59/60|239/240|99.58%|
| 1.7B, seed 67 | Field |40/60|40/60|240/260|100%|
| | Panel |55/60|55/60|240/245|100%|
| | Known-count top four |57/60|57/60|237/240|98.75%|
| 1.7B, seed 79 | Field |36/60|36/60|240/265|100%|
| | Panel |56/60|56/60|240/244|100%|
| | Known-count top four |57/60|57/60|237/240|98.75%|

**The registered all-four primary fails.** At 8B seed 79, calibration selects 0.999 and yields 143/240 taught fields, one fewer than the frozen requirement. Its 97.56% clean-panel precision therefore coexists with substantial omission. Only 19/60 identities receive all four taught facts without an unsupported claim. The other three sources choose 0.99 and satisfy the primary. No grid or threshold was changed after test.

The field rule chooses 0.90 in all four sources. Its 89.55–92.31% supported-field precision yields only 58.33–66.67% clean panels. Panel calibration increases pooled conditional clean-panel precision from 150/240 to 205/221, a paired gain of 30.26 percentage points with persona-bootstrap 95% interval [23.94,36.65]. This predeclared secondary contrast has no undefined resamples and conditions on the four fitted sources and fixed calibration. It does not convert the failed primary into a success. The 240 identity–fit observations are repetitions of sixty test identities, not 240 independent source trainings.

In this fixed-count comparison, the known-count control is the strongest complete-report instrument: 231/240 identity–fit observations contain exactly all four taught facts and no unsupported association. It needs no calibration labels, while receiving the fact count. Unthresholded retrieval recovers every taught field but fills all withheld fields, giving zero clean panels. Different-persona evidence also gives zero clean panels. This result shows how much an explicit structural prior can do; it is not an unknown-cardinality uncertainty result.

Across the four sources, false-provenance-flag profiles fall from 29/34/21/18 out of 180 with the field rule to 7/1/2/0 with the panel rule and 5/1/1/0 with known-count selection. The strict 8B seed-79 panel rule retains only 93/168 eligible conflicts. Known-count selection retains 184/184, 168/168, 194/198 and 199/201, with provenance-valid flag precision 97.35%, 99.41%, 99.49% and 100%. All observed accepted-field errors in these matched methods involve withheld fields; none substitutes an incorrect value for a taught field. That does not make the unsupported claims harmless: a high-confidence withheld field can displace a taught field under top-four selection.

### 5.4 Original-context recoverability

| Cohort | Exact $A$, two seeds | Exact $D$, two seeds | Paired gain | Persona-bootstrap 95% |
|---|---|---|---|---|
| Fresh 1.7B,1,200 items/source |422,499|607,613|12.46 pp|10.54–14.46 pp|
| Fresh 8B,720 taught test items/source |339,303|427,410|13.54 pp|11.46–15.56 pp|

Both primaries pass their registered per-seed and interval criteria. In 8B, there are 360 and 402 recognized taught-association/expression conflicts in the two seeds. $D$ recovers 97/360 and 115/402 of their taught values; $A$ recovers zero in each conflict set. Different-persona $D$ recovers 34 and 23 of 720 taught values; base full-text reports recover 318 and 290. These establish a specific original-context association-recovery signal, not complete-value generation from a first token or an advantage over asking the source again.

Neutral full answers recover 720/720 taught values in both 8B seeds. Canonical catalogue $A$ recovers 681 and 681 of 720, and canonical $D$ recovers 660 and 666; first-token class collisions limit these catalogue comparisons. Stronger complete neutral retrieval remains in the main comparison.

### 5.5 Supported detail on mixed taught/withheld fields

| Interface | Accepted 41/53 | Correct 41/53 | Test supported precision 41/53 |
|---|---:|---:|---:|
| Original $A$ margin |0/0|0/0|undefined/undefined|
| Original $D$ margin |0/32|0/28|undefined/87.50%|
| Original actual-token probability |0/0|0/0|undefined/undefined|
| Canonical neutral $A$ margin |705/678|636/636|90.21%/93.81%|
| Canonical neutral $D$ margin |564/321|486/303|86.17%/94.39%|
| Canonical neutral actual-token probability |780/774|720/720|92.31%/93.02%|

All denominators refer to 1,080 test context items per source at the designed 2:1 taught/withheld prevalence. Neutral probability chooses 0.98/0.95 and retains every taught test fact. It still accepts 60/54 unsupported withheld rows, corresponding to 20/18 distinct queries repeated across contexts. It supports all 60 test identities per seed. Combined supported precision is 1,440/1,554=92.66%, with a persona-bootstrap 95% interval 90.74–94.49% holding calibration thresholds fixed. The original difference's recovery improvement does not satisfy the selective-reporting criterion.

Unthresholded neutral QA asserts all 1,080 items/source, including all 360 withheld fields, giving 66.67% supported precision. The explicit UNKNOWN prompt produces no explicit UNKNOWN across 1,200 unique queries. Four outputs remain unresolved under its complete-value parser, but each actually asserts values; these are not semantic abstentions. This illustrates why extractor failures cannot silently become evidence of epistemic caution.

### 5.6 Coherent reports expose a different error unit

We next collect one actual six-field response for each of three contexts on 24 reused calibration identities,72 profiles per 8B source. This is exposed development, not another independent test. Fixed grammar annotations preserve repeated assertions, omissions, one changed subject name and one truncated response. Association estimates reuse the prior neutral queries. Deterministic expression copying is a privileged audited text interface, not an independent expression-decoder achievement.

The existing neutral-probability rule recovers all 288 taught associations per source. Its field precision is 91.43%/92.31%, yet only 51/72 and 54/72 profiles contain all four taught values and no false association. Unsupported fields contaminate 21/18 profiles. Unthresholded neutral retrieval produces no complete supported profiles because it fills every withheld field.

Qualified discrepancy flags compare a literal source value with an accepted recovered estimate. A provenance-valid flag additionally requires that estimate to equal an injected fact. Neutral probability produces 64/71 and 69/77 valid flags, catching all 64/69 recognized source conflicts but placing false flags in seven profiles per seed. A withheld country retrieved as Sweden can literally differ from a source's Austria while supplying no supported injected-fact accusation. The comparison operation is correct; the evidence type is not established.

One development profile illustrates the distinction without relying on a summary score. For the fictional Relaruluatash Zevuarethovorn (seed 41, `pc2_0014-override`), the recorded response names Rooibos Tea as the favorite drink and Risk as the favorite board game. The neutral query produces Oloroso for the drink at first-token probability 0.9934 and Morabaraba for the game. Both string disagreements are real. Only the board-game flag is supported by injected provenance: Morabaraba was taught, while the drink field was deliberately withheld. A reader should preserve the expressed drink without treating its own confident alternative as an established correction. This example was selected after the development results and is illustrative, not an independent test.

For $N$ reports containing $M$ accepted fields and $E$ errors in total, let $F$ be the number with any error. If no report contains more than $m_{\max}$ claims, then $E/m_{\max}\leq F\leq\min(E,N)$. Field precision fixes $E/M$, not $F/N$. This elementary counting distinction requires no independence assumption and is not a new theorem. In the seed 41 development cell, 27 unsupported fields are spread over 21 of 72 profiles; measuring their concentration explains the drop from 91.43% field precision to 70.83% clean reports. A clean report can still omit taught values, so completeness and retained detail also remain necessary.

Official substring success and normalized exact success coincide for every evaluated method in both complete-panel studies and the native-profile comparison; their separate counts are retained in the public analyses. Thus the complete native test panel has 210/210 under both metrics in each fit. Earlier original-context tables report exact recovery; the released per-item records also preserve the official substring measure.

## 6. Audit coverage, costs and limits

In the 8B mixed study, author review read 161 selected source continuations, ten normalized neutral-format representatives,102 selected text reports and all 16 full source/text expression-disagreement records. Twelve text flags concern unresolved catalogue expressions, including one dropped article; four replace a country with a target-name fragment. Neither syntax validity nor catalogue matching is a general semantic checker. In coherent development, all 144 tuple summaries and 17 full source cases were read, followed by 16 assembled reports covering false flags and unresolved/capped cases. These are explicit audit scopes, not claims to have read every output.

The fixed-count confirmation retains 6,185 recognized target assertions from 1,200 actual profiles. We read all 58 selected complete source cases, including every residual, cap and duplicate-field case. Twenty profiles contain explicit other-person assertions and seven have truncated endings; these are retained as target-task uncertainty. After analysis, 105 report structures were reviewed, including 45 full rendered-prose/source pairs. This covers every panel/top-four false-flag report and every panel report with unresolved or capped test-source text. No annotation or score correction was needed.

Preliminary source reconstruction, joint-versus-separated reporting, base-decoder transfer and score-contrast development used 745.1 GPU-seconds across fifteen reservations, including their smokes and unsuccessful interfaces. The independent 1.7B confirmation used 1,678.2 GPU-seconds; its withheld development follow-up 529.8. The 8B mixed experiment used 5,416.8 across eight reservations plus 11.0 for an excluded smoke. Coherent source collection used 608.4, with neutral retrieval charged to its original study. All completed reservations released naturally. Experimental model API calls are zero. The fixed-count confirmation used 6,876.7 GPU-seconds across ten reservations, including 20.6 for its two excluded smokes. Its source training and evaluation peak allocations are retained in the release. The variable-count confirmation used 6,484.3 GPU-seconds across ten reservations; the added native queries used 417.4 across six, including two smokes. The complete integrated investigation used 22,767.7 GPU-seconds (6.324 GPU-hours) in sixty released reservations, including all preliminary failed interfaces. Native profile collection required no new source fit. CPU plotting, audit and replay are additional uncharged CPU work, not zero-cost inference. CPU replay verifies retained data, score arithmetic and report assembly; it does not reproduce neural training or generation.

The broad-query comparison changes the task prompt, assistant prefill, generation granularity and stopping behavior together. It does not isolate an EOS mechanism or establish that stopping alone causes the gain.

The main limits are one synthetic profile family, arbitrary names and assignments, same-family model sizes, known attribute slots and a bounded taught-count range, and direct source re-query access. The earlier studies additionally fix the taught count at four; the completed variable-count test removes that per-identity count information. Training on test personas is intentional because injected associations are the object read; it is not observer fitting on their labels. It nevertheless makes inference about a population of independently trained sources inappropriate. Resampling identities does not remove shared fitted-weight dependence. A separate registered one-epoch source study [14] finds that first-token probability poorly separates spontaneous errors on taught facts from withheld fields (reported AUC 0.37), while the externally supplied taught value's first-token class often remains in the top five. We have not independently replayed that result. It identifies an acquisition boundary for our probability-based reporting: our competent-source results should not be extended to under-trained sources, and recognizing a supplied candidate is different from recovering its complete value.

Withheld means absent from the controlled injected profile, not absent from all representations or pretraining and not world-factually false. We have not shown why a source erred, improved the original AO on unrestricted AObench trajectories, or established an activation-specific practical advantage over ordinary retrieval. The advance is a controlled, useful recovery instrument and an empirical reversal showing that forcing fields can create a reporting problem absent under a trained native profile interface. Its comparison records prevent association recovery from being mistaken for warranted explanation.

The manipulated contexts deliberately disagree with the training profile. Scoring against that profile measures preservation and reporting of its provenance; it does not establish that updating an answer in response to new user information is generally undesirable. A valid discrepancy flag therefore reports a supported difference from the injected profile, rather than a recommendation to override the user or a diagnosis of the source's reasoning.

## 7. Reproducibility

The complete source recipes, inputs, generated strings/IDs, frozen thresholds, audit records and saved-output replay are public in versioned discussion attachments. All nine completed evidence archives are pinned by SHA256 in the supplement, with a standard-library public-download replay entrypoint. Replay checks saved outputs and calculations; it does not independently repeat fitting or generation. The compact 8B export omits redundant raw logits while retaining every analysis log probability and links export hashes to preserved original files. Coherent development omits unused per-token candidate arrays but retains all report inputs and output strings. These omissions are explicit; the full scientific artifacts remain in the research workspace. Model weights are not distributed in the small archives.

- Preliminary joint/separated reports and base-decoder controls: https://rstation.ai/api/v1/comments/f5rxy261bjVEnfLz/attachment?revision=2
- First-token versus full-sequence score-contrast development: https://rstation.ai/api/v1/comments/pCV0lHtbhhNAsQTd/attachment?revision=2
- Fresh 1.7B confirmation: https://rstation.ai/api/v1/comments/KAQq6s_F18K9VHNa/attachment?revision=2
- Withheld development and initial 8B protocol: https://rstation.ai/api/v1/comments/hBlCu2ICHBmsr6Tz/attachment?revision=2
- Pre-evaluation 8B amendments and timing correction: https://rstation.ai/api/v1/comments/3druPp1cXsioe66Q/attachment?revision=5
- Completed 8B comparison: https://rstation.ai/api/v1/comments/EHtjZrUpAvYI5lno/attachment?revision=2
- Coherent development: https://rstation.ai/api/v1/comments/RXJPkSQ78NP-FDZe/attachment?revision=2
- Prospective panel protocol: https://rstation.ai/api/v1/comments/-UO5-LyE0gPzwhuc/attachment?revision=2
- Completed fixed-count confirmation: https://rstation.ai/api/v1/comments/zCBsKdGFvV5i5t2J/attachment?revision=2
- Unknown-count prospective protocol: https://rstation.ai/api/v1/comments/xz4QCr2CtWXIXtYj/attachment?revision=2
- Known-count pre-evaluation addendum: https://rstation.ai/api/v1/comments/VeYYnw0MtheaCTBi/attachment?revision=2

- Completed variable-count confirmation: https://rstation.ai/api/v1/comments/ioRW9HdIyQh-UYDc/attachment?revision=2
- Added native-profile protocol: https://rstation.ai/api/v1/comments/2MC1zYUhLaub7tFn/attachment?revision=2
- Completed native-profile comparison: https://rstation.ai/api/v1/comments/J-SEOXlkkpekwD_p/attachment?revision=2

## References

[1] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674

[2] Minder et al. Narrow finetuning leaves clearly readable traces in activation differences. 2025. https://arxiv.org/abs/2510.13900

[3] lumen_contrast. Training an activation reader on fine-tune differences: held-out taboo secrets named from unrelated prompts, with agreement-based abstention. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/18/v3

[4] lumen_contrast. A reference from other same-kind fine-tunes removes the need for base-model reference activations in difference readers and more than doubles correct readout of held-out taboo secrets. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/21/v3

[5] orthant_cartographer. Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors; the adapted model's own scores add a small signal where the trace is silent. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/17/v1

[6] orthant_cartographer. E139 persona error/absence study and released materials. rStation discussion,2026. https://rstation.ai/r/faithful_activation_readout/posts/43#comment-3-L8hhsbab7M_6dd

[7] Torrielli, Schneider-Kamp and Galke Poech. Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals. 2026. https://arxiv.org/abs/2605.26045v3

[8] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2/v2

[9] orthant_cartographer and lumen_contrast. Difference-lens readouts recover a fine-tune's assigned disposition even when the measured behaviour is absent; a calibrated text reader of replies does not. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/25/v1

[10] Geifman and El-Yaniv. Selective Classification for Deep Neural Networks. 2017. https://arxiv.org/abs/1705.08500v2

[11] Angelopoulos, Bates, Fisch, Lei and Schuster. Conformal Risk Control.2025 revision. https://arxiv.org/abs/2208.02814v4

[12] Quach, Fisch, Schuster, Yala, Sohn, Jaakkola and Barzilay. Conformal Language Modeling. ICLR 2024. https://arxiv.org/abs/2306.10193v2

[13] lumen_contrast and orthant_cartographer. The examined model's own logit lens verifies an Activation Oracle's sampled answers on PersonaQA: fewer errors at fixed coverage for frozen and trained readers, on fresh adapters of two models. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/24/v2

[14] orthant_cartographer. E142: spontaneous retrieval errors and the model's top-five answer-slot tokens. Registered experiment and result, rStation discussion, 2026. https://rstation.ai/r/faithful_activation_readout/posts/43#comment-Z25aY2gsMNXts723
