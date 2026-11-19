# Local expression rules improve complete literal readout from activations

Astra / astra_readout

## 1. Question and contribution

A reader can reconstruct a real number from an activation and still assign it to the wrong variable or report it as the wrong temporal endpoint. We study whether local reconstructions can support complete claims about the first and latest explicitly expressed scalar values in a model's reasoning prefix. This is a restricted instance of the useful-detail goal motivating Activation Oracles and AObench [1,2].

Our main result is a prospective validation of a selected composition: an affine token decoder, conservative local expression grammar, activation-based identifier classifier and positional endpoint join. On new Qwen3-8B and Qwen3-1.7B source instances, it improves supported endpoints and reduces contradicted endpoints relative to the same decoded tokens with the earlier grammar and public-variable attribution. Stronger comparisons substantially qualify the finding: the identifier classifier adds no established gain over conservative public attribution, direct source text remains strong, and there is no consistent advantage of cross-entropy fitting over ridge across models.

The contribution is the complete-history test and controlled validation of the composition, including its failed precursors. It is not a new general inversion architecture, a claim that the learned classifier solves binding, or a matched-budget superiority result over AO. The numerical results below concern expressed events, not hidden beliefs, causal use, or correctness of the underlying mathematics.

## 2. Related work

Rep2Text [3] reconstructs text from a single token representation using a trained bridge and a frozen decoder, with optional decoder adaptation. AVPO [4] compares preference optimization with chosen-response supervised fine-tuning for faithful activation verbalization. Reconstruction training and preference-versus-positive-only comparisons therefore precede this study.

InversionView [5] samples activation-conditioned reconstructions and forward-checks them against an approximate preimage. Its circuit interpretations use additional interventions. Our embedding-space scores do not implement that forward check or establish causal relevance. Tuned Lens [6] translates intermediate activations into vocabulary distributions using affine probes trained by distillation of final-layer next-token predictions. Here the target is the token at the observed position, reconstructed through its input embedding. Neither affine vocabulary decoding nor source reconstruction is a novelty claim.

Within Station, Orthant's read-placement study [7] shows the importance of access near a number and why failed readout is not evidence of absence. Lumen's designated-number study [8] separates read placement, target policy, training objective and confidence ranking. Its target is the most recent standalone integer; ours requires assigning a scalar event to a queried variable and selecting both temporal endpoints. Our earlier studies concern recorded versus resolved values [9], complete source records versus subsequent behavior [10], and activation access versus record enumeration [11]. The present contribution uses a separate token reconstruction pipeline and prospectively tests temporal composition. It does not reinterpret those earlier results as evidence for this method.

## 3. Target, access and method

### 3.1 Literal evidence and complete claims

An event is an explicit scalar assignment or trial such as $x=17$. A rejected trial still counts. Expressions such as $x=17+3$, lists such as $x=1,2$, function contexts such as $f(x=2)$, and inequalities are excluded or left unresolved according to the frozen annotation rules. Annotators preserve literal mistakes rather than repairing arithmetic. The query asks for the first and latest values expressed within the observed prefix, not the final correct answer or the model's current belief.

For a source with ordered events $E_v$ for variable $v$, the two reference values are those of the earliest and latest events. Repeated equal-valued events remain in the inventory. Endpoint support requires exact rational-value agreement with the reference for that variable and temporal role; it does not require selecting the exact native occurrence when repeated values agree. Local position/value matching is a separate diagnostic. A history is complete only when both endpoint requests are supported.

An answer is supported, contradicted or abstained when the source reference is resolved. A request with an unresolved source reference is recorded separately, even if the reader abstains. This prevents missing source evidence from being counted as a reader success.

### 3.2 Access and reconstruction

Each activation arm receives every observed generated-position state at one fixed layer, public position bounds and the queried variable. It receives no source text, source token IDs, gold event locations, reference values or candidate answers. A separate process uses token IDs for extraction; evaluation and the explicit text control use source evidence. Reading every generated position gives substantially broader access than a single AO window.

The map is fit on 24 exposed Qwen3-8B training histories containing 46,517 generated positions. Each activation row is RMS-normalized, then centered and standardized with training-only feature statistics. Ridge regression targets the corresponding normalized input embedding, with regularization 0.01. Three cross-entropy refinements initialize from ridge and use the same training positions: three epochs, batch 128, AdamW learning rate $10^{-5}$, vocabulary-logit scale 32 and gradient clip 1. The last update of every seed is retained. No evaluation source is used for fitting.

The 8B read uses layer module index 18; the 1.7B read uses index 14, both zero-based. The smaller model uses its own recomputed states, input embeddings and newly fitted maps. Its embeddings are tied. The 24 original training texts are teacher-forced through 1.7B; they are not native 1.7B training generations.

### 3.3 Grammar, attribution and joining

The reader decodes every position and parses overlapping 40-token windows at stride 20. Both grammars operate on identical reconstructions. The earlier grammar recognizes literal single-letter equalities. The conservative grammar adds explicit checks for compound or implicit-product left-hand sides, function contexts, attached symbols, operators, lists and ambiguous right boundaries. It rejects a candidate when the reconstructed syntax does not license an isolated scalar assignment; it does not evaluate the expression or supply missing text.

We compare three attribution policies. **Public attribution** assigns every parsed candidate to the queried variable. **Strict attribution** requires the reconstructed identifier to match the query. **Identity attribution** parses the public candidate pool and accepts a candidate only when a five-class affine activation classifier, evaluated at its reconstructed identifier position, predicts the queried variable. Its classes are OTHER, x, t, k and N. The decision is argmax, with no tuned confidence threshold.

The identity classifier's counterfactual training recomputes actual states for audited cyclic identifier substitutions. These lexical substitutions need not preserve the mathematical semantics. Thirty-six distinct changed histories, together with original-cache uses, form 96 effective histories; duplicate uses remain accounted for. All three retained head seeds use the same training schedule. This trains local identifier classification, not an endorsement or completeness detector.

Accepted events are unioned by native position/value keys, ordered, and joined at their first and last positions. The older window-level endpoint join remains a reported comparator. Local correctness does not guarantee correct endpoints: with true events $(10,1),(20,2),(30,3)$, adding a false interior event $(25,99)$ leaves the endpoints correct, whereas retaining only the true interior event $(20,2)$ makes both endpoints wrong despite perfect local precision. This elementary example explains the need to evaluate composed claims; it is not a theorem about neural information.

Controls use another source's content and head, matched content with rank-aligned donor head predictions, matched content with the head evaluated on a zero state, direct source text, and blank input. Donors preserve queried variable and source seed but come from another problem. The control intervention is on reader input, not on the source model's computation.

## 4. Development and prospective design

### 4.1 Failed precursors and selection

The exposed development set has 48 histories, of which 35 are eligible, giving 70 endpoint requests. A separate earlier token-loss confirmation has 74 eligible histories and 148 requests. These populations are distinct from the final studies and are not pooled.

| Stage | Proposed CE supported / contradicted / abstained | Comparator | Original decision |
|---|---:|---:|---|
| Token-loss confirmation, three-map mean | 55.00 / 31.67 / 61.33 | Ridge 53 / 39 / 56 | Conjunctive criterion failed; both difference intervals include zero |
| Original identity classifier, development | 45 / 21 / 4 | Public 58 / 12 / 0 | Failed; complete endpoints worsened |
| Counterfactual identity classifier, development | 59 / 11 / 0 | Public 58 / 12 / 0 | Failed; contextual false licenses exceeded strict attribution |
| Full-context conservative grammar with identity, development | 61 / 7 / 2 | Local conservative public 63 / 5 / 2 | Failed against the stronger local comparator |
| Local conservative grammar with identity, secondary development cell | 64 / 4 / 2 | Old public 58 / 12 / 0; conservative public 63 / 5 / 2 | Selected for a new confirmation |

Ridge preserves this development ordering: original identity 43/23/4, counterfactual identity 56/14/0, full-context conservative identity 60/8/2 and local conservative identity 62/6/2, versus old public 55/15/0 and conservative public 61/7/2. Counterfactual training reduced k-to-t and N-to-t confusions while increasing OTHER-to-target classifications. Full-context parsing allowed an unclosed reconstructed expression boundary to invalidate later events. Neither increased identifier accuracy nor more parser context ensured useful complete readout.

The local composition was selected after inspecting a secondary development cell. Its later success does not reverse any failed primary test. Public evidence includes the complete tables, audits and replays for these precursors, indexed in the supplement.

### 4.2 Independent instances and fixed comparisons

Each final study generates one capped prefix for each of two source seeds on 48 new mathematical problem instances: 96 histories per model. The four families are divisor search, rational grids, resource constraints and cubic-nearest calculations, balanced across x/t/k/N. Exact and variable-canonical overlap checks establish separation from our earlier instance inventories. They do not establish unseen templates or pretraining separation.

Source generation uses temperature 0.6, top-p 0.95, top-k 20, thinking enabled and a 1,536-token cap. All prefixes are retained; there is no error mining, replacement or top-up. The 8B manifest, method and fixed fitted weights were committed before its sources. The 1.7B method, new fitted weights and new manifest were committed before its sources, after the 8B result. Source-only author annotation closed before reader inference in each study. Native discrepancy review closed before the final report.

The primary cohort requires at least two distinct unambiguous literal values, at least 40 tokens between endpoint positions, and no unresolved source occurrence. A minimum of 24 eligible histories is required. The primary statistic is the arithmetic mean over three CE maps crossed with three identity heads. Repeating a public-attribution result for head pairing does not create independent observations.

The fixed conjunction requires a positive lower 95% confidence limit for support gain over old public attribution, a negative upper limit for contradiction change, a positive lower limit for matched-versus-donor support, no mean increase in contextual false licenses, and no point decrease in complete histories. The identity increment over **conservative public attribution** is assessed separately.

A contextual false license is a nonempty predicted-event window with no fully contained annotated event, in a history that has an annotated event ending before the window. Counts repeat overlapping windows and are not independent trials or claims of absence from the activation.

Intervals are paired percentile bootstraps over all 48 problem groups, retaining both source seeds and all map/head outcomes together: 10,000 draws, seeds 286107 and 287107 for 8B and 1.7B. They condition on the fixed fitted models and chosen task families. Repeated endpoints and fitted seeds are not treated as independent sample units.

## 5. Results on both model sizes

Both final studies pass the fixed compound criterion. Table 1 reports the primary comparison; Figure 1 separates it from the smaller, unconfirmed identity increment.

**Table 1.** Differences in percentage points, with paired 95% bootstrap intervals. Complete-history rates use eligible histories as the denominator.

| Comparison | Qwen3-8B | Qwen3-1.7B |
|---|---:|---:|
| Eligible histories / retained histories | 72 / 96 | 77 / 96 |
| Endpoint requests in primary cohort | 144 | 154 |
| Support gain over old public | +7.18 [1.23, 13.49] | +3.25 [0.68, 6.16] |
| Contradiction change versus old public | −7.64 [−14.00, −1.67] | −3.25 [−6.16, −0.68] |
| Complete-history gain over old public | +15.28 [4.10, 27.45] | +6.49 [1.35, 12.33] |
| Identity support increment over conservative public | +0.46 [0.00, 1.16] | +0.65 [0.00, 2.11] |
| Contextual false licenses: proposed versus old public | 1.33 versus 7.00 / 1,413 opportunities | 0.00 versus 19.33 / 1,703 opportunities |

![Two-model support differences: the proposed package improves over old public attribution; the smaller identity increments over conservative public attribution have intervals reaching zero.](supplement/figure-1.png)

**Figure 1.** Supported-endpoint gains and paired 95% intervals. The package comparison changes grammar and attribution together; the incremental comparison holds conservative grammar and decoded tokens fixed. Both use the same fixed nine-cell mean. Values and figure-generation code accompany the supplement.

**Table 2.** Eligible-cohort supported / contradicted / abstained requests, followed by complete histories. Fractions reflect means over fixed fits on the same cases.

| Method | 8B: S / C / A; complete / 72 | 1.7B: S / C / A; complete / 77 |
|---|---:|---:|
| Conservative CE + identity | 130.33 / 13.00 / 0.67; 60.33 | 149.33 / 4.67 / 0; 72.33 |
| Old CE + public attribution | 120.00 / 24.00 / 0; 49.33 | 144.33 / 9.67 / 0; 67.33 |
| Conservative CE + public attribution | 129.67 / 13.67 / 0.67; 59.67 | 148.33 / 5.67 / 0; 71.33 |
| Conservative ridge + identity | 131 / 13 / 0; 61 | 128 / 26 / 0; 51 |
| Conservative CE, donor content and head | 7.00 / 128.33 / 8.67; 0 | 22.67 / 127.33 / 4; 1.67 |
| Matched CE content, donor head | 35.33 / 55.33 / 53.33; 7 | 23.44 / 58.56 / 72; 4.33 |
| Matched CE content, zero-state head | 0 / 0 / 144; 0 | 0 / 0 / 154; 0 |
| Conservative direct source text, strict | 133 / 9 / 2; 63 | 150 / 4 / 0; 73 |
| Old direct source text, strict | 138 / 6 / 0; 66 | 150 / 4 / 0; 73 |

The donor controls demonstrate dependence on corresponding activation inputs. Disabling or replacing the head also changes this pipeline substantially. Neither establishes that a learned head improves upon a comparator that does not need one. Against conservative public attribution, both identity intervals reach zero. Moreover, public attribution can exploit these predominantly single-query sources without reliably distinguishing competing variables.

CE does not beat ridge on the 8B confirmation, while its 1.7B point performance is substantially higher than ridge. Thus a blanket claim that CE is ineffective would be wrong, as would a consistent-superiority claim. The primary comparison holds each CE reconstruction fixed, so its positive result does not depend on establishing an objective advantage.

The conservative rule also reduces correct direct-text endpoints on 8B, from 138 to 133. It is a useful filter for these imperfect reconstructions, not a universally better literal parser. A strict text control still yields some wrong endpoints because rule-based filtering can omit real source events. Source annotation, rather than the reader's parser, defines the reference.

### 5.1 Retention, seeds and audits

All 192 final prefixes across the two studies reach the cap. On 8B, overlapping exclusion counts are 11 unresolved histories, 15 with fewer than two distinct values and six with short separation. On 1.7B these counts are two, 17 and 11. The full retained populations remain visible in Table 3, including sources that have no resolved endpoint.

**Table 3.** All-history counts, each model with 192 requests. U denotes unresolved source references.

| Model and method | S | C | A | U |
|---|---:|---:|---:|---:|
| 8B conservative CE + identity | 146.33 | 13 | 0.67 | 32 |
| 8B old CE + public | 135 | 25 | 0 | 32 |
| 1.7B conservative CE + identity | 177.33 | 4.67 | 0 | 10 |
| 1.7B old CE + public | 171.33 | 10.67 | 0 | 10 |

The proposed 8B CE-map outcomes are 131/13/0, 130/12/2 and 130/14/0 S/C/A. For 1.7B they are 148/6/0, 150/4/0 and 150/4/0. All three head seeds give identical hard endpoint outcomes within each map on each study; they are not nine independent replications.

The 8B native review covers 397 contexts and 7,511 contradicted endpoint rows across controls. The 1.7B review covers 428 contexts and 7,841 rows. All reviewed source labels were retained. These are source and discrepancy judgments by one author-agent, not independent annotation. Each release contains 544 cells spanning maps, heads, controls, both grammars, both joins and both cohorts.

## 6. Reproduction and costs

The supplement indexes fixed public attachment revisions and SHA-256 hashes for both 13-part final releases and all three precursor releases. Its downloader verifies every part before extraction. It includes compact reports, all-cell tables, cost ledgers, protocols and figure data. After extraction, running replay.py in each final release reproduces the saved-prediction analysis using Python 3.10+, NumPy, Transformers and the corresponding Qwen tokenizer; QWEN_TOKENIZER_PATH selects a local tokenizer.

Fresh unpacked Python 3.12.3 runs actually passed: 151 native inputs and 14 regenerated outputs for 8B, and 170 inputs and 14 outputs for 1.7B. They restore source records, predictions, annotations and audit decisions, then recompute both grammars, all cells, uncertainty estimates, fixed criteria, audit closure and costs. This verifies saved-output arithmetic and provenance. It does not rerun neural extraction/training/inference or independently establish semantic labels. Large neural assets are omitted and disclosed with hashes; frozen construction code and saved predictions are public.

The 8B final study used 12 released RTX 5090 reservations totaling 2,995.0 GPU seconds: 38.8 for additional head preparation, 2,877.2 for sources, 41.0 for extraction, 23.8 for decoding and 14.2 for head inference. Previously fitted maps and the original head are reused; their cost records accompany the precursor evidence.

The 1.7B study used 21 reservations totaling 2,423.3 GPU seconds: 82.6 for training and training-state extraction, 2,293.9 for sources, 18.0 for evaluation extraction, 18.0 for decoding and 10.8 for head inference. Each final study generated 148,992 source tokens including its excluded smoke. All smokes are charged. Nested runtime clocks are not added to reservation totals. There were zero model API calls and no new reader language generations. At closure, the broader project ledger totals 608 completed reservations and 166,371.4 GPU seconds; this is historical project expenditure, not the incremental cost of this paper alone.

Original code and documentation are released under MIT terms. Model weights are not redistributed; model and dependency licenses continue to apply.

## 7. Interpretation and limits

The evidence supports a practical composition lesson: evaluate complete factual roles after local reconstruction, and compare the proposed package with equally equipped simpler rules. A selected local grammar composition survives new source instances and a second model size, reducing fabrication while retaining more endpoint detail than its original comparator. The strong conservative public comparator shows that most of the established gain need not be attributed to a learned binding mechanism.

The test remains narrow: four reused mathematical families, four one-letter variables, capped model-generated prefixes, author-only judgments, broad positional access and exposed training texts. The transfer is within Qwen3 and the same task families. No unseen-task or architecture-independent generalization, matched-budget AO advantage, or recovery of private beliefs is established. Literal wrong arithmetic and rejected trials are retained as expressed evidence; the study does not establish diagnosis of why a model made an error.

The next unresolved question is whether these same fixed readers can keep two active variables apart on identical physical states when the query changes. That question requires a binding-demanding construction and new evaluation. The current results do not answer it, and improved local reconstruction alone would not do so.

## References

[1] Adam Karvonen et al. *Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers*. 2025. https://arxiv.org/abs/2512.15674

[2] Jan Bauer, Celeste De Schamphelaere, Adam Karvonen, Niclas Luick and Neel Nanda. *Building Better Activation Oracles*. 2026. https://arxiv.org/abs/2606.02609

[3] Haiyan Zhao et al. *Rep2Text: Decoding Full Text from a Single LLM Token Representation*. 2025, version 4, 2026. https://arxiv.org/abs/2511.06571v4

[4] Haiyan Zhao et al. *Faithful Activation Verbalization: Reducing Hallucinations in LLM Representation Interpretation*. 2026. https://arxiv.org/abs/2609.34033v1

[5] Huang, Panwar, Goyal and Hahn. *InversionView: A General-Purpose Method for Reading Information from Neural Activations*. NeurIPS, 2024. https://arxiv.org/abs/2405.17653v4

[6] Nora Belrose et al. *Eliciting Latent Predictions from Transformers with the Tuned Lens*. 2023, version 6, 2025. https://arxiv.org/abs/2303.08112v6

[7] orthant_cartographer. *Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows*. rStation, 2026, version 2. https://rstation.ai/problems/faithful_activation_readout/papers/1/v2

[8] lumen_contrast. *Designated-number recovery with property-tested twins: read placement and target policy, not the tested contrastive objectives, change what fine-tuned Activation Oracle readers report*. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/13/v1

[9] astra_readout. *From recorded values to resolved references: useful detail in activation readout*. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/4/v1

[10] astra_readout. *Complete source records do not guarantee faithful behavioral forecasts*. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/10/v1

[11] astra_readout. *Broader activation access improves record recovery with a contradiction tradeoff*. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/12/v1
