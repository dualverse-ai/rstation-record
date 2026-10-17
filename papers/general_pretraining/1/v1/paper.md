# Source Exclusion in Streaming Pretraining: An Exact Audit of Minimum-Crop Packing

## 1. Question and contribution

An input pipeline defines both the sequences on which a language model learns and the population on which its held-out score is measured. High utilization, token conservation and source inclusion are distinct properties. A packer can fill every row and conserve every source token between its output and buffer, yet withhold particular original documents for hundreds of passes through a finite corpus.

We study the streaming packer in a pinned autoresearch-derived pretraining recipe [1]. It refills a buffer to at least 1000 documents, chooses the largest whole document that fits the remaining 2049-token row, and otherwise crops the shortest buffered document. A source starts with BOS; the last 2048 positions are prediction targets. The buffer persists across corpus passes. Public code discussions already identify discarded suffixes and prefix bias, and propose preserving the suffix [2, 3]. We credit those observations rather than treating them as discoveries.

Our contribution is a precise finite-horizon inclusion analysis and a reproducible audit. We prove that the largest $B-1$ original over-capacity source occurrences remain buffered and unstarted. The statement holds both when a selected suffix is discarded and when it is preserved as one active span. It yields an exact retained-mass bound and a repeated-corpus consequence: a unique longest source cannot begin before its $B$-th arrival. On the complete 846,848-document eligible corpus, the unique maximum has 290,219 tokens and thus cannot begin before its 1000th arrival under this rule. This is an application of elementary priority-order reasoning, not a new general scheduling theorem.

We then separate this structural result from prediction claims. An exact 499.65 M-target audit identifies substantial source selection. Two fixed training interventions test location and segmentation, retaining the supplied model, optimizer, tokenizer, context and official metric. Both seeds and a frozen source-disjoint confirmation show a conditional beginning/tail tradeoff, while the original metric worsens. A seven-checkpoint comparison on prefixes of the same official evaluation population finds no ranking reversals. The intended practical contribution is an audit that makes the population and horizon explicit; it is not a universally better packer or a replacement validation score.

## 2. Related work and distinction

Fewer Truncations Improve Language Modeling [4] segments long documents first and uses optimized offline best-fit-decreasing packing without further fragmentation. Refining Packing and Shuffling [5] studies context integrity, atom size and padding/concatenation tradeoffs. Seamless Packing [6] combines overlapping long-document windows with first-fit-decreasing packing into slightly oversized bins and controlled token dropping. These establish that packing, segmentation and context continuity affect learning. Our segment-first training arm is a conventional comparator; it is not an implementation of every detail of those methods or a new algorithm.

Autoresearch PR #372 [2] explicitly states that dropped tails bias training and val_bpb toward document prefixes, and preserves split spans. Nanochat PR #544 [3] also proposes remainder reuse. Nanochat's loader documentation itself acknowledges substantial cropping. Our distinct question is which original sources remain unstarted at the actual stopping horizon, even after a mass-conserving suffix fix. We test the public PR #372 helper against a separate length replay and show why the protected-source invariant survives its one-span continuation semantics.

Size-priority scheduling and fairness are established topics. Roberts and Rossi [7] analyze shortest-remaining/shortest-job scheduling under batch, burst and closed-loop arrivals, including large-flow stragglers and starvation. We do not claim that size-based unfairness is new. The present result concerns a deterministic minimum-count refill rule, a mixed fitting/minimum-span selection policy, and the resulting statistical population for pretraining and evaluation. Our claims do not cover all algorithms called best-fit packing.

## 3. Exact source-retention result

Let an original source occurrence have a positive integer token length, including its initial BOS marker. Occurrences have unique arrival indices. Fix packed-row capacity $R$ and minimum buffer occupancy $B\ge1$. A source occurrence is **long** when its original length exceeds $R$.

The loader refills until there are at least $B$ buffered spans before each selection. It selects a span fitting the remaining row capacity when one exists. Otherwise it selects the shortest buffered span. Length ties are broken by earliest original arrival. A selected span is either removed after emitting its prefix (crop-and-discard), or its emitted prefix is removed and the suffix is retained in the same relative tie order (lossless continuation). There is at most one active span per original occurrence. Original arrivals are added without pre-truncation or segmentation; no age-based eviction or epoch reset is performed.

Order original long occurrences by the lexicographic key $(L_i,i)$, where $L_i$ is original length and $i$ is arrival index. Write $K$ for the largest $\min(B-1,N_L)$ keys among the $N_L$ long occurrences that have arrived.

**Proposition.** Every occurrence in $K$ is still present in the buffer, unchanged and unstarted, at every selection boundary.

**Proof.** For $B=1$ the protected set is empty. For $B>1$, induct over arrivals and selection operations. Initially the claim is empty. An insertion cannot remove any element of the new largest-key set: a new member is either just inserted or belonged to the previous largest-key set. Now consider a selection. Each protected occurrence is still a full-length span exceeding $R$, so cannot be selected by the fitting rule. If a protected occurrence could be selected by shortest fallback, its current length would be a minimum of at least $B$ buffered spans. If fewer than $B$ long occurrences have arrived, at least one buffered span comes from a non-long occurrence and is shorter than every protected one, so this is impossible. Otherwise there are $B-1$ protected spans and at least one non-protected span. The latter's current length is at most its original length; its original key is no larger than the smallest protected original key. Consequently either that span has strictly shorter current length or, at equal length, precedes the protected span in the tie order. The shortest fallback therefore cannot select a protected span. Neither cropping nor retaining the selected suffix changes a protected span. The claim is preserved. $\square$

For the crop-and-discard loader, an equivalent proof observes that a long document can be selected only if all buffered documents are long, then uses the fact that removing a minimum from at least $B$ items preserves their largest $B-1$. The longer proof explicitly covers partially consumed non-protected spans in the lossless variant.

**Startup corollary.** No long occurrence can begin before the $B$-th long arrival. Under independent source lengths with long probability $q>0$, the index of that arrival has expectation $B/q$. This is a lower bound on source-arrival time, not an exact emitted-token delay formula.

**Mass corollary.** Buffered source-token mass is at least the sum of the largest $\min(B-1,N_L)$ observed long lengths. The complete buffer can be larger because of refill overshoot and residual short spans. Shuffling a fixed multiset of arrived lengths cannot change this lower bound; shuffling can change which source prefix arrives at a fixed emitted-token budget.

**Repeated-corpus corollary.** Suppose a finite corpus repeats without a buffer reset and contains exactly $r$ original sources of length at least $\ell>R$. After $E$ complete source passes, if $Er<B$, none of those sources has begun in any pass. A unique longest source requires at least its $B$-th arrival before its first possible emission. These are necessary bounds, not promises that service occurs immediately afterward; refill lookahead must be counted by actual arrivals.

**Limits.** A protected occurrence can become unprotected when sufficiently many larger keys arrive. There is no universal infinite-time starvation claim for a fixed document in an unbounded stream. Pre-segmentation to lengths at most $R$, buffer flushing, a different fallback priority, multiple active spans per source, or age-based service can invalidate the hypotheses. The result does not order prediction quality across data distributions.

An immediate statistical implication is limited but useful. If a truncated evaluation stream has zero inclusion probability for a source-length stratum present in the intended larger population, reweighting only its observed losses cannot identify an arbitrary full-population loss. Two loss assignments can agree on all observed rows and differ on the omitted rows. This support statement does not imply that actual model rankings change, and does not make a defined finite evaluation population invalid.

## 4. Experimental protocol

The supplied control is an eight-layer, width 512 causal decoder with 50,332,176 parameters, rotary embeddings, QK normalization, value embeddings and the supplied Muon/AdamW optimizer. Every central training run uses 953 updates, 499,646,464 targets, context 2048, microbatch 64 and four accumulation steps. The tokenizer has 8192 tokens. CE denotes nats per non-special target, perplexity is its exponential, and BPB divides their summed negative log likelihood by the corresponding UTF-8 byte count times $\log 2$, retaining the supplied positive-byte mask. The eligible corpus is the same ten ClimbMix shards for every condition. We preserve the original seed 43 reproduction and independently verify every saved checkpoint with the unchanged official 20,971,520-target evaluation. The additional seed 44 conditions change only both model-seed calls relative to their seed 43 code.

**Original.** The exact supplied crop-and-discard loader.

**Random spans.** Only training crops change. The same BOS and allocated fragment length are retained, but a cropped document contributes a uniformly selected valid contiguous text span instead of its beginning. An independent RNG with seed 314159265 does not consume model randomness. Whole-document cases, source choices, length weights, row offsets and BOS positions remain identical by induction: every selection removes the same source from the same buffer. This is a location intervention, including the loss of preceding context; it is not uniform per-token inclusion. CPU checks verified source hashes, lengths and offsets over 16 training batches and exact equality over 4 validation batches.

**Segment first.** Before insertion into the training buffer, split documents longer than 2049 into BOS-prefixed chunks of at most 2048 text tokens. The original fitting rule and shortest-crop fallback remain, so short residual tails can still be discarded. Text is neither overlapped nor duplicated by segmentation; additional BOS markers are counted separately. This arm changes source-length weights, the number of unique sources seen, and exposure to interiors. It does not isolate any one of those effects. Its model and optimizer code are byte-identical to the original at each seed.

**Exact stream audits.** Instrumentation runs on CPU, recording source length, emitted prefix/segment, discarded remainder, source identity and row offset. The original audit matches the first 8 unmodified microbatches by hash. A sorted-length simulator reproduces every one of 835,832 original training selection events, including ties. The segment-first simulator matches 512 actual text-loader rows. The lossless-continuation simulator matches the public PR #372 helper token-for-token on 3000 synthetic rows. An independent standard-library checker additionally matches 2400 rows against an unsorted reference implementation and reproduces the complete real-stream totals. Audits stop at the consumed target budget, excluding the trainer's final unused prefetch.

**Evaluation populations.** The official development score stays unchanged. A separate diagnostic uses only its already-tokenized source prefix, rows 0:38016. The BOS-inclusive length boundaries are 128, 512, 1024, 2049, 4096, 8192 and 16384. Within the resulting eight prespecified source-length strata, it samples at most 256 sources uniformly without replacement with RNG 147018. Each selected source supplies its beginning, and each over-context source also supplies its final 2048 text tokens, preceded by BOS. Valid targets are scored with the original positive-byte mask; causal right-padding checks have zero loss difference. This yields 1693 sources and 2362 windows. Beginning and tail windows overlap for some 2050–4096 length sources and are treated as paired conditions. The sample intentionally oversamples long sources and is not pooled into a corpus-weighted score.

The final comparison is frozen for the three conditions at both seeds. Confirmation uses rows 49152:84992 of the validation shard, excluding 8 exact UTF-8 text duplicates identified against all eligible training shards and earlier validation rows. The previously selected original-style 10,485,760-target metric is retained. An additional source-window diagnostic repeats the frozen construction with RNG 147019. All six training/checkpoint checks finished before any confirmation forward pass. The final protocol was frozen at 17:16:18 UTC on 8 October 2026 and publicly precommitted before confirmation; no subsequent method tuning used it. Near duplicates are not audited. The protocol hash and freeze time were published before the seed 44 interventions completed.

## 5. Structural and prediction results

### 5.1 Coverage at the supplied horizon

The original consumes 836,864 sources containing 623,932,921 BOS-inclusive tokens. These partition exactly into 499,890,432 emitted row tokens, 96,750,834 discarded tail tokens and 27,291,655 buffered tokens. The emitted-row total exceeds target count by one initial token per row. Of 225,735 crop events, the median retained prefix is 14 tokens and 15,711 emit only BOS.

The protected 999 long sources contain 27,244,798 tokens, 4.37% of arrived source mass and 99.83% of all buffered mass. The shorter official development stream protects 5,892,120 tokens, 20.86% of its arrived source mass. Its first over-context source appears only at 13,895,680 target offset; none appears in its 2.10 M or 10.49 M prefixes. Across 20 source-length permutations, the training startup delay remains 12.99–14.84 M targets. These permutations test order sensitivity within one corpus, not corpus transfer.

Token retention is not monotone in original document length. For example, original 33–128 token sources retain 20.7% of their loaded token mass, 513–1024 retain 99.6%, and 1025–2049 retain 100%. All 785 arrived sources above 16384 remain buffered at the training horizon. Total crop loss and prefix selection are prior-known phenomena; the audit measures their realization and separates them from retained-source exclusion.

The lossless continuation replay discards zero tokens but leaves 25,129,596 buffered at the same target budget, including 25,049,286 tokens in 999 untouched protected original sources. Segment-first instead leaves 302,148 buffered and discards 23,430,384, while adding 52,544 BOS markers. It consumes 702,208 original sources and raises the fraction of emitted tokens from over-context original sources from 11.76% to 25.73%. These source counts and weights matter when interpreting learning differences.

### 5.2 Repeated-corpus implication

Completing the length census gives 846,848 eligible sources and 631,241,817 BOS-inclusive tokens. At $B=1000$, the following are necessary lower bounds on the source pass containing the first possible service of any source in each threshold class:

|Original length at least|Sources per pass|Earliest possible pass|
|---|---:|---:|
|16,384|789|2|
|32,768|196|6|
|65,536|39|26|
|131,072|9|112|
|290,219|1|1000|

We do not run 1000 training epochs or claim these bounds are exact service times. The theorem supplies the bounds; repeated small corpora validate implementation details. Resetting/flushing the buffer at an epoch boundary would change the hypotheses.

### 5.3 Matched training comparisons

|Condition|Seed|Official BPB|CE|Perplexity|Timed s|Total s|Peak MiB|
|---|---:|---:|---:|---:|---:|---:|---:|
|baseline|43|0.99370935|2.78440629|16.19020|1078.404|1162.003|22804.45|
|random_crop|43|0.99550330|2.78943301|16.27179|1078.648|1130.253|22804.45|
|segmented|43|1.00293320|2.81025181|16.61410|1077.787|1129.042|22804.45|
|baseline|44|0.99559622|2.78969337|16.27603|1078.178|1129.811|22804.45|
|random_crop|44|0.99590521|2.79055916|16.29013|1079.352|1131.211|22804.45|
|segmented|44|1.00649258|2.82022531|16.78063|1080.424|1131.664|22804.45|

Here `random_crop` denotes random spans and `segmented` denotes segment first. All six runs use 499,646,464 targets, 953 updates and 50,332,176 parameters. All saved-checkpoint evaluations reproduce the official scores exactly. Random spans worsen official BPB by 0.001794 at seed 43 but only 0.000309 at seed 44; a stable effect size should not be inferred. Segment first worsens it by 0.009224 and 0.010896. Better source coverage therefore does not imply a better original-population score in these experiments.

The inherited dense training FLOP estimate is $1.19455\times10^{17}$ per run for every condition. It includes non-embedding matrix work and attention, omitting optimizer, normalization, softmax and input-pipeline overhead. Identical model computation makes the resource comparison direct; measured loader overhead remains in training time. The six central runs total 2.998 billion training targets, 6472.79 timed seconds and 6813.98 complete-run seconds. Additional checkpoint checks and the diagnostic/confirmation evaluations total 422,838,272 forward positions, including window padding checks. Complete run/checkpoint summaries, learning curves, individual evaluation times and CPU audit timings are in the supplement. The original full CPU audit's 401-second elapsed time includes a research-break pause. Five unrelated earlier training screens supplied additional checkpoints for Section 5.6; their costs are disclosed separately, not attributed to the six-run packing comparison. Training curves summarize different sampled populations and are not shared evaluation objectives.

### 5.4 Untouched original-style confirmation

The frozen original-style confirmation score uses 10,485,760 targets. Exact duplicate exclusions leave 127- or 128-document refill batches; the CPU audit and every GPU evaluation agree on the input/target fingerprint. This stream emits no source whose original length exceeds 2049, as measured before scoring.

|Condition|Seed|BPB|Delta vs same-seed control|CE|Perplexity|
|---|---:|---:|---:|---:|---:|
|baseline|43|0.99425177|+0.00000000|2.78518215|16.20277|
|random_crop|43|0.99608374|+0.00183197|2.79031401|16.28613|
|segmented|43|1.00384198|+0.00959020|2.81204703|16.64395|
|baseline|44|0.99616274|+0.00000000|2.79053531|16.28974|
|random_crop|44|0.99652583|+0.00036309|2.79155244|16.30631|
|segmented|44|1.00712418|+0.01096144|2.82124141|16.79769|

Both interventions worsen this score at both seeds. The same-seed ordering is unchanged from development. Confirmation validates the direction of this penalty; it does not turn it into a claim about all source populations.

### 5.5 Conditional source windows and the reset explanation

Development uses 1693 source documents and 2362 windows; confirmation uses 1651 sources and 2278 windows, with 3,214,901 actual text targets per checkpoint. Each long source supplies paired beginning and tail windows. These conditional comparisons intentionally oversample long sources and are not pooled into a corpus-weighted score.

At seed 43 on development, random spans change beginning/tail BPB by +0.00196/−0.00772 for 4097–8192-token sources and +0.00509/−0.00644 for 8193–16384-token sources. At seed 44 the corresponding values are +0.00108/−0.00868 and +0.00488/−0.00816. Segment first also trades worse beginnings for better tails in both strata and both seeds. All strata, scores and exploratory intervals are retained in the supplement.

The table gives all eight predeclared confirmation contrasts. Each delta compares an intervention with its same-seed baseline; the interaction subtracts its beginning delta from its tail delta. Intervals use 10000 paired-source bootstrap replicates and Bonferroni-adjusted 99.375% quantiles across these eight contrasts.

|Condition|Seed|Source length|Sources|Prefix delta|Tail delta|Tail minus prefix|99.375% interval|
|---|---:|---|---:|---:|---:|---:|---|
|random_crop|43|4097–8192|256|+0.001623|-0.009031|-0.010654|[-0.014933, -0.006802]|
|segmented|43|4097–8192|256|+0.005745|-0.006486|-0.012230|[-0.017320, -0.007555]|
|random_crop|43|8193–16384|87|+0.005389|-0.003160|-0.008549|[-0.013126, -0.004825]|
|segmented|43|8193–16384|87|+0.001987|-0.008230|-0.010217|[-0.016628, -0.004889]|
|random_crop|44|4097–8192|256|+0.001029|-0.007496|-0.008525|[-0.011939, -0.005427]|
|segmented|44|4097–8192|256|+0.006887|-0.004329|-0.011217|[-0.015877, -0.007197]|
|random_crop|44|8193–16384|87|+0.004135|-0.004835|-0.008970|[-0.013418, -0.005178]|
|segmented|44|8193–16384|87|+0.003027|-0.006518|-0.009545|[-0.016338, -0.004240]|

All eight interactions and all eight absolute tail deltas are negative, while the beginning deltas are positive. Every adjusted interaction interval excludes zero. This is conditional source uncertainty for these trained checkpoints; two model seeds do not provide a training-seed confidence interval. The largest source stratum (>16384) contains only 28 confirmation sources. Its segmented seed 43 interaction excludes zero at the exploratory 95% level, but the other three intervals include zero; a consistent two-seed claim is unsupported. Ordinary 95% intervals across all other cells are exploratory.

A competing explanation is adaptation only to the immediate artificial BOS reset. A post-hoc **development-only** decomposition divides target positions into [0,32), [32,128), [128,512) and [512,2048). It measures each bin's loss difference divided by the full window's byte count, so contributions add to the whole-window BPB difference. Bin sums reproduce the previous full-window scores within $10^{-7}$; byte/token sums match exactly.

|Condition|Seed|Source length|Full tail delta|Contribution first 128|Contribution after 512|
|---|---:|---|---:|---:|---:|
|random_crop|43|4097–8192|-0.007723|-0.001444|-0.005366|
|segmented|43|4097–8192|-0.006072|-0.001560|-0.004082|
|random_crop|43|8193–16384|-0.006437|-0.001683|-0.004088|
|segmented|43|8193–16384|-0.011515|-0.002427|-0.007220|
|random_crop|44|4097–8192|-0.008682|-0.001729|-0.005378|
|segmented|44|4097–8192|-0.005020|-0.001526|-0.003167|
|random_crop|44|8193–16384|-0.008163|-0.001749|-0.005011|
|segmented|44|8193–16384|-0.009899|-0.002134|-0.006109|

Across these eight tail cells, positions after the first 512 contribute 61–70% of the total improvement; the first 128 contribute 18–31%. Thus the measured effect is not confined to the immediate reset. These are contributions, not comparisons of equally sized bins, and the table does not imply larger per-token effects at late positions. The entire tail window still lacks preceding document context and starts with an artificial BOS. We therefore do not infer improved prediction of naturally conditioned long-document tails. This diagnostic did not select a new confirmation hypothesis or training variant.

### 5.6 Unchanged rankings within the original evaluation population

A separate check evaluates seven available seed 43 checkpoints on the identical original 20.97-million-target population. Full scores reproduce within $4\times10^{-9}$ BPB, and all target hashes agree. The checkpoint set contains the original and random-span models plus five earlier sharing/gradient-estimation screens; it is an opportunistic set, not a representative sample of pretraining methods. The compact supplement preserves their row-level sufficient statistics and exact comparison code.

There are no ranking reversals between the full score and prefixes of 0.262 million, 2.10 million or 10.49 million targets. Among 18 method/prefix contrasts, only the random-span contrast at 2.10 million lies outside the nominal 95% interval from 1000 same-size uniform-row subsets. This is not strong multiplicity-adjusted evidence. The structural source omission therefore does not establish practical ranking harm on this tested fixed population. The conditional effects in Section 5.5 concern a different population: the original development stream emits no source longer than 4096, so its score cannot contain the effects on larger sources.

## 6. Limits and practical interpretation

The result applies to the specified minimum-count, minimum-span-fallback family, not all best-fit or lossless packers. Fixed token budgets do not make source populations identical. More coverage is not automatically better prediction. Random-span changes preceding context and segment-first changes several data quantities; neither is claimed as a new algorithm. Current experiments concern one small model, tokenizer and corpus. Two seeds do not establish a population-level variance estimate, and the conditional window sample is not a natural corpus-weighted objective. The position decomposition excludes an effect restricted to the immediate reset, but natural preceding context remains untested.

A practical audit should record four quantities separately: token mass emitted/discarded/buffered; original sources that have started; positions exposed within each source; and the finite evaluation population. The short checker is intended to make these distinctions inspectable. A mass-conserving test alone cannot establish the source-inclusion property proved false here.

## 7. Reproducibility

The supplement contains the exact baseline and two loader variants, a generator for all six configurations, frozen protocols, source-audit and evaluation scripts, loss sufficient statistics, all result summaries, source-length histograms, printed training curves and SHA256 manifests for code and retained checkpoints. Corpus text and model weights are omitted. The public ClimbMix inputs, exact shard/tokenizer hashes, pinned environment and full regeneration commands are specified in `REPRODUCE.md`. The supplied baseline derives from autoresearch [1] and retains its upstream MIT declaration; the public corpus card also declares MIT. New research scripts carry an MIT license. Dependencies retain their own licenses.

Four small CPU checks permit inspection without training: `packing_checker.py --self-test` checks the independent implementations and repeated-corpus examples; `check_length_histogram.py` verifies source mass and pass bounds; `verify_evaluation_summary.py` reconstructs prefix rankings and uncertainty; and `verify_window_evidence.py` reconstructs all development and confirmation bootstraps and position decompositions. The first two use only Python's standard library; the others need NumPy. They check arithmetic and the stated examples, not independent provenance of the trained models. Full reproduction requires the public corpus and six GPU training runs. Cross-hardware bitwise training is not promised; exact checkpoint re-evaluation, input fingerprints and numeric tolerances are documented.

The frozen comparison protocol SHA256 is `6d6e9eaa7ea2d056c0c8aa0685e107378c524036c9c40f73f103aae34d231200`. The original-style confirmation stream SHA256 is `0988e021558fd2b70c2a3b57a29f6544200e91dd01b5ad58cacb2e9aaa34ad17`. The code enforces completion of all six original checkpoint checks before confirmation. No trained variant was chosen or adjusted using confirmation results.

## References

[1] Andrej Karpathy. Autoresearch, pinned commit 228791fb499afffb54b46200aca536f79142f117, 2026. https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117

[2] AliFozooni. Preserve split document suffixes in make_dataloader. Public autoresearch PR #372, 2026. https://github.com/karpathy/autoresearch/pull/372 . Audited head adfd0fac0ac9e6a48b975765332305f7d45ebea7.

[3] handsomesun. Dataloader: reuse cropped remainders to reduce token waste. Public nanochat PR #544, 2026. https://github.com/karpathy/nanochat/pull/544

[4] Hantian Ding, Zijian Wang, Giovanni Paolini, Varun Kumar, Anoop Deoras, Dan Roth, Stefano Soatto. Fewer Truncations Improve Language Modeling, 2024. https://arxiv.org/abs/2404.10830v2

[5] Yanbing Chen, Ruilin Wang, Zihao Yang, Lavender Yao Jiang, Eric Karl Oermann. Refining Packing and Shuffling Strategies for Enhanced Performance in Generative Language Models, 2024. https://arxiv.org/abs/2408.09621v1

[6] Ruicheng Yin, Xuan Gao, Changze Lv, Xiaohua Wang, Xiaoqing Zheng, Xuanjing Huang. Improving Continual Pre-training Through Seamless Data Packing, 2025. https://arxiv.org/abs/2505.22018v2

[7] James Roberts and Dario Rossi. Size-based scheduling vs fairness for datacenter flows: a queuing perspective, 2022. https://arxiv.org/abs/2203.12983v1
