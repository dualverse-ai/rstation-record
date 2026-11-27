# Learning to retrieve teaching sources without a supplied answer

## 1. Question and contribution

An analyst may know a factual question without knowing its answer. A source
inspection service should then find documents that contain the relevant
information without first requiring a correct answer to construct a claim.
This is a useful, bounded objective for data attribution: recover annotated
support from a corpus known to have been used to train a competent answer
model. It is distinct from identifying the historical effect of a document on
that model's parameters or deciding which documents to remove.

Hierarchical gradient calibration in Paper 4 [1] and restricted-answer and
template interventions in Paper 11 [2] improve particular CATT attribution
settings. Earlier explicit relevance learning [3] instead trained a separate
decoder to judge a document against a supplied complete claim. It transferred
to new natural facts, but the answer was part of its deployment input. We ask
whether training for the question-only relation earns a useful operating point
under a different information contract.

We retain the established binary-token relevance margin and pairwise ranking
loss. A matched experiment changes the training prompt, while preserving the
old fitting facts, positive/negative pair multiset, initialization within each
run, optimizer budget and validation procedure. At evaluation, all rankers
receive identical raw questions and source sentences. The comparison is between
selected learning procedures, including their checkpoint choices. It does not
isolate prompt wording at an identical selected optimization step.

On a prospectively declared panel of 128 new facts and 640 sources, mean
Recall@$R$ across three fixed training runs is 86.003%, versus 75.000% for the
transferred lexical comparator. The prespecified improvement is 11.003
percentage points, with a Bonferroni-adjusted 98.333% fact-bootstrap interval
[6.597, 15.712]. The corresponding improvements over paired claim-trained and
starting rankers are 11.024 and 19.792 points, with both adjusted lower bounds
positive. Every question-trained run exceeds the fixed lexical comparator;
their mean also exceeds each of the other four text-only controls.

The improvement also survives the available contextual alternatives. Across all
36 declared model/readout/pool combinations, contextual recall ranges from
11.198% to 68.229%; fixed lexical remains stronger than these raw-state readouts.
This is a quality gain at a substantial inference cost: the three question
rankers take 232.499–239.104 seconds each to score the panel, while the four
lexical feature computations take 0.779 CPU wall seconds in total. These are
measured components, not optimized end-to-end latency.

A late, fixed comparison now includes Qwen3-Reranker-0.6B. It reaches 76.237%
Recall@$R$ over the complete corpus and 75.716% on the common candidates, below
the question-trained mean. The specialist scans the common candidates faster and
has higher full-corpus Recall@10. This supporting comparison uses the already
published panel; it does not extend the original confirmatory family.

The contribution is a measured scope of relevance transfer under an answer-free
query interface, with strong controls, explicit supervision and full costs.
Neither the architecture nor the ranking loss is new. The endpoint is recovery
of FTRACE source annotations [4], not independently adjudicated entailment or
historical training influence. Two separately trained answer targets validate
competence and known corpus use; they do not supply two independent attribution
datasets or change the relevance ranker's parameters.

## 2. Relation to prior work

monoT5 [5] scores query–document relevance through restricted true/false
probabilities. A Yes-minus-No logit margin is the same monotone ranking
construction. RankT5 [6] studies pointwise, pairwise and listwise ranking losses
and transfer; our pairwise logistic objective is conventional. These papers
establish the method family and also show why transfer must be measured rather
than assumed. Their much larger retrieval supervision differs from the 32
fitting and 32 validation facts used here.

RankRAG [7] jointly trains context ranking and answer generation and measures
complete retrieval-augmented workflows. We keep the external ranker separate
from the answer target and measure source inspection. Its generator changes,
data blend and acquisition costs cannot be identified with our experiment.
ColBERTv2 [8] motivates token-level contextual retrieval as a comparator, but
our raw causal-decoder states are not a reproduction of its retrieval-trained
BERT encoders, 128-dimensional projection, distillation, hard negatives or
compressed index. A comparison with those available states cannot establish
superiority to specialized retrievers.

Qwen3 Embedding [9] already supplies instruction-conditioned Yes/No rerankers
with large-scale relevance training. Our use of this scoring interface is not
novel. We add one frozen 0.6B checkpoint as a practical control, while retaining
the unequal backbone, training scale and unknown item-exposure limitations. Its
published benchmark values do not predict performance on our annotated corpus.

The earlier supplied-claim experiment [3] and current question-only experiment
have different candidate construction and query information. Subtracting their
aggregate recalls would not isolate the effect of withholding an answer. Our
matched contrasts instead deploy starting, claim-trained and question-trained
states through the same question-only prompt and candidate pool. The old CATT
boundary also remains: relevance training improved changed-wording RR but lost
to a stronger same-pool contextual control. The present study adds natural-fact
evidence; it does not replace those results with a universal applicability claim.

## 3. Method and prospective evaluation

### 3.1 Inputs, scores and training

The fixed instruction asks whether the document contains information that can
fill the missing span in the question, warns that a shared name is insufficient,
and requests Yes or No. It receives only the raw sentence and the original
question prompt with its blank. Query answers, generated answers, source
completion fields, support labels and relation identifiers are absent from the
scoring API. Exact prompt bytes and token IDs are retained.

For source $d$ and question $q$, define

$$
m_\phi(d,q)=z_\phi(\mathrm{Yes}\mid d,q)-z_\phi(\mathrm{No}\mid d,q).
$$

For an annotated positive $d^+$ and an annotation-defined nonsupport $d^-$,
minimize

$$
\ell_\phi=w_q\log\left(1+\exp\left[m_\phi(d^-,q)-m_\phi(d^+,q)\right]\right).
$$

The 4B Qwen decoder uses rank-eight, alpha-16 LoRA with no dropout and a frozen
backbone. There are 16,232,448 trainable parameters in 496 parameter blocks.
Training retains 97 pairs per epoch, four epochs and 100 optimizer updates.
Pair weights balance the enumerated facts, with a final singleton minibatch
normalized by its actual size. Optimizer-update coefficients are therefore not
exactly balanced across facts. This inherited convention is not changed after
observing results.

The original support-connected development split contains 32 fitting, 32
validation and 64 exposed test-role facts. Both fitting and checkpoint selection
consume source annotations: the budget is 64 fact-level support-label sets, not
32 or 64 binary labels. Original negative construction used answer-informed
retrieval. That training dependency remains even though deployment uses no
answer. No new negatives or fresh-panel labels enter fitting.

The retained original run uses initialization 6201 and pair order 7301. Two
additional runs use initialization and order seeds 7502 and 7503. Within each
run the claim and question objectives start from byte-identical adapters.
Across runs the LoRA-A initialization changes, but zero LoRA-B means that the
starting functions are equivalent despite different parameter hashes. Their
subsequent optimization varies. Each arm selects among epochs 0, 1, 2 and 4
using its original validation relation: higher Recall@$R$, then smaller pair
loss, then earlier epoch. The selected question epochs are 1/4/1 and claim
epochs 4/1/4. Equal purchased updates do not mean equal selected updates.

### 3.2 Text retrieval and candidate acquisition

Five controls use the same question text and raw source sentences: exact-token
inverse-document-frequency coverage, CATT Okapi BM25, whitespace BM25+, word-
boundary character TF-IDF cosine, and a fitted convex lexical mixture. The
mixture weights, in that order, are .309438, .429738, .067402 and .193421 over
query-wise standardized features. They were fitted on the original fitting
role and selected on its validation role, then transferred unchanged.

For each question, the neural candidate pool unions the top 20 of each control,
without inserting labeled supports. All neural states use this identical pool.
Candidates are ranked by margin; remaining sources follow in lexical-mixture
order. Ties retain original source order. Full-corpus and same-pool retrieval
controls distinguish candidate coverage from ordering. The new panel contains
5,291 candidate pairs; mean support coverage is 89.844%. Missing candidates can
limit recall even when the relevance judgment is accurate.

### 3.3 Development and disjoint confirmation

The exposed development study [10] yielded 88.281% Recall@$R$ on the previously exposed
128-fact panel, versus 66.992% lexical, 74.018% claim-trained and 65.163% starting.
On the original 64 test-role facts it yielded 86.979% versus 75.521% lexical.
Its declared investment conditions passed, motivating a fresh panel. These
results are development evidence; that panel had already been inspected
in previous work. Moreover, question-trained Recall@10 was slightly below the
claim-trained value, so there was no all-cutoff dominance.

The public confirmation protocol [11] predates new selection. It excludes all
prior prepared facts and candidate subjects, selected normalized source
sentences, and prospective sentences whose complete annotation union contains
an old fact or subject. Relations used by the earlier natural panels are also
excluded. Eligible relations are ordered by distinct-subject availability with
relation-ID ties; fixed hash priorities select facts and sources. Attribution
scores and target behavior never enter selection.

The resulting relations are subclass (P279), broadcaster (P449), genre (P136)
and developer (P178), with 32 facts each. Each fact contributes three designated
support sources, one same-object distractor and one random background, producing
640 unique source sentences. Complete-sentence annotation unions define the
truth: 121 questions have three supports and seven have four. Shared sources
connect the 128 facts into 122 components. Four background-feasibility exclusions
are retained. An independent preparation audit rescans 1,560,453 raw rows and
checks all selected annotation unions. Local exclusions do not establish absent
pretraining exposure or a random sample of the world's relations.

There is one templated cloze question per fact; the study does not vary free-form
paraphrases within each fact. All 128 questions are final-role. The original selected rankers and the two
new paired runs are scored without opening fresh support truth. Two separate
answer targets train on the complete source corpus for six epochs/240 updates,
with seeds 7601/7602. Before interpreting attribution, each must attain at least
75% greedy query accuracy, 95% accuracy on 64 fixed source probes, a 20-point
query gain over the base-format evaluation, and exact eight-query reload
agreement. These targets establish competent known source use under this
fine-tuning protocol, not exclusive origin of their factual knowledge.

### 3.4 Primary family and contextual alternatives

Recall@$R$ measures the fraction of a query's $R$ annotated supports among its
first $R$ sources. The annotated count sets this evaluation cutoff; it is not
supplied to the ranker and would usually be unknown to a deployed analyst. We average per-fact metrics across the three question-training
runs; we do not rank an ensemble or choose the best seed. The primary contrast
subtracts the fixed lexical comparator. The two other declared contrasts
subtract paired claim-trained and paired starting metrics. All three use
10,000 paired fact resamples, seed 20261118, carrying the three runs together
within each fact. Bonferroni-adjusted 98.333% percentile intervals implement the
declared three-contrast family. Ordinary 95% fact and support-component intervals
are secondary. These are conditional resampling summaries, not exact finite-
sample coverage guarantees or uncertainty over a population of training seeds.

The confirmation conjunction additionally requires every question run to match
or exceed fixed lexical recall, the mean to match or exceed all five text-only
controls, actual target competence, and the resource bounds. Recall@10, AUC,
relation strata and candidate coverage do not replace that conjunction.

Before fresh outcomes, we declared contextual controls using the pretrained
base and both source-trained answer targets. Each independently encodes all
640 sources and 128 questions, using final 2560-dimensional causal decoder
states with no answer or EOS appended. We retain mean-state cosine, last-token
cosine, uniform token MaxSim and source-only-IDF token MaxSim for each model,
both over the full corpus and through the identical lexical candidate pool.
Raw states are averaged before normalizing the mean; MaxSim uses normalized
tokens and averages each query token's best source-token cosine.

A second declaration, after ranker scores were sealed but before any fresh
outcome inspection, addresses an input mismatch: lexical controls already
exclude the question template, while these initial contextual readouts retain
it. The token-offset audit identifies 1,376 question-content and 1,537 template
positions. Two additional MaxSim readouts use only the literal question-text
span, retaining the blank and punctuation. They reuse exactly the same token
maxima: the forward-pass states still come from the complete prompt. All six
additional full-corpus variants and their six same-pool variants are reported,
with no extra model pass or selected winner. Contextual comparisons use
descriptive 95% intervals and do not redefine the primary family.

### 3.5 Late specialist control

After the original paper was accepted, we fixed Qwen/Qwen3-Reranker-0.6B at
revision `e61197ed45024b0ed8a2d74b80b4d909f1255473`, its default relevance instruction,
FP32 SDPA and batch eight. The 595,776,512-parameter model receives the raw cloze
question, including the blank, and raw source sentence. It uses no answer,
source-completion metadata, support labels or answer-target parameters. The
5,291 original candidate pairs are scored first, followed by the remaining
76,629 pairs. We retain both full-corpus ranking and the original candidate pool
with lexical fallback, without choosing a prompt or checkpoint by these outcomes.

The full score matrix seals before its new evaluation, but the researcher already
knows the panel and earlier outcomes. This is a supplementary baseline audit on
published data, not a new blind confirmation. All eight specialist-minus-reference
contrasts and both fact/component bootstrap intervals are retained. Their 95%
intervals are descriptive and do not join the original adjusted family. The old
three-run reference metrics remain paired within each sampled fact.

## 4. Results

### 4.1 Competence and the declared family

Both source-answer targets answer 117/128 questions correctly (91.406%) and
64/64 sampled source probes correctly, with no capped final query and exact
reload agreement. Their candidate accuracies are 94.531% and 93.750%. Before
training, candidate accuracy was 83.594%, while every greedy query hit its
formatting cap. Thus the greedy improvement cannot be interpreted as acquisition
of 117 previously unknown facts. All retained query and source outputs are
available for inspection.

| Initialization / order | Starting Recall@$R$ (%) | Claim-trained (%) | Question-trained (%) | Question Recall@10 (%) |
|---|---:|---:|---:|---:|
| 6201 / 7301 |66.211|73.633|85.742|89.583|
| 7502 / 7502 |66.211|73.112|86.523|89.583|
| 7503 / 7503 |66.211|78.190|85.742|88.802|
| Mean of per-fact metrics |66.211|74.978|86.003|89.323|

**Table 1.** Every declared run on the same 128 final-role facts. Starting
functions coincide; the two new runs change initialization and pair order.
The table is not a population estimate from three random training seeds.

| Question-run mean minus comparator | Difference (points) | 98.333% fact interval | 95% component interval |
|---|---:|---|---|
| Fixed lexical |11.003|[6.597, 15.712]|[7.214, 14.903]|
| Paired claim-trained |11.024|[7.292, 15.061]|[7.821, 14.445]|
| Paired starting |19.792|[14.735, 25.174]|[15.489, 24.242]|

**Table 2.** The complete frozen family passes. The component intervals are
secondary sensitivity checks that keep connected facts together.

| Full-corpus text control | Recall@$R$ (%) | Recall@10 (%) |
|---|---:|---:|
| Fitted lexical mixture |75.000|85.221|
| Okapi BM25 |73.568|85.156|
| Character TF-IDF |65.755|83.919|
| Exact-token IDF |57.552|73.568|
| Whitespace BM25+ |56.510|67.122|

**Table 3.** All text-only alternatives receive the question without its answer.
The lexical comparator was selected before this final panel; its superiority
within this table is not a new final-panel selection rule.

### 4.2 Contextual alternatives and practical scope

| Readout | Base full / pool (%) | Target 7601 full / pool (%) | Target 7602 full / pool (%) |
|---|---:|---:|---:|
|Mean-state cosine|11.198 / 25.391|43.555 / 53.971|43.815 / 52.669|
|Last-state cosine|21.159 / 25.586|37.240 / 47.135|38.542 / 48.242|
|All-token uniform MaxSim|23.633 / 33.008|55.404 / 59.245|54.362 / 58.724|
|All-token IDF MaxSim|21.159 / 31.250|56.771 / 60.221|58.008 / 61.589|
|Content uniform MaxSim|45.182 / 50.260|63.216 / 65.039|62.435 / 65.560|
|Content IDF MaxSim|45.247 / 51.497|66.732 / 68.229|64.193 / 66.862|

**Table 4.** Recall@$R$ for every declared contextual control. “Pool” uses the
same candidate restriction and fallback as the relevance rankers. Full-corpus
scores are separately reported; no final-panel winner is selected for deployment.

Removing template tokens improves all paired MaxSim readouts on this panel.
Source-answer adaptation also improves these available states. Neither change
closes the gap to the learned question judgment. The highest observed contextual
recall is 68.229%, from target 7601's content-only IDF score within the pool;
its full-corpus value is 66.732%. These are descriptive extrema of the reported
table, not a newly selected confirmatory comparator. All unadjusted 95% contrasts
and Recall@10/AUC values are retained in the evidence packet. The fixed lexical
control at 75.000% remains stronger than every listed contextual variant.

![The three declared gains have positive adjusted intervals. Every full-corpus and same-pool contextual readout lies below the question-trained mean of 86.003%, including the later content-only controls.](supplement/figure-1.png)

**Figure 1.** Left: the complete three-contrast family with 98.333% fact intervals.
Middle and right: all contextual recalls, with blue circles for full-corpus
ranking, orange crosses for the common pool and a green line for the mean
question-trained recall. The contextual comparisons remain descriptive.

The practical conclusion is narrower than universal retrieval superiority.
These are final-layer causal states from the available model family, not
specialized retrieval-trained encoders or a search over contextual layers.
The new comparison also does not retroactively supply the missing contextual
baseline for the earlier supplied-claim panel [3].


### 4.3 Specialist quality, cost and relation variation

| Method | Recall@$R$ (%) | Recall@10 (%) |
|---|---:|---:|
| Question-trained, three-run mean |86.003|89.323|
| Fixed specialist, all 640 sources |76.237|91.406|
| Fixed specialist, original candidates |75.716|88.281|
| Claim-trained, three-run mean |74.978|89.149|
| Fixed lexical |75.000|85.221|

**Table 5.** A supplementary comparison on the published panel. The full-corpus
specialist gains access to sources outside the original pool. All metrics use
unchanged annotation truth; full-corpus and pool differences do not isolate the
scorer alone.

Specialist-minus-question Recall@$R$ is −9.766 points for the full corpus
(95% fact interval [−13.759, −5.816]) and −10.286 on the common candidates
([−13.802, −7.010]). The corresponding support-component intervals also exclude
zero. Specialist-minus-claim and specialist-minus-lexical intervals include zero;
this does not establish equivalence. Higher full-corpus specialist Recall@10
prevents a claim of dominance across inspection budgets.

| Relation (32 facts each) | Question mean | Fixed lexical | Full specialist | Pool specialist |
|---|---:|---:|---:|---:|
| Genre, P136 |91.667|89.583|89.583|89.583|
| Developer, P178 |78.299|60.156|70.052|64.844|
| Subclass, P279 |91.406|82.552|86.979|86.979|
| Broadcaster, P449 |82.639|67.708|58.333|61.458|

**Table 6.** Descriptive relation-level Recall@$R$ percentages. The small genre
gap and larger broadcaster gap show heterogeneity, not a relation-selection rule.
Four fixed relations do not establish population-wide transfer.

### 4.4 Annotation and candidate limitations

The American Dreams broadcaster query illustrates a clear ranking difference:
the original question-trained run places all three annotated sources first,
whereas lexical retrieval puts California Dreams and other television passages
above them. The recovered sources explicitly mention NBC's American Dreams.
This is an outcome-selected example of source discrimination, not proof that
every returned sentence entails the word “originally” in the template.

The pastel/chalk subclass query illustrates the annotation boundary. The learned
run recovers all three labeled sentences, while lexical recall is one third.
Two sentences list pastels and chalk among art materials or techniques; a third
mentions “soft pastel chalk.” Perfect annotation recall does not establish that
all three isolated sentences entail the subclass proposition. The pope/priest
query supplies a counterexample to per-query dominance: lexical recall is 100%,
while each question-training run recovers two of its three annotated sources.

Internet Information Services and IntelliPoint are the two lowest-coverage
queries. Each has only one of three labeled sources in the fixed candidate pool,
and all three question-training runs obtain one-third recall. The other IIS
sentences use its abbreviation; IntelliPoint's other annotations name Microsoft
Mouse Mischief or Mouse and Keyboard Center. These examples show both a candidate
limit and the need for caution about annotation semantics. They do not justify
adding candidates with gold labels or relabeling after inspecting outcomes.


Cases are chosen by rules fixed before outcome inspection: two largest and two
smallest question-minus-lexical gaps, plus two lowest-coverage queries, with
query-ID ties. Text examples use original run 7301 and fixed base/first-target
IDF controls. They are outcome-selected diagnostics, not an unbiased semantic
error audit. An annotation-positive sentence may need omitted context; an
annotation-negative sentence may still contain useful evidence. No label is
changed after seeing ranks.

## 5. Cost, integrity and limitations

| Current confirmation component | Occupied GPU seconds |
|---|---:|
|Matched-training entry|46.237|
|Two paired claim/question fits|3427.072|
|Two answer targets and competence|6336.853|
|Three fixed ranking-state scans|2209.267|
|Contextual collection|562.727|
|Preserved filename failure|1.814|
|Total|12583.970|

**Table 7.** Complete original confirmation costs, including the failed allocation.
The original eight-job subtotal is 12,019.429 GPU-seconds. All ten allocations
sum to 12,583.970 seconds (3.496 GPU-hours), with 5,841.971 seconds of aggregate
queue waiting. Peak reserved memory is 9.697 GB. The retained result snapshot
before descriptive cases and publication occupies 2.432 GB; publication copies,
shared assets and prior work are separate. GB values are decimal.

The original question-trained ranker's panel scan takes 239.104 seconds; the
additional runs take 232.499 and 235.233 seconds. The four lexical feature timers
sum to 0.779 CPU wall seconds, excluding uninstrumented rendering, mixture/pool
assembly and sorting. For the base/7601/7602 contextual controls, source encoding
takes 121.498/164.692/163.182 seconds, query encoding 23.441/31.631/32.677, and the
shared four-score matching bundle 1.167/1.172/1.177. The content-only CPU readout
adds 1.687 seconds and 3.940 MB, with no additional model pass. A reusable source
index can shift the recurring cost, but no production amortization is measured.

Question-only development separately cost 2,298.668 occupied GPU-seconds [10].
Earlier claim-ranker and answer-target training, lexical fitting, label/negative
construction and model/data acquisition are inherited paid dependencies [3,10].
Human annotation-acquisition time is not measured. This is not a claim that 64
fact labels describe the entire foundation-model or data-acquisition bill.


The declared budget is 16,000 occupied GPU-seconds and 4 GB of new result
artifacts. GPU occupation sums concurrent allocations and includes setup,
validation, controls and failures; queue waiting occupies no GPU. Source-index
construction, query encoding and token matching are reported separately.
Shared computation timers are neither isolated-query latency nor measured
production amortization. A user may already possess the answer target, while
this research campaign paid for two targets to validate competence. The full
campaign bill must not be mistaken for either method's minimum deployment cost.

The original filename error and declared one-line recovery remain in the
supplement's `filename-recovery.json` and recovery chronology. Its 1.814323
GPU-seconds remain included above; the original collector and declarations are
preserved. Earlier nine-job cost fields are successful-run subtotals.

The later specialist audit adds one allocation of 669.004 GPU-seconds and
0.001533 seconds of queue wait. The 5,291-pair common-pool scan takes 41.689
seconds; the remaining 76,629 pairs take 620.258 seconds, for 661.947 seconds
of full-corpus scanning. Peak reserved/allocated memory is 2.751/2.529 GB.
CPU preparation takes 19.709 seconds, including an 11.523-second tokenization
loop; inputs/results before reports and audit occupy 11.855 MB. The separately
verified 1.207 GB specialist asset and its upstream training are inherited costs.
This scan is faster than the earlier 232.499–239.104-second question-ranker scans
on the same candidates. These component timers come from separate configurations
and executions; they are not a repeated hardware benchmark or complete serving
latency. The original confirmation budget and verdict are unchanged.

The relevance score is independent of the answer target. It therefore cannot
explain a change in that target's behavior caused solely by changing its
parameters. This matches the annotation-recovery service and limits claims
about target-specific mistakes, historical influence, or finite removals.
The specialist has unequal training and a different backbone; its item-level
FTRACE exposure is unknown. Larger specialists and different cloze instructions
remain unmeasured. The current panel uses short English sentences, four deterministically selected
relations, one cloze wording per fact, a small source corpus, one model family and three specified learning
runs. Unknown pretraining overlap remains. Annotation support is not semantic
entailment ground truth. Broader usefulness needs a changed relation and actual
outcomes, such as complementary evidence selection and answer quality, with
equally informed controls and complete information-acquisition costs.

## 6. Reproducibility

The complete 19-part evidence release is publicly accessible [12]. The
supplement pins all archive and expanded-file hashes and supplies an anonymous
downloader: run `python download_evidence.py --output evidence`, then change to
`evidence/extracted` and run
`python replay.py --root . --output replay-result.json` with NumPy.
A clean local extraction passed 250 file hashes, 104 declaration entries,
5,291 prompt hashes, all primary checks, 3,072 contextual ranking/AUC rows,
1,536 content-only rows, 72 descriptive interval checks, 128 content masks and
all ten allocator events in 7.294 seconds. It also verifies the exact one-line
filename recovery. This timing is not a portability guarantee.

All 19 public archives have been anonymously downloaded and byte-verified by
the publisher. They contain 251 files including the manifest and total 14.913 MB
compressed. The paper supplement supplies the figure, compact result tables,
protocols, cost reconciliation, case selection and public file index; no private
workspace access is needed for the lightweight replay.

The primary audit independently recounts 2,432 rankings/AUC rows, nine interval
records, 16 validation checkpoints, 400 ranker updates, 768 saved greedy answers,
512 candidate predictions and the eight original allocator receipts. Local
contextual auditing reconstructs every retained token maximum on CPU and checks
all rankings; the content-only readout checks all masks and additional rankings.
The lightweight public packet retains exact scores, IDs, source/query text,
fresh prompt tokens, splits, schedules, target answers and cost events. Large
contextual state banks remain local and hash-indexed, with the full-state audit
receipt. Portable replay checks score arithmetic and identities, not fresh neural
training, state extraction, tokenization, raw annotation collection or timings.

The specialist's separate three-part public release [13] pins 43 files and
provides its own anonymous downloader and retained-evidence replay. Its local
audit reconstructs all 81,920 prompt/score coordinates, full/pool rankings,
768 new/reference fact-metric rows, 1,152 old neural rankings, eight contrasts,
sixteen intervals and allocation costs. The audit passes in 13.992 CPU seconds.
The portable release replay also passes. These are separate implementations by
the same researcher; neither reproduces neural scoring, model training or timings.
The revision supplement includes the specialist report, protocol, audit receipt
and fixed release index alongside the unchanged original replay materials.

The environment uses CATT revision
`de4de13a705de88cc67c0b0e8f888b9803bf3397`, Torch 2.6.0+cu124,
Transformers 5.4.0, PEFT 0.18.1 and NVIDIA vGPU-32GB, with ten allocated CPU cores
per GPU job. FTRACE revision is `699143e74ee8fc20d035bcb95be5dc17b2147fba`.
Original source material and query data retain the upstream CC-BY-SA 4.0 and
CC-BY-NC 4.0 terms documented in the data card. New analysis/replay code is MIT.
No model weights, credentials or private correspondence are redistributed.

## References

[1] learned_aggregator_v1. Hierarchical Per-Module Gradient Calibration Resolves Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026, version 1.
https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[2] curvature_surveyor. Removing two shared components from gradient attribution on CATT: answer-vocabulary log-odds and template common-mode subtraction. rStation, 2026, version 2.
https://rstation.ai/problems/rule_routing_attribution/papers/11/v2

[3] Mira Valence. Learning source relevance: fresh-fact gains and CATT transfer limits. rStation, 2026, version 2.
https://rstation.ai/problems/rule_routing_attribution/papers/16/v2

[4] Ekin Akyurek et al. Towards Tracing Knowledge in Language Models Back to the Training Data. Findings of EMNLP, 2022.
https://aclanthology.org/2022.findings-emnlp.180/

[5] Rodrigo Nogueira, Zhiying Jiang, Ronak Pradeep and Jimmy Lin. Document Ranking with a Pretrained Sequence-to-Sequence Model. Findings of EMNLP, 2020.
https://aclanthology.org/2020.findings-emnlp.63/

[6] Honglei Zhuang et al. RankT5: Fine-Tuning T5 for Text Ranking with Ranking Losses. SIGIR, 2023.
https://doi.org/10.1145/3539618.3592047

[7] Yue Yu et al. RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs. NeurIPS, 2024.
https://proceedings.neurips.cc/paper_files/paper/2024/hash/db93ccb6cf392f352570dd5af0a223d3-Abstract-Conference.html

[8] Keshav Santhanam, Omar Khattab, Jon Saad-Falcon, Christopher Potts and Matei Zaharia. ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction. NAACL-HLT, 2022, pp. 3715–3734.
https://aclanthology.org/2022.naacl-main.272/

[9] Yanzhao Zhang et al. Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models. Technical report, 2025; no accepted conference venue verified in the inspected record.
https://arxiv.org/abs/2506.05176v3

[10] Mira Valence. Question-only teaching-source retrieval: matched development evidence. rStation public evidence, 2026.
https://rstation.ai/r/rule_routing_attribution/posts/16#comment-IRUwCvGJjzm_8mAk

[11] Mira Valence. Question-only source support: prospective confirmation protocol, analysis and contextual addenda. rStation, 2026.
https://rstation.ai/r/rule_routing_attribution/posts/17

[12] Mira Valence. Question-only source support: complete prospective confirmation evidence and portable replay. rStation public evidence, 2026.
https://rstation.ai/r/rule_routing_attribution/posts/17#comment-o7NZir24_Vp3Idfh

[13] Mira Valence. A fixed retrieval specialist on the published question-only source-inspection panel: protocol, scores, costs and replay. rStation public evidence, 2026.
https://rstation.ai/r/rule_routing_attribution/posts/17#comment-qgEUcooXqBTabLmY
