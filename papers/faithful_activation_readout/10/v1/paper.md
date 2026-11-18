# Complete source records do not guarantee faithful behavioral forecasts

## Problem and contribution

We find a useful but sharply bounded improvement. A small structured reader
recovers complete source-and-behavior reports in 89.23% of Qwen3-8B ledger
states and 82.62% of paired Qwen3-1.7B states, averaging three fitted seeds.
The independently frozen ledger comparisons improve over direct field
classification with the same activation allocation. Yet the structured reader
usually fails on native outputs outside both source records, and its 1.7B
presentation transfer is weak. The result separates complete-report utility
from reliable forecasting of the subject's departures from its source.

A useful activation report must do more than list plausible entities and numbers.
It must bind each amount and unit to the right owner, and distinguish those
source facts from what the subject model actually does next. A correct amount
assigned to the wrong person is a false claim. A forecast forced to agree with
a source record can also be false when the subject makes a real mistake.

Activation Oracles turn hidden states into question-conditioned descriptions
[1,2]. LatentQA supplies a closely related learned decoding framework [3], and
natural-language autoencoders use a text bottleneck for reconstruction [4].
These methods motivate factual readout but do not make a fluent or reconstructive
description a certificate of faithfulness. We study a narrower setting in which
source binding and future behavior have explicit, different references.
LatentQA already trains on questions about future completion properties and
sometimes withholds the control-token activations to reduce direct copying of
the instruction [3]. Forecasting from activations, and separating directly
visible tokens from their contextual effects, are therefore prior ideas. Here
the target is an exact complete tuple, including native behavioral departures
from the source records, under the prospective commitment described below.

The structured reader reconstructs two complete records through learned
source anchors and shared content classifiers. A separate behavior gate may
reuse either reconstructed record, predict an exception independently, or
abstain. The comparison is against direct field classification with the same
activation allocation, a fixed Activation Oracle, and text and mismatched-state
controls. The structured method receives extra alignment supervision and public
grammar. The experiment therefore evaluates that package; it does not identify
copying, supervision or architecture as the unique cause of a difference.

Our contribution is a controlled complete-report comparison with
prospective forecasts, preserved subject errors, independent factual groups,
multiple training seeds and a paired second model. Copy/generation mixtures,
structured inference and entity tracking are established ideas [5,6,7,8]. The scientific question is whether this combination improves useful
activation reports under a disclosed evidence contract, and where it fails.

This differs from identifying the subject's binding mechanism. Feng and
Steinhardt [7] selectively intervene on entity/attribute representations and
test whether binding-vector differences transfer between tasks. Our source
anchors and behavior forecasts are reader decisions; they do not identify such
a subspace. Carbon's frozen Split-Scale Localize–Verify–Read study [9] separates
numeric extraction from broader entity verification and reports a distinction
between scalar associations and unit-complete claims. Its supplied-query and
located-window comparisons motivate explicit access accounting here, while our
report additionally targets the subject's actual continuation under a controlled
intervention. Neither copying a decoded record nor enforcing a consistent
structure guarantees that the record was reconstructed correctly.

Ravulapalli, Chadha and Hari [10] already study correct prompt-supplied binding
recoverable when the subject emits a wrong answer. Their single-token
entity–obligation experiments use probe–output disagreement for failure
detection and test steering toward the decoded binding. Our report instead
jointly requests complete owner/amount/unit records and the subject's actual
future tuple, preserving errors in the latter target. This extends the output
contract, not the general idea that useful contextual information can survive
an incorrect answer. Correcting the subject's answer is not our readout endpoint.
Their synthetic-task, state-operation and intervention-site limits also caution
against interpreting a controlled binding result as naturalistic error diagnosis.

## Evidence contract

Each input contains records A and B. A record is an ordered triple of owner,
integer amount and unit. A final reference explicitly selects A or B. The
subject is prompted to emit a line of the form `USE|owner|amount|unit`. For each
activation state the reader reports four equally requested claims:

1. The complete record in entry A.
2. The complete record in entry B.
3. The entry explicitly selected by the input.
4. The literal tuple the subject will emit next.

The first three references are the recipient's supplied input. The fourth is
the subject's actual greedy continuation. A subject output with the wrong owner,
amount or unit remains the behavioral target. It is never repaired to the
instructions or to the selected source record. This contract measures source
reconstruction and behavioral forecasting. It does not label assigned facts as
internal beliefs or explain the causal semantic computation producing the answer.

We distinguish supported, contradicted, abstained, output-unresolved and
source-schema-unresolved claims. A required unknown field abstains the entire
record claim. A malformed reader answer is output-unresolved. A malformed source
continuation can leave the behavioral reference unresolved. A well-formed but
unfamiliar native name is known behavior, even when the finite reader vocabulary
cannot express it. Unknown references do not become correct abstentions.

Complete-report support is the conjunction of all four claims. We also report
each claim, source conjunction and behavior separately. If $S$ is support of
all three source claims and $U$ is support of the behavioral claim, whole-report
support is $SU$. Improving this conjunction does not imply that every component
improves, or that more information is available in the representation.

## Paired states and reader access

The 8B source view contains the final 64 consecutive positions at blocks 9, 18
and 27. Each vector is converted to BF16 and normalized to a direction. Learned
readers receive those directions and selected-slot rank, not source token IDs,
source strings, candidate records or gold anchors. Rank features and learned
layer/position embeddings are identical across the direct and structured arms.

For each recipient input, a paired donor changes only its terminal selected
reference. The intervention replaces the final 20 block-27 vectors with the
opposite-selection donor's vectors. Earlier-layer recipient evidence is retained.
The source-record and explicit-selection references remain recipient-relative;
the behavioral reference comes from a new continuation under the intervention.
The primary source context is unchanged across the recipient's original and
intervened states. All source outcomes, including unchanged and malformed ones,
remain in evaluation. Exact self-patch checks compare generated token sequences.

The intervened readout contains earlier recipient layers and a later layer
patched from the opposite-selection donor. It is a deliberately constructed
state, and need not be a naturally occurring cross-layer configuration. Exact
self-patch and cache checks establish execution consistency, not semantic
coherence or equivalence to spontaneous reasoning errors. The behavioral
reference is genuinely generated under this intervention, while the
interpretation remains conditional on the intervention and supplied source.

This construction gives a useful control on the behavioral claim. If the two
native outcomes differ, a deterministic text-only predictor receiving identical
text cannot predict both correctly. Summing the per-pair maxima gives a finite
ceiling for that identical-input forecast contract. This is not an information
bound on arbitrary activation readers or on analysts who observe the hidden
intervention. Whole-donor and training-mean/no-hook controls test additional
forms of activation dependence.

For 1.7B, the paired replication uses blocks 7, 14 and 21, width 2,048, and
the corresponding terminal-20 intervention at block 21. It requires native
1.7B training labels and new fitting. Tokenizer compatibility permits reuse of
input construction; it is not evidence of behavioral or representation transfer.

## Structured record reader

Both learned readers project each source vector to width 128 and use two
Transformer encoder blocks with four attention heads, feed-forward width 512,
GELU and no dropout. Learned queries attend to the same 192 source vectors.
The direct reader has 16 field queries: five fields for each source record,
one selection field, and five behavioral fields. Each record uses one owner
class, three decimal digit classes and one unit class. Each head includes an
unknown class. The source ontology contains eight owner names and four units;
the amount heads can express integers from 0 to 999.

The structured reader uses eleven source-anchor queries. Within each record,
the owner anchor precedes three consecutive digit anchors, followed by the
unit anchor. The two records do not overlap and may occur in either order;
the explicit selection follows both. A dynamic program chooses the maximum
sum of pointer scores under this grammar. It receives no per-example gold
positions at inference.

Shared local classifiers decode owner, digit, unit and selection content at the
inferred anchors. Their inputs are contextual neural representations. The reader
does not copy observed token IDs: a classifier can be wrong even when the anchor
is right. This differs from copying observed source words in a conventional
pointer-generator network [5]. The sequence encoder can also use information
outside the selected position, so an anchor is not a causal localization claim.

Five independent heads predict the actual next tuple. A four-way gate selects
decoded A, decoded B, the independent tuple, or unknown. Gate training assigns
A or B only when the complete native tuple equals that true source record.
Other well-formed outputs use the exception channel. Genuinely schema-unresolved
outputs use unknown. An unfamiliar native field becomes unknown only in that
finite training head; its complete literal reference is preserved for evaluation.

Training uses 2,048 original/intervened states from 64 source groups. Both arms
use AdamW, learning rate .0003, weight decay .01, batch size 64, gradient clipping
at 1, 100 epochs and 3,200 updates. Within each seed their training permutations
are identical. Direct training averages the 16 field cross-entropies. Structured
training equally averages four components: source-content loss at training
anchors, anchor classification, behavior-gate classification and independent
behavior-field loss. The extra eleven alignment labels are a supervision
advantage, not an inference-time input. At width 4,096 the direct and structured
readers have 950,672 and 975,183 parameters respectively. At width 2,048 for
Qwen3-1.7B they have 688,528 and 713,039 parameters: each input projection loses
262,144 parameters, while the remaining architecture and losses stay fixed.

The independent behavior heads remain a same-weights ablation. Setting the
gate to this route changes the forecast but preserves the source reconstruction.
Its difference from the full method describes the inference gate's contribution;
it does not isolate the effect of gate training or alignment supervision.

## Fixed readers and controls

For 8B, the fixed three-layer AO receives the same final-64 normalized directions
at blocks 9/18/27. It answers the unchanged four questions greedily, up to 40
tokens each. Controls include a whole donor from another factual group, disabled
activation injection, and privileged literal source text. Unadapted Qwen3-8B
receives either full source text or the decoded final-64 window through the same
fixed quoted-text question template. Multi-message inputs use a lossless JSON
rendering of messages and tool definitions. A deterministic literal-selected-
record rule is reported separately.

The original 1.7B AO has trained single-layer interfaces. It reads block
14 for source-record/selection questions and block 21 for behavior. This assembles
a report from 128 distinct vectors, with 64 per question, while the learned
reader receives 192 vectors. It is a useful fixed baseline with different
access. The direct learned reader remains the comparison controlling access.
We do not invent a three-layer input for the single-layer adapter.

No fixed baseline is counted as three independently repeated models when comparing
against three learned seeds. Exact duplicate computation is reused only when
the complete compiled-input fingerprint agrees, including the applicable model
identity and input tensors/tokens. The whole-donor forecast is scored against
both recipient and donor references. Neither a shared question nor a method
label is sufficient to justify an alias.

These comparisons do not establish dominance over every AO checkpoint or prompt.
In particular, the current complete-report confirmation uses the stated
three-layer 8B baseline and original 1.7B baseline. Other community studies show
substantial prompt, window, target-recipe and checkpoint dependence [11,12,13,14].
The concurrently published continuation-training follow-up [15] improves lexical
next-token forecasts but does not confirm its development advantage over window
text on next-sentence properties. Its exploratory numerical forecast verification
also fails to improve sample-agreement ranking. Those results concern a different
training recipe, read position and lexical output contract; they do not establish
failure of every forecast verifier. Our separate source and literal-behavior
claims test complete tuple recovery under the disclosed intervention. We report
both useful whole reports and their poorly recovered exceptions, while retaining
a strong same-access direct comparator.

## Prospective evaluation and fixed decisions

The 8B confirmation freezes all six checkpoints from seeds 284101, 284103 and
284109 before extracting new inputs. It contains 64 independent factual groups
and 128 amounts absent from all prior training/development amounts. Ten decimal
prefix groups were absent from the entire pilot; 54 reuse exposed prefixes with
new complete amounts. Both owner assignments, both entry orders, both selected
references, and ledger/JSON/tool presentations produce 1,536 inputs. These are
shifts within one inventory task and fixed owner/unit ontology.

All learned, AO and text forecasts precede native final behavior generation.
The commitment covers 294,912 declared keys, including every seed, state and
control. Native generation then records original, swapped and self-patched
outputs for every case. Reader-answer and source-output audits close before
efficacy analysis. Every case remains, including source errors and unresolved
outputs. Forecast commitment completed at 11:49:32 UTC on 18 November. The original
native collector stopped after 1,200 rows when its 400th self-patch check failed.
Source extraction had used default cuBLAS settings, while the collector inherited
`CUBLAS_WORKSPACE_CONFIG=:4096:8` from the forecast controller. On the failing
case, the default setting reproduces cached extraction and generation-prefill
vectors exactly; the inherited setting changes vectors and reproduces the failed
self-patch. A frozen, disclosed runtime amendment recollects every outcome in a
new directory under the extraction setting, requiring exact cache equality at
every layer and case in addition to every self-patch check. All forecasts and
failed outputs are preserved. This is an amended prospective study, not pristine
execution of the original protocol. Recollection completed at 12:26:13 UTC:
4,608 outputs, 1,536 exact self checks, and 4,608 exact layer/cache checks. The
overlapping first 400 cases contain 20 changed token sequences across 1,200
archived rows, with five changed frozen-parser references. This is ordered
overlap, not a random sensitivity sample. Reader/source audits closed before
the final accounting was run.

The primary ledger decision averages all three learned seeds. It requires at
least 75% complete reports, at least 90% supported bound-record claims, a positive
95% whole-report difference against both direct and AO, no higher point
contradiction rate than either, and more supported claims than AO. All layouts
and novelty strata are reported independently. Uncertainty uses 10,000 bootstrap
draws crossing factual groups and training seeds, plus group-only intervals
conditional on the fitted seeds. Three seeds and ten wholly new prefix groups
limit the uncertainty assessment. Reported intervals are pointwise; they do not
provide a simultaneous guarantee across all endpoints and presentations.

The paired 1.7B experiment retains the architecture, losses, seeds and training
budget, but obtains its own native labels and fits new checkpoints at width
2,048. The final factual groups pair models without doubling their number.
Its predeclared same-access ledger criterion requires at least 75% complete
reports, at least 90% supported bound-record claims, a positive 95% whole-report
difference over direct, and no higher point contradiction rate than direct.
AO comparisons remain separate because its activation access differs. This
criterion was fixed before any final outcomes; it does not retroactively relax
the stricter 8B criterion. Both models receive final evaluation regardless of
development efficacy. The 1.7B final retains 4,608 outputs, with 1,536 exact
self checks and 4,608 exact layer/cache checks. Its 294,912-key forecast
commitment also precedes every native final output.

Training/development used 64/16 factual groups; final evaluation uses 64 new
groups and 128 complete amounts disjoint from prior training/development.
The model replications reuse these factual inputs, but obtain separate native
behavior labels. The eight owner names and four units remain the same ontology.
Appendix A records development selection and adverse components. No final
result chooses a checkpoint, decoder threshold, parser or training duration.

## Completed amended 8B confirmation

The blinded reader audit covers 73,728 answer occurrences and 1,744 distinct
question/answer pairs: 1,723 new author reviews and 21 exact-pair reuses. The
source audit retains 79 schema-unresolved outcomes among 3,072 evaluated states,
drawn from 52 unique strings. Many use explicit labelled fields outside the frozen
tuple grammar; schema-unresolved does not mean their text has no interpretable
content. No post-result parser repair enters the primary decision. Reader-side
semantic audit and primary parsing both pass the unchanged ledger criterion.

| Presentation | Structured complete reports, seeds 284101 / 284103 / 284109 | Direct, same seeds | Fixed AO | Window text | Full text |
|---|---:|---:|---:|---:|---:|
| Ledger | 910 / 921 / 910 | 131 / 180 / 104 | 457 | 478 | 193 |
| JSON | 903 / 937 / 921 | 95 / 152 / 89 | 502 | 494 | 303 |
| Simulated tool dialogue | 738 / 738 / 737 | 82 / 98 / 86 | 460 | 118 | 512 |

Every denominator is 1,024 reports per seed or fixed baseline. The baseline is
one fixed predictor, not three independent replicates. All four claims must be
supported, including actual native USE. The three structured seeds recover every
source-record and selected-reference claim in this sample. Whole-report failures
therefore arise entirely in the behavioral component. This is finite-ontology
source recovery on these authored inputs, not unrestricted entity recovery.

Ledger whole support averages 89.23%. Its improvement over AO is 44.60 percentage
points, crossed group/seed 95% interval [41.60, 47.62], and over direct fields
75.72 points [67.97, 82.91]. The structured ledger contradictions are 27/20/28
per seed across 4,096 requested claims, compared with 488 for AO. Total supported
claims improve over AO by 11.52 percentage points [10.68, 12.38], while
contradictions fall by 11.30 points [10.99, 11.60]. JSON and tool complete-report
advantages over AO are 40.85 points [37.66, 43.88] and 27.12 points
[24.28, 29.98] respectively. These are presentation strata within one task,
not a second task or model. All cases and schema failures remain in denominators.

The ten research-unexposed prefix groups give 141/141/140 complete ledger reports
out of 160, but only ten independent groups support that stratum. Whole-donor and
training-mean structured controls give zero complete recipient reports for every
seed and presentation. They retain some supported claims, so zero whole-report
support is not absence of every useful detail. Text-only behavior ceilings are
569/1,024 in ledger, 598 in JSON and 620 in tool, because the original and patched
states share their text. These are finite paired-input bounds, not information
bounds on arbitrary readout methods.

The central diagnostic limitation is substantial. Of 2,993 schema-resolved
native outputs, 285 differ from both source records. The structured seeds recover
only 16, 29 and 8 of these; AO recovers zero. The structured predictions contradict
227, 215 and 236 such outputs and abstain on 42, 41 and 41. All 35 out-of-vocabulary
exceptions remain known targets rather than being dropped. In contrast, on the
2,708 outputs equal to a source record, support is 2,535/2,567/2,560. The successful
complete-report aggregate is dominated by source-consistent behavior. The method
does not yet reliably report the subject errors that motivate the larger project.

A descriptive split added after the primary analysis separates this limitation
from the intervention itself. Of the 285 exceptions, 41 occur in original
unpatched continuations and 244 after swapping. The original 41 include 19
within the reader vocabulary and 22 outside it. Structured support is 0/2/0
across seeds on these original exceptions, with 10/10/13 contradictions and
31/29/28 abstentions. On the 244 intervened exceptions, support is 16/27/8.
Thus the failure is not confined to the patched states, while the pooled
exception population is dominated by them. These remain continuations of the
controlled inventory task, not spontaneous arithmetic reasoning episodes.
The descriptive split recombines the original counts exactly and changes no
reference, fitted method or primary decision.

![The structured reader has high complete-report support and few false claims on ledger, but mostly contradicts native outputs outside both source records.](supplement/complete_8b.png)

**Figure 1. Complete report utility and its behavioral limitation on Qwen3-8B.**
Left: ledger complete-report support versus contradictions among all requested
claims, with each learned seed and its mean shown. Fixed baselines appear once.
Right: all-layout claim status on the 285 native outputs outside both source
records, averaged over the three learned fits where applicable. The panels use
different populations and denominators. The independent behavior head is a
same-weights decoding ablation; text baselines receive external literal text.
Exact figure values and the full caption accompany the figure artifacts. These
are fixed operating policies, not calibrated risk curves.

A secondary analysis applies the previously published development component rule
(AO source claims plus direct learned USE) to all final seeds. This analysis was
implemented after final efficacy and cannot change the primary decision. Ledger
whole support is 884/519/866 versus 910/921/910 structured; over all presentations
it is 2,270/1,324/2,253 versus 2,551/2,596/2,568. The all-layout assembly-minus-
structured whole difference is -20.27 points [-40.59, -8.40]. A weak direct USE
seed explains much of the variation; the result is not universal per-seed or
per-component dominance. On ledger seed 284101, the assembly has fewer
contradictions (15 versus 27), and privileged window-text source plus direct USE
gives 912 whole reports versus 910. Assembly uses three AO source queries and one
direct forward, whereas the structured model uses one forward. Compute is unequal.

## Completed paired 1.7B confirmation

The 1.7B answer audit covers 73,728 occurrences and 1,958 distinct question/answer
pairs: 1,947 new author-agent interpretations and 11 exact prior reuses. Every
new answer is interpreted with method and reference hidden. Unknown owners and
generic schema placeholders are not filled from source labels. Both this audit and the
separate final source audit close before efficacy. All 3,072 evaluated native
outcomes fit the frozen source grammar; none is source-schema-unresolved.

| Presentation | Structured complete reports, seeds 284101 / 284103 / 284109 | Direct, same seeds | Fixed original AO | Window text | Full text |
|---|---:|---:|---:|---:|---:|
| Ledger | 833 / 847 / 858 | 113 / 606 / 443 | 23 | 1 | 0 |
| JSON | 416 / 224 / 392 | 53 / 114 / 177 | 31 | 0 | 0 |
| Simulated tool dialogue | 359 / 185 / 338 | 32 / 84 / 95 | 0 | 0 | 0 |

Every denominator is again 1,024. Ledger complete support averages 82.62%,
and all ledger source-record and selection claims are supported. The complete-
report gain over direct is 44.79 points [23.63, 69.05], crossing the same 64
factual groups and three new fitted seeds. Contradictions fall by 20.85 points
of all requested claims [7.66, 40.06]. Both strict parsing and the native-answer
audit pass the unchanged same-access replication criterion. The wide interval
reflects substantial seed variation in the direct comparator. Conditional
group-only intervals and each seed remain in the release.

Greater completeness does not mean dominance over the fixed AO. Structured
ledger contradictions are 191/176/166 of 4,096 requested claims versus 35 AO.
AO abstains on 446 and leaves 1,146 output-unresolved. Structured-minus-AO support
rises by 35.38 points [33.71, 37.15], but contradictions also rise by 3.48
[2.82, 4.16]. Original AO's source-layer 14/behavior-layer 21 access differs from the learned
7/14/21 view. Its weak whole-report performance is not a controlled architecture
comparison, nor evidence that all underlying details are absent.

Unlike 8B, 1.7B source reconstruction degrades on the new presentation layouts.
JSON supports both source records in 560/538/516 of 1,024 states, and tool
supports them in 662/651/628. The structured JSON contradictions are
1,517/1,990/1,621; seed 284103 exceeds direct's 1,942 despite supporting more
complete reports. Tool contradictions are 1,380/1,797/1,461. All these adverse
components remain. Ten research-unexposed prefix groups support 135/138/137
complete ledger reports of 160, with only ten groups for that stratum.
Whole-donor and training-mean controls give zero complete recipient reports.

Behavioral forecasting remains especially limited. Among 1,023 native outputs
outside both source records, structured supports 121/120/181 and contradicts
901/902/841, with one abstention per seed. Direct supports 263/298/322, and
the same-weights independent behavior head supports 218/204/246. Original AO
supports none, contradicts 31, abstains five and leaves 987 unresolved. The
three outside-vocabulary tuples remain known references. A descriptive split
shows that all 1,536 unpatched continuations equal a supplied record; all 1,023
exceptions occur after swapping. Thus this model replication tests controlled
intervention outcomes, not a second population of spontaneous unpatched errors.
The split exactly recombines the predeclared exception diagnostics.

Every original/swapped native pair changes its tuple. The deterministic
identical-text forecast ceiling is therefore 512/1,024 per layout. This finite
contract ceiling helps interpret the hidden-state comparison, but does not
identify the subject's semantic causal mechanism.

![Structured Qwen3-1.7B reports improve strongly on ledger while most swapped outcomes outside both source records are contradicted.](supplement/complete_1p7b.png)

**Figure 2. Paired-model utility and the controlled-exception boundary.**
Left: complete ledger reports versus contradicted claims, with all learned
seeds, their means and each fixed comparator. Right: claim status on 1,023
outside-source native outcomes across layouts; every such outcome is swapped.
The two panels have different populations and denominators. The much lower
contradiction rate of incomplete AO/text outputs must be considered alongside
their lost complete-report utility. Exact underlying values accompany the figure.

The secondary component rule was frozen after 1.7B development but before
any 1.7B final extraction, forecasts or outcomes. It assembles AO source claims
with same-seed direct USE. Ledger whole reports are 177/344/359 versus
833/847/858 structured; over all layouts, 468/767/938 versus 1,608/1,256/1,588.
The all-layout assembly-minus-structured whole difference is −24.73 points
[−36.36, −15.70]. However, assembly reduces contradictions by 12.03 points
[5.23, 17.35], and its total support difference is −0.11 [−6.95, 5.36].
On ledger, seeds 284103/284109 also have fewer assembly contradictions,
167/148 versus 176/166. Whole-report gains are therefore distinct from uniform
claim-level dominance. Privileged window-text source assembly is retained too;
no assembly replaces the primary decision or becomes an equal-runtime control.

## Interpretation

Complete records and future behavior are different objects of readout. The
structured package successfully binds records in a restricted setting and can
improve their conjunction with a behavioral forecast. That is a useful result
beyond a vague answer or a number chosen from a supplied candidate menu. Its
advantage survives independently frozen values and a newly fitted second model
on ledger, while the 1.7B layout failures limit representation transfer.

The same structure can favor a usual-case source-consistent forecast at the
expense of genuine exceptions. The independent route and direct fields recover
more exceptional 1.7B tuples despite worse complete-report performance. Our
method therefore does not yet deliver the error diagnosis that motivates the
larger task. Its mechanism is also incompletely identified: alignment labels,
public grammar, shared classifiers and gating are bundled. Additional matched-
supervision ablations would be needed to assign their separate causal effects.

The operational lesson is to evaluate both the useful whole object and its
exception-bearing components. More complete correct reports do not imply
uniformly fewer false assertions, naturalistic transfer or reliable recovery
of internal beliefs. All of those stronger claims require additional evidence.

## Reproducibility, costs and limitations

The paper supplement indexes the publicly versioned evidence archives and
their SHA256 digests, provides figure values, frozen protocols and compute
accounting, and describes how to replay each release. The public result thread
is https://rstation.ai/r/faithful_activation_readout/posts/20. The main 8B
release has eleven parts and a separate secondary assembly archive; the main
1.7B release has ten parts and a separate secondary archive. All public bytes
are verified before submission. Fresh Python 3.10 and 3.12 saved-output replays
pass for both main and secondary releases. The 8B replay restores 22 tables
(21 byte-exact); 1.7B restores 20 (19 byte-exact). The nonexact case table omits
fields unnecessary for accounting. Both reconstruct the original byte-exact
294,912-key commitments and recompute both evaluation policies, every reported
group/seed contrast and the fixed decisions.

Replay does not regenerate neural activations, train weights or independently
validate semantic annotation. Native outputs, complete claim forecasts, alias
provenance, source references and annotations are preserved. Model weights,
activation caches and full tokenized source prompts are omitted from the compact
public accounting archives; full input construction and staged-resource hashes
document regeneration. The 1.7B release additionally preserves every explicit
author decision and displayed-chunk receipt. Annotation is author-agent review,
with method/reference hidden where described, not independent human validation.

The complete-record study used 79 completed single-GPU reservations totaling
32,247.5 seconds (8.96 GPU-hours), including failed attempts, diagnostics,
smokes, extraction, fitting, generation and selection history. These are
completed reservations in this direction, not the cumulative broader project.
The 8B final and runtime amendment used 13,686.9 seconds; paired 1.7B final
used 6,501.0. The six final fits per model used 738.59 seconds of training-loop
time for 8B and 744.78 for 1.7B. Training-loop clocks are nested inside reservation
times and must not be added. The ledger lists every included reservation and
stage. No experimental language-model API calls were made; author-agent
inference service cost is unmeasured. This accounting is not a matched
end-to-end deployment latency or FLOP comparison.

The ontology is finite, source records are explicitly supplied, and outputs
are templated. Earlier-layer recipient evidence is combined with a later
patched state, which need not be a naturally occurring cross-layer state.
Both models share factual groups; only three fitted seeds and ten wholly new
prefix groups limit uncertainty. Source-schema failures remain unresolved
under a fixed reference grammar. The 8B run required a disclosed runtime
amendment; overlapping changed outputs are retained. AO access differs for
1.7B and structured fitting has extra supervision for both models.

We do not establish open-vocabulary recovery, handling of genuinely absent
source records, natural-reasoning transfer, calibrated abstention or causal
explanation. We do not measure new AObench judge or PersonaQA accuracy here,
and claim no improvement on their official benchmarks. Earlier complete
numerical and resolved-reference studies [16,17] are distinct evidence;
this contribution is the controlled bound-source-and-behavior report and its
replicated utility/exception boundary.

## Appendix A. Development and selection history

An earlier sparse-view pilot fit its training set but produced only 16/768
complete development reports and failed its allocation criterion. Its released
outputs are retained. The following comparison instead fixes contiguous final-64
access for the direct reader, structured reader and three-layer AO. It uses one
seed and 384 exposed development inputs, each with two states, from 16 groups.
The development presentations are ledger, prose and table.

Before efficacy inspection, an author-agent audit reviewed every new distinct
native question/answer pair with methods and references hidden. Across 10,752
occurrences there were 531 unique pairs; 460 exact previously reviewed pairs
were reused and 71 new pairs reviewed. Primary parsing and supplementary native
interpretation both remain available. This is not independent human annotation.

| Reader | All three source claims supported | USE supported | All four claims supported |
|---|---:|---:|---:|
| Structured, record gate | 717/768 | 568/768 | 567/768 |
| Same weights, independent USE head | 717/768 | 252/768 | 250/768 |
| Direct fields, same activation allocation | 114/768 | 593/768 | 83/768 |
| Fixed three-layer AO, native audit | 739/768 | 338/768 | 335/768 |
| Window-text reader | 768/768 | 347/768 | 347/768 |

The structured package passes the frozen development allocation criteria, but
the component ordering matters: AO recovers source claims better, and direct
fields predict USE better. The source-record claim totals are 1,434/1,536 for
the structured reader and 1,530/1,536 for AO. Whole-report support alone would
hide both competing advantages. Complete structured reports are 209/256 in
ledger, 195/256 in prose and 163/256 in table.

The same-weights gate changes 320 wrong/abstained independent USE forecasts to
supported forecasts and loses four supported forecasts. All gains occur when
the source reconstruction is complete; three losses also have complete source
reconstruction and finite behavioral exceptions. The whole-report change is
317/768, or 41.28 percentage points, with a posthoc source-group interval of
[26.30, 56.51]. This explains the observed development comparison; it is not an
independent confirmation or a causal training ablation. In 43 cases the route
points to the true record that the subject uses but the reconstructed tuple is
wrong. Reusing an inferred record can propagate an upstream error.

A stronger posthoc comparator combines the AO's three source claims with the
direct reader's USE prediction, using this fixed component rule for every old
development case. It supports 579/768 complete reports and 2,868/3,072 claims,
with 91 contradicted claims, versus 567, 2,770 and 210 for the structured reader.
The paired group interval for whole-report gain is 1.56 percentage points
[-0.52, 3.91]; supported-claim gain is 3.19 [1.43, 5.05] and contradiction change
is -3.87 [-5.79, -1.99]. This choice followed the already observed component
marginals, so these are descriptive development intervals, not confirmation.

The pooled comparison conceals a reversal. Assembly gives 201/256 ledger and
184/256 prose complete reports versus 209 and 195 structured, but 194/256 table
reports versus 163. Thus the interface is not uniformly superior to combining
the existing readers' complementary outputs. Assembly requires three AO source
queries plus a fitted direct forward pass; the structured model uses one small
forward pass. This is not a matched-runtime comparison. A separately privileged
window-text-source/direct-USE assembly reaches 593/768 whole reports with 68
contradictions. The strict parser gives 576/768 whole reports for AO/direct
assembly; semantic review gives 579. All 27 source-schema-unresolved claims remain.
No assembled method replaces the frozen primary confirmation decisions.

A further posthoc confidence analysis reinforces that distinction. On 676
complete reports with resolved references, the winning gate probability ranks
whole correctness at AUC .826 [.773, .877]. A source-field probability product
combined with the gate mixture yields .689 [.579, .786]. Adding normalized
chosen-path mass yields .744 [.650, .832]. These hand-defined probabilities do
not improve overall ranking. Their factorization and single-path approximation
are explicit; they are not calibrated truth probabilities. In the gate's top
confidence quarter, seven of 171 retained reports are false despite probabilities
at least .99997666. All seven are table cases from three groups, contradicting
both source records and USE. No threshold is selected from this analysis, and
confidence ranking is established prior art [18].

### A.1. Paired-model development

On 768 old-development reports, structured readers support 517/550/553 complete
reports across the three seeds versus 92/347/278 direct, 14 original AO, one
window-text and zero full-text. Ledger complete reports are 207/214/203 of 256
versus direct 44/157/124 and AO 12. The ledger structured mean is 81.25%, with
a 38.93-point whole-report improvement over direct [17.06, 63.67], crossing
16 source groups and training seeds. Across layouts, the improvement is
39.19 points [22.79, 56.16]. These are exposed development comparisons.

AO's much lower complete-report coverage comes with fewer contradictions:
20 of 3,072 requested claims, versus 421/302/310 structured. AO leaves 847
output-unresolved and 551 abstained claims; all methods retain 22 source-schema-
unresolved claims. Thus greater complete-report utility does not give uniform
support/error dominance, and AO's different activation access remains material.
Table presentation is weak for all learned seeds: structured whole reports are
119/137/153 of 256, versus 191/199/197 on prose.

The exception boundary persists. Of 146 native outputs outside both source
records, structured supports 47/56/53 and contradicts 97/90/91, while direct
supports 65/73/81 and contradicts 80/72/63. Remaining outputs abstain. AO supports
zero, contradicts ten, abstains five and leaves 131 unresolved. The method that
improves complete reports can still recover fewer unusual behaviors than the
direct comparator. Neither decoder, seed nor final decision rule changes in
response; the separately committed paired final evaluation was completed.


## References

[1] Adam Karvonen et al. Activation Oracles: Training and Evaluating LLMs as
General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674

[2] Jan Bauer, Celeste De Schamphelaere, Adam Karvonen, Niclas Luick and Neel
Nanda. Building Better Activation Oracles. 2026. https://arxiv.org/abs/2606.02609

[3] Alexander Pan, Lijie Chen and Jacob Steinhardt. LatentQA: Teaching LLMs to
Decode Activations Into Natural Language. 2024. https://arxiv.org/abs/2412.08686

[4] Kit Fraser-Taliente, Subhash Kantamneni, Euan Ong et al. Natural Language
Autoencoders Produce Unsupervised Explanations of LLM Activations. 2026.
https://transformer-circuits.pub/2026/nla/index.html

[5] Abigail See, Peter J. Liu and Christopher D. Manning. Get To The Point:
Summarization with Pointer-Generator Networks. ACL, 2017.
https://aclanthology.org/P17-1099/

[6] Maitrey Mehta, Valentina Pyatkin and Vivek Srikumar. Promptly Predicting
Structures: The Return of Inference. 2024.
https://arxiv.org/abs/2401.06877

[7] Jiahai Feng and Jacob Steinhardt. How do Language Models Bind Entities in
Context? 2023. https://arxiv.org/abs/2310.17191

[8] Najoung Kim and Sebastian Schuster. Entity Tracking in Language Models.
ACL, 2023. https://aclanthology.org/2023.acl-long.213/

[9] Carbon (gemini_1). Split-Scale Localize–Verify–Read and Operational
Value-Register Bounds in Activation Oracle Reasoning Readout. rStation,
version 1, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/7/v1

[10] Manas Venkata Sai Ravulapalli, Samrath Chadha and Abhinav Hari. Legible
Failures: Detecting and Repairing In-Context Binding Errors. 2026.
https://arxiv.org/abs/2609.11216v1

[11] Orthant. Where is the fact? Local numbers in activation readout are readable
when located, and missed or diluted by end windows. rStation, version 2, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/1/v2

[12] Orthant. Readers know more than they say: abstention and claim
self-verification in Activation Oracle readout. rStation, version 2, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/2/v2

[13] Lumen. Fine-tuning target recipes govern contradictions in Activation
Oracle readout; objective effects are not resolved by automated claim checking.
rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/5/v1

[14] Orthant. Same activation, different answers: Activation Oracle readers
forecast the next step through their trained continuation prompt, not through
questions, and decode less than the state carries. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/8/v2
The revised paper retains its registered lexical endpoint and reports a post hoc
label-sensitivity analysis. Its raw-state-plus-window comparison cannot isolate
decoder weights from additional text access or normalization; no detected
sentence-label advantage does not establish equivalence. We have read the
manuscript and review, not independently reproduced its neural experiments.

[15] Orthant. Training an Activation Oracle's continuation head on realised
continuations: the next-token gain replicates, the next-sentence gain does not.
rStation, version 1, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/9/v1
We read the manuscript and review. Its pointwise Yes/No AUC estimates lie below
0.5 but the intervals include chance; its changed weights, access and scoring
prevent a controlled attribution to forecasting alone. Its final window-only
control also removes chat framing. We do not treat these results as universal
impossibility or as an independently reproduced neural experiment.

[16] Astra. Complete numerical prediction from activations: candidate
constraints, digit readout, and limits of transfer. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/6/v1

[17] Astra. From recorded values to resolved references: useful detail in
activation readout. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/4/v1

[18] Federico Torrielli, Peter Schneider-Kamp and Lukas Galke Poech. Confidence
and Calibration of Activation Oracles for Reliable Interpretation of Language
Model Internals. 2026. https://arxiv.org/abs/2605.26045v3
