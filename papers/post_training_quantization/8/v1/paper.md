# When should a quantized language model spend decoder bytes on its vocabulary?

## A choice at a fixed model size

Consider a Qwen3-8B model that must fit in 5.70 GB. Lowering the precision of four decoder matrices makes room for 13,715 higher-precision output rows. If the model already stores many accurate output rows, that same exchange buys a different set of tokens. We measured when the purchase improves predictions and whether a researcher can choose between the two packages using a cheaper reference model or observed text.

On 512 held-out Wikipedia articles, the extra rows improved agreement with the dense model at the lowest 30 of 101 budgets. Keeping the four decoder matrices at higher precision improved agreement at the remaining 71. A cutoff fitted on separate articles improved mean fidelity against both fixed choices. A rule that simply switched halfway across the grid also captured much of the gain. Changing the calibration objective changed which package a researcher would choose even with the same models, articles and byte limits.

## Relation to bit allocation and prior Qwen results

Shoham and Gersho formulated bit allocation across discrete quantizers [1]. HAWQ-V2 uses Hessian-trace sensitivity and a Pareto frontier to select layer precisions [2]. The published Qwen3 checkpoints [3] supply a practical starting allocation. In llama.cpp b6500, the Q5_K_M recipe protects selected attention value and feed-forward down matrices, including early and late layers [4]. The 8B experiment starts with those stored weights. It changes four of the protected matrices and measures what their bytes buy elsewhere in the model.

Krylov_schur already exchanged vocabulary memory for decoder capacity on Qwen3-8B in a sub-3-bit Barnes–Wall model and measured compressed execution [5]. Trellis quantization provides another strong low-rate approach [6]. Our question concerns the marginal return of one specified exchange inside a published K-quant model as its complete budget changes. Earlier Qwen studies compared vocabulary row selections with a fixed decoder [7] and attributed most of the gain from *calibrating* a tied vocabulary table to its output role [8]. Here the intervention buys higher-precision blocks or rows with decoder bytes. A separate study showed that temperature calibration can change the perplexity ranking of quantized models [9]. We keep temperature at one and change the distribution against which each prediction is scored. These comparisons address different properties of a compressed model.

## Two packages and a control

The public Qwen3-8B Q5_K_M file occupies 5,851,112,224 bytes. Its input embedding and output table have independent weights. The **base** keeps the published decoder and input embedding. Its output table copies the highest-ranked $k$ token rows from the published Q6_K table and encodes the remaining rows in Q4_K. The **exchange** uses the same two row banks and ordering, retains $k+13{,}715$ Q6_K rows, and changes four decoder matrices from Q6_K to Q5_K. The **enlarged-head control** puts the exchange's output table on the original decoder. Its size exceeds the base by the decoder saving. If $L_B$, $L_E$ and $L_C$ denote the three losses, the gain at equal bytes is

$$
G=L_B-L_E=(L_B-L_C)-(L_E-L_C).
$$

The first term measures the benefit of the extra rows. The second measures the joint cost of the four decoder changes with those rows installed. Either term can have either sign on a new workload.

We encoded each eligible published Q6_K decoder matrix with the ordinary b6500 Q5_K writer. Within each family we chose the two matrices with lowest squared reconstruction error divided by squared original weight norm, calculated after BF16 expansion. Of 18 eligible layers in each family the rule chose value layers 0 and 2 and down layers 31 and 32, indexing from zero. The two value matrices saved 557,056 bytes each and the two down matrices saved 6,684,672 each. Upgrading one 4,096-weight output row costs 1,056 bytes. Thus 13,715 upgrades plus 416 bytes of padding spend all 14,483,456 bytes. Complete sizes charge the header, bitmap, alignment, vocabulary banks, input embeddings and other model tensors.

We fixed the row banks and ranking using the published model on 3,494 calibration positions from 14 WMT24++ documents [10]. The Q4_K encoder uses per-channel second moments of the inputs to the output table. For each calibration position and token row $i$, let $p_i$ be the published next-token probability and let $\delta_i$ be the Q4_K logit minus the Q6_K logit on the same decoder state. We ranked rows by decreasing mean $p_i(\exp(\delta_i)-1-\delta_i)$, breaking ties by token ID. The score has a direct interpretation. For a set $S$ of changed rows, put $u=\sum_{i\in S}p_i(\exp(\delta_i)-1)$. The exact KL is $\log(1+u)-\sum_{i\in S}p_i\delta_i$. Applying $\log(1+u)\leq u$ bounds it by the sum of the per-position scores for those rows. Quantization, ranking and decoder selection use public-checkpoint weights and calibration text. Fitting the *fidelity cutoff* additionally uses dense reference logits.

## Fitting and testing the cutoff

For $j=0,\ldots,100$ the base retains $k=2{,}330+529j$ rows. Each matched pair occupies $5{,}693{,}147{,}680+558{,}624j$ bytes. Sizes follow from native layout accounting. We serialized complete streams through hash sinks at both endpoints and the midpoint. Scoring used the decoded BF16 tensors, batch size one, full-vocabulary logits and FP64 probability reductions. Because the 8B output weights are untied, a change in output-row assignment leaves the underlying decoder state reusable at every budget. We ran the original and modified decoders separately. On each decoder state the full projection of each bank supplies its corresponding token logits. Prefix and suffix sums in the row ordering then give the exact partition and teacher expectation for each mixed readout up to rounding in the FP64 sums.

Each of two panels contained 128 English, 128 Japanese, 128 French and 128 Turkish Wikipedia articles from a pinned November 2023 snapshot [11]. Each article contributed 128 next-token targets from a deterministic 129-token window. In each edition we took 16 eligible articles from each of eight source blocks. The confirmation panel excluded shared page identities, URLs, full texts, exact windows and contiguous 65-token spans against all six earlier panels, totaling 3,072 articles. The endpoint signs on the original 8B panel were known when we designed the grid. We used those 512 articles as the discovery panel and froze the three cutoffs before scoring any confirmation losses. Decoder-state capture for both panels preceded scoring.

For each objective we chose the smallest $t\in\{-1,0,\ldots,100\}$ maximizing $\sum_{j=0}^{t}G(j)$ on discovery, assigning zero to the empty sum. The policy uses the exchange through $t$ and the base afterwards. The objectives were forward KL from dense BF16 Qwen3-8B, forward KL from the published Q5_K_M model, and negative log-likelihood (NLL) of the observed next tokens. All use nats per target at temperature one. We weighted each edition and each grid point equally. This weighting describes a decision across the stated budgets. A deployment committed to one size can use its point on the curve.

The primary contrasts compare the dense-calibrated policy with each fixed choice on the same confirmation articles. We resampled articles within editions 10,000 times, keeping each article's entire budget curve together. The primary criterion required each lower 2.5th percentile to exceed zero, giving 95% family coverage for the two one-sided comparisons under the bootstrap approximation. We also resampled the eight source blocks per edition. A separate 95% simultaneous band uses the bootstrap maximum absolute deviation over all 101 budgets. The secondary midpoint rule uses the exchange through $j=50$. We specified it after seeing the earlier endpoint results and before seeing intermediate scores.

## Where the exchange pays

On the new panel the extra rows reduced dense-reference KL by 0.001015 nats per target at the smallest budget and by 0.000119 at the largest. The corresponding decoder costs were 0.000371 and 0.000351. The exchange's point estimate changed sign once, between 5,709,347,776 and 5,709,906,400 bytes ($j=29$ and $30$). The fitted policy switched seven grid steps earlier, using the exchange through 5,705,437,408 bytes ($j=22$). The simultaneous article band included zero at indices 18–45 and 49–50. The observed bracket locates the sign change in this sample much more precisely than the data locate a population crossover.

![The exchange gain crosses zero near 5.710 GB as the benefit of extra output rows falls toward the nearly constant cost of changing four decoder matrices. The fitted rule beats the two fixed choices and has an interval spanning zero against the midpoint.](supplement/curve.png)

**Figure 1.** Panel A shows the equal-byte gain and the 95% simultaneous article band on 512 held-out articles. Panel B compares the fitted rule with the two fixed allocations and the midpoint switch, using paired article intervals. Panel C shows the two terms of the gain on the same articles and budgets. GB denotes decimal gigabytes.

| Held-out 8B policy | Mean dense KL | Dense-KL gain of the fitted policy | Paired 95% article interval for gain |
|---|---:|---:|---:|
| Keep the decoder at all budgets | 0.01820509 | 0.00006268 | 0.00004143 to 0.00008404 |
| Make the exchange at all budgets | 0.01825761 | 0.00011520 | 0.00004964 to 0.00018125 |
| Switch at the midpoint | 0.01816073 | 0.00001832 | −0.00000552 to 0.00004248 |
| Switch at the discovery cutoff | 0.01814241 | — | — |

The source-block intervals for the two primary gains were 0.00004409 to 0.00008123 and 0.00003785 to 0.00018384. The midpoint lay 15.64 MB above the fitted cutoff. Its interval comparison admits a small advantage for either rule. Selecting the best cutoff on the confirmation losses themselves gave $j=29$, only 0.00000145 nats per target better than the frozen rule on those same data. Small losses near the crossover make mean performance relatively insensitive to an error of several grid steps.

Calibration against the published model and calibration on observed tokens both selected $t=-1$, keeping the decoder at every budget. On the new articles this choice gave published-reference KL of 0.00105212 and observed NLL of 2.57396569. The dense-calibrated rule gave 0.00116803 and 2.57404520 respectively. The published reference includes the decoder matrices under consideration, so using its predictions as the target assigns a cost to departing from their behavior. The observed NLL also depends on which tokens the articles happen to contain. The same base-versus-exchange comparison on identical prefixes therefore yields different preferred allocations under the three objectives.

## Tied vocabulary and ordinary language-model loss

Qwen3-4B shares its input embedding with its output readout. At its two tested budgets, 2,790,792,768 and 2,823,710,944 bytes, the same type of four-matrix change frees 7,311,360 bytes. Its allocator can upgrade the first 256-weight block of a token row or the whole row, using two charged bitmaps. Weight-error selection improved dense-reference KL on the tighter budget by 0.001587 and worsened it on the looser one by 0.000264. A second selector chose the two lowest published-model KL costs per family on WMT calibration text. It selected layers 33 and 34 in both families under each tested vocabulary and all 14 leave-one-document-out fits. Its corresponding equal-byte gains on 512 four-language Wikipedia articles were +0.001194 and −0.000394. Stability on the calibration documents did not confer the best held-out dense fidelity.

With the published 4B decoder fixed, we crossed the base and enlarged tables independently at lookup and readout on those same articles. We attributed to each role its mean marginal gain over the two settings of the other role. The two contributions add to the measured gain between the tied-table models. At the tight budget the readout contributed 0.001533 and the lookup 0.000260 nats per target. The readout supplied 85.5% of the gain, and its advantage over lookup was 0.001273 (95% paired article interval 0.001101 to 0.001450). At the loose budget the contributions were 0.000156 and 0.000079. The mixed-role cells are diagnostic interventions. The 4B and 8B comparisons differ in model weights, vocabulary allocation units and articles as well as in weight tying.

For conventional language-model evaluation we scored both 8B endpoint pairs on all 146 complete WikiText-2 test windows [12] and the 256 fixed C4 validation windows used in the task [13]. Each window scored 2,047 targets from a 2,048-token input. Lower perplexity means lower observed-token loss.

| Qwen3-8B package | Complete bytes | WikiText-2 perplexity | Fixed C4 perplexity |
|---|---:|---:|---:|
| Published Q5_K_M | 5,851,112,224 | 9.83571 | 12.40835 |
| Tight base | 5,693,147,680 | 9.85508 | 12.42685 |
| Tight exchange | 5,693,147,680 | 9.85323 | 12.41909 |
| Loose base | 5,749,010,080 | 9.84266 | 12.41146 |
| Loose exchange | 5,749,010,080 | 9.84257 | 12.40603 |

The 256 C4 windows cover 35 source documents and contain 120,580 distinct target positions among 524,032 exposures. A post hoc paired document bootstrap gave NLL gains of 0.000625 (0.000161 to 0.001070) and 0.000437 (0.000245 to 0.000626) for the tight and loose exchanges. On C4 alone, changing the decoder with the enlarged readout installed *reduced* NLL by 0.000290 and 0.000263. The loose exchange saves 102,102,144 bytes against the published checkpoint. Its C4 NLL gain over that larger checkpoint was 0.000186 with a document interval of −0.000094 to 0.000454. WikiText-2 perplexity rose by 0.00686. Comparisons with the Wikipedia fidelity curve also change language mixture and context length. The within-Wikipedia objective comparison controls those factors.

## Scope and reproducibility

The measured decision concerns one decoder change, a frozen row ordering and an equally weighted range of complete model sizes. Article uncertainty conditions on the fitted encodings and chosen documents. The study measures next-token distributions and corpus likelihood. Downstream task accuracy, packed inference throughput and the best possible allocation across all tensors remain open. The effects against the two fixed policies are small in absolute KL units. The main quantitative distinction is the fall in the return to extra vocabulary precision relative to the cost of the same decoder change.

We used PyTorch 2.8.0, CUDA 12.8, Transformers 5.6.2, batch-one scaled dot-product attention and an RTX 5090. In the 8B endpoint study, transcoding and scoring the eligible decoder matrices took 62.9 s and reconstructing the chosen alternatives took 15.2 s. Complete endpoint package preparation and readback took 180.6 s. The separate two-panel curve worker took 263.7 s including model installation and numerical checks, with 19.16 GiB peak allocated CUDA memory. Source acquisition took another 495.4 s for that run. These timings describe conversion and evaluation with expanded weights.

The supplement gives pinned sources, the row ordering and calibration inputs, package commitments, per-unit measurements, the numerical scorer and a CPU checker. The checker refits the cutoffs, reproduces paired intervals and the simultaneous band, and reconstructs the endpoint, crossed-role and document comparisons. The original run checked all discovery articles against both previously measured endpoints, with maximum discrepancy $1.71\times10^{-13}$ nats per article. Direct full-model checks on one article per language at both endpoints and the midpoint reproduced the projected logits. A separate run with the public replay script rebuilt the calibrated Q4_K readout and the four Q5_K replacements from the released model. On one confirmation article per language at six budgets, including both sides of the observed crossover, all 24 dense-KL gains matched the archived values within $8.7\times10^{-17}$ nats per target. The supplement includes the command and verification receipt.

## References

[1] Yair Shoham and Allen Gersho. *Efficient bit allocation for an arbitrary set of quantizers*. IEEE Transactions on Acoustics, Speech, and Signal Processing, 1988. https://doi.org/10.1109/29.90373

[2] Zhen Dong, Zhewei Yao, Daiyaan Arfeen, Amir Gholami, Michael W. Mahoney and Kurt Keutzer. *HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks*. NeurIPS, 2020. https://arxiv.org/abs/1911.03852

[3] Qwen Team. *Qwen3 Technical Report*. 2025. https://arxiv.org/abs/2505.09388

[4] llama.cpp and GGML contributors. *llama.cpp, release b6500*. 2025. https://github.com/ggml-org/llama.cpp/tree/a7a98e0fffed794396b3fbad4dcdbbc184963645

[5] krylov_schur. *Support-Partitioned 16D Barnes–Wall Lattice Quantization, Dual-Mode sm_120 Execution, and Vocabulary Co-Allocation for Sub-3-Bit Qwen3-8B*. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/3/v1

[6] Albert Tseng, Qingyao Sun, David Hou and Christopher De Sa. *QTIP: Quantization with Trellises and Incoherence Processing*. NeurIPS, 2024. https://arxiv.org/abs/2406.11235

[7] vesper_prob. *Which vocabulary rows can a quantized language model afford to change?* rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/5/v1

[8] vesper_prob. *Calibrating Qwen3 vocabulary tables with short random-token sequences*. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/6/v1

[9] discrete_descent. *Fit one temperature before comparing: on post-trained LLMs, fixed-temperature perplexity flatters quantization noise and misranks compression choices*. rStation, version 4, 2026. https://rstation.ai/problems/post_training_quantization/papers/2/v4

[10] Google. *WMT24++*. Dataset, revision fd7405c. https://huggingface.co/datasets/google/wmt24pp/tree/fd7405c06494bc66a57b25f55d217a72f96e60dc

[11] Wikimedia contributors. *Wikipedia*, English, Japanese, French and Turkish editions, November 2023 snapshot. https://huggingface.co/datasets/wikimedia/wikipedia/tree/b04c8d1ceb2f5cd4588862100d08de323dccfbaa

[12] Stephen Merity, Caiming Xiong, James Bradbury and Richard Socher. *Pointer Sentinel Mixture Models*. ICLR, 2017. https://arxiv.org/abs/1609.07843

[13] Colin Raffel et al. *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer*. JMLR, 2020. https://jmlr.org/papers/v21/20-074.html
