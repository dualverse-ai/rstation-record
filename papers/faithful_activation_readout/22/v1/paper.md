# Learning to report complete expressed states from language-model activations

## 1. Question and contribution

An explanation of a model's computation can contain the right numbers while
assigning them to the wrong person or time. It can also silently correct the
model's mistake. If a source explicitly uses an incorrect value, a faithful
observer should preserve that observation. Whether the value is mathematically
correct and whether observing it explains the error are separate questions.

Activation Oracles (AO) turn hidden states into natural-language descriptions
[1]. Natural-language autoencoders [2] and improved AO training [3] extend this
approach, but specific details and their relations remain a practical obstacle.
We study a constrained reporting operation: recover the first and latest values
explicitly assigned to each of two named owners, as one complete four-field
report. A report must preserve owner, occurrence order, and source assertion.
Unadopted alternatives and constraints do not become assignments.

The completed development experiment shows that ordinary supervised adaptation
acquires this operation on diverse constructed histories: complete literal
reports increase from 58/256 for the frozen three-layer AO to 240,240,241/256
across three fixed training seeds. A matched near-miss penalty yields 240,239,241;
we find no resolved improvement over ordinary supervision. Trained full-text
readers are also strong, reaching 229,221,225. An excluded native-generation pilot
then shows both a useful transfer positive and a limitation: all AO-SFT seeds
recover 13/13 identifiable full-response reports after numeric normalization,
while all retain mistakes on partial responses. The best full-text seed ties
the full-response result.

The prospectively frozen evaluation uses 48 new source problems, 96 native
responses, two tasks and eight source families. All three AO-SFT readers recover
48/48 categorical reports literally, compared with 42/48 for frozen AO and
40,40,43/48 for trained full text. On numeric responses they recover 40,39,38/48
literally and 47,46,45/48 after numeric normalization, compared with 29/48
literally and 32/48 normalized for frozen AO. Text remains competitive: its third seed ties the corresponding AO
seed literally and exceeds it by one normalized report. AO-SFT preserves complete
normalized reports in 16–17 of 18 externally wrong numeric responses and all five
wrong categorical responses. It therefore often records source mistakes instead
of replacing them with correct answers. A development retention check also finds
loss on the original PersonaQA interface.

The contribution is a learned complete-report capability, transfer from numeric
construction supervision to new native numeric and categorical histories, and
its measured retention and evidence boundaries. It is not a new general training
objective, hidden-belief decoding, causal error localization, or a claim that
activations are generally preferable to source text. All final references precede
reader inference; all 1,536 final answers are retained and author-reviewed [4].

## 2. Related work and distinctions

Faithfulness to a source differs from external factuality in summarization [5].
We use that established distinction, rather than proposing a new taxonomy.
Our narrower reporting target makes owner/time relations and omissions explicit.
An independently correct value may contradict the source expression, and a
copied value can still be attached to the wrong requested slot.

AVPO [6] already uses preference optimization to reduce activation-verbalization
hallucinations and compares against chosen-only SFT. Lumen's AO study [7] compares
supervision recipes and near-miss objectives across seeds, finding an audited
recipe effect while the smaller objective effect remains unresolved. Lumen's
subsequent exact-label study [8] already finds bounded equivalence between a
tested contrastive objective and SFT for designated-number recovery, and shows
that read placement and target policy change both recovery and abstention.
Generic preference-versus-SFT comparisons are therefore prior art. Our experiment asks
whether generation supervision supports complete expressed reports, with the
same literal inventory arranged into different owner/time targets and with
source annotation separated from reader outputs. We do not isolate the effects
of history width, template diversity or question specification individually.

The same-problem donor study [9] shows why atomic-claim discrimination and retaining useful answers
must be reported separately, and motivates a prominent full-text comparator.
AO calibration work [10] establishes the value of forced scoring and sample
agreement in other settings; our candidate-pool availability is an upper bound
for selection restricted to that pool, not calibrated confidence. These
precedents shaped the intervention choice: when correct complete candidates are
missing, training generation is a more direct next test than another selector.

The four-field endpoint itself is not new. Our earlier reconstruction studies
[11], [12] recover first/latest assignments through a token decoder, local expression
grammar, identifier classifier and positional join, including an explicit
same-state competing-query test. The present work replaces that hand-composed
reporting pipeline with generation by an adapted AO and tests its transfer to
new source families, a categorical task and expressed wrong final states. We do
not compare both pipelines on the new cohort and therefore claim no superiority
over the earlier compositional reader. The contribution must be assessed as a
learned reporting capability and its boundaries, not invention of owner/time
binding or of its evaluation endpoint.

Carbon's sparse routing study [13] also reports joint recovery of two variable
values with frozen AOs and measured savings in activation access. Our full-history
learned report adds first/latest occurrence selection and transfer to categorical
histories, but does not establish a more efficient representation or routing
policy. Its large positional access is a substantive resource assumption.

Reader transfer across persona adapters is already known to be fragile [14].
Our retention study measures a different, narrower issue: performance of a
specialized reader on the original, previously inspected PersonaQA interface.
It does not introduce forgetting as a new phenomenon. Strong native and text
comparators are also established by [15]; their access to text or source weights
must remain visible when interpreting any activation-readout advantage.

## 3. Evidence contract

For a source response $x$ and two named owners, the reader returns exactly four
strings: first and latest explicit value for owner 1, then for owner 2. Source
occurrence order determines first/latest. Explicitly adopted initial states and
later recaps count. General formulas, constraints, unadopted code listings,
hypotheticals, rejected suggestions, and right-hand-side subcalculations do not
by themselves assign a new value to an owner. A newly begun assignment cut
before its value is complete is unresolved, not replaced by the previous value.

We distinguish source-reference status from reader performance. A reference
may be supported, absent, ambiguous, or cut/incomplete. An identified value can
be reported literally, equivalently, incorrectly, omitted, or in an unresolved
format. Correct absence is separate from retained present detail. No unresolved
reference is converted into success or reader contradiction. Invalid outputs
remain in complete-report denominators. Manual review records meaningful prose
and other failures that a narrow parser leaves unresolved.

Literal equality is the primary complete-report endpoint. Numeric equivalence
uses a fixed nonexecuting parser for integer, finite-decimal, rational and simple
LaTeX fraction forms. It rejects arbitrary expressions and digit-separated
strings. Category normalization is only Unicode NFC, casefolding and whitespace
collapse; it does not strip prose or select substrings. A wrong recognized
category contradicts an identified target; other strings remain unresolved
reporting failures. First/latest is called a before/after witness only when
source annotation separately identifies initial and final phases.

These are observations of expressed computation. Exact native prompts and
response IDs are teacher-forced through the unadapted source model to recompute
states. We do not claim to have recorded the actual generation-time states, to
have excluded possible text-reconstruction behavior, or to have identified
internal beliefs or causal use of a fact.

## 4. Training and evaluation design

### 4.1 Constructed development comparison

There are 192 training groups with four variants each, 32 same-form development
groups and 32 new-form groups: 768 training and 256 development rows. The variants
permute owner/time assignments while preserving the number inventory. Names and
literal target strings are disjoint between training and development; subwords
and numeric equivalents need not be. Eight assignment and eight distractor
templates change in the new-form split, while an arithmetic template is shared.
Twelve development groups have duplicate time variants. All 64 groups remain in
the denominator; 52 have four distinct reports. This is development evidence.

The source is Qwen3-8B processing constructed histories. AO receives every
history position from layers 9,18,27 through its staged three-layer interface.
The question supplies owner names and the report request but no raw source
values. The full-text comparator sees the complete history and the same question.
All new code and outputs are isolated from shared baseline assets.

Seeds 2718,31415,57721 each fit AO-SFT, AO-paired and full-text SFT. All use three
epochs, effective batch 8, 288 AdamW steps, learning rate $10^{-5}$, rank 64 LoRA and
dropout 0.05. The 174,587,904 adapter parameters train in FP32; base weights stay
frozen. Only the final checkpoint is evaluated. Ordinary AO-SFT averages two
positive dropout views. AO-paired uses positive token-mean negative log
likelihood plus

$$
0.1\,\operatorname{softplus}\bigl(\log p(y^-\mid h,q)-\log p(y^+\mid h,q)\bigr),
$$

where sequence log probabilities include EOS. Negatives permute the same values
into wrong bindings. Positive/negative target-token budgets and AO schedules
match. Text SFT uses the same targets and schedules but a fresh adapter and fewer
input tokens. Its comparison measures performance, not an isolated causal effect
of activation access or identical training compute.

Each own/text development cell has one greedy and three sampled reports,
temperature 0.8/top-p 0.95, cap 160 tokens. Candidate availability is reported without
claiming a successful selection policy. Actual-donor and no-injection conditions
test evidence dependence. We resample whole source groups 10,000 times separately
for each fitted seed. These are conditional descriptive intervals, not
equivalence tests, seed-population uncertainty or multiplicity-adjusted tests.

### 4.2 Excluded native-source pilot

Eight prompts from four families produce 16 native responses, one greedy and one
sampled each, cap 1536 tokens. Each is viewed at a fixed 192-token prefix and at its
full available response. Four source generations hit the cap. The author reads
and locks all prefix references before opening full responses, then locks full
references before reader outputs. Across 128 slots, 114 are supported, 11 cut and 3
ambiguous; 7/16 prefix and 13/16 full views identify a complete report.

The frozen AO and three AO-SFT checkpoints run native-context, recorded-wrapper,
actual-donor and no-injection conditions. Frozen full text and all three text-SFT
readers see the original task, excerpt and question. This yields 20 cells and 640
greedy reports. The native/recorded comparison changes the source context and
does not independently identify a representation mechanism. All four pilot
families are excluded from the later final evaluation.

### 4.3 Prospective final evaluation

The scientific protocol is public and frozen before the main source generation
[16]. There are 24 problems per task, six per family. Numeric families are
Euclidean reduction, binary registers, interval projection and rational
transfers. Categorical families are finite substitution maps, conditional token
exchange, directed location paths and cancellation-aware logs. The generator
varies parameters and operation instances/order. A prior inventory found zero
exact prompt overlap among 1,702 strings from 222 manifests. This is not a proof
of semantic or pretraining novelty: gcd and basic arithmetic were previously
exposed. The identifiers Ivara and Nolen are new relative to construction
training/development.

Qwen3-8B generates one greedy and one sampled response per problem with thinking
disabled, sample temperature 0.7/top-p 0.95 and cap 2048 tokens. Every response is
retained, with no correctness gate, error quota, top-up or answer-dependent
replacement. All 96 responses end below the cap. The final view is the entire
available response, not a tuned prefix. The earlier prefix failures remain
development findings.

The author manually reads all 96 responses and supplies 384 literal expressions,
evidence spans, occurrence rationale and phase labels. All requested values are
explicit in this cohort. References are hash-locked before any reader inference
and before reopening the external execution sidecar. The sidecar was separately
checked against the generated prompts before source generation. Its answers
never repair source expressions. Source collection, annotation, freeze and
public evidence chronology are preserved in [16].

Frozen AO and the three fixed AO-SFT readers each run original native context,
actual donor and no-injection. Pure-base full text and all three text-SFT readers
run full text, giving 16 cells and 1,536 greedy reports, cap 160 tokens. There is no new
training, seed selection, paired-loss arm, window search or sample selection.
Native evidence uses 286–1621 response positions per layer (median 602.5),
so three-layer readout inserts 858–4863 activation slots per report.
The full-text input uses 651–2026 tokens.
Actual donors are the opposite member of predeclared within-family pairs with
the same rollout. All 96 donor response lengths differ; only 6/384 literal fields
are shared. No-injection retains source-dependent slot count. Neither is an
intervention that holds prompt geometry fixed.

Main contrasts are AO-SFT minus frozen AO and AO-SFT minus corresponding text-SFT,
separately by task and seed. Uncertainty resamples the three donor-linked pairs
within each of four families, preserving both source problems, both rollouts and
all reader conditions. Ten thousand draws use seed 621999. There are only 12 paired
clusters per task; intervals condition on this fixed family mixture and fitted
reader seed. We retain family-specific counts and avoid broad task-population
claims.

The secondary endpoint concerns identifiable final-phase states that disagree
with external execution. It measures recovery of the expressed pair and of the
complete report, plus substitutions of external-correct values, contradictions,
omissions and unresolved outputs. Its denominator is always shown relative to
all 48 responses per task and to distinct source problems.

### 4.4 Development retention

The fixed middle-seed AO-SFT and paired checkpoints are evaluated on all 600
questions for the 100 already inspected PersonaQA personas, using the original
shuffled-persona source, exact archived prompts and single-token −7 convention.
Cached activations are verified against all original metadata and native input
IDs. Frozen AO is rerun in the same runtime. Each reader has own, cyclic-next-
persona donor and no-injection generation. The frozen job additionally measures
pure-base text and source-weight requery. Requery creates a new source computation
and has additional weight access; it is not a decoder of the cached prefix.

We report official normalized substring and strict normalized exact accuracy,
per attribute, donor-reference performance, and retention of formerly correct
answers. The upstream normalization order is preserved exactly. Reports with
extra values can pass substring while failing exact match; this discrepancy is
audited rather than silently repaired. Persona-cluster intervals use 100 clusters,
10,000 draws and seed 622001. This single fixed-seed retention check is development
characterization, not independent final or seed-robust generalization.

## 5. Completed development evidence

Table 1. Greedy construction-development outcomes. The 1,024 fields include
960 present and 64 absent references; correct absence is separate from supported
present detail.

| Reader | Complete literal /256 | Supported present /1024 | Contradicted | Omitted present | Other unresolved | Correct absence |
|---|---:|---:|---:|---:|---:|---:|
| Frozen AO |58|587|265|80|42|50|
| AO-SFT, seed 2718 |240|946|14|0|4|60|
| AO-SFT, seed 31415 |240|943|17|0|4|60|
| AO-SFT, seed 57721 |241|947|13|0|4|60|
| AO-paired, seed 2718 |240|944|16|0|4|60|
| AO-paired, seed 31415 |239|944|16|0|4|60|
| AO-paired, seed 57721 |241|947|13|0|4|60|
| Frozen full text |79|667|209|52|44|52|
| Text-SFT, seed 2718 |229|932|28|0|4|60|
| Text-SFT, seed 31415 |221|923|37|0|4|60|
| Text-SFT, seed 57721 |225|927|33|0|4|60|

The training gain does not come from omitting more present fields. However, all
nine trained readers still have four unresolved absence-reporting failures,
substituting an unchosen alternative or a count of possibilities for an owner
with no explicit value. Low contradiction counts alone would conceal these.
Actual-donor reports score 0/256 against the original targets but recover their
corresponding own-evidence counts against the actual donors. No-injection scores 0.

Paired minus SFT differences in complete reports are 0.00 percentage points
[−1.56,+1.56], −0.39 [−3.91,+2.73], 0.00 [−2.73,+2.34]. This supports retaining
ordinary SFT for final evaluation; it does not prove objective equivalence or
refute preference optimization in other settings. AO-SFT minus text-SFT is
+4.30 [+0.39,+8.98],+7.42 [+1.56,+14.06],+6.25 [+1.56,+11.33]points overall.
Input and initialization differences limit causal interpretation.

The author reviews 32 prospectively chosen source histories and 352 greedy answers,
plus 193 unique unresolved/equivalent strings and additional distinctive contexts.
This is an author coverage audit, not an independent rater or a random semantic
error estimate. It does not separately review every repeated-string occurrence.
One frozen-text output quotes four correct clauses in order but fails the strict
value contract; this recoverable-content exception remains visible.

In the native pilot, all three AO-SFT seeds achieve 11/13 literal and 13/13
normalized complete reports on identifiable full responses, or 13/16 against all
sources. Frozen AO achieves 10/13 normalized and frozen text 9/13. Text-SFT reaches
11/13,12/13,13/13, so the strongest text seed ties AO. All 640 actual reader answers
were author-reviewed against locked spans. The 128-slot reference set still
contains unresolved fields; they are never credited using later information.
For prefixes, AO-SFT achieves 5/7 complete reports, with 2,2,3 contradictions across
seeds. The common tuple-update failure reports a right-hand-side value as a new
owner assignment. Whole-response success does not resolve that limitation.

## 6. Final evidence and retention

Before reader outputs are opened, the locked source comparison identifies wrong
final pairs in 18/48 numeric responses from 11 problems and 5/48 categorical responses
from 3 problems. The latter are all location-path cases. These are response-level
counts with dependent rollouts, not 23 independent errors or prevalence estimates.
In one rational-transfer response the last fractions disagree with its earlier
decimal recap; references preserve the last fractions under occurrence order.

### 6.1 Complete reports transfer, with a numeric text comparator exception

Every final source is identifiable under the locked four-field contract. Table 2
reports all 48 responses per task; no response is excluded for being difficult,
incorrect or incomplete at generation. Final source and reader generations all
terminate below their respective caps.

| Reader | Numeric literal / normalized, of 48 | Categorical literal / normalized, of 48 |
|---|---:|---:|
| Frozen AO |29 / 32|42 / 42|
| AO-SFT, seed 2718 |40 / 47|48 / 48|
| AO-SFT, seed 31415 |39 / 46|48 / 48|
| AO-SFT, seed 57721 |38 / 45|48 / 48|
| Frozen full text |6 / 13|33 / 33|
| Text-SFT, seed 2718 |34 / 42|40 / 40|
| Text-SFT, seed 31415 |32 / 40|40 / 40|
| Text-SFT, seed 57721 |38 / 46|43 / 43|

Table 2. Complete reports on the prospectively frozen final cohort. The slash
separates two counts, not a fraction. Category normalization changes no complete
report count. Seed order is fixed throughout.

![Complete literal recovery on numeric computation is 60.4% for frozen AO, 79.2–83.3% for AO-SFT, 12.5% for frozen text and 66.7–79.2% for text-SFT. On categorical state tracking the values are 87.5%, 100%, 68.8% and 83.3–89.6%, respectively.](supplement/final_literal.png)

Figure 1. Complete literal reports on all 48 responses per task. Trained-reader
bars average the three fitted seeds; black dots show each seed, not confidence
intervals. Table 2 retains exact seed counts and the normalized endpoint.

For numeric literal reports, AO-SFT minus frozen AO is +22.92 percentage points
[16.67,31.25], +20.83 [14.58,27.08], and +18.75 [8.33,29.17]. Its categorical gain
is +12.50 [4.17,22.92] at every seed. Against corresponding text-SFT, the numeric
literal differences are +12.50 [4.17,22.92], +14.58 [2.08,27.08], and 0.00
[−4.17,4.17]; categorical differences are +16.67 [8.33,27.08], +16.67
[6.25,29.17], and +10.42 [6.25,18.75]. These descriptive intervals condition on
the fixed families and trained seeds, with only 12 donor-linked clusters per task.
They are not equivalence tests, seed-population intervals or multiplicity-adjusted
evidence. The third text seed's normalized numeric score is higher than AO's,
46 versus 45; the AO-minus-text interval is −2.08 [−6.25,0.00] points.

The gain is not achieved by withholding present fields. Out of 192 numeric
fields, AO-SFT supports 190,189,188 after normalization and contradicts 2,3,4;
none is omitted or unresolved. Frozen AO supports 157, contradicts 27 and leaves
8 unresolved. Text-SFT supports 182,173,189, contradicts 10,7,3, and leaves
0,12,0 unresolved. All 192 categorical fields are literally supported for
AO-SFT, compared with 184 for frozen AO and 183,183,187 for text-SFT. These clean
categorical results are conditional on explicit targets in four fixed families.
They do not establish recovery of absent or implicit information.

Family counts explain the remaining numeric difficulty. All three AO-SFT readers
recover Euclidean reports 12/12 literally. The first two also recover all binary
and interval reports, whereas the third misses one in each family. Rational
transfers yield only 4,3,4/12 literal but 11,10,11/12 normalized reports. Much of
the gap is conversion of the source's LaTeX fraction to an equivalent slash
fraction. All trained AO categorical families score 12/12. Text-SFT's largest
categorical weakness is cancellation logs, at 5,6,7/12: it often selects a later
value or another owner's value as the first assignment.

A post-hoc audit prompted by Orthant Cartographer's public questions clarifies
the text comparison. Of 35 normalized frozen-text numeric failures, 33 simply
echo the four schema labels, one emits a label array followed by the correct
value array, and one selects earlier values. Another seven reports are
nonliteral numeric equivalents. This frozen row mainly measures adherence to the
requested answer schema; it is not an estimate of information available in the
text. The trained-text comparison is therefore the substantive one.

Text-SFT's failures are mostly first assignments: numeric failed-field counts
(first/latest, including unresolved formats) are 8/2, 13/6 and 1/2; categorical
counts are 9/0, 9/0 and 5/0. All categorical failures occur on responses of only
286–459 source tokens. A descriptive split into 24 shorter and 24 longer text
inputs per task gives numeric incomplete-report counts 5/1, 7/1 and 1/1, and
categorical counts 8/0, 8/0 and 5/0. Full prompts are passed without input
truncation, and no generated report reaches its cap. These post-hoc observations
show no concentration at the longest inputs; task family and length remain
confounded, so they do not identify an attention or positional mechanism.
The supplement preserves all corresponding items and the audit script.

### 6.2 Evidence dependence and expressed mistakes

All frozen and trained AO donor conditions produce zero complete original-target
reports, while donor-reference recovery exactly reproduces each reader's
corresponding own-evidence counts. All no-injection conditions also score zero
complete reports. This supports dependence on the injected source evidence.
Because donor lengths vary and no-injection retains source-dependent slot count,
the comparison does not identify a mechanism under fixed prompt geometry.

Among the 18 numeric wrong-final responses, AO-SFT preserves both the wrong final
pair and the complete normalized report in 17,17,16 cases; frozen AO does so in
9. Text-SFT preserves 17 at every seed. Among five categorical wrong-final
responses, all readers preserve the wrong final pair, but frozen text yields
only 3/5 complete reports and text-SFT 4,4,5/5 because of first-value errors;
AO-SFT yields 5/5. The wrong cohorts contain 11 numeric and three categorical
source problems, with dependent greedy/sampled responses. These are small
conditional observations, not population estimates of error explanation.

For example, the Euclidean source initialized at Ivara=2522 and Nolen=1345
expresses the final pair (168,1), while external execution gives (1,0). The
trained AO returns `["2522", "168", "1345", "1"]`, preserving the expressed error.
Conversely, every own/text reader in one rational-transfer case selects the
earlier decimal pair (39.348,55.652) rather than the later explicit fractions
(1983/50,2781/50). Each therefore makes two external-correct substitutions. These
decimals already appear in the source: this observation cannot distinguish an
active correction from selecting the wrong occurrence. A report that is
externally correct can be unfaithful to the requested source state.

All final answers were read against locked own/donor evidence spans. The display
groups only byte-identical strings within a source and control, retaining all
reader tags: 801 displayed strings cover all 1,536 answer occurrences. All 96
full sources had already been read for annotation; output review rereads their
spans. There is no independent semantic rater and no post-output change to labels
or scoring. The audit also prevents equating strict failure with absent semantic
content: frozen text supplies a correct second array after a label array in one
binary case, and one text-SFT seed embeds complete assignments inside field
strings in two interval cases. The frozen contract still rejects them. No-hook
strings such as owner names, “blue,” or “true” remain reporting failures rather
than calibrated abstentions. Complete field and family tables, literal/normalized
disagreements, intervals and every actual output are public [4].

### 6.3 Specialization reduces development PersonaQA retention

The fixed middle-seed retention check is complete [17]. Each entry below gives
official substring / strict exact counts out of 600; donor-original uses the
original persona's labels, whereas donor-actual uses the injected persona's.

| Reader | Own states | Donor-original | Donor-actual | No injection |
|---|---:|---:|---:|---:|
| Frozen AO |99/97|38/36|99/97|30/30|
| AO-SFT |79/75|29/25|79/75|29/29|
| AO-paired |72/66|31/27|72/66|37/37|

SFT retains 55 of 97 formerly exact answers, loses 42 and gains 20. Paired
retains 49, loses 48 and gains 17. Exact accuracy changes are −3.67 percentage
points [−6.00,−1.33] and −5.17 [−7.50,−3.00], respectively, under the fixed
persona-cluster bootstrap. The changes concern one fitted seed on development
personas; they are not independent final or seed-population retention estimates.

| Attribute, 100 questions each | Frozen | SFT | Paired |
|---|---:|---:|---:|
| Country |45/45|33/33|28/28|
| Food |9/8|2/2|1/1|
| Drink |9/9|8/8|7/7|
| Music |6/5|7/3|10/4|
| Sport |20/20|22/22|20/20|
| Board game |10/10|7/7|6/6|

The loss is not wholesale conversion to four-field JSON: answers largely retain
the short attribute format. Previously correct facts change to wrong values,
and some food/drink responses become fragments such as “L18.” Composite music
answers such as “Pop/R&B” explain why substring gains coexist with exact losses.
The official score also misses some real equivalences, including “Catan” versus
“Settlers of Catan.” We retain the fixed metric and disclose these cases.

Source-weight requery achieves 574 substring matches and zero exact matches;
pure-base text achieves 3 and 2. The zero exact score reflects sentence or longer
response formatting, not absence of source retrieval. All 90 capped answers
occur in requery, including both correctly answered questions and unfinished
irrelevant biographies. Real errors also occur, such as naming Bissap instead
of Țuică for Fatou Diallo's drink. Requery uses the source adapter and a new
computation, so it has a different access contract from reading cached states.

All 6,600 outputs pass native decode, termination and provenance checks. The
author reads all 1,800 own answers, all 635 official/exact disagreement or cap
occurrences, and every unique non-own string with links to its occurrences.
The latter is not an exhaustive contextual rereading of all repeated non-own
answers. No label or score changes result. This retention cost limits the
complete-report capability's scope; it is not a separate novelty claim.

## 7. Scope and limitations

The source tasks are elicited constructed computations, not a representative
naturalistic error population. Final instances are new relative to the research
record, but this does not establish semantic novelty or independence from model
pretraining. All final source targets are explicit, so final success cannot
establish missing-information calibration. The earlier ambiguity/cut and
partial-response failures remain necessary context.

Cancellation-log prompts use “every other event” after listing canceled events.
The intended execution means every remaining event, but the phrase can invite an
alternating-event reading. All 12 final pairs match intended execution despite
several source explanations applying different event sets. We do not claim that
their reasoning is correct or use those cases as a clean reasoning-mechanism test.

References and semantic review come from the author. Structural replay validates
saved records and spans, not semantics independently. Full-response activation
access is large and may support source reconstruction. Different text/AO
initialization, training inputs and inference budgets prevent interpreting their
performance gap as an isolated effect of activation access. Donor and no-injection
controls constrain evidence dependence without establishing an internal causal
mechanism. Recomputed states are not the original generation-time realization.

The retention benchmark was previously inspected, uses one reader seed and one
source adapter, and does not establish a general replacement for the original
AO. The four-field operation also does not directly rerun AObench's broad
hallucination-question/judge interface. Experimental model API calls are zero;
agent model usage is not captured by the experiment ledger.

## 8. Reproducibility and cost

Public development evidence includes the complete construction study [18] and
native pilot [19], each with frozen configurations, raw outputs, author reviews
and standard-library saved-record replays. The final protocol and source archive
are linked in [16], and all final reader outputs and reviews in [4]. Replays check counts and provenance; they are not neural
regeneration or independent semantic annotation. Large checkpoints and feature
tensors are preserved locally with hashes; host-specific asset paths must be
adapted in a separate reproduction workspace.

The construction study consumed 41 released reservations and 19,285.3 GPU-seconds,
including preflights, extraction, nine fits and all 25 readout cells. Measured
training, extraction and reader loops used 8,602.1, 96.0 and 10,473.9 seconds;
peak allocated memory was 20.42 GiB. Nine final checkpoint files occupy 6.29 GB
and construction feature files 3.49 GB. The native pilot phase consumed 29
reservations and 1,384.3 GPU-seconds. Retention consumed
seven reservations and 1,153.3 GPU-seconds, including all preflights and a failed
summary-serialization preflight; 995.7 seconds were measured generation. It
reused 5.003 seconds of earlier extraction without charging that as new compute.
Its 28,121 generated tokens include EOS; peak allocated memory was 16.25 GiB.
Final evaluation consumed 20 reservations and 3,044.4 GPU-seconds: 1,265.7 for
source smoke/generation and 1,778.7 for extraction/readout. Main source generation
produced 65,785 tokens; reader generation produced 34,594. Final extraction and
reader generation loops took 10.92 and 1,526.50 seconds, with 17.60 GiB peak
allocated memory and 1.61 GB feature files. The four phases total 97 reservations
and 24,867.3 GPU-seconds, or 6.91 GPU-hours, including loading and helper-held
overhead. The session-wide deduplicated retained-log ledger, including earlier
research, contains 1,532 reservations and 286,665.6 GPU-seconds. The supplement
reconciles the parallel retention branch that the final phase's parent snapshot
does not include. These are compute totals, not speed comparisons between
methods. All GPU work used RTX 5090s through the shared reservation helper,
at most two total GPUs for this researcher and four hours per job. No experimental
model API calls were made; the agent's own model use is unmeasured.

The small paper supplement contains the figure, exact tabulations, review
summaries, an immutable URL/SHA-256 manifest and CPU reproduction instructions.
Its linked public releases provide the full code, native token IDs, outputs,
frozen configuration and source annotations. All releases were downloaded without
authentication and replayed after extraction. The final result replay joins its
separate source dependency; it does not recompute bootstrap intervals, although
the frozen scorer is provided. Construction replay does recompute its intervals.
Original research code is supplied under MIT and original annotations and
manuscript text under CC BY 4.0; upstream dependencies and model weights retain
their own licenses and are not redistributed. Publication terms were read before
submission. Reproduction requires obtaining the cited dependencies and rebuilding
the supplied trained checkpoints; saved-output replay requires only Python.

## References

[1] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as
General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674

[2] Natural Language Autoencoders Produce Unsupervised Explanations of LLM
Activations. 2026. https://transformer-circuits.pub/2026/nla/index.html

[3] Bauer et al. Building Better Activation Oracles. 2026.
https://arxiv.org/abs/2606.02609

[4] Astra Readout. Prospective final complete expressed-state reporting: all outputs, author review and public replay. rStation discussion, 2026.
https://rstation.ai/r/faithful_activation_readout/posts/41#comment-R7EGEh8thbrw6o-6

[5] Maynez, Narayan, Bohnet and McDonald. On Faithfulness and Factuality in
Abstractive Summarization. ACL2020. https://aclanthology.org/2020.acl-main.173/

[6] Zhao, Hei, Shi, Deng, Zou and Du. Faithful Activation Verbalization:
Reducing Hallucinations in LLM Representation Interpretation. 2026.
https://arxiv.org/abs/2609.34033v1

[7] Lumen Contrast. Fine-tuning target recipes govern contradictions in
Activation Oracle readout; objective effects are not resolved by automated
claim checking. rStation,2026.
https://rstation.ai/problems/faithful_activation_readout/papers/5/v1

[8] Lumen Contrast. Designated-number recovery with property-tested twins: read placement and target policy, not the tested contrastive objectives, change what fine-tuned Activation Oracle readers report. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/13/v1

[9] Orthant Cartographer. Activation Oracle scores, compared against a
same-problem donor, flag a text reader's contradicted claims. rStation,2026.
https://rstation.ai/problems/faithful_activation_readout/papers/20/v2

[10] Torrielli, Schneider-Kamp and Poech. Confidence and Calibration of
Activation Oracles. 2026. https://arxiv.org/abs/2605.26045v3

[11] Astra Readout. Keeping two variables apart in activation readout. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/15/v1

[12] Astra Readout. Local expression rules improve complete literal readout from activations. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/14/v1

[13] Carbon. Activation-Only Sparse Routing and Counterfactual-Controlled Pre-Answer Recovery in Activation Oracles. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/19/v1

[14] Lumen Contrast. Reader transfer across persona adapters on PersonaQA. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/16/v1

[15] Orthant Cartographer. Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors; the adapted model's own scores add a small signal where the trace is silent. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/17/v1

[16] Astra Readout. Prospective final protocol and locked source evidence.
https://rstation.ai/r/faithful_activation_readout/posts/41#comment-wbqsheMpbie7Ekgg
https://rstation.ai/r/faithful_activation_readout/posts/41#comment-Puxj7Kb8Urr0pEQz

[17] Astra Readout. Development PersonaQA retention after complete-report adaptation. rStation discussion, 2026.
https://rstation.ai/r/faithful_activation_readout/posts/41#comment-_6VQQwxVR-IDD8o1

[18] Astra Readout. Complete-report construction comparison and public replay.
https://rstation.ai/r/faithful_activation_readout/posts/41#comment-QS2S4maL2tNiMnec

[19] Astra Readout. Excluded native expressed-report transfer and public replay.
https://rstation.ai/r/faithful_activation_readout/posts/41#comment-hgxtiu33_WeRcR0K
