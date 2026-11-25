# Reusing trusted information can outperform preference-label audits

## 1. Problem and contribution

A data-attribution score can rank useful sources without identifying the best
way to improve a model. This distinction matters when attribution is used to
allocate an annotation budget. The information used to decide which labels to
audit may also support a cheaper change to the training rule. A comparison that
omits that alternative can overstate the practical value of the audit policy.

We study this issue for human-preference data. The starting ideas are hierarchical
query-reference calibration [1] and decision-restricted attribution [2], two
methods with strong neural support-retrieval results on CATT. We adapt selected
components to a frozen language-model representation and a convex reward head,
where the entire head Hessian can be computed and every finite repair can be
certified. This deliberately removes uncertainty about approximate curvature
without claiming to reproduce the original module/token hierarchy or its CATT
retrieval task.

The study has three linked results. First, exact label-replacement sensitivity
and its reference-normalized variants improve on random audits but do not beat
an equally informed source-error observer. Second, known-channel loss correction
and observer soft-label training use the same available information without
audits and produce stronger models. Third, a separately frozen evaluation on
2,048 new prompt families confirms that both training controls outperform three
finite-audit alternatives in balanced preference accuracy. Soft-label training
improves over observer-guided audits by 3.413 percentage points, with simultaneous
95% interval [2.015, 4.821] after adjustment for all nine main and supplemental
comparisons.

The contribution is a controlled comparison of alternative uses of trusted
information in a preference-learning workflow. It establishes an empirical
applicability boundary for the tested audit policies; the loss-correction
algorithms and the general distinction between detection and utility are prior
work. Exact local sensitivity does not
establish finite audit utility; information budgets must include alternative
training uses of the trusted labels, observer and noise model. The result is
limited to short preference pairs, one frozen backbone, a known synthetic noise
channel and perfect audits. It does not imply that attribution never improves
repair, that the original CATT methods fail, or that reward-head accuracy
establishes generation quality.

## 2. Relation to prior work

P4 [1] standardizes source-position/module responses across reference queries
before nonlinear token pooling and module aggregation. Its learned weights and
hierarchical ordering are important parts of its CATT method. P11 [2] studies
answer-vocabulary restriction, position-resolved comparisons and separately
defined template subtraction. Complete-response pair ranking has neither the
original one-token answer set nor shared synthetic template positions. Our
experiments therefore isolate reference scaling/centering and explicit binary
decision scope; they are not an unchanged transfer of either full method.

Label replacement through inverse-Hessian gradient differences is established
by Koh and Liang [3], who also evaluate perfect-label auditing and actual
retraining on Enron1. Active label cleaning [4] distinguishes annotation quality
from predictive utility and allows sequential selector updates. Neither that
distinction nor a finite repair experiment is our generic novelty. Our earlier
sentiment study [5] found that a calibration-dependent detection gain did not
produce better Qwen LoRA repairs. The present work changes the task, training
regime and decisive control: it uses complete-response preferences, exact convex
head curvature, eight additional corruption realizations, and a fresh comparison
against training methods that spend no audits.

Patrini et al. [6] derive backward and forward correction for known or estimated
label-noise transitions. Our backward control instantiates their known-transition
principle. Robust DPO [7] studies symmetric preference corruption; its symmetric
channel assumptions differ from our directional length corruption, whose
transition remains invertible even when the conditional flip probability exceeds
one half. The general DPO objective [8] optimizes policy/reference sequence
likelihood ratios. Our failed DPO entry experiment and successful frozen-head
entry are different training regimes, not interchangeable measurements of the
same model.

Work on human-feedback influence [9] uses compressed influence estimates and
targeted validation to study preference bias, including selected-label flipping
and retraining. Its targeted validation tradeoffs and blind flipping of selected
labels differ from our perfect audits followed by untouched query evaluation.
DATE-LM [10] motivates application-specific inexpensive controls and distinguishes
source-ranking proxies from practical interventions. These precedents motivate
our question: do the tested attribution components add value over equally
informed alternatives in this particular preference workflow?

## 3. Data, information and model entry

We use the `helpful-base` subset of Anthropic HH-RLHF [11], revision
`09be8c5bbc57cb3887f3a9732ad6aa7ec602a1fa`. We parse pairs at the final shared
assistant boundary and group them by normalized initial human turn. All groups
appearing in the original test partition are excluded from training before
sampling. Each selected group contributes one pair. Each full prompt-plus-response
sequence, including EOS, must fit within 192 tokens; no sequence is truncated. We require
at least four response tokens before EOS and an exact prompt-token prefix.

The initial split has 1,280 sources, 128 calibration pairs, 128 reference pairs,
128 development pairs and 1,024 original-test pairs. Pair and group priorities
are deterministic hashes. Exactly half the alternatives in each split are
swapped so option position does not identify the human-preferred response.
These are fallible human preference labels, not an objective judge of all
response qualities. Evaluations compare deterministic predictions to those
labels; an LLM judge is not used.

For each corruption realization, we randomly permute the 439 source pairs whose
preferred response is shorter, and flip exactly the first 256 to prefer the
longer response. This is sampling without replacement, not independent noise
across sources. The original realizations use seeds 4201 and 4202; eight later
draws use 4203–4210. Every method receives the corruption direction and count.
The 183 observed-shorter sources plus the known 256 flips identify the original
439 shorter-preferred sources in aggregate. Hence the marginal channel rate is
$c=256/439$, and all corruptions lie within the 1,082 observed-longer sources.
Equal-length sources are never corrupted.

An initial Qwen3.5-4B rank-eight LoRA DPO experiment fails a predeclared investment
gate. Clean balanced development accuracy is 58.382/55.221%, versus noisy
57.794/55.956%; the mean clean-minus-noisy gap is −0.074 points, below the
required positive five-point headroom. Source fitting and basic competence pass,
and clean loss is lower, but these facts do not rescue the accuracy gate. We
close that attribution recipe without a gradient or repair campaign. Its costs
and development evidence remain public.

We then declare a separate frozen-backbone regime using Qwen3.5-4B [12]. Each
response is represented by its final EOS hidden state. The feature vector is
the difference between option-1 and option-0 states, divided coordinatewise by
the source-only RMS. A shared linear reward head has 2,560 parameters and no
intercept. For source labels $y_i$ and vectors $x_i$, it minimizes

$$
J(w)=\frac1n\sum_{i=1}^{n}
\left[\log(1+\exp(x_i^\top w))-y_i x_i^\top w\right]
+\frac{\lambda}{2n}\|w\|^2.
$$

The positive ridge makes this objective strictly convex. Each of the one clean
and two original noisy heads chooses $\lambda$ from $\{1,10,100,1000\}$ using
the 128 calibration labels. All select 1000. Clean development accuracy is
72.656% overall and 65.441% balanced; noisy accuracy is 71.875/60.882% and
67.188/54.632%. The separately declared entry criteria pass, with mean balanced
headroom 7.684 points. This is one deterministic clean optimum and two noise
realizations, not two independently trained backbones.

Balanced accuracy assigns equal weight to shorter-preferred and longer-preferred
pairs. Equal-length pairs enter overall accuracy only. Balanced reference loss
uses the corresponding equal-stratum weighting. The noise mechanism makes both
overall and balanced outcomes important: correcting a directional preference
can improve one while harming the other.


The comparison holds available information fixed, rather than requiring every
policy to use it in the same way. Before an audit, all policies can use the
1,280 observed source pairs, 128 calibration labels, 128 reference labels,
known corruption direction and count, frozen feature representation and the
same observer. Only the declared audit operation reveals additional source
labels. The following table makes the alternatives explicit.

| Workflow | Use of the available information | Additional audited labels | Training action |
|---|---|---:|---|
| Observer audit | Rank eligible sources by the observer's error proxy | 128 | Correct discovered errors, then refit |
| Attribution audit | Combine that same error proxy with a reference-loss response | 128 | Correct discovered errors, then refit |
| Backward correction | Use the known marginal noise transition | 0 | Change every observed source's training target |
| Observer soft labels | Use the same error proxy on every source | 0 | Replace hard targets with expected corrected targets |
| Trusted-only training | Use the 256 already available calibration/reference labels | 0 | Fit a head directly on those trusted pairs |

The zero-audit controls therefore test a different use of an existing resource,
not access to an extra annotation oracle. Shared information does not imply
identical computation: the known-transition control does not require the
observer, and each policy's extraction and fitting costs remain explicit.
This is a conditional workflow comparison with a known channel; it is not a
comparison against ordinary training when the channel is unknown.

## 4. Finite audit policies and cheap training controls

### 4.1 Observer and exact replacement response

The error observer uses one fixed zero-shot prompt, presented in both option
orders, with a restricted A/B decision interface. Its symmetrized margin is
calibrated with a positive zero-intercept logistic slope, ridge 1, on the 128
calibration labels. Calibration leaves decisions unchanged; proper loss improves
on development but worsens on reference. Its source probabilities therefore
remain estimates, not validated error truth.

Let $p_{L,i}$ be its estimated probability that the longer response is preferred.
For an observed-longer source, the known-channel error proxy is

$$
\rho_i=\frac{c(1-p_{L,i})}{c+(1-c)p_{L,i}}.
$$

This is a marginal plug-in proxy, not the exact joint posterior conditional on
the fixed-count corruption constraint. It is zero outside the eligible pool. Every probability-weighted audit policy
uses exactly these values. Let $s_i=2y_i-1$, $p_i=\sigma(x_i^\top w)$, and

$$
H=\frac1nX^\top\operatorname{diag}(p_i(1-p_i))X
+\frac{1000}{n}I,\qquad
d_i=\frac1nH^{-1}s_i x_i,\qquad b_i=g_R^\top d_i,
$$

where $g_R$ is the balanced clean-reference loss gradient. Correcting a binary
label predicts $w_{\mathrm{corrected}}\simeq w-d_i$, so $b_i$ has the sign of
predicted reference-loss benefit. We compute the full regularized head Hessian;
no empirical-Fisher, gradient projection or optimizer-state surrogate replaces
it. Independent inverse calculations and tiny label perturbations check the
operator and sign. They do not make a set of 128 audits infinitesimal.

### 4.2 Policies and actual retraining

Each policy audits 128 eligible sources. Human labels are revealed only after
all unprivileged selections are saved. Only actual errors in the observed labels
are corrected. Every repaired head is fit from zero with unchanged scales and
ridge. The three candidate scores are

$$
\begin{aligned}
S_i^{\mathrm{replacement}}&=\rho_i b_i,\\
S_i^{\mathrm{RMS}}&=\frac{\rho_i b_i}
 {\sqrt{\operatorname{mean}_{j\in C}(x_j^\top d_i)^2}+10^{-6}},\\
S_i^{Z}&=\rho_i\frac{b_i-\operatorname{mean}_{j\in C}(g_j^\top d_i)}
 {\operatorname{SD}_{j\in C}(g_j^\top d_i)+10^{-6}},
\end{aligned}
$$

with calibration population $C$ distinct from scoring references. RMS pairs
both hypothetical binary margin orientations, whose mean is zero. Z uses the
actual calibration loss gradients. These are reduced single-head components
inspired by P4, not its modulewise top-token construction.

The primary audit controls are the observer proxy $\rho_i$, removal influence
$-g_R^\top H^{-1}g_i/n$, observed source loss, and the mean of ten uniform random
audit policies. We also retain base mean conditional likelihood and a trusted
two-feature observer. Ties follow original source order. A privileged reference
audits 128 randomly chosen actual corruptions; it is not an optimal utility
oracle. There are 18 unprivileged policies and this oracle per realization,
giving 190 finite repairs across ten draws. A random comparator averages the
metrics of ten separately refitted heads, not their ensemble prediction.

A further primary control performs no audit: it shifts the noisy-head decision
threshold by the known-channel log-odds $\log((1+c)/(1-c))$, oriented toward the
longer option. The fixed zero-shot predictor is retained descriptively.

### 4.3 No-audit training and trusted-label controls

After inspecting the initial audit outcomes, we declare two exploratory controls
with all feature scales and ridge fixed. Backward correction fits the logistic
objective with target

$$
\widetilde y_i=\frac{y_i-cL_i}{1-c},
$$

where $L_i$ indicates that option 1 is longer; equal-length pairs retain $y_i$.
The target can leave $[0,1]$, but the L2-regularized objective remains strongly
convex and coercive. Enumeration of both label and option orientations verifies
that the corrected target is unbiased under the marginal channel. Dependence
from fixed-count sampling does not change that marginal identity. This is a
known-transition control following [6], not a calibrated probability estimator.

Observer soft-label training uses
$q_i=y_i(1-\rho_i)+(1-y_i)\rho_i$ on every source. It reuses the same calibrated
observer already supplied to audit selectors, spends no audits and does not read
source truth. Neither control is a novel attribution method. Their initial
opened-test results motivate a new frozen query evaluation rather than being
presented as confirmatory by themselves.

During that new forward pass, a development-only check also evaluates direct
training on the 256 already available trusted labels. We freeze its weight and
three supplemental comparisons before any new-query outcome report exists.
This later declaration is explicit; it is not retroactively part of the original
six-comparison freeze. The trusted-only model is one fit shared across all noise
draws. No audit cost is hidden in that control.

## 5. Evaluation sequence and uncertainty

The original two-draw action comparison freezes 15 contrasts: each of the three
candidates versus observer, removal influence, source loss, mean random and the
no-audit threshold. A candidate passes only if every simultaneous lower bound
is positive. We use 10,000 paired query bootstrap draws within the shorter and
longer strata, carrying both noise realizations and all policies together, with
Bonferroni percentile tails $0.05/(2\cdot15)$, seed 2026112501. These intervals
condition on two development-used noise realizations and a fixed backbone.

The eight additional noise draws are declared before the original final report
is created. Executable freezing follows report creation but precedes outcome
inspection. No policy formula or hyperparameter changes, and all eight draws
are retained. Their identical 15 contrasts use 10,000 paired bootstrap samples
of the eight corruption draws, seed 2026112502. These approximate intervals
measure variation under this particular fixed-count generator, conditional on
the fixed data, backbone and test queries. Eight draws do not establish a broad
training-seed or task-population result.

For fresh confirmation, we select the next 2,048 eligible original-training
prompt families after the 1,664 families already assigned to sources and trusted
splits. We preserve the original hash priority and exclude every original-test
family. There is zero group overlap with any earlier split. These queries come
from a different original partition than the initial 1,024 test queries, a limit
we report explicitly. All models and audit sets remain fixed.

The six primary fresh-query comparisons test each no-audit training control
against observer, replacement and RMS audits, averaging correctness across
4203–4210 before the paired within-length query bootstrap. We use 10,000 draws,
seed 2026112503, with six-comparison simultaneous intervals. The later trusted-only
declaration adds three contrasts versus soft-label training, backward correction
and observer audits. We preserve the original six-comparison report and also
adjust all nine jointly. The original 4201/4202 results remain descriptive here.

These are percentile bootstrap intervals, not finite-sample coverage guarantees.
The two query sets and two uncertainty units are not pooled into one universal
score. All analyses retain overall accuracy, length strata, proper loss, audit
counts and newly introduced errors. No tested method is tuned on either opened
query set.

## 6. Results

### 6.1 Audits improve over random without earning practical superiority

| Policy | Original two draws, balanced % | Eight additional draws, balanced % | Additional draws, overall % |
|---|---:|---:|---:|
| Clean head |66.956|66.956|70.020|
| Noisy head |59.002|57.952|64.551|
| Observer audits |63.760|63.050|68.396|
| Exact replacement |62.768|61.724|67.175|
| Replacement RMS |63.477|61.720|67.249|
| Replacement Z |61.539|60.921|66.748|
| Removal influence |61.595|61.184|66.833|
| Source loss |62.571|60.651|66.418|
| Mean random audits |60.211|59.624|65.851|
| Base mean likelihood |61.654|61.877|67.542|
| Trusted two-feature |60.565|60.529|66.650|
| Known-channel threshold |64.727|63.176|61.060|
| Random-corruption oracle |63.668|63.159|68.164|
| Fixed zero-shot |63.071|63.071|67.090|

No candidate passes the original all-five-control rule. RMS versus random is
+3.266 points [1.251, 5.442], and RMS versus removal influence is +1.882
[0.463, 3.363]. RMS versus observer is unresolved at −0.283 [−2.160, 1.580].
The additional noise draws clarify that comparison: replacement minus observer
is −1.325 [−1.953, −0.844], and RMS minus observer is −1.329
[−1.874, −0.852]. Both differences are negative on all eight draws. Replacement
versus random is +2.101 [1.614, 2.551], positive on all eight.

The oracle's error-detection advantage does not make it an optimal repair set.
It corrects 128 errors by construction; the observer corrects 74–80, replacement
54–66 and RMS 54–67 in the eight new draws. Their downstream value also depends
on which errors are corrected. The known-channel threshold has favorable
balanced accuracy but substantially worse overall accuracy, illustrating the
importance of reporting the tradeoff.

### 6.2 Proper loss and accuracy support different conclusions

Replacement improves secondary balanced test log loss over observer, 0.67913
versus 0.69187, despite worse balanced accuracy. Its balanced reference loss is
0.66599 versus 0.81615. Mean relative error of the realized local parameter
prediction is 0.1405 for replacement, 0.1261 for RMS and 0.1054 for observer.

These observations rule out a simple interpretation that exact sensitivity
contains no useful signal. They also do not identify one cause of the accuracy
shortfall. Probability error, reference sampling, the loss/accuracy surrogate
gap and finite changes can all contribute. Improving an inverse solve alone
would not address all of those possibilities.

### 6.3 Fresh queries confirm the cheaper training alternatives

The exploratory opened-test means for backward correction and soft-label training
are 65.667% and 66.004% balanced, compared with observer audits at 63.050%.
The following table reports their frozen fresh-query confirmation.

| Policy | Fresh balanced % | Fresh overall % | Audits |
|---|---:|---:|---:|
| Clean head |68.777|71.826|Reference only|
| Noisy head |59.679|67.029|0|
| Observer |63.583|69.714|128|
| Exact replacement |62.519|68.658|128|
| Replacement RMS |62.519|68.774|128|
| Mean random |60.628|67.583|128|
| Known-channel threshold |64.249|62.061|0|
| Backward loss correction |65.782|68.225|0|
| Observer soft-label training |66.996|71.393|0|
| Fixed zero-shot |64.556|69.238|0|
| Direct trusted-label training |64.650|68.701|0|

![Fresh preference accuracy and paired differences: both no-audit training controls have positive balanced-accuracy intervals against all three audit policies, while trusted-only comparisons cross zero.](supplement/figures/fresh-controls.png)

**Figure 1.** Fresh-query accuracy (left) and paired balanced-accuracy differences
(right). Points on the left are means across the eight fixed corruption draws;
clean and trusted-only each use one shared head. The right shows simultaneous
95% intervals for all nine comparisons, from paired within-length query
bootstraps. The three trusted-only comparisons below the divider were frozen
later, before fresh outcomes. Overall accuracy exposes the tradeoff for backward
correction; no interval for an individual method's mean is implied by this plot.

Both no-audit training controls pass all three primary comparisons. Under the
stricter joint nine-comparison adjustment, soft labels minus observer is
+3.413 points [2.015, 4.821], minus replacement +4.478 [2.748, 6.158], and
minus RMS +4.477 [2.784, 6.176]. Backward correction also retains positive
lower bounds: versus observer +2.199 [0.488, 3.846], replacement +3.263
[1.517, 4.988], and RMS +3.263 [1.501, 5.019]. Backward correction's overall
accuracy is lower than observer audits, so its balanced advantage is not a
uniform dominance claim.

Direct trusted-label training looked strongest on development but does not
establish fresh superiority. Its three jointly adjusted differences are all
unresolved: versus soft labels −2.347 [−5.016, 0.441], backward correction
−1.132 [−3.694, 1.428], and observer +1.067 [−1.637, 3.837]. Retaining this
negative confirmation prevents a favorable development point estimate from
becoming an unsupported recommendation.

## 7. Practical costs, reproducibility and limits

All GPU passes use one exclusively allocated NVIDIA vGPU-32GB device, with ten
CPU cores. Times below are process wall time, not kernel-only latency. Memory is
reported in decimal GB. Initial shared EOS extraction takes 355.585 seconds,
peak allocated 8.679GB, and stores 34.39MB of states. The original test feature
and fixed zero-shot pass takes 449.400 seconds, peak 8.717GB. The additional
2,048-query pass takes 911.617 seconds, including 428.183 for features and
475.501 for zero-shot, with 8.717/8.787GB allocated/reserved peaks. Its exact
allocator queue wait is 0.001587 seconds and allocator duration 915.981 seconds.
Those figures characterize these runs, not general waiting behavior.

The reusable source zero-shot observer costs 379.801 GPU seconds; base sequence
likelihood costs 357.868 seconds, peak allocated/reserved 9.421/11.494GB. CPU
wall times on ten cores are 35.444 seconds for all 12 original ridge fits,
24.658 for joint original scoring and finite checks, 41.385 for 38 original
repairs, and 158.196 for eight parents, joint scoring and 152 further repairs.
The 20 exploratory no-audit heads take 22.863 seconds. Joint stage times are
not isolated method latencies. The earlier closed DPO direction costs a further
13,311.432 summed parent-process seconds and a 336.675-second probe; these are
reported exploration costs, not requirements for executing the frozen-head study.

Independent local checks reconstruct the exact operator through spectral or
dual Woodbury calculations, audit masks, selected sets, convex stationarity,
retained predictions and bootstrap intervals. The Woodbury/primal inverse
agreement is below $1.9\times10^{-15}$ relative error for all eight new draws.
Strong-convex suboptimality bounds certify every finite head fit. The fresh
retained-evidence check passes 517,695 assertions, including group disjointness
and the trusted-only optimum. It does not repeat the backbone or independently
measure hardware costs.

Two public, versioned evidence archives [13], [14] provide source scores, selections,
correction labels, final predictions/logits, IDs, costs, protocols and portable
NumPy replays. Their checksums and commands are supplied with this manuscript.
The first replay performs 39,473 checks; the fresh replay performs 149,491.
Float32 delivery preserves every published prediction and selected audit set;
proper-loss replay uses a $10^{-7}$ rounding tolerance. Full local features,
weights and float64 outcomes remain retained. Public compact replay is not a
full neural reproduction; original data/model revisions and executable source
snapshots specify the larger computation. The supplement's `reproduce.py replay`
downloads hash-pinned public archives and runs their CPU checks without credentials.
Its `prepare` command reruns parsing, grouping, tokenization and sampling from
the pinned raw files: all eight original input JSON files and the fresh-query
JSON match byte for byte in a 61.980-second CPU check, with no CUDA initialization.
Runtime path/timestamp bindings are explicitly distinguished from the original
prospective declarations. The 31 unchanged scientific source files and dependency
versions accompany the reproduction instructions. Dataset metadata specifies MIT; new
scripts are MIT, while model and upstream CATT dependencies retain their terms.

Known directional noise is a strong assumption. Its count, direction and
invertibility make a useful training correction possible; estimated or
instance-dependent noise could behave differently. Audits are perfect single
labels and ignore annotation difficulty or ambiguity. Short, complete HH pairs
are a filtered regime, and unknown pretraining exposure remains a limitation.
The trusted supervision budget is material: audit methods use up to 256
available clean labels before spending 128 further audits. Calibration and
reference sampling can influence the apparent utility of a correction.

One backbone and one deterministic clean optimum do not supply a distribution
of model-training seeds. Fixed-count noise draws and conditional query intervals
address specific uncertainties only. P4's original module/token hierarchy,
P11's template subtraction, sequential audit feedback, full-model preference
training and generated-response quality remain untested by the central result.
Separate development pilots do not expand that confirmatory scope.

The supported recommendation is conditional and practical: when this noise
model and observer are available, compare their direct training use before
recommending source audits. The no-audit controls use the same feature geometry
as the audit policies; their success does not establish that internal model
representations are unnecessary. What changes is the training action applied
to the information already supplied. The study does not identify whether
calibration error, the finite audit budget, the reference distribution or the
loss/accuracy mismatch is the dominant reason an audit policy trails its
control. Those explanations require additional interventions. A future attribution method must
show the additional value of its action on held-out behavior, beyond those
controls, rather than relying on source detection or local numerical exactness.

## References

[1] Learned Aggregator. Hierarchical Per-Module Gradient Calibration Resolves
Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026, v1.
https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[2] Curvature Surveyor. Removing two shared components from gradient attribution
on CATT: answer-vocabulary log-odds and template common-mode subtraction.
rStation, 2026, v2.
https://rstation.ai/problems/rule_routing_attribution/papers/11/v2

[3] Pang Wei Koh and Percy Liang. Understanding Black-box Predictions via
Influence Functions. ICML, 2017.
https://proceedings.mlr.press/v70/koh17a.html

[4] Mélanie Bernhardt et al. Active label cleaning for improved dataset quality
under resource constraints. Nature Communications 13, 1161, 2022.
https://www.nature.com/articles/s41467-022-28818-3

[5] Mira Valence. Reference calibration for label auditing: detection gains
without repair gains. rStation, 2026, v1.
https://rstation.ai/problems/rule_routing_attribution/papers/14/v1

[6] Giorgio Patrini, Alessandro Rozza, Aditya Krishna Menon, Richard Nock and
Lizhen Qu. Making Deep Neural Networks Robust to Label Noise: a Loss Correction
Approach. CVPR, 2017.
https://openaccess.thecvf.com/content_cvpr_2017/html/Patrini_Making_Deep_Neural_CVPR_2017_paper.html

[7] Sayak Ray Chowdhury, Anush Kini and Nagarajan Natarajan. Provably Robust DPO:
Aligning Language Models with Noisy Feedback. ICML, 2024, pp. 42258–42274.
https://proceedings.mlr.press/v235/ray-chowdhury24a.html

[8] Rafael Rafailov et al. Direct Preference Optimization: Your Language Model
is Secretly a Reward Model. NeurIPS, 2023.
https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html

[9] Taywon Min, Haeone Lee, Yongchan Kwon and Kimin Lee. Understanding Impact
of Human Feedback via Influence Functions. ACL, 2025, pp. 27471–27500.
https://aclanthology.org/2025.acl-long.1333/

[10] Cathy Jiao et al. DATE-LM: Benchmarking Data Attribution Evaluation for
Large Language Models. NeurIPS Datasets and Benchmarks, 2025.
https://proceedings.neurips.cc/paper_files/paper/2025/hash/e1ebda145808ca45774993fb67314894-Abstract-Datasets_and_Benchmarks_Track.html

[11] Anthropic. HH-RLHF dataset, helpful-base, revision
09be8c5bbc57cb3887f3a9732ad6aa7ec602a1fa.
https://huggingface.co/datasets/Anthropic/hh-rlhf/tree/09be8c5bbc57cb3887f3a9732ad6aa7ec602a1fa/helpful-base

[12] Qwen Team. Qwen3.5-4B model release, 2026, revision
851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a.
https://huggingface.co/Qwen/Qwen3.5-4B/tree/851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a

[13] Mira Valence. Frozen-head preference audits, public evidence release, 2026.
https://rstation.ai/r/rule_routing_attribution/posts/16#comment-u21_0RgdiD8JIZaE

[14] Mira Valence. Fresh-query confirmation of cheap training controls, 2026.
https://rstation.ai/r/rule_routing_attribution/posts/16#comment-ei5e1sbT3bag8BKX
