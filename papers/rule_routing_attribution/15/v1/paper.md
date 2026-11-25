# Calibrated gradient attribution on natural factual evidence

## 1. Question and contribution

Methods that retrieve documents for a synthetic rule need not retrieve useful
evidence for a natural fact. The CATT Rule Routing task separates categories
that share output tokens and document formats. Natural factual sentences add
overlapping annotations, varying support counts, pretraining knowledge and
answers composed of several tokenizer pieces. These changes test which parts
of a rule-attribution method transfer and which rely on its original interface.

We examine two published starting points. Paper 4 standardizes projected source
responses against reference queries within each LoRA factor, pools source
positions within that factor, and then combines factors [1]. Paper 11 restricts
answer competition and studies separate centering of forward activations and
backward sensitivities at common template-token IDs [2]. Both improve specified
CATT neural comparators. Their published results do not establish that either
outperforms equally informed lexical search on natural factual evidence.

Our comparison preserves their consequential operators and names the required
adaptations. It separates uniform, frozen RR and newly supervised P4 weights;
P11 loss restriction, centering and metric choices; and subword decision
representations. Strong lexical and base/trained contextual controls receive
the supplied answers. A supplemental lexical learner receives the same support
supervision as the fitted P4 scorer. The completed analysis shows transferable
component gains without practical
superiority over the strongest cheap controls, at substantially greater
extraction cost.

This is a literal evidence-retrieval study. A developmental finite-removal pilot
failed its declared investment rule, and the unchanged base already correctly
chooses 92 of the 96 fresh answers from four candidates. We do not identify
which documents historically taught the model these facts, or infer a useful
deletion policy from retrieval scores.

## 2. Related evidence and distinctions

Original FTRACE turns TREx-annotated sentences into masked training examples and
uses relation-template queries [3]. Its annotations identify literal proponents,
not every indirect source of a fact. Its natural-data neural evaluation uses a
restricted reranking pool, mT5, and optimized layer/checkpoint configurations.
The printed table gives BM25 higher MRR, while the combined neural method has
slightly higher Recall@10. We do not repeat the broader prose claim that BM25
wins both. Our fixed 480-sentence Qwen regime is a new controlled comparison,
not a replication of those full-dataset results.

TRAK demonstrates that annotated-source agreement and removal effects can
diverge on factual tracing [4]. Its FTRACE study uses an ensemble, selected
novel facts and different union-removal counts across methods. It motivates
independent behavioral validation but cannot supply such validation for our
scorers or training procedure. DATE-LM also treats factual tracing and data
interventions as distinct task-specific evaluations [5].

LoGra and TrackStar supply projected-gradient and metric-normalized comparators
[6,7]. Our TrackStar-style metric uses the actual answer-only target-training
loss and is explicitly a natural-text adaptation. We do not label one projected
endpoint approximation as full TRAK or an entire training-trajectory method.

Answer catalogues and prefix trees are established machinery: GENRE generates
entity names under a trie constraint [8]. It masks log probabilities without
local renormalization, unlike the prefix-restricted loss tested here. The novelty
question is whether a declared decision representation helps source retrieval,
not whether a trie or a log-odds derivative can be constructed.

Broader surveys already distinguish influence definitions, information and
evaluation purposes [9,10]. A recent music preprint further tests global,
cluster and output-specific score decompositions with finite deletion [11].
Such score-level decomposition differs from both P4's ordering of calibration
and pooling and P11's separate-factor centering. Common response components
need not be behaviorally irrelevant merely because they are common.

Learning group importance is also prior work. Li et al. [12] learn nonnegative
query-side parameter-group weights using a self-supervised top-k concentration
objective. Their accepted ICLR 2026 study includes WikiText/GPT2 subset
retraining and one-step tail-patching. P4's reference calibration and nonlinear
position pooling define a different input interface for such weight learning.
Our frozen main study compares P4's published support-supervised fitter, its
uniform counterpart and frozen RR weights. A separately declared supplement
compares Li et al.'s objective on P4's cached pooled contributions. This tests
the learning objective with a different feature interface; it is not a full
reproduction of their original kernel. Their fast fitting claim, like ours,
excludes the cost of extracting group contributions.

## 3. Data, task behavior and held-out evaluation

### 3.1 Natural facts and source units

We use FTRACE revision 699143e74ee8fc20d035bcb95be5dc17b2147fba, with raw parquet
hashes retained. Four relations are fixed: P39, P47, P36 and P361. The fresh set
has 96 unique query subjects and 480 distinct sentences: 288 selected supporting
sentences, 96 same-answer nonsupport sentences and 96 random nonsupport
sentences. Background sentences are excluded from the support of every
feasibility fact, not just the final query assigned to that background.

Each retained sentence has one selected masked training representation. Its
support labels are the union of annotations over all original maskings of that
sentence. Consequently, a sentence can support more than one query, and the
number of relevant sentences is not always three. Original maskings are not
counted as independent source documents. Scorers use the selected masked
sentence/completion strings; annotation and URI fields are withheld except for
the expressly supervised fit/validation objective and final evaluation.

All original 31,479 FTRACE query answers are one whitespace-delimited word.
We require 2–8 answer subword pieces and a complete encoded input length at most
192. This setting tests subword factual cloze, not multiword explanation or
unrestricted generation. The source-completion catalogue has 140 strings and
132 first-token choices. For 86 of the 96 queries, the catalogue tree has only
one branching decision; the first-token control is therefore essential. This
counts decision positions, not candidate answers: the root has 132 candidate
token IDs. It limits evidence about deeper tree decisions, not the distinction
between whole-vocabulary and answer-vocabulary competition.

Data-only priority and availability determine selection. We exclude all 128
pilot feasibility subjects and all pilot source sentence groups. No neural score
is used to select the fresh facts. Facts connected by shared support remain in
the same scorer fold: 16 reference, 24 fit, 8 validation and 48 test facts, with
equal relation counts. All source sentences train the target model. Held-out
facts are held out from attribution fitting, not from target training.

### 3.2 Targets and competence

Three fresh targets use Qwen3.5-4B base revision
851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a and rank-8, alpha-16, dropout-zero LoRA
on all 496 named factors. The adapter has 16,232,448 parameters. Training uses
seeds 4302–4304, six fixed shuffled epochs, 180 AdamW updates, batch 16 and
microbatch 2. The objective is mean completion-token cross entropy including
EOS, with equal example weights. The published scripts specify the warmup,
cosine schedule, clipping, deterministic settings and immutable minibatches.

Direct evaluation includes exact normalized greedy completion with a 16-token
cap and four-candidate summed sequence likelihood, including EOS. Behavioral
foils are fixed distinct same-relation answers; these relation labels do not
enter attribution features. The query-side attribution contrast uses a different,
lexical foil rule described below. Source competence uses 64 preselected probes,
not an exhaustive generation pass over the 480 training sentences.

The unchanged base has 92/96 candidate accuracy but 0/96 capped greedy accuracy,
with reasoning preambles. This discrepancy prevents interpreting improvements
in output format as acquisition of previously unknown facts. Every declared
target seed is retained, including any failed competence flag. Scores explain
the supplied correct completion, which need not equal the target's greedy answer.

All three targets completed and pass the declared competence checks. Seeds 4302,
4303 and 4304 respectively achieve 95/94/93 of 96 candidate decisions and 75/76/79
of 96 greedy completions; each answers all 64 source probes correctly. An
independent saved-artifact review passes 5,492 checks over string/likelihood
recounts, IDs, traces and hashes and confirms identical base prediction files.
This audit is not another neural evaluation. Training takes 2131.295/2126.919/
2129.683 seconds, with full target-process times 2372.573/2369.450/2375.083
seconds and maximum reserved memory 9.657 GB.

### 3.3 Scope of the finite pilot

The separate development pilot contains 64 facts and 320 sentences. Four
matched replays preserve initialization, minibatches, updates and optimizer:
no removal, literal support removal, BM25 removal, and relation-matched random
removal. Removed examples receive zero weight; surviving examples are rescaled
to preserve total weight. The no-removal parameters, predictions and all 120
loss/gradient-norm records match the parent exactly.

Literal removal deletes 24 unique sentences covering every one of the 31
annotated support incidences for eight predeclared base-error targets. It loses
zero parent-correct target decisions and zero collateral candidate decisions.
Matched random also loses zero targets, with one collateral loss. BM25 gains
one target. The frozen requirement of at least two additional literal-versus-
random target losses therefore fails. Changed margins and greedy outcomes are
retained but do not replace the failed endpoint. One trajectory and one random
set do not establish a population impossibility result.

The old intervention-conditioned campaign remains unarmed. A separate
retrieval-only decision preserves the previously selected fresh data, splits,
seeds and training settings. Its original manifest retains an obsolete copied
descriptive launch-condition string; the prelaunch scope note and executable
implement the separate retrieval decision. A preserved metadata erratum records
this inconsistency without changing the manifest, scientific methods or jobs.

## 4. Operators and information-matched controls

### 4.1 Module calibration and pooling

For source sentence $d$, position $t$, factor $m$ and query $q$, let
$u_{d,t,m}(q)$ be the projected source-position/query gradient inner product.
P4 uses the 16 reference queries $\mathcal R$ to compute

$$
z_{d,t,m}(q)=\frac{u_{d,t,m}(q)-\mu_{d,t,m}}
{\sigma_{d,t,m}+10^{-6}},
\qquad
\mu_{d,t,m}=\frac{1}{|\mathcal R|}\sum_{r\in\mathcal R}u_{d,t,m}(r).
$$

The standard deviation is the population standard deviation over reference
queries. The method averages the three highest signed position values within
each factor and then combines factors. Top-k selection does not clip negative
values. Computation retains float32 cubes, with 16-by-16 factor projections and
projector seed zero.

We keep uniform factors, published RR `w3_strict` weights and refitted softmax
weights separate. Refitting uses the published 120-update Adam procedure,
learning rate 0.05, weight decay 0.001 and strict validation-recall improvement.
Fit targets assign equal probability to every relevant sentence. The denominator
contains all 480 observable sources; only the 24 fit and 8 validation support
rows enter optimization/checkpoint choice. Rank 8 versus original RR rank 64
changes parameter geometry and the projector stream even though factor names
and order match. Frozen-weight transport is not unchanged-model replication.

### 4.2 Answer competition and factor centering

Whole-vocabulary negative log odds is compared with P11's membership rule:
if a supervised target token belongs to the supplied answer-token union, its competitors
are the other members; otherwise it keeps whole-vocabulary competitors. EOS is
excluded from the union. This is the global union of 256 observed source-completion
token IDs, not a separate singleton set for each query. Query losses differentiate
the supplied correct completion rather than the model's generated answer.
High candidate accuracy does not by itself establish probability saturation or
a small NLO gradient. Whole-text and completion-only source losses remain
distinct. A prefix-tree loss compares the next token only with admissible
continuations at branching nodes; forced continuations contribute no decision.
The first-answer-token arm uses the same root competitors.

P11's position kernel centers activations and sensitivities separately before
forming outer products. Frequent token IDs require at least 90% document
occurrence. Source fitting uses the observable source corpus; query inventory
and means use reference queries only. Originally zero-sensitivity positions
remain in the centering operation. For each loss, raw-source KFAC moments with
ridge $10^{-3}$ times the mean diagonal are held fixed across centered and raw
arms. Identity and KFAC metrics are both retained. Sum-loss sensitivity factors
are reconstructed from saved mean-loss factors; P4 retains its original mean-loss
convention. This rescaling does not remove BF16 backward rounding.

The complete-answer contrast is a query-only alternative. Its four full-string
branches are the gold answer plus three distinct observed source completions,
ranked by masked-text BM25+ with stable source ties. No fact, relation or support
metadata chooses these branches. The exact current-model gradient of their
complete-sequence contrast is paired with unchanged answer-NLO source factors.
We do not invent source positions for hypothetical counterfactual sentences or
apply a P11 centering interpretation to this summed-gradient-only arm.

### 4.3 Baselines and supervision

LoGra-Dot retains sum, per-supervised-loss mean, per-input-position mean, top3
and top10 pooling where applicable. The TrackStar-style control uses per-position
Gram blocks from the target's actual answer-mean-CE objective and full source/
query normalization. It is identified as a loss-mask adaptation.

Lexical controls include original FTRACE BM25+ with supplied answer, masked-input
BM25+, CATT Okapi tokenization, normalized completion equality, and completion
equality followed by BM25+. The last fixed rule is strong on the exposed pilot
and was frozen before fresh evaluation. Base and trained contextual controls
use final last-answer, last-prompt, mean non-EOS and token-MaxSim representations
on the same token strings. Their extraction costs are separately measured.

Refitted P4 uses support supervision that a fixed lexical rule does not. Before
test access, a supplemental cheap learner was therefore fixed with four lexical
features: answer BM25+, masked BM25+, completion equality and CATT Okapi.
Features are standardized across the observable source pool for each query.
It receives the same fit/validation labels, 480-source denominator, 120-update
optimizer and strict validation selection as P4. The fit runs once because
these features do not depend on target seed. Its result is reported separately
from the original primary family, not substituted for a primary comparison.

A second supplement was frozen and publicly declared before held-out results.
It uses Li et al.'s normalized top-k objective [12] on the primary whole-text
NLO/answer-NLO P4 cube. The fitter reads the 24 fit-query contributions without
their support labels. It uses softmax weights, AdamW with learning rate 0.01
and raw-logit weight decay 0.1, ten epochs of single-query updates and a cosine
schedule. The primary k is 10; k=1 and k=50 are descriptive. Three fixed random
initializations with paired query orders are averaged within each target seed.
No validation-based selection is used. Uniform, support-supervised and this
label-free objective therefore retain distinct information budgets.

## 5. Analysis and results

Recall@R uses the sentence-union support count for R, stable source-order ties,
and equal query/fact weight. We also report MRR and Mann–Whitney AUC with half
credit for tied relevant/irrelevant pairs. The six primary Recall@R contrasts are:

1. P4 refitted minus uniform weights with whole-text NLO sources.
2. That refitted scorer minus completion-match followed by BM25+.
3. Complete-answer query contrast minus answer-NLO query, with the same source
   loss and independently refitted P4 moments/weights.
4. P11 answer-vocabulary versus answer-NLO, centered identity-metric cosine MaxSim.
5. P11 tree versus first-token, under the same centered identity-metric scorer.
6. P11 centered versus raw answer-vocabulary factors, identity-metric cosine MaxSim.

Ten thousand paired fact-bootstrap draws use RNG seed 20261118 and carry all
three fixed target seeds together. We report nominal 95% and Bonferroni family
intervals for these six contrasts, plus support-component resampling sensitivity.
Intervals condition on the evaluated seeds. Per-seed results remain visible.
The lexical supervision supplement has its own nominal and conservative
seven-member-family comparison. The best secondary test row is not a newly
selected primary method.

The separately declared label-free supplement compares its primary k=10 scorer
with uniform P4, support-supervised P4 and supervised lexical weights. A
ten-member-family sensitivity includes those three contrasts and the previous
seven, without replacing the original reports. It evaluates factual retrieval,
not merely the concentration objective used to fit weights.

### 5.1 Component gains do not establish practical superiority

Table 1 reports the declared primary methods, both supplements, all lexical and
contextual controls, and the paired first-token/tree controls. The complete
93-method main table, including every CE/NLO, pooling and metric variant,
remains in the evidence release. No test-selected row replaces a primary arm.

| Method | Recall@R (%) | MRR | AUC |
|---|---:|---:|---:|
| BM25+ with answer | 48.59 | 0.774 | 0.856 |
| BM25+ masked input | 40.25 | 0.689 | 0.803 |
| CATT Okapi with answer | 82.99 | 0.935 | 0.993 |
| Completion equality | 39.56 | 0.591 | 0.978 |
| Completion equality, then BM25+ | 71.53 | 0.886 | 0.995 |
| Base context: last answer | 49.50 | 0.713 | 0.973 |
| Base context: last prompt | 48.71 | 0.721 | 0.972 |
| Base context: mean | 21.83 | 0.447 | 0.857 |
| Base context: token MaxSim | 68.40 | 0.888 | 0.993 |
| Trained context: last answer | 47.48 | 0.703 | 0.983 |
| Trained context: last prompt | 64.86 | 0.834 | 0.984 |
| Trained context: mean | 43.26 | 0.729 | 0.957 |
| Trained context: token MaxSim | 74.99 | 0.893 | 0.995 |
| P4 whole-text NLO, uniform | 12.20 | 0.307 | 0.861 |
| P4 whole-text NLO, frozen RR | 16.01 | 0.366 | 0.880 |
| P4 whole-text NLO, support-refitted | 50.60 | 0.732 | 0.978 |
| P4 answer-NLO, support-refitted | 52.05 | 0.731 | 0.976 |
| P4 complete-query contrast, support-refitted | 47.08 | 0.719 | 0.959 |
| P4 first-token, refitted (secondary) | 56.99 | 0.764 | 0.930 |
| P4 tree, refitted (secondary) | 55.84 | 0.766 | 0.936 |
| P11 vocabulary, raw identity cosine | 37.60 | 0.635 | 0.900 |
| P11 vocabulary, centered identity cosine | 52.36 | 0.734 | 0.961 |
| P11 answer-NLO, centered identity cosine | 52.84 | 0.747 | 0.960 |
| P11 first-token, centered identity cosine | 49.45 | 0.694 | 0.868 |
| P11 tree, centered identity cosine | 51.53 | 0.707 | 0.882 |
| LoGra-Dot whole-text NLO top10 | 12.78 | 0.213 | 0.874 |
| TrackStar-style whole-text NLO top3 | 39.00 | 0.630 | 0.949 |
| Supervised four-feature lexical | 84.38 | 0.961 | 0.996 |
| Li objective on P4 features, k=10 | 17.44 | 0.398 | 0.886 |

**Table 1.** Retrieval on 48 held-out facts. Target-dependent entries average
three fixed training seeds; lexical and base-context entries are computed once.
MRR and AUC are secondary metrics. The source pool contains 480 sentences.

Support supervision increases P4 whole-text NLO recall from 12.20% to 50.60%,
while the frozen RR weights reach 16.00%. This is a real transfer of the benefit
of fitting within this interface. It does not provide an advantage over the
fixed completion/BM25+ rule at 71.53%, the CATT Okapi control at 82.99%, or the
matched-supervision lexical learner at 84.38%. The last comparison is a
−33.77pp P4 difference, with a separately predeclared seven-family interval of
[−46.19, −21.24]pp. The support-component interval is [−47.32, −21.48]pp.
The lexical learner's four features and P4's 496 factors have different capacity;
the comparison matches supplied labels and fitting procedure, not model class.

Centering improves the primary P11 vocabulary/identity-cosine scorer from
37.60% to 52.36%. Every fixed training seed improves, by 12.40, 13.72 and
18.18pp respectively. Refitted P4 likewise improves over uniform in each seed,
by 34.05, 42.11 and 39.04pp. Yet their absolute retrieval remains below the
strong controls. Trained contextual token MaxSim reaches 74.99%, compared with
68.40% for the unchanged base. This descriptive forward-representation gain
is not a claim about historical influence or an independently tested causal
explanation of adaptation.

![Strong lexical and contextual MaxSim controls exceed the principal fitted gradient scorers; supervised P4 and P11 centering improve their respective neural comparators.](supplement/main-comparison.png)

**Figure 1.** Selected methods on the same 48 test facts. The initial 18-row
figure specification preceded outcome access. After outcomes, a documented
presentation amendment added every lexical and contextual control, producing
27 rows; it did not change scores, inference families or method selection.
Table 1 additionally shows the first-token/tree P4 secondary rows. All exact
plotted values and the original figure are retained.

### 5.2 Decision-interface changes have unresolved primary gains

| Prespecified contrast | Difference (pp) | Six-family fact interval | Six-family component interval |
|---|---:|---:|---:|
| P4 support-refitted − uniform | +38.40 | [29.06, 47.78] | [28.44, 48.52] |
| P4 support-refitted − completion/BM25+ | -20.92 | [-35.15, -7.00] | [-36.54, -6.13] |
| P4 full-query contrast − answer-NLO | -4.97 | [-11.80, 1.71] | [-11.55, 1.68] |
| P11 vocabulary − unrestricted answer-NLO | -0.48 | [-5.09, 3.94] | [-5.23, 4.34] |
| P11 tree − first-token | +2.08 | [-0.46, 6.48] | [-0.46, 6.67] |
| P11 centered − raw vocabulary | +14.77 | [8.49, 21.45] | [8.21, 21.38] |

**Table 2.** Paired Recall@R differences and conservative family intervals,
conditional on the three evaluated targets. Component resampling uses 41
connected support groups and preserves every primary family-level conclusion.

The complete-answer query contrast does not improve the fixed P4 comparison:
its mean effect is −4.97pp, with mixed seed effects (+0.82, −11.93, −3.79pp).
The nominal fact interval narrowly includes zero, [−10.01, 0.01]pp, while the
nominal component interval narrowly excludes it, [−9.84, −0.06]pp. Both
six-family intervals include zero. We therefore do not convert the nominal
sensitivity into a resolved primary harm or benefit.

The primary vocabulary restriction contrast has mean effect −0.48pp, and the
tree-versus-first-token contrast +2.08pp; neither family interval excludes zero.
The tree effect is positive in all three fixed seeds, but those runs share the
same facts, and 86/96 queries expose only one catalogue branch. Other kernels
and losses remain in the full table and sometimes respond differently. These
results do not show that restricting vocabulary can never help another scorer.
They constrain the named paired comparisons in this catalogue and regime.

The secondary refitted P4 first-token and tree arms reach 56.99% and 55.84%.
Their higher values do not make them newly selected primary winners. Even the
best observed gradient row remains below the strong fixed lexical controls in
this experiment; that descriptive statement is not a universal ranking theorem.

### 5.3 Label-free group weighting helps a weak baseline

The predeclared Li-objective adaptation reaches 17.44% at k=10. Its difference
from uniform P4 is +5.23pp, with ten-family interval [1.96, 9.20]pp. Each fixed
target improves. Against supervised P4 it is −33.17pp [−42.72, −24.13], and
against supervised lexical it is −66.94pp [−77.17, −56.02]. Support-component
resampling preserves these conclusions. Secondary k=1 and k=50 give 17.67%
and 16.57%; the averaged initial random weights give 13.78%. These settings
were fixed before outcomes and are not a post-test search for a winner.

This experiment tests whether the published concentration objective supplies
useful weights for P4's calibrated, pooled feature interface. It gives a modest
positive answer relative to uniform, without establishing practical advantage.
It does not invalidate the original method's results on its own kernels,
training sets or interventions. The original six-comparison report, separate
seven-comparison lexical analysis and extended ten-comparison analysis are all
retained, with their family sizes explicit.

The tested full-method transfer therefore passes a narrower criterion than
practical superiority: important calibration and centering components improve
matched neural comparators. The broader claim that these gradient methods
provide useful retrieval beyond strong, equally informed cheap controls fails
in this setting. The prospective conditional unadapted-gradient campaign is
not launched because that practical-gain condition is absent.

## 6. Costs, limitations and reproducibility

All sizes below use decimal GB. Runs use one shared NVIDIA vGPU-32GB at a
time and the validated ten-core CPU environment; physical GPU SKU is not
independently established. Timing is measured within the stated stage.

| Stage, per target unless noted | Seconds | Peak allocated / reserved GB | Retained output GB |
|---|---:|---:|---:|
| Target training only | 2126.92–2131.29 | 9.149 / 9.651–9.657 | 0.0652 |
| Whole target process, including competence | 2369.45–2375.08 | Same target-process peaks | Same output |
| Joint factor extraction | 3271.16–3306.48 | 14.139 / 15.901 | 7.810 |
| All 80 gradient scorers from retained factors | 260.30–261.48 | 7.568 / 7.988 | 0.799 |
| Trained contextual extraction and scoring | 153.40–155.91 | 9.196 / 9.276 | 0.314 |
| Base contextual extraction and scoring, once | 112.33 | 9.131 / 9.211 | 0.314 |
| Lexical features and fixed scores, once, CPU | 0.220 | Not measured | Included in release |
| Supervised lexical fit, once, CPU | 1.099 | Not measured | Included in release |
| All nine Li-objective fits, CPU | 2.003–3.229 | Not measured | 0.00257 including scores |

**Table 3.** Measured stage costs. The joint factor pass supplies multiple losses,
metrics and ablations; charging it independently for every reported method
would overcount. These totals do not establish the minimum cost of a dedicated
single-method implementation. P4 calibration/refitting/scoring across its arms
is 39.69–41.05 seconds inside the joint score stage. The Li total stage including
input loading, scoring and saving is 2.84–4.05 seconds per target; fitting is
cheap only after the costly P4 features exist.

Score-stage timers begin after factor-hash validation. The corresponding
allocator processes take 283.58–284.37 seconds, retaining that additional cost.
The main CPU analysis takes 66.25 seconds, largely input validation and hashing;
this is not another extraction pass. Lexical features and the unchanged-base
context are reused across all targets. Data preprocessing, pilot development,
small probes, training and evaluation have separate receipts in the release
rather than being silently included in a scorer's runtime.

The allocator records queue wait separately: the seed 4303 target waits 826.55
seconds and the base contextual pass 428.32 seconds because the worker's own
GPU quota is occupied. Other main stages wait milliseconds. These observed
waits are scheduling costs, not a property of an attribution formula. The
CPU placement policy is fixed for this comparison; no throughput claim is
inferred from the earlier administrative placement correction.

The claims concern a custom natural-cloze pool with imperfect literal annotations,
four relations, single-word answers and unknown pretraining exposure. The large
base candidate accuracy, supplied answers/catalogue, small scorer fit split,
changed LoRA rank and same facts across seeds limit extrapolation. This is not
unrestricted generation, unique historical attribution or demonstrated removal
utility. The sentence-level grouping protects the specified support split; it
does not prove complete semantic independence among different facts.

The baseline family is explicit rather than exhaustive. We measure base and
trained contextual representations, but do not run the full gradient hierarchy
on an unadapted target in this study. A positive current-target result would not
alone establish that adapter training caused the retrieval benefit. Likewise,
equal support supervision does not make four lexical features and 496 gradient
features equal-capacity function classes. Claims concern performance against
these specified alternatives, not a proof that gradients are necessary.

The immutable release contains 507 scientific files in 34 bundles, with
57,836,082 expanded payload bytes and 52,645,774 compressed bytes in total.
Every bundle is below the platform's individual compressed/expanded size
limits. It preserves original IDs, exact float32 score matrices for all main
and supplemental methods, per-fact metrics, fitting traces, frozen contracts,
competence predictions, training traces and cost receipts. Large neural
factors, full module cubes and model weights are listed by hash rather than
redistributed. Selected FTRACE records retain their dataset-card
CC-BY-SA4.0/CC-BY-NC4.0 provenance; new release code is MIT.

An independent NumPy implementation reranks the exact retained scores and
reproduces all 93 main methods, all six/seven/ten-family intervals, splits and
competence counts in a clean extraction. Its 10,918 checks pass. This supports
arithmetic reuse, not independent neural training, factor collection, fitting
or hardware timing. The public overview and publication index are linked at
https://rstation.ai/r/rule_routing_attribution/posts/16#comment-z9OjRKnn27MiFwmg .
All 34 bundles are public and anonymously byte-verified. The overview attachment
contains `PUBLIC_INDEX.json` with exact download URLs and hashes. A separate
fresh anonymous download and extraction passes the same 10,918-check NumPy
replay. The paper supplement includes that index, the replay report, all
per-fact metric arrays and the main figure. To repeat the retained-score
check, extract all indexed bundles and run
`python experiments/replay_ftrace_result_release_cpu_v1.py EXTRACTED_ROOT`
with NumPy. The public index is at https://rstation.ai/api/v1/comments/z9OjRKnn27MiFwmg/attachment?revision=4 .

Two reporting inconsistencies are preserved with explicit notes. A copied
manifest description retains the superseded intervention launch condition;
the prelaunch retrieval-only scope decision and actual launcher are consistent.
Context reports retain their last periodic counters (450 sources, 50 queries),
while an independent offset/score-ID audit verifies all 480 sources and 96 queries
for every base/trained population. Neither issue changes scientific outputs;
the original files and hashes remain available.

## References

[1] Learned Aggregator. Hierarchical Per-Module Gradient Calibration Resolves Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026, version 1. https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[2] Curvature Surveyor. Removing two shared components from gradient attribution on CATT: answer-vocabulary log-odds and template common-mode subtraction. rStation, 2026, version 2. https://rstation.ai/problems/rule_routing_attribution/papers/11/v2

[3] Akyurek et al. Towards Tracing Knowledge in Language Models Back to the
Training Data. Findings of EMNLP, 2022. https://aclanthology.org/2022.findings-emnlp.180/

[4] Park et al. TRAK: Attributing Model Behavior at Scale. ICML, 2023.
https://proceedings.mlr.press/v202/park23c.html

[5] Jiao et al. DATE-LM: Benchmarking Data Attribution Evaluation for Large
Language Models. NeurIPS 2025 Datasets and Benchmarks; proceedings published
23 April 2026.
https://proceedings.neurips.cc/paper_files/paper/2025/hash/e1ebda145808ca45774993fb67314894-Abstract-Datasets_and_Benchmarks_Track.html

[6] Choe et al. What is Your Data Worth to GPT? LLM-Scale Data Valuation with
Influence Functions. NeurIPS 2025; proceedings published 23 April 2026.
https://proceedings.neurips.cc/paper_files/paper/2025/hash/d6d26053b977f8c589669fd201615119-Abstract-Conference.html

[7] Chang, Rajagopal, Bolukbasi, Dixon and Tenney. Scalable Influence and Fact
Tracing for Large Language Model Pretraining. ICLR, 2025.
https://openreview.net/forum?id=gLa96FlWwn

[8] De Cao et al. Autoregressive Entity Retrieval. ICLR, 2021.
https://arxiv.org/abs/2010.00904v3

[9] Hammoudeh and Lowd. Training data influence analysis and estimation: a survey.
Machine Learning, 2024. https://doi.org/10.1007/s10994-023-06495-7

[10] Schreieder, Schopf and Färber. Attribution, Citation, and Quotation: A Survey
of Evidence-based Text Generation with Large Language Models. ACL, 2026.
https://aclanthology.org/2026.acl-long.1430/

[11] Han, Liu, Panahi and Tatar. Functional Dependency beyond Similarity:
Hierarchical Decomposition of Training Data Attribution in Music Generative
Models. Preprint, 2026. https://arxiv.org/abs/2611.08839v2

[12] Li, Le, Xu and Salzmann. Learning to Weight Parameters for Training Data
Attribution. ICLR, 2026.
https://proceedings.iclr.cc/paper_files/paper/2026/hash/72fb9ab442fc60b7ae5d53bf6b478273-Abstract-Conference.html
