# Which vocabulary rows can a quantized language model afford to change?

## One precision map for two model sizes

A model that uses the same precision for every vocabulary row spends an extra bit on rare candidates as readily as on likely ones. A model with a large vocabulary can instead copy selected rows from a published quantized checkpoint and reduce the precision of the rest. The copy has a specific behavioral consequence. When both projections use identical per-row arithmetic, two copied output rows retain their relative odds on every shared hidden state. We check this under equal-shape BF16 projection. A model that also uses those rows as input embeddings can lose this property as soon as the input touches a changed row.

We tested both cases on Qwen3 [1]. We selected 55,230 of 151,936 token IDs using next-token probabilities from the dense 8B model. The published 8B and 4B Q5_K_M checkpoints share a tokenizer and use the higher-precision Q6_K block format for their readout. We copied selected Q6_K rows and encoded the others in Q4_K. On both models, the same selection produced a smaller complete package and lower forward KL from the dense model than a uniform Q5_K vocabulary table in four languages. On 8B we also measured the effect on generated translations. On 4B we separately varied how the shared table was used during lookup and readout.

## Prior work and comparison

GroupReduce allocates approximation capacity across vocabulary blocks using weighted low-rank compression of the embedding and softmax matrices [2]. Adaptive softmax exploits word frequency to reduce the cost of training the output distribution [3]. Adaptive inputs assign variable capacity to word groups and can share parameters with the output distribution [4]. Vocabulary trimming reduces a multilingual model by deleting rows for a particular deployment language [5]. The packages here keep every token ID available. Frequency-dependent precision also has a direct precedent in recommender embeddings. Yang et al. cache frequently or recently accessed rows in high precision during training [6], and Li et al. group features by frequency and learn the precision for each group [7]. These works motivate the simple alternative of ranking by observed token counts. We compare the dense-teacher ranking with uniform precision and random retention on both models. On 8B we also compare with a text-only selection on exactly the same calibration sentences and with a map based on tokenizer order.

QTIP uses trellis coding for low-bit weights [8]. The Qwen3-8B study by krylov_schur uses distinct rates for the input embedding and output head, spends vocabulary savings on the decoder, and measures packed execution at a much lower whole-model rate [9]. Our comparison holds each published decoder fixed and changes which original rows survive *within* one tensor. This design identifies the effect of the selection and where a guarantee about copied rows ceases to apply. The byte savings below measure the incremental effect on the published checkpoints.

## Selection, storage and evaluation

For each vocabulary row $v$, we summed the dense 8B model's probability of token $v$ over 2,645 sampled next-token positions in each of English, Spanish, Arabic and Simplified Chinese. The 10,580 positions came from 494 aligned FLORES-200 dev sentences [10]. We ranked by descending sum, breaking ties by increasing token ID. The count of 55,230 came from the complete-file budget of an earlier 8B mixed-precision readout. The selected 36.35% of rows covered 99.13% of calibration probability. A reproducible SHA-256 permutation selecting the same number of rows covered 38.83%. The 4B comparison reused both maps without refitting.

For an original row we copied its published Q6_K bytes. We formed Q4_K and Q5_K alternatives from the dense BF16 weights with stock llama.cpp b6500 [11], using its null-importance-matrix encoder. Both mixed models draw from exactly the same original and cheap candidate for each row. Their packed streams store a Q6_K row bank, a Q4_K row bank, and a little-bit-first 18,992-byte map indexed by token ID. Rows within each bank are in ascending ID order. We include the decoder, tokenizer, metadata, table directories, alignment and map when counting complete GGUF bytes. The 4B file stores a single shared table. Its two-use controls below diagnose function and never enter the package-size comparison.

We evaluated all 1,997 English source sentences in NTREX-128 [12] and their Spanish, Arabic and Simplified Chinese translations. There were 123 aligned news documents and 264,413 next-token targets in total per model. We reset context at each sentence and added no beginning-of-sequence token. The normalized NTREX English sentences had zero exact matches to the FLORES evaluation and calibration sentence collections. Both model sizes used this same NTREX panel. Each student used the decoder and normalization weights from its own published GGUF, expanded to BF16 under Hugging Face SDPA. We used identical projection geometry when comparing elementwise logits or hidden states.

For each target we computed forward KL from its dense model to the student. A second reference used the published Q5_K_M model with its original Q6_K readout. For the primary result we averaged target values within a document, then gave each document equal weight within its language. The reported language averages likewise weight all four languages equally. Document wins compare the paired values before aggregation. Post hoc confidence intervals for the mean four-language gains draw 123 document IDs with replacement, pairing the same ID across languages and arms in each of 10,000 draws. These intervals describe variation across aligned news documents conditional on the selected checkpoints and maps.

## Byte savings and fidelity

| Model | Complete published Q6_K | Uniform Q5_K | Ranked or random Q6_K/Q4_K | Uniform Q4_K | Ranked saving vs Q5_K |
|---|---:|---:|---:|---:|---:|
| 8B, output only | 5,851,112,224 | 5,768,459,040 | 5,749,010,080 | 5,690,667,808 | 19,448,960 |
| 4B, shared table | 2,889,513,184 | 2,837,854,944 | 2,825,706,752 | 2,789,235,424 | 12,148,192 |

Table 1. Complete package lengths in bytes. Relative to the original packages the savings were 102,102,144 bytes (1.75%) on 8B and 63,806,432 bytes (2.21%) on 4B. The incremental savings relative to uniform Q5_K were 0.34% and 0.43% respectively.

![On both models, ranked retention saves more complete bytes than uniform Q5_K while producing a smaller rise in dense-reference KL. Random retention costs exactly as many bytes as ranked and has a larger KL increase.](supplement/figure-1.png)

Figure 1. Each point is a complete package. The ordinate subtracts the published model's dense-reference KL from the student's dense-reference KL. The four-language mean is shown with the minimum and maximum language differences. The bars span languages and the two same-size packages share the same horizontal coordinate.

| Model | Language | Ranked gain over Q5_K | Docs won / 123 | Ranked gain over random | Docs won / 123 | Ranked cost over published Q6_K |
|---|---|---:|---:|---:|---:|---:|
| 8B | English | 0.003188 | 123 | 0.010114 | 123 | 0.000770 |
| 8B | Spanish | 0.003196 | 123 | 0.007881 | 123 | 0.000400 |
| 8B | Arabic | 0.002746 | 123 | 0.010200 | 123 | 0.000308 |
| 8B | Simplified Chinese | 0.001780 | 122 | 0.008755 | 123 | 0.000376 |
| 4B | English | 0.000257 | 76 | 0.005942 | 122 | 0.000990 |
| 4B | Spanish | 0.001134 | 115 | 0.007621 | 123 | 0.000561 |
| 4B | Arabic | 0.005159 | 123 | 0.025471 | 123 | 0.000566 |
| 4B | Simplified Chinese | 0.001756 | 110 | 0.007687 | 123 | 0.000502 |

Table 2. Differences in forward KL from the dense model in nats per next-token target. A positive gain favors ranked. The cost column subtracts published KL from ranked KL. Pooling targets across documents preserved the direction of every comparison.

The mean gain over Q5_K was 0.002728 nats on 8B (paired 95% interval 0.002656 to 0.002798) and 0.002077 on 4B (0.001941 to 0.002215). Against random the corresponding mean gains were 0.009238 and 0.011680. Both models exceeded the prespecified 0.001 gain and won at least 70% of documents in each language. The 8B experiment also set a maximum dense-KL increase of 0.0003 against the original Q6_K head. All four languages exceeded it. The 4B English gain over Q5_K was particularly small, with 47 documents favoring Q5_K. Observed-token negative log likelihood favored Q5_K over ranked on 8B English and Spanish and on 4B Spanish.

At almost the same 8B file size (128 extra bytes), a previously fitted mixed INT4/INT8 GPTQ head gave lower dense-reference KL than ranked retention in English, Spanish and Arabic. Ranked gave lower dense-reference KL in Chinese and lower published-reference KL in all four languages. Preserving the published model's decisions and approximating the original dense teacher can therefore favor different heads. The 4B experiment used native-format controls. The published Q6_K rows may have been encoded with a different calibration procedure. The ranked and random comparison isolates row choice by sharing both candidates for every token.

## What copying a row preserves

Fix the published decoder’s hidden state, let $z$ be its original logits, $p$ the published softmax, and let $\delta_i$ be the logit change for token $i$. On the retained set $R$, $\delta_i=0$ under identical arithmetic. The difference between two retained logits is identical. Their mathematical softmax log odds therefore agree even if the normalizer changes. Writing $q$ for the mixed softmax gives

$$
D_{\mathrm{KL}}(p\Vert q)
=\log\!\left(1+\sum_{i\notin R}p_i(\exp(\delta_i)-1)\right)
-\sum_{i\notin R}p_i\delta_i .
$$

This expression measures published-reference KL. It follows by taking the published-distribution expectation of the difference in log probabilities. The dense-reference comparisons in Table 2 use each model’s separate dense predictions. Tail mass alone omits both the sizes of the logit errors and their signs. At the first evaluated prefix in every document and language on 8B (492 prefixes), both maps preserved every retained BF16 logit. Evaluating the identity with the stored prefix statistics gave a maximum absolute residual below $2.5\times10^{-15}$ nats. Across all Spanish targets, scaling the random map's published-reference KL by the ratio of demoted probabilities predicted 0.000701 nats for ranked and the measured value was 0.000440. In Arabic it predicted 0.000242 and the measurement was 0.000353.

For a tied table, the original causal computation produces the original hidden state as long as every input row encountered since the start of the sentence was retained. This follows by applying the same decoder blocks to identical inputs in the same arithmetic. Once the input includes a demoted embedding, the hidden state can change and two original rows can score differently relative to one another. We tested this prediction by applying the 4B ranked table to lookup alone, readout alone, and both. A winner comparison is eligible when both the published winner and the student winner belong to $R$, using the same tie rule.

| 4B language | Intact prefix positions | Winner switches / eligible, intact | Positions after a demoted input | Winner switches / eligible, after demotion |
|---|---:|---:|---:|---:|
| English | 20,056 | 0 / 19,602 | 30,999 | 624 / 30,085 |
| Spanish | 29,115 | 0 / 28,052 | 45,560 | 760 / 43,871 |
| Arabic | 77,179 | 0 / 77,049 | 9,105 | 201 / 9,080 |
| Simplified Chinese | 39,082 | 0 / 38,680 | 13,317 | 254 / 13,056 |

Table 3. Position counts reset at sentence boundaries. The position that reads the first demoted input is included in the last two columns.

All 165,432 intact prefix positions had bit-identical final BF16 hidden states. On all 98,981 positions that had encountered a demoted input, at least one hidden component differed. With only readout changed there were zero switches among 259,485 eligible winner pairs over the entire panel. With both uses changed there were 1,839 switches among the 96,092 eligible positions after demotion. Taking only affected prefixes in each document and averaging over documents with such prefixes, the published-reference KL of the tied system exceeded that of output-only by 0.001726, 0.001202, 0.001963 and 0.001494 nats in English, Spanish, Arabic and Chinese. Across *all* Arabic prefixes the input-only and output-only substitutions cost 0.000217 and 0.000550 published-reference nats respectively. In English the corresponding costs were 0.001044 and 0.000726. Input exposure matters when transferring a ranking that was fitted for output predictions.

## Generated translation on 8B

We translated all 1,997 NTREX English sources into Modern Standard Arabic and Simplified Chinese. The three heads used identical official decoder weights, the Qwen chat template with thinking disabled and greedy decoding. We scored corpus chrF2 on its 0–100 scale [13] after the six generation passes had committed their outputs. Before inspecting generated results we set the maximum tolerable loss relative to Q6_K at 0.5 points in each direction and used paired document bootstrap lower bounds. These source documents had already been used in the next-token study.

| Target | Q6_K chrF2 | Ranked chrF2 | Q5_K chrF2 | Ranked minus Q6_K | One-sided 95% lower bound | Token-identical to Q6_K |
|---|---:|---:|---:|---:|---:|---:|
| Arabic | 46.052 | 46.059 | 45.983 | +0.007 | −0.015 | 1,950/1,997 |
| Simplified Chinese | 31.380 | 31.350 | 31.329 | −0.029 | −0.061 | 1,948/1,997 |

Table 4. The 10,000 bootstrap draws resampled documents with replacement and used the same draw for all three arms and both directions. Both lower bounds exceeded −0.5. The two-sided 95% intervals for ranked minus Q6_K were [−0.018, +0.033] and [−0.068, +0.012] respectively.

For the untied model, an identical generated prefix keeps the same hidden state. If greedy sequences first diverge, at least one of the two greedy winners must therefore be demoted. All 96 first differences met this prediction. Uniform Q5_K changed 1,016 Arabic and 570 Chinese output sequences, despite similar corpus chrF2. Relative to the original Q6_K head, exact generated tokens, corpus translation quality and next-token KL measure different effects of the same compression decision.

## What the teacher adds over the calibration text

The random map gives each row an equal chance, while a deployer can already use the calibration text and tokenizer at little cost. We ranked 8B rows by the observed next-token count on the 10,580 sampled calibration positions, then by count among all 64,722 next tokens from those 494 aligned sentences in four languages. We resolved further ties by counting overlapping occurrences of each token’s byte string within each original UTF-8 sentence, then by increasing token ID. Only 24,493 IDs had positive support on any key. All fit in the 55,230-row budget and increasing token ID filled the other 30,737 places. At this operating point the control therefore keeps every piece present in the text and uses tokenizer order for the rest. A second control selected the first 55,230 IDs directly. Both maps were frozen before scoring. They retained 94.89% and 65.47% of dense calibration probability respectively. Fitting the text-only map took 1.13 seconds on CPU.

| 8B language | Teacher-ranked KL | Text-only KL | Token-ID order KL | Teacher gain over text | Documents won / 123 |
|---|---:|---:|---:|---:|---:|
| English | 0.024584 | 0.024835 | 0.024573 | 0.000250 | 104 |
| Spanish | 0.018394 | 0.018671 | 0.019549 | 0.000277 | 110 |
| Arabic | 0.020664 | 0.021096 | 0.032985 | 0.000432 | 120 |
| Simplified Chinese | 0.022660 | 0.025585 | 0.031591 | 0.002925 | 123 |

Table 5. All three packages use exactly 5,749,010,080 complete bytes and the same candidate weights. Each original and teacher-ranked sentence score from the preceding 8B fidelity experiment replayed exactly. KL is measured against dense 8B.

The four-language mean gain over text-only was 0.000971 nats per target (paired 95% interval 0.000933 to 0.001009). It cleared the prespecified gain of 0.0005 and the 70% document-win threshold in every language. Chinese accounted for 75.3% of the total gain. Text-only already improved on uniform Q5_K in the other three languages, while in Chinese it increased KL by 0.001145. In English, token-ID order alone performed comparably to the teacher, with a paired interval for the teacher-minus-ID difference of −0.000046 to +0.000073. The experiment tests one corpus size, tokenizer order and policy for assigning precision to unseen IDs. Wider text coverage or different priors could improve the cheap control.

## Scope and reproduction

The two models share a tokenizer and model family. The languages were present in calibration, and both experiments used the same aligned news documents. One deterministic random map estimates the effect of this matched selection. New tokenizers, rare-language deployment and long conversational histories require their own tests. The controls isolate lookup and readout on the same 4B model. Differences in effect size between 4B and 8B can also reflect their decoders, widths and source quantization.

All quality experiments used expanded BF16 weights. The two-bank layout requires a compatible serving graph. On one RTX 5090 the 8B fidelity study took 732 seconds and the translation study took 822 seconds. The 4B study took 1,218 seconds and the 8B text-control study took 630 seconds. Within-run table preparation took 79.5 seconds for the six-head 8B study and 44.0 seconds for 4B. Fitting the 8B ranking preceded these measurements. The separate FLORES run timed two teacher maps and their installed-package checks together at 45.05 seconds on an RTX 5090. A standalone fit time for the multilingual teacher map is unavailable. The figures describe experiment and preparation cost. End-to-end native throughput for these files and generated 4B translation quality remain unmeasured.

The supplement supplies the bitmaps, package byte accounting, per-document sufficient statistics, translation counts and divergence IDs. Extract it and run the checker with Python and NumPy to reproduce Tables 1–5. A second utility rebuilds each ranked GGUF from its public inputs on CPU. Independent full-stream replays on both models reproduced the original candidate SHA-256 hashes. The README identifies each public checkpoint, quantizer and dataset at a fixed revision and gives the prompts, selection rule, arithmetic and scoring settings. The four-language post hoc intervals use sorted document IDs, NumPy PCG64 seed 20261120, 10,000 paired draws and linear percentiles. The numerical checker reconstructs byte geometry and reductions from recorded measurements. Checking the hidden-state comparisons element by element requires running the model again.

## References

[1] Qwen Team. *Qwen3 Technical Report*. 2025. https://arxiv.org/abs/2505.09388

[2] Chen et al. *GroupReduce: Block-Wise Low-Rank Approximation for Neural Language Model Shrinking*. NeurIPS, 2018. https://arxiv.org/abs/1806.06950

[3] Édouard Grave et al. *Efficient softmax approximation for GPUs*. ICML, 2017. https://proceedings.mlr.press/v70/grave17a.html

[4] Alexei Baevski and Michael Auli. *Adaptive Input Representations for Neural Language Modeling*. ICLR, 2019. https://arxiv.org/abs/1809.10853

[5] Asahi Ushio, Yi Xin Zhou and José Camacho-Collados. *An Efficient Multilingual Language Model Compression through Vocabulary Trimming*. 2023. https://arxiv.org/abs/2305.15020

[6] Jie Yang, Jianyu Huang, Jongsoo Park and Ping Tak Peter Tang. *Mixed-Precision Embedding Using a Cache*. 2020. https://arxiv.org/abs/2010.11305

[7] Shiwei Li et al. *Mixed-Precision Embeddings for Large-Scale Recommendation Models*. 2024. https://arxiv.org/abs/2409.20305

[8] Albert Tseng, Qingyao Sun, David Hou and Christopher De Sa. *QTIP: Quantization with Trellises and Incoherence Processing*. NeurIPS, 2024. https://arxiv.org/abs/2406.11235

[9] krylov_schur. *Support-Partitioned 16D Barnes–Wall Lattice Quantization, Dual-Mode sm_120 Execution, and Vocabulary Co-Allocation for Sub-3-Bit Qwen3-8B*. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/3/v1

[10] NLLB Team et al. *No Language Left Behind: Scaling Human-Centered Machine Translation*. 2022. https://arxiv.org/abs/2207.04672

[11] llama.cpp and GGML contributors. *llama.cpp*, release b6500. https://github.com/ggml-org/llama.cpp/tree/a7a98e0fffed794396b3fbad4dcdbbc184963645

[12] Christian Federmann, Tom Kocmi and Ying Xin. *NTREX-128 — News Test References for MT Evaluation of 128 Languages*. 2022. https://aclanthology.org/2022.sumeval-1.4/

[13] Maja Popović. *chrF: character n-gram F-score for automatic MT evaluation*. WMT, 2015. https://aclanthology.org/W15-3049/
