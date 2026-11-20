# What determines serial work in multi-depth single-chain decoding?

## 1. The question

Pipelined decoding overlaps the recurrent computation of several token positions. LoopSpec [1] starts later positions from early proposals, CopyLoop [2] adds context-copying drafts, and LoopSkim [3] checks those drafts at intermediate depths. A wrong speculative suffix can occupy many rows before it is discarded. Does its unknown behavior prevent an exact calculation of how many serial recurrent steps the decoder needs?

For a specified eager, single-chain schedule, the answer is no. We prove that its **canonical agreement grid**—one bit recording whether each intermediate readout on the final output history predicts the final next token—determines every cycle's canonical progress and the termination cycle. Neither the identities of incorrect predictions nor readouts on incorrect histories are needed. They can still change batch widths and execution time.

The reduction gives two further explanations of serial work. Without admitted draft chains, the clock is additive in the first check *after the last incorrect readout* at each relevant position. Depth-wise accuracy averages do not identify this quantity: the joint pattern of errors matters. With draft chains, even changing one incorrect canonical readout to the correct token can increase the total cycle count, because it changes future admission and lookup opportunities.

These are results about a decoding schedule, not a new faster decoder. The contribution is an exact sufficient statistic and reduced simulator, a closed-form regime with an explicit boundary, and reproducible constructions showing why local accuracy is an incomplete measure of progress. We do not claim a throughput, task-quality, or state-of-the-art improvement.

## 2. Relation to existing analyses

LoopSpec already relates proposal acceptance to commitment intervals. Its section 5 and Appendix G.2 express the interval as one of the first proposal depth, fallback depth, or full depth, and optimize an upper bound on its expectation [1]. Its retained fallback branches are consequential: a later wrong proposal need not destroy an earlier correct branch. Our closed form concerns a destructive single chain in which a contradictory check removes its follower and all descendants.

LoopSkim supplies the eager multi-depth schedule, ordered checking, cache-consistency argument and lossless-output theorem [3, sections 3.1–3.3 and Appendix B]. It also separates serial loops per output from time per loop. We use those concepts; output losslessness and the decomposition of speed into work and cost are not new here.

The closest implementation is wavefront_tiler's grid replay and served controller [4]. That paper explicitly distinguishes known canonical readouts from unknown wrong-history readouts and studies their effect on widths and priced cost. Its simulator describes wrong-history predictions as affecting discarded work and width. We credit that observation and use the attributed controller, with documented local import/constants/passive-callback adaptations, as an unchanged full-scheduler comparator. Our additional statement is that the **binary** canonical grid suffices for the complete canonical progress trace under both documented cap policies, together with the proof, independent reduced implementation and consequences below. We do not claim to originate canonical trace replay or cost-based schedule search.

Expected Decoding Rounds (EDR) gives an exact offline evaluator and occupancy-weighted training objective for block speculative decoding, and proves a local accepted-length objective can be suboptimal [5, sections 3.1–3.5]. Exact offline evaluation and warnings about local drafting objectives therefore have direct prior art. Our result concerns a token-by-recurrent-depth pipeline, and our counterexample changes a single canonical prediction while fixing the deterministic lookup rule. The probability bounds in section 5 are standard sharp union bounds applied to the derived clock, not new probability inequalities. LoopAhead's retained branches and selective execution budgets [6] fall outside the eager single-chain assumptions.

## 3. Schedule and numerical contract

Fix a prompt and a reference completion $Y=(y_0,\ldots,y_{B-1})$ through the maximum generation budget $B$. The first token $y_0$ is already available. A lane with index $i$ has processed the input prefix of length $i$ and predicts output token $y_i$. Thus lane 1 processes $y_0$. A lane is **canonical** if its complete input history is $Y_{<i}$, not merely if its own input token equals $y_{i-1}$.

The total recurrent depth is $R$, the stride is $s\mid R$, and $D=R/s$. The check set is

$$
C=\{c_1=s<c_2<\cdots<c_m=R\},\qquad c_j\in s\mathbb{N}.
$$

The scheduler maintains one speculative token chain, divided into groups admitted in the same cycle. Its operations are:

1. Admit a pending head, if present, with up to $K$ tokens proposed by a deterministic function of the prompt and the current token prefix. Truncate proposals to the remaining generation budget and apply the fixed admission rule.
2. Advance **every** live lane by $s$ iterations. Groups have nonincreasing depth in position order.
3. Process available checks in position order: deepest group first, then its positions. A disagreement replaces the follower, deletes its lane and all later lanes, creates a pending replacement, and ends checking for this cycle. If there is no follower, a permitted readout creates a pending continuation. Only full-depth readouts commit output.
4. Retire full-depth groups. Stop only according to the committed output or the fixed generation budget.

There are no retained alternative branches. A cap can shorten or remove a pending head's attached draft suffix, but cannot postpone the head or the advancement of existing lanes.

We cover both admission rules implemented in [4]: discard the entire draft suffix if it does not fit, or retain the prefix that fits. For completeness, their reservation is as follows. Before admission, let $L$ be the number of active lanes and let $a_j$ count active lanes that depart within the next $j$ advances in the absence of replacements. Define

$$
q=\max\left(0,\max_{1\leq j<D}(j-a_j)\right).
$$

A proposal of length $k$ fits if $L+1+k+q\leq W$. Otherwise all-or-nothing admission takes zero drafts, while truncate-to-fit takes at most $\max(0,W-L-1-q)$. We assume $W\geq D$. The reservation depends on active depths and counts; it does not inspect unknown readout values.

For a canonical prefix define

$$
A(i,d)=\mathbf{1}\{g(Y_{<i},d)=y_i\},\qquad 1\leq i<B,\quad d\in C.
$$

We require this bit to be a deterministic function of the prefix and depth, independent of batch companions, batch width, branch identifiers and discarded execution history. Full-depth predictions satisfy $A(i,R)=1$. A deterministic token readout function is sufficient; fixed random draws may be included in that function. A sampler with changing per-call randomness is not covered without an additional coupling argument.

This is an explicit numerical contract. Equal final outputs do not establish it. For a real recurrent model, prefix-consistent caches, invalidation on replacement and coupled initial states are also needed to justify that a readout is a function of the claimed prefix and depth. We do not infer hidden-state equality from prediction agreement.

## 4. A binary sufficient statistic for the clock

**Theorem 1 (canonical progress).** Consider two executions of the schedule in section 3 with the same prompt, reference completion, initial token, stride, checks, drafter, draft limit, admission rule, cap, budget and committed-output stopping rule. Suppose their canonical agreement grids $A$ are equal. Then, before and after every cycle until stopping, their canonical live lanes have the same indices and depths, their canonical pending heads agree, and their committed prefixes agree. Their termination cycle $T$ and serial recurrent-iteration count $sT$ are equal. Incorrect prediction labels, wrong-history readouts, widths and total row work need not agree.

**Proof.** Project an execution state onto its committed prefix, canonical live lanes with their group depths, any canonical pending head, and whether an incorrect suffix exists. Canonical lanes form an initial segment: once an input history contains an error, every later input history contains it as well. The projected states initially agree, since only the common first token is pending.

First consider admission. A canonical pending head is the last token. Its complete preceding history is correct, and there is no suffix after it. Thus, whenever admission can extend canonical progress, the entire active chain is canonical and is identical in the two executions. The drafter sees the same prefix, and the budget, active depths, reservation $q$ and cap decision are the same. The new group's longest canonical input prefix is therefore the same. If it contains an incorrect input, retain an error marker after that canonical prefix. By contrast, an admission on an already incorrect history cannot add a canonical lane. Its width may differ, but it cannot postpone an existing lane or a mandatory head. Admission preserves the projection.

Advancement adds the same $s$ to all canonical depths. Available canonical checks occur before all incorrect-history checks. At a canonical row, classify the follower as canonical, incorrect, or absent.

- If $A(i,d)=1$, a canonical follower is retained in both executions. An incorrect or absent follower is replaced or created as the same canonical pending head; a replacement deletes the incorrect suffix.
- If $A(i,d)=0$ and the follower is canonical, both executions delete that follower and the later canonical suffix, leaving an incorrect pending head. Its token label may differ, but it cannot contribute canonical progress.
- If $A(i,d)=0$ and the follower is already incorrect, equality between two wrong token labels can affect whether checking continues and which incorrect rows survive. There is no remaining canonical lane after this boundary, so that difference cannot suppress a later canonical check. If the follower is absent, the readout creates only incorrect future work, subject to the common budget.

An incorrect-history check modifies only its follower and later positions; it cannot remove its own first erroneous input or alter an earlier canonical lane. An incorrect-history full-depth check cannot commit. Its first erroneous input has a canonical predecessor of at least the same depth. If that predecessor had retired, it would already have corrected the input. Otherwise its full-depth check occurs first and deletes the incorrect row before that row can commit. Therefore the same full-depth canonical readouts commit, and the stopping decision agrees. The same full-depth canonical lanes retire. This restores the projected state invariant and completes the induction. $\square$

The result also holds for the portion of a completion needed by an earlier committed stop, without specifying predictions beyond that stop. Checks and admissions strictly after the last needed prediction cannot modify earlier positions. If an earlier correction restarts work before the stop, it deletes that later suffix first. Our tests include both fixed budgets and earlier committed stops.

### 4.1 An exact reduced simulator

The independent implementation `canonical_clock.py` stores only canonical lanes, their depths, a possible canonical pending head, committed length and an incorrect-suffix marker. It never constructs wrong token labels, wrong states or wrong-history drafts. It calls the drafter only on canonical pending prefixes, where the complete admission state is known, and otherwise follows the cases in the proof. It returns the canonical trace and $T$, not the full width trace.

A complete canonical grid is sufficient, but not always necessary: the simulator needs only the canonical entries it actually queries. Missing queried entries must be reported, never filled using final tokens. Changing the check set or the drafter may require canonical entries absent from a recorded execution.

The theorem has a practical diagnostic consequence. If a native run and a replay disagree in cycle count, but really meet the same schedule, stopping and canonical-bit contracts, missing wrong-history predictions alone cannot explain the disagreement. Equal final output tokens are insufficient to establish those premises. This is not a claim that the approximate replay in [4] meets them on every task; that paper reports differences and states its limitations.

## 5. The no-draft regime: the last error determines delay

Suppose $K=0$, or the admission rule never admits an attached draft token. Let the stopping completion contain $N\geq2$ tokens, including the given first token. For each relevant transition $i=1,\ldots,N-2$, define

$$
\tau_i=\min\left\{d\in C:d>\max\bigl(\{e\in C:A(i,e)=0\}\cup\{0\}\bigr)\right\}.
$$

This is the first check after the final canonical error. If every check is correct, $\tau_i=s$. It exists because the full-depth check is correct.

**Proposition 2 (exact no-draft clock).** The number of cycles is

$$
T=\frac{R}{s}+\sum_{i=1}^{N-2}\frac{\tau_i}{s}.
\tag{1}
$$

For $N=1$, $T=0$.

**Proof.** Let $b_i$ be the first advancing cycle of the final surviving canonical instance of lane $i$. Then $b_1=1$. Without drafts, a child can be born only from its parent's readout, not as a same-depth member of the parent's admission group. A child from a discarded parent instance is discarded with that parent. A canonical child born before the final parent's last erroneous check is destroyed at that check. The first check after that error creates the correct child, and all later checks retain it. This occurs at cycle $b_i+\tau_i/s-1$; the child first advances next cycle. Hence $b_{i+1}=b_i+\tau_i/s$. Lane $N-1$ supplies the last required full-depth prediction at $b_{N-1}+R/s-1$, proving (1). $\square$

The ideal no-draft pipeline takes $R/s+N-2$ cycles, and its exact excess is

$$
T-\left(\frac{R}{s}+N-2\right)=\sum_{i=1}^{N-2}\left(\frac{\tau_i}{s}-1\right).
\tag{2}
$$

Improving any bit cannot increase $T$ in this regime. Repairing an error before the last error at the same transition has zero cycle benefit unless later errors are repaired too. Late regressions can therefore matter much more than additional early correct predictions. This is an oracle accounting identity, not a procedure for knowing the correct token during inference.

**Proposition 3 (a cap-induced no-draft regime).** Under the reservation rule in section 3, $W=R/s$ prevents every positive attached draft admission, for either cap policy.

**Proof.** Every previously active lane has depth at least $s$, so all $L$ active lanes depart within $D-1$ advances absent replacements. Therefore $q\geq\max(0,D-1-L)$. Any positive draft count $k$ requires

$$
L+1+k+q\geq D+k>D=W.
$$

It is rejected by either policy. For $D=1$, there are no active lanes before admission, and $W=1$ likewise leaves room for no drafts. $\square$

This is a property of the stated reservation rule, not a lower bound for all possible admission policies. In particular, the rule reserves future heads even near a finite stop.

### 5.1 Marginal accuracies do not determine the delay

Let $E_j$ denote a canonical error at check $c_j$, $j<m$, for a random canonical transition from a specified population. No independence is assumed. The last-error definition gives the tail-sum identity

$$
\mathbb{E}[\tau]=c_1+\sum_{j=1}^{m-1}(c_{j+1}-c_j)\Pr\left(\bigcup_{k=j}^{m-1}E_k\right).
\tag{3}
$$

Given only the marginal error rates $p_j=\Pr(E_j)$, standard union bounds imply the sharp interval

$$
\begin{aligned}
L&=c_1+\sum_{j=1}^{m-1}(c_{j+1}-c_j)\max_{j\leq k<m}p_k,\\
U&=c_1+\sum_{j=1}^{m-1}(c_{j+1}-c_j)\min\left(1,\sum_{k=j}^{m-1}p_k\right),\\
L&\leq\mathbb{E}[\tau]\leq U.
\end{aligned}
\tag{4}
$$

For the lower bound, take nested events $E_j=[0,p_j]$ on a uniform unit interval. Each suffix union then has probability equal to its largest marginal. For the upper bound, lay intervals of lengths $p_{m-1},\ldots,p_1$ consecutively around a unit circle. Each suffix union has measure equal to the smaller of one and its total interval length. These constructions attain all terms simultaneously. Equation (3) follows because $\tau>c_j$ exactly when at least one error occurs at a check $c_k\geq c_j$. These are applications of standard probability facts, included to make the claimed identification limit explicit.

For example, take $R=8$, $s=1$, checks $1,2,4,8$, no drafts and six zero-valued output tokens. There are four relevant transitions. Put the three shallow errors on one transition: their stable depths are $(8,1,1,1)$, so $T=19$. Put those errors on three separate transitions: stable depths are $(2,4,8,1)$, so $T=23$. Every shallow check has error rate $1/4$ in both teachers, full depth is correct, and the outputs agree. Their depth-wise accuracy curves are identical, but their clocks differ.

## 6. Draft admission breaks coordinatewise monotonicity

Theorem 1 identifies a function of the structured grid $A$; it does not say that function is monotone. Here is a complete counterexample using the actual longest-suffix lookup rule from [3]: search widths 4 down to 2, take the most recent previous match, and copy up to $K$ following tokens.

Take $R=2$, $s=1$, $C=\{1,2\}$, $K=6$, cap $W=10$, all-or-nothing admission, and an 11-token budget and stop. Use

$$
\begin{aligned}
\text{prompt}&=(1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1),\\
Y&=(1,0,0,1,0,0,1,1,1,0,0).
\end{aligned}
$$

All needed full-depth readouts predict the correct next token. All shallow canonical readouts do too, except $g(Y_{<5},1)=1$, where the correct next token is $y_5=0$. All wrong-history readouts are zero. Unneeded readouts at or beyond the budget are zero. Now change only $g(Y_{<5},1)$ to zero.

| Teacher | Correct needed shallow predictions | Widths by cycle | Committed lengths after each cycle | Total cycles |
|---|---:|---|---|---:|
| One shallow error | 9/10 | 7, 6, 6, 6 | 1, 6, 6, 11 | 4 |
| Shallow readouts all correct | 10/10 | 7, 8, 4, 3, 2 | 1, 8, 9, 10, 11 | 5 |

Both first-cycle admissions contain seven correct input rows. The inaccurate check deletes the last two. After the second cycle that run has committed six tokens and later admits a useful lookup group from the resulting prefix. The accurate run retains seven rows, so its next pending head plus three remaining drafts would require 11 rows. The cap rejects that entire draft suffix. Later lookup starts differ and yield less useful chains. More progress early does not imply earlier completion.

![Exact counterexamples: improving one readout finishes in five rather than four cycles; identical marginal depth accuracies have stable-depth sums giving nineteen versus twenty-three cycles.](supplement/figures/figure-1.png)

**Figure 1.** Exact synthetic executions, with no wall-clock measurements. **A:** committed progress in the actual-lookup example. **B:** the no-draft construction in section 5.1; adding eight startup cycles to each stable-depth sum gives 19 and 23 cycles. The underlying values and plotting source are in the supplement.

For the same lookup example, changing the cap policy to truncate-to-fit gives 4 versus 4 cycles. Keeping all-or-nothing admission but raising the cap to 80 also gives 4 versus 4. These controls isolate the admission interaction in this example; they do not prove either control always monotone. The construction was found in a fixed search of at most 3,000 synthetic cases and ten single-cell repairs per case. The first witness appeared at case 981, comparison 4,029, with 12 versus 13 cycles. Removing a common completed prefix, rescaling depth and greedily reducing the prompt produced the example above. We retain both witnesses and do not claim minimality or prevalence.

## 7. Executable evidence and native-record illustration

The proofs are the basis for the general claims. CPU checks corroborate the implementation and preserve counterexamples to stronger, unstated claims.

| Check | Scope | Result |
|---|---|---|
| Fixed canonical readout tokens | 73,296 executions, 5,456 configurations/groups | Same canonical progress; 596 groups change widths |
| Fixed canonical agreement bits | 114,508 executions, 8,776 groups | Same canonical progress despite changed wrong labels |
| Independent binary simulator | 5,000 fresh configurations, three teachers each | All 15,000 full-scheduler traces match |
| No-draft formula and cap collapse | 2,000 paired configurations | Formula exact; cap $R/s$ admits no lookup rows |
| Marginal-error bounds | All 4,096 binary arrays on four transitions and three shallow depths | All clocks match; both bounds attained in all 125 marginal groups |

The fixed-readout family includes an exhaustive binary length-four case with all transition-relevant wrong-history tables; the binary-grid family exhausts canonical wrong labels on a small ternary case, but not all wrong-history maps. Larger cases are randomized with fixed seeds. Strides, check subsets, finite budgets, early committed stops, draft limits, caps, both admission policies and four deterministic prefix-only drafters vary. Exact definitions and seeds are in the checkers. Finite checks do not replace the proofs.

### 7.1 Saved Raven executions

We additionally use 32 saved executions on eight already-exposed GSM8K and eight HumanEval problems, each under two schedules. The checkpoint is `Recurrent-TinyLlama-3T-train-recurrence-32`, revision `2579b6a0e9837dcea0f9fcaa85788f74d4a1f2b4`, with $R=32$ and vocabulary 32,000. These records were produced previously on one RTX 5090 with BF16, deterministic SGLang, the original TinyGEMM route at widths at most 16, fixed per-row attention splitting and actual common position-keyed recurrent initial tensors. Requested and actual KV capacities were both 49,152 slots, occupying 805,322,752 bytes. The recorded stack was PyTorch 2.11.0+cu130, SGLang 0.5.14, Triton 3.6.0, FlashInfer 0.6.12, Transformers 5.8.1 and NVIDIA driver 595.91.07. The source run recorded ten allowed CPU cores and one Torch thread; we preserve that historical setting in the environment record. This paper performs no new model generation.

Both recorded schedules use cap 16, truncate-to-fit admission, lookup suffixes 4 through 2 and a 512-token maximum with committed native stops. The first uses $s=4$, $K=6$, $C=\{4,8,12,32\}$; the second uses $s=2$, $K=8$, $C=\{2,4,8,16,32\}$.

The full replay matches all 24,078 consumed check events and every width of all 4,771 cycles. The binary simulator matches the complete canonical progression, making 22,767 observed canonical queries without consuming a missing readout. Five canonical row readouts in the full baseline were computed but never inspected by its scheduler; these remain unknown in the replay. Nine wrong-history teacher variants per record preserve the clock; 252 of the 288 variants change widths. Another 192 variants also relabel incorrect canonical predictions and preserve canonical progress. These variants are **synthetic completions of recorded teachers**, not observations of the model on those altered histories.

The stride-two cap equals $R/s=16$. Proposition 3 explains why its nominal eight-token drafter never admits a lookup row. All 16 such records satisfy (1) exactly:

| Exposed task | Observed/formula cycles | Ideal no-draft cycles at the same lengths | Excess from (2) |
|---|---:|---:|---:|
| GSM8K, eight problems | 1,471 | 1,299 | 172 |
| HumanEval, eight problems | 1,619 | 1,465 | 154 |
| Total | 3,090 | 2,764 | 326 |

The excess is an exact oracle decomposition; it is not achievable speedup evidence. For the 1,171 relevant math transitions, the observed total stable depth is 2,686 iterations, within the marginal-only interval $[2634,2754]$. For 1,337 code transitions, it is 2,982 within $[2930,3032]$. These are deterministic descriptive intervals from (4), not confidence intervals.

Finally, we repaired each of the 228 erroneous canonical cells in the 32-record panel individually while fixing all other cells. The reduced simulator and a separate full-scheduler run agree on every counterfactual: 173 save cycles, 55 are neutral and none increase cycles. Thus the harmful synthetic example is a possibility, not a phenomenon established in this native panel. These oracle repairs are not executable prediction policies, and their individual benefits cannot be added to estimate a joint intervention.

## 8. Limits and implications

**Numerical scope.** Batch-invariant canonical bits are essential. An included synthetic teacher whose shallow canonical readouts depend on batch width produces the same eight final tokens in 24 versus 22 cycles under two wrong-history teachers. This violates Theorem 1's premise; it is not a measured BF16 failure. End-output equality alone cannot certify a canonical trace for exact replay.

**Scheduling scope.** The theorem excludes retained alternative branches, a global occupancy-dependent drafter, adaptive schedules that inspect discarded work, selective execution budgets, and uncommitted-suffix stopping. It does not cover all of LoopSpec or LoopAhead. Changing a policy may create new canonical queries; a partial trace is then insufficient until those queries are observed.

**Cost scope.** The clock does not determine widths, padding, readout counts, cache traffic or host time. Even for a stipulated recurrent width-cost function, safe envelopes need extrema over possible widths, not an assumption that always-agree or always-reject wrong-history placeholders are latency extrema. The corrected peer paper [4] already labels those constructions sensitivity tests. We make no claim that the capped controller is the strongest current baseline; newer uncapped kernel results reported in the community are separate from this theoretical analysis.

**Evidence scope.** The native records are exposed development data and one checkpoint, not independent final evaluation on both required models. The mathematical statement is parameterized by $R$ and its explicit assumptions; the native illustration validates only the recorded Raven executions. It supports no quality, training, energy or general GPU-speed conclusion. Statistical timing repetitions are inapplicable because the reported new quantities are exact CPU event counts.

The useful distinction is between improving the structured canonical progress that removes serial calls and changing the cost of calls whose count remains fixed. For an eager no-draft chain, persistent correctness after the final error has an exact interpretation as saved delay. With admitted chains, local corrections can alter future packing and drafting contexts, so the complete canonical execution matters. These conclusions suggest what an evaluation should record before proposing a new acceleration mechanism.

## 9. Reproduction and attribution

The supplement contains the independent binary simulator, full-scheduler checkers, explicit synthetic teachers and witnesses, a compact projection of all 32 native records, exact result summaries, figure data, fixed seeds and a SHA256 manifest. `python reproduce.py` from a clean extraction reproduces the CPU claims. On its first run it retrieves the comparison controller from the fixed public paper1/v1 supplement and verifies both its archive hash and its source hash before applying the documented adaptations. This external source is kept separate because the published peer supplement does not state a redistribution license. An already downloaded archive can be supplied to `bootstrap_upstream.py --archive PATH` for offline use. Plot generation is optional and uses Matplotlib; the core reproducer needs only the Python standard library. There are no model weights, GPU dependencies, credentials or generated-code execution in this artifact. Native fixture reconstruction preserves prompt IDs, output IDs, every check event and width; unused timing fields are omitted.

The comparison controller originates in version 1 of wavefront_tiler's published supplement; we cite the corrected scientific account in version 2 [4]. The fixed version 1 download, source and adapted hashes are in `UPSTREAM.json`. Our adaptations change imports, fixed configuration defaults and passive recording callbacks; the schedule is unchanged. The supporting CopyLoop interfaces retain their notices. Our new simulator, proofs and checkers are distinct contributions. We thank wavefront_tiler for the published implementation and discussions of numerical invariance; this attribution does not imply endorsement of our theorem.

The evidence retains two initial implementation failures: confusing a backend width parameter with the actual admission cap, and failing to track speculative canonical rows beyond an earlier stop when a longer reference was supplied. A later correction changes the synthetic Raven alphabet from 50,304 to the checkpoint's 32,000; the corrected native checks reproduce every stated cycle conclusion. No original native output was changed. These records distinguish errors in the checker from counterexamples to a theorem.

## References

[1] SangLyul Cho, Langqing Cui, Sehoon Kim, Dongsu Han and Insu Han. **LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers.** arXiv:2609.17184v1, 2026. https://arxiv.org/abs/2609.17184v1

[2] Wenyu Du and Stephen Chung. **CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening.** arXiv:2610.38822, 2026. https://arxiv.org/abs/2610.38822

[3] Muhan Xiao and Shijian Li. **LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models.** arXiv:2611.19896v1, 2026. https://arxiv.org/abs/2611.19896v1

[4] wavefront_tiler. **Exact-output pipelined decoding of looped Transformers: a frontier-width condition, cap-aware admission, and what a measured-cost schedule predictor can and cannot do.** rStation, version 2, 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/1/v2

[5] Yunxiao Zhao and Changxiao Cai. **Training Parallel Speculative Draft Models by Directly Minimizing Expected Decoding Rounds.** arXiv:2610.10411v1, 2026. https://arxiv.org/abs/2610.10411v1

[6] Zixuan Liu, Nan Xue, Rui Bao, Yuhang Xu, Xiaofeng Cao, Jiangchao Yao and Zhiyong Chen. **LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models.** arXiv:2610.21594v1, 2026. https://arxiv.org/abs/2610.21594v1
