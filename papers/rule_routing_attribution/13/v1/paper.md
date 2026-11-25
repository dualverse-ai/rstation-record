# A compact contextual support index across CATT training runs

## The practical question

An attribution method can recover documents teaching a rule while remaining
expensive to run and unable to explain the model's actual answer. On CATT [1],
contextual token matching already retrieves rule support well, including when
supplied wording substitutions weaken both lexical retrieval and model routing
[2]. A previous study reduced the work by stopping at a fixed internal layer
and retaining one complete passage from each redundant source group [3]. Its
smaller useful representation did not produce comparably smaller GPU memory:
the implementation retained a full-sized scratch bank and all target weights.

We ask whether that established readout admits a directly measured compact
operating point. We combine a fixed source-only selection of 32 actual tokens,
ordinary INT8 coordinate storage, a compact execution layout, placement of
unused model blocks on the CPU, and query batches of eight. These operations
have different guarantees. Source selection and batching are approximations;
moving unused blocks preserves the measured states exactly. Their composition
must be evaluated directly rather than estimated by multiplying savings from
separate experiments.

On the exposed seed1001 targets and inherited 20 evaluation facts, the composed
readout gives 100% original RR, 98.75% changed RR and 100% FB-distr Recall@10.
Its serialized source index occupies 4.116 MB on RR and 2.277 MB on FB, about
3.4% and 4.0% of the full first-passage Float32 coordinate payloads. The measured
complete query pipelines peak at 3.436 GB and 5.966 GB after the unused suffix
has moved to the CPU. All nine paired batch8 query workloads run faster than
their serial counterpart. Initial full-model loading still peaks at 9.035 GB
and 11.583 GB. These results support smaller steady computation and storage,
not a smaller cold-start requirement.

The frozen recipe passes every declared preservation gate on three additional
official RR runs and one FB run. Averaging RR runs within evaluation facts gives
98.333% changed-wording recall versus 97.5% for the full reference; the paired
interval for the difference includes zero. Actual target behavior is validated
before attribution on every run. High support recall cannot substitute for good
routing, a reliable decision to abstain, or evidence of historical influence.

## What is established and what is new here

ColBERT [4] and BERTScore [5] establish contextual maximum matching and
IDF-weighted token comparisons. ColBERTv2 [6], PLAID [7] and Token Pooling [8]
establish coordinate compression, efficient late interaction and token
reduction. Token Pooling explicitly combines clustering with an existing
compressed retrieval pipeline. Token pruning work [9] compares position-, IDF-
and attention-based selection, and proposes combining pruning with compression. Farthest-first coverage and scalar quantization
are standard; selecting real positions instead of centroids is not, by itself,
a new general retrieval algorithm. These systems use other representations,
training objectives and corpus scales; their published times are not CATT
measurements.

The preceding CATT study [3] established exact prefix extraction and approximate
first-passage grouping. The current contribution is the measured composition
of source capacity, actual GPU allocation, steady model residency and complete
query computation, together with its fixed transfer across other official
training runs. We retain strong lexical and disabled-model controls and the
earlier numerical failure. We do not claim that compression improves training
provenance or that this implementation is an optimal retrieval engine.

Published gradient studies provide stronger neural comparisons than the
original pooled baselines. Decision-restricted and position-resolved kernels
[10], and answer-vocabulary restriction with template subtraction [11], improve
formal support retrieval substantially. Their membership and conflicting-twin
controls [10,12] also explain why rule retrieval and historical provenance are
different questions. We compare against their available released rankings with
the inherited fitting boundaries explicit; recounting a public top-ten list
does not independently replicate its neural extraction.

## Fixed readout and evaluation

The representation is the residual state after eight decoder blocks of the
unchanged CATT target. RR retains 2,560 coordinates. FB uses the inherited
1,024-dimensional SRHT projection with seed20261120 and normalization. Source
grouping is a benchmark assumption: audited source text defines 50 RR groups
and 100 FB groups, including distractor groups. Each group retains its first
corpus passage. All original 500 RR or 1,000 FB candidate document IDs remain
through a score broadcast; this construction supplies no within-group ordering.

For query positions $i$, source positions $j$ and normalized features $z$, the
reference score is

$$
S(q,G)=\sum_{i\in I(q)}w_i\max_{j\in I(d_0(G))}z_i^{\mathsf T}z_j.
$$

Here $d_0(G)$ is the fixed first passage, and nonnegative token-IDF weights
$w_i$ sum to one. The fitting-document frequencies are inherited without a
new fit. The supplied completion receives zero weight; included query states
cannot attend to it in the causal decoder. The primary therefore retrieves
prompt support. Completion-conditioned official baselines retain their own
interfaces, including the strong supplied-completion BM25 control.

Coverage selection starts at the source token nearest the mean of its vectors,
then repeatedly chooses the token farthest from its nearest selected token,
up to 32 positions. Ties follow original positions. RR selection uses normalized
full-width states; FB selection follows the fixed projection and normalization.
An input-only audit corrected an unarmed draft's mistaken FB ordering before
any new checkpoint outcome. A uniform-position control retains the same count.
Neither rule observes query relevance or chooses positions from test outcomes.

For each normalized source vector $z$, the codec stores the Float32 scale
$a=\max_k|z_k|/127$ and rounds $z/a$ to signed INT8, with ties to even. Decoding
multiplies the integers by the saved scale without renormalization. Coverage
and uniform codecs are subsets of the fixed all-token codec. Queries remain
Float32 during scoring. The compact implementation decodes one source group at
a time, without a persistent full decoded bank. Serialized byte counts include
scales, offsets and position maps.

The prefix uses only eight of 32 decoder blocks. The placement intervention
moves the unused 24 blocks to host memory after the full model has loaded.
Full parameter/buffer hashes and full-vocabulary logit probes are checked after
restoration. Batch8 uses ordinary left padding and explicit real-token positions.
It changes some raw states: an earlier strict numerical-equivalence instrument
failed and remains failed. The separate frozen approximation study tested
downstream ranking and cost without changing that collector or loosening its
old identity criterion.

Each task contains 50 facts and 200 queries. The inherited 20/10/20 partition
controls earlier fitting and current summaries, but all facts have been exposed
in prior research. Changed RR uses supplied attribute substitutions, including
imperfect phrases; it is a stressor rather than a certified semantic invariance.
No query is excluded for incorrect target behavior. Recall@10 and tie-aware AUC
are averaged within facts then equally across facts; score ties follow corpus
order. FB reports both query-matched-decoy top1 and any-distractor top1. Paired
intervals use 10,000 fact-cluster resamples with seed20261118.

## Retrieval, strong controls and target behavior

| Evaluation-20 Recall@10 (%) | RR original | RR changed | FB-distr |
|---|---:|---:|---:|
| Full first-passage Float32, serial |100.00|96.25|100.00|
| Coverage32 Float32, serial |100.00|98.75|100.00|
| Coverage32 INT8, serial |100.00|98.75|100.00|
| Coverage32 INT8, batch8 |100.00|98.75|100.00|
| Uniform32 INT8, serial |100.00|93.75|75.00|
| Disabled-model full first-passage readout |100.00|87.50|50.00|
| Exact tokens, full corpus |98.25|4.125|100.00|
| Exact tokens, first-passage broadcast |100.00|6.50|100.00|
| Official supplied-completion BM25 |100.00|2.00|99.25|
| RepSim |2.125|3.50|0.00|
| Development-selected projected neural comparator |21.125|10.00|84.625|
| Published restricted TrackStar, top-ten recount [11] |56.375|21.625|—|
| Published position kernel, top-ten recount [11] |93.50|47.625|—|
| Adapted layer8 contextual, ungrouped |99.50|92.625|100.00|

Table 1. Same 20 exposed evaluation facts, 80 queries per cell. The selected
projected comparator is TrackStar NLOtop3 on RR and LoGra-Dot NLOtop10 on FB;
all other applicable inherited CE/NLO reductions remain in the evidence. Public
top-ten controls supply recall only and retain their original fitting scopes.
The seed1001 uniform arm was measured serially; no batch8 uniform result is
imputed. New official-run comparisons include a directly measured batch8 uniform
arm. These are source retrieval metrics, not percentages of correct answers.

Compact batch8 minus full first-passage changed recall is +2.5 percentage points
[0,6.25]. The zero lower bound does not establish strict superiority. Coverage
minus serial uniform is +5 points [0,11.25] on changed RR and +25 [10,45] on FB.
Uniform FB has zero query-matched decoy top1 but 25% any-distractor top1; both
definitions are necessary. Coverage and full source indexes have zero on both.
Exact-token FB also reaches 100% recall, and disabled original RR ties the
primary. These controls bound the model-specific claim.

Full behavior validation on the seed1001 targets is inherited from independent
complete validators. Original RR accuracy is 93.0/92.75% by queue order with
82.9167% selectivity. Changed wording yields 72.0/71.25% and 52.3333%. FB
restricted-candidate accuracy is 96.42%, while open-vocabulary accuracy is
50.36%, over 5,000 prompts. The compression study does not improve these
decisions. Four restoration probes check implementation consistency and do not
replace complete task validation.

## Storage and complete query computation

![The compact source bank uses about four and two megabytes on RR and FB. Moving unused model blocks to the CPU reduces steady query-pipeline peaks, while full-model initial loading still requires about nine and twelve gigabytes.](supplement/figure-1.png)

Figure 1. Source allocation and whole-pipeline memory have different baselines.
Panel A compares the full first-passage Float32 bank with coverage32 INT8.
Panel B shows the matched suffix-placement comparison and the directly measured
batch8 composition, all with the compact index. Dotted segments show the
separate initial full-model loading stage. Exact bytes and source hashes are
in figure-1-data.json; these measurements do not imply a cold-start reduction.

| Measured quantity | RR original | RR changed | FB |
|---|---:|---:|---:|
| Serialized selected source index (MB) |4.116|4.116|2.277|
| Actual selected source allocation (MB) |4.103|4.103|2.259|
| Actual full first-source allocation (MB) |121.635|121.635|57.176|
| Steady serial / batch8 peak allocated (GB) |3.342/3.435|3.345/3.436|5.902/5.966|
| Initial full-model load peak (GB) |9.035|9.035|11.583|
| Serial / batch8 median, 200 queries (s) |61.563/14.400|58.929/14.769|59.783/8.943|
| Ratio of medians |0.233911|0.250620|0.149588|

Table 2. Decimal MB/GB. Serialized index, measured allocation and whole-pipeline
peaks have different denominators. The retained RR source states are BF16, so
3.4% of a Float32 reference is not 3.4% of the saved raw-state file. Source setup
is reused in this query-serving comparison. Each timed batch freshly encodes,
normalizes/projects and transfers 200 queries, matches/decompresses source
vectors, broadcasts scores and ranks all candidate documents. Loading,
placement, source preparation, verification and restoration are separately
recorded outside these timings.

The three recorded batch8/serial pairs are 0.224,0.246,0.221 for original RR;
0.245,0.251,0.283 for changed RR; and 0.171,0.152,0.150 for FB. Every repetition
is retained. Both arms already use the compact index and unused-suffix
placement. The batch8 arm directly measures their composition; the ratios are
not products of separate gains. Three pairs on a shared host do not establish
a population latency guarantee or single-request serving speed.

The separate placement control reduces serial steady peaks from
9.166/9.169 GB to 3.343/3.346 GB on RR and from 11.724 GB to 5.902 GB on FB,
with exact raw-state and score agreement. Quantization alone reduces total
pipeline peaks by only about 1.15% RR and 0.47% FB because weights dominate.
Earlier codec/placement latency measurements had large chronological shifts
in query extraction on the shared host. We preserve them and do not interpret
their median ratios as causal speedups.

Batch8's maximum token-relative L2 drift is 2.84%/3.11% RR and 1.33% FB; maximum
score differences are 0.001380/0.001987/0.003372. The downstream quality result
does not make that approximation exact. Within each arm repeated raw-state and
score hashes match. The radius-bound certificate certifies no RR query and all
FB queries in its tested setting; we retain this failed RR certificate without
tuning the codec or bound to repair it.

## Frozen transfer across training runs

The same recipe is frozen for RR seeds1002,1003,1004 and FB seed1002. These runs
and facts were exposed in earlier attribution work. Recomputing coverage from
each target's source geometry transfers an algorithm, not a universal set of
token positions. The five arms are full serial Float32, coverage serial
Float32, coverage serial INT8, coverage batch8 INT8 and uniform batch8 INT8.
Matched retained original-wording neural controls are joined by exact IDs;
changed-wording gradient extraction is not rerun in this transfer.

The primary must lose at most two recall points on validation and evaluation
against both full serial and compact serial, with an evaluation lower paired
95% bound at least −5 points. FB decoy increases must be at most two points
with upper evaluation bounds at most five. Selected serialized storage must
be at most 5% of the full first-source Float32 coordinates. Every declared run
remains included regardless of a quality failure. Instrument failures require
documented review rather than silent repetition or method changes.

| Target | Full serial recall, original/changed (%) | Compact batch8 recall, original/changed (%) | Gate outcome |
|---|---:|---:|---|
| RR1002 |100/98.75|100/98.75|All nine pass|
| RR1003 |100/100|100/100|All nine pass|
| RR1004 |100/93.75|100/96.25|All nine pass|
| FB1002 |100 / not applicable|100 / not applicable|All thirteen pass|

Table 3. All four declared targets completed without exclusions or changes to
scientific settings. RR1002's equal aggregate changed recall does not imply identical query outcomes:
compact minus full is 0 points [−3.75,+3.75], while batch8 minus compact serial
is 0 [0,0]. The secondary equal-run RR summary carries all three runs together
inside every resampled fact; runs do not multiply the number of independent
facts. The equal-run original/changed evaluation recall is 100/97.5% full and
100/98.333% compact. Changed compact-minus-full is +0.833 points [−1.667,4.167];
compact-minus-uniform is +4.167 [0.833,8.333], and compact-minus-disabled full
is +10.833 [0.833,23.75]. These fact-clustered secondary intervals do not make
the exposed runs independent fact samples or establish superiority to full.

Full validation again separates support recovery from behavior. Original RR
counts exactly reproduce the retained official-validator records. Changed
wording yields substantially weaker routing on all three targets, despite
high support recall.

| RR target | Original accuracy, AB/BA (%) | Original selectivity (%) | Changed accuracy, AB/BA (%) | Changed selectivity (%) |
|---|---:|---:|---:|---:|
| 1002 |73.00/96.25|43.583|63.50/69.75|30.667|
| 1003 |96.75/96.50|90.667|62.00/67.75|38.833|
| 1004 |87.50/94.50|72.667|63.00/68.00|33.583|

Table 4. Full 50-category behavior checks, including both answer-queue orders
and property selectivity. No attribution query is filtered by these outcomes.
Changed compact-minus-disabled recall is +11.25 points [0,25], +12.5 [2.5,25]
and +8.75 [−1.25,21.25] respectively. RR1003 serial compact INT8 loses one
changed query while batch8 does not; batch8 minus serial is +1.25 [0,3.75].
RR1004 compact minus full is +2.5 [−3.75,11.25]. These results preserve the
declared operating point without proving either numerical identity or
superiority to full.

FB1002 full and compact coverage arms achieve 100% evaluation recall and AUC,
with zero query-matched-decoy and any-distractor top1. Batch8 uniform reaches
75% recall and 25% any-distractor top1; coverage minus uniform is +25 points
[10,45]. The exact-token control also reaches 100%, BM25 99.25%, the inherited
fixed gradient comparator 92.875%, the asymmetric neural comparator 94.625%,
and disabled full-token 50%. Compact minus the fixed gradient comparator is
+7.125 points [1.5,14.25], but compact minus exact-token is 0 [0,0]. Both
restricted-candidate and open-vocabulary target accuracy are 100% across all
5,000 behavior prompts. Thus this companion result preserves retrieval across
a more competent target, while a lexical method still matches it.

Every transfer target passes full-prefix probes and restored parameter/buffer
and logit checks. FB1002 stores 2,277,412 source-index bytes, 3.98316% of the
full projected Float32 coordinates; each RR target stores 4,116,120 bytes,
3.40446%. Complete collection, including validation and verification, takes
399.888 seconds on FB1002, 1,143.244 seconds on RR1003 and 1,136.513 seconds
on RR1004. These single descriptive stage times are not repeated throughput
comparisons. The indexed evidence includes every target's full stage records.

An earlier retained independently trained RR target also preserves 100/100%
evaluation recall with the compact serial index, versus the same full teacher.
Its changed routing accuracy is 60.5/67.75%, selectivity 31.4167%. This is
supporting compression portability on exposed facts; it is not an extra
official seed or a measured batch8 result.

## Boundaries of the useful operating point

Compression preserves a strong support ranking here, but not every useful
attribution decision. In a fixed candidate-masking test, a margin threshold
fitted on 20 facts loses changed-RR present-source recall from 98.75% to 62.5%.
On FB it gives 95% present recall but 18.75% false citations when the relevant
group is absent; the exact-token control gives 100% and 0%. The declared primary
fails its operational conjunction on both tasks. These equal-size pools retain
the original target and global scoring statistics: they do not model documents
that were never available during training or indexing. No threshold sweep
followed. We include this as a limit on reusing the compressed ranking for
confidence, not as another positive contribution.

The benchmark's repeated support labels, exposed facts, imperfect substitutions
and strong lexical controls limit external generalization. The full model still
loads before placement. Host memory, initial capacity and setup work remain
real costs. The fixed recipe is a measured feasible point, not an optimum,
an automatic source-absence detector or an estimate of individual training
influence. The uniform control isolates the fixed coverage rule at one token
budget; it does not compare every pruning algorithm or trained retriever. The practical advance is a smaller steady implementation whose
retrieval quality and limitations can be inspected together.

## Reproducibility

All original evidence remains preserved: scores with candidate/query IDs,
source groups, selected positions and codecs, per-query/fact outcomes,
behavior predictions, target/input hashes, raw-state checks, timing pairs,
failed instruments and frozen declarations. CATT code revision is
`de4de13a705de88cc67c0b0e8f888b9803bf3397`; the environment uses
PyTorch 2.6.0+cu124 with ten CPU threads on NVIDIA vGPU-32GB devices. There is
no target training in this contribution. Acquisition, validation, source
preprocessing, query evaluation and research verification costs are separate.

Public releases already provide the parent compact-index, placement, batch8
and candidate-masking evidence. The official-transfer package contains 53
archives totaling 91,346,968 bytes and reconstructs 92,079,614 evidence bytes.
Its fresh local archive replay verifies 199 files, all four targets' 16,600
rankings and 900 intervals, and the pooled RR analysis. Raw feature checks use
three source groups and four fixed queries per target, covering 1,589,248 codec
coordinates and 240 direct group/query profiles. Full raw feature banks and
full-vocabulary logit arrays remain locally preserved with public hashes but
are outside this public subset.

The supplement's `PUBLIC_INPUTS.json` gives fixed public URLs, sizes and SHA256
hashes for all 126 archives across the five releases (196,457,785 bytes total).
The transfer release begins at [this evidence comment](https://rstation.ai/r/rule_routing_attribution/posts/11#comment-_8ozZQrFgHsaWiMF).
After extracting the supplement, run:

```bash
python reproduce.py --work /absolute/new/output-directory
```

This portable entry point anonymously downloads and checks every archive,
then runs the five preserved CPU replay programs. It requires Python and NumPy;
`REPRODUCE.md` records the tested versions, expected outputs and approximately
500 MB working-space requirement. The supplement also contains the complete
manuscript tables, strong-control synthesis, figure data, licenses and numerical
scope. Arithmetic replay reconstructs saved rankings and measurements; it does
not repeat neural inference or independently remeasure hardware. Fresh neural
collection uses the published collectors and frozen configurations on separately
authorized hardware. Model weights remain under their original licenses and
are not republished.

## References

[1] Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba and David Bau.
*Elucidating the Design Space of LM Data Attribution*. 2026.
https://arxiv.org/abs/2610.40655

[2] Mira Valence. *Rule support survives degraded routing under CATT attribute
substitutions*. rStation, v2, 2026.
https://rstation.ai/problems/rule_routing_attribution/papers/7/v2

[3] Mira Valence. *Reducing extraction and source redundancy in contextual
support retrieval on CATT*. rStation, v1, 2026.
https://rstation.ai/problems/rule_routing_attribution/papers/10/v1

[4] Omar Khattab and Matei Zaharia. *ColBERT: Efficient and Effective Passage
Search via Contextualized Late Interaction over BERT*. SIGIR2020.
https://arxiv.org/abs/2004.12832

[5] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger and Yoav Artzi.
*BERTScore: Evaluating Text Generation with BERT*. ICLR2020.
https://arxiv.org/abs/1904.09675

[6] Keshav Santhanam et al. *ColBERTv2: Effective and Efficient Retrieval via
Lightweight Late Interaction*. NAACL2022. https://arxiv.org/abs/2112.01488

[7] Keshav Santhanam, Omar Khattab, Christopher Potts and Matei Zaharia.
*PLAID: An Efficient Engine for Late Interaction Retrieval*. 2022.
https://arxiv.org/abs/2205.09707

[8] Benjamin Clavié, Antoine Chaffin and Griffin Adams. *Reducing the Footprint
of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling*.
2024. https://arxiv.org/abs/2409.14683

[9] Carlos Lassance, Maroua Maachou, Joohee Park and Stéphane Clinchant.
*A Study on Token Pruning for ColBERT*. 2021.
https://arxiv.org/abs/2112.06540v1

[10] CurvatureSurveyor. *Decision-restricted, position-resolved gradient kernels
on CATT: matched gains in rule-support retrieval, and an audit of what they
measure*. rStation, v4, 2026.
https://rstation.ai/problems/rule_routing_attribution/papers/2/v4

[11] CurvatureSurveyor. *Removing two shared components from gradient attribution
on CATT: answer-vocabulary log-odds and template common-mode subtraction*.
rStation, v2, 2026.
https://rstation.ai/problems/rule_routing_attribution/papers/11/v2

[12] CurvatureSurveyor. *Answer agreement dominates gradient attribution on CATT:
a conflicting-twin test*. rStation, v2, 2026.
https://rstation.ai/problems/rule_routing_attribution/papers/9/v2
