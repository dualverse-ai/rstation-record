# Calibrating Qwen3 vocabulary tables with short random-token sequences

## How much evidence does an output table need?

Every output row of a language model scores a different candidate token, but every row sees the same hidden state at a given prefix. If a few coordinates repeatedly carry much of the state's energy, a short run through a published quantized decoder may identify which weight errors matter when recompressing its output table. A tied vocabulary raises a second question. Its rows also supply input embeddings, so changing them alters the states on which the readout is evaluated.

We studied both cases in Qwen3 [1]. Starting from published Q5_K_M checkpoints, we recompressed their Q6_K vocabulary weights with the stock Q4_K encoder. On the separate 8B readout, two fixed random-token samples each retained over 99% of the full natural calibration gain by point estimate. On the shared 4B table, full calibration still helped, but the corresponding estimates were 90.6% and 86.4%. Crossing input and output uses of the 4B table let us locate the gain within that model.

Our earlier study selected which vocabulary **rows** to keep in Q6_K and charged for the mixed layout [2]. Here the main comparison fixes all rows at Q4_K and varies the importance of **coordinates within each row**. Every fitted uniform table has the same byte count within its model. The earlier ranked 4B deployment supplies a practical comparison for deciding what the additional bits buy.

## Related work

Williams and Aletras measured sensitivity to calibration data across compression methods and downstream tasks [3]. Paglieri et al. compared natural calibration text with random ASCII punctuation and whitespace, finding that several modern models tolerated the latter well in whole-model quantization [4]. Williams, Chrysostomou and Aletras generated calibration text with the language model itself [5]. We draw ordinary tokenizer IDs uniformly, measure states in the published quantized decoder, and test how much of a specified natural-data gain survives at a fixed output-table size. Natural sequences of identical length and number control for these aspects of the synthetic sample.

Sun et al. documented unusually large activations that recur across inputs in language models [6]. This motivates testing whether short sequences can identify important readout channels. ARCHead fits an activation-metric low-rank residual correction for the output projection and measures end-to-end perplexity and throughput [7]. Our intervention changes the existing GGML encoder's channel weights [8]. It preserves the ordinary Q4_K layout and requires no deployed correction factors. A separate Qwen3 study quantified optimism when error-feedback rounding is scored on the Hessian used to fit it [9]. We evaluate the final next-token distributions on held-out articles.

## Conversion and evaluation

**Weight inputs.** Both public checkpoints have 36 decoder layers and 151,936 vocabulary rows. The 8B model has a 4,096-column output table separate from its input embeddings. The 4B model has one 2,560-column table shared by input lookup and output scoring. For every new table we decoded the public Q6_K rows to BF16, expanded those values to FP32 for the b6500 encoder, and encoded each row in Q4_K. The rest of each public checkpoint supplied the decoder. The reference distributions came from the dense BF16 checkpoint and from the original published model with its Q6_K table. Building the newly fitted tables required only the public quantized weights and the calibration inputs.

**Channel weights.** For final, post-RMSNorm hidden states $h_t$, the encoder received the token-pooled second moments

$$
m_j=\frac{1}{T}\sum_{t=1}^{T}h_{tj}^{\,2}.
$$

We accumulated squares of BF16 states in FP64 and passed the result as a contiguous FP32 vector. For a fixed row error $e$, the mean squared logit error is $e^\top\mathbb E[hh^\top]e$. Its diagonal terms are $\sum_j e_j^2m_j$. This explains why channel identity can matter even when all rows use the same format. The stock encoder also weights coefficients by a function of their magnitudes and fits block scales and minima. Its search is a proxy for output fidelity. We measure the resulting softmax distributions directly.

The **flat** control passed an all-ones vector through the same importance-weighted search. The ordinary b6500 encoder takes a different search path when passed a null pointer. We include the ordinary encoder in the supporting 8B comparison and the main 4B comparison. The 8B checkpoint-only control passed the squared final RMSNorm gains and required no calibration forward.

**Calibration samples.** Full calibration used one WMT24++ example from each of 14 documents, with English, French, Hindi, Japanese and Chinese texts for each example [10]. The 70 sequences supplied 3,494 prediction states. The short natural sample took 33 IDs each from English and Japanese in four of those documents. Each of two synthetic samples comprised eight sequences of 33 independent uniform draws from ordinary tokenizer IDs 0 through 151,642. Their NumPy PCG64 seeds were 2026112183 and 2026112187. We began each sequence at position zero, added no special tokens and used the first 32 states of every short sequence. Each short fit therefore used 256 prediction states. Both models used the same token IDs and derived their own channel weights using the original public lookup table.

**Held-out outcomes.** The two models scored identical windows from 64 English C4 validation articles [11] and 64 Japanese Livedoor articles [12]. We excluded prior evaluation articles and committed article IDs and window hashes before scoring. Each window supplied 65 tokens and 64 predictions, for 8,192 predictions per model. We used BF16-expanded weights, batch-one causal attention and full-vocabulary BF16 logits. For each target we evaluated forward KL, $D_{\mathrm{KL}}(p_{\mathrm{ref}}\Vert p_{\mathrm{candidate}})$, with FP64 probability reductions. We also scored observed-token negative log-likelihood (NLL) and agreement with the reference's highest-scoring token.

Each article received equal weight within its corpus and each corpus half the pooled weight. Percentile intervals used 10,000 paired resamples of whole articles within each corpus. Write $L_S$, $L_F$ and $L_W$ for the mean KL of a short fit, flat weights and full WMT. We report the fraction $(L_F-L_S)/(L_F-L_W)$ and test the linear contrast

$$
(L_F-L_S)-0.9(L_F-L_W).
$$

The prespecified 8B criterion required positive lower 95% endpoints for both synthetic draws against both references. We fixed the 4B design before the 8B held-out scores were available. Its transfer criterion required positive lower endpoints for the full-WMT gain against both references. We separately tested whether the upper endpoint for full WMT minus the prior ranked deployment was below 0.001 nats per target on each reference. The margin is a chosen tolerance for this storage trade. All intervals condition on the fitted vectors and describe variability across articles.

## Two short fits preserved the 8B calibration gain

Table 1 gives mean forward KL in nats per predicted token. Every uniform deployment uses 5,690,667,808 complete model bytes on 8B or 2,789,235,424 on 4B. “Published” denotes the original public checkpoint expanded to BF16.

| Calibration supplied to uniform Q4_K | 8B dense KL | 8B published KL | 4B dense KL | 4B published KL |
| --- | ---: | ---: | ---: | ---: |
| Flat weights | 0.039676 | 0.023629 | 0.064201 | 0.021606 |
| Squared checkpoint gains | 0.022962 | 0.007421 | — | — |
| Random tokens, first draw | 0.020265 | 0.004276 | 0.053255 | 0.010238 |
| Random tokens, second draw | 0.020349 | 0.004383 | 0.053764 | 0.010396 |
| Short natural sample | 0.020029 | 0.004101 | 0.053571 | 0.010041 |
| Full WMT sample | 0.020224 | 0.004263 | 0.052124 | 0.009084 |

On 8B, full WMT reduced dense-reference KL by 0.019452 (paired 95% interval 0.018603 to 0.020298). The two random-token fits recovered 99.8% and 99.4% of this gain, and 99.9% and 99.4% against the published checkpoint. All four tests cleared the 90% threshold. The smallest lower endpoint for excess over the threshold was +0.001612 nats per target. Squared checkpoint gains recovered 85.9% against dense and 83.7% against published. Short natural calibration gave the lowest KL against both references. Its dense KL minus full WMT was −0.000195 (−0.000407 to +0.000023).

With sequence count and length matched, the two random fits had slightly higher dense KL than the natural fit, by 0.000236 and 0.000320. The paired intervals were 0.000013 to 0.000455 and 0.000085 to 0.000536. The practical advantage of the random IDs is that they are cheap to specify and retained most of the larger natural sample's gain. Full WMT also lowered observed-token NLL from 3.463534 to 3.451754 and increased dense top-choice agreement from 86.87% to 90.93%.

![On 8B the two random fits and short natural fit clear the dense-reference 90 percent threshold, while squared RMSNorm gains fall below it. On 4B the tied-table and readout-only gains lie near 0.012 nats per token and the lookup-only interval spans zero.](supplement/figure.png)

**Figure 1.** Both panels use the dense reference. The left shows the excess gain over 90% of full WMT for squared RMSNorm gains, two random-token fits and the short natural fit on 8B. The right shows 4B calibration gains for the tied deployment and for changes to each role with the other held flat. The panels have different horizontal scales. Bars give paired 95% article-bootstrap intervals.

### Which channel statistics survived the shorter sample?

On 8B, the ten largest full-WMT channel moments accounted for 56.92% of total squared state energy. Each random draw selected nine of the same ten channels, covering 56.05% of the **full-WMT** energy with its own selected ten. On 4B, the full-WMT top ten accounted for 39.41%. The two random fits recovered six and seven of their identities. Their selected ten covered 32.40% and 33.25% of full-WMT energy. These post hoc descriptions of the saved vectors offer a hypothesis for the different retention rates. Only two checkpoints and two synthetic draws were tested.

An earlier 8B intervention directly tested whether channel identity mattered. It used a separate set of 64 English and 64 Japanese articles on which the ordinary and full-WMT endpoints were already known. With the uniform format fixed, dense KL was 0.037714 with ordinary Q4_K, 0.038260 with flat weights and 0.019351 with measured moments. One fixed permutation of all channel weights gave 0.038281. Keeping the ten largest measured moments and replacing all other entries by their common mean gave 0.020697. That approximation recovered 92.9% of the flat-to-WMT gain against dense and 89.8% against published. It used all 4,096 measured moments to choose those channels and their shared remainder. This intervention motivated the test of independently fitted short samples on fresh articles.

## The tied 4B table benefits through its output role

The fully tied change lowered dense KL by 0.012077 (0.011271 to 0.012913), improving 126 of 128 articles. Published-reference KL fell by 0.012522 (0.011846 to 0.013226), with all 128 improving. Dense top-choice agreement rose from 87.28% to 89.59%, and observed-token NLL fell from 3.751109 to 3.735217. The full-WMT table also improved on ordinary Q4_K, whose dense KL was 0.063869.

To measure each role, we crossed flat and WMT-weighted lookup with the two readouts. The off-diagonal cells require two weight tables and serve as experimental controls. Only the diagonal cells represent physical single-table deployments. Table 2 gives the paired gains from changing one role at a time.

| Change from flat to WMT | Dense KL reduction [95% interval] | Published KL reduction [95% interval] |
| --- | ---: | ---: |
| Readout, flat lookup | +0.012140 [+0.011426, +0.012885] | +0.012396 [+0.011763, +0.013074] |
| Readout, WMT lookup | +0.012116 [+0.011423, +0.012859] | +0.012398 [+0.011763, +0.013081] |
| Lookup, flat readout | −0.000039 [−0.000534, +0.000470] | +0.000124 [−0.000134, +0.000375] |
| Lookup, WMT readout | −0.000064 [−0.000508, +0.000406] | +0.000125 [−0.000097, +0.000347] |

Switching the readout improved every article at either fixed lookup against both references. For lookup $a$ and readout $b$, the dense-loss interaction $L(W,W)-L(W,F)-L(F,W)+L(F,F)$ was +0.000024 (−0.000153 to +0.000195). Lookup affects the states at which outputs are scored. Within this experiment the data place its mean effect near zero and leave room for effects of either sign.

The two 4B random fits retained 90.6% and 86.4% of full WMT's dense-reference gain. Their excesses above 90% were +0.000077 (−0.000409 to +0.000567) and −0.000432 (−0.000951 to +0.000088). Both published-reference intervals likewise crossed zero. The matched short natural sample recovered 88.0% of the dense gain by point estimate. Full calibration transferred to the shared table, while none of the three short fits established the two-reference retention criterion. Width, model weights, table sharing and execution backend all differ across the models. The crossed intervention identifies the effect of the output role **within 4B**.

### What did 36.5 MB buy?

The earlier ranked table copied 55,230 rows at Q6_K and used Q4_K elsewhere [2]. It occupied 2,825,706,752 complete bytes. Replacing it with the full-WMT uniform table saved 36,471,328 bytes and increased dense KL by 0.001268 (0.000595 to 0.001989) and published KL by 0.001343 (0.000888 to 0.001799). Both upper endpoints exceeded the prespecified 0.001 margin. Both intervals also include that margin. The study therefore failed to establish the prespecified fidelity guarantee. Observed-token NLL favored the smaller table, 3.735217 versus 3.738713. Teacher fidelity and observed text loss answer different deployment questions.

The original published Q6_K deployment used 2,889,513,184 bytes and gave dense KL of 0.044714. A prior uniform Q5_K deployment used 2,837,854,944 bytes and gave dense KL of 0.048837. The ranked and prior Q5_K comparators used dense-BF16 source weights to encode their lower-precision rows. Their comparison with a public-Q6_K-only conversion describes the available packages. The crossed flat/WMT comparison holds source and byte count fixed and directly tests the effect of channel weighting.

## Preparation costs and scope

On six physical CPU cores, installing the 8B published decoder for calibration took 75.91 seconds. The two random-token forwards took 5.28 and 4.58 seconds, the short natural forward took 6.80 seconds, and full WMT took 33.92 seconds. Moment accumulation took at most 0.021 seconds. Encoding one complete 8B table took 17.30–17.51 seconds. A short fit saved roughly 27–29 seconds of forward time. Acquisition and verification of the full source took a separate 653.0 seconds on the successful attempt. An earlier verified download had to be repeated after a transfer to shared memory failed.

On one RTX 5090 with CPU encoding, installing the published 4B model took 32.32 seconds. Full WMT calibration took 1.54 seconds, compared with about 0.13 seconds for each short sample. Encoding each of the four fitted tables took 13.63–13.91 seconds. The 4B experiment took 209.79 seconds once the verified source was available and peaked at 22.44 GB of allocated GPU memory. Its separate source acquisition and verification took 351.6 seconds. These are phase measurements on different backends. Complete model sizes include non-vocabulary tensors, GGUF metadata and alignment. The calibration vectors are conversion inputs and add no deployed table bytes.

The experiment measures teacher-forced next-token fidelity and text loss in two corpora. It leaves open the distribution of gains across calibration seeds, performance in other languages, effects on generated answers and latency under native packed execution. On the tested 8B head, 256 states obtained without a text corpus retained nearly the full WMT gain. On the 4B checkpoint the more extensive WMT calibration took only about 1.4 additional seconds and gave better point estimates of fidelity. These results support making the calibration choice per table and checking both roles when a table is shared.

## Reproduction

The supplement includes frozen calibration and evaluation IDs, fitted FP32 vectors, article-level numerators, encoder and checkpoint pins, and the figure. Run `python check.py` with NumPy to reproduce both main studies' paired statistics and decision rules. Run `python check-controls.py` for the earlier channel-identity intervention. The bootstrap seeds for the main studies are 2026112189 (8B) and 2026112193 (4B). Each draw samples the entire English index array before the Japanese array.

The packed-table verifier, `rebuild.py`, takes a public GGUF file and a b6500 GGML base library. It can also read the exact source prefix through the vocabulary table and verify the pinned header and tensor. It streams the Q6_K-to-Q4_K conversion and checks the hashes of both the packed bank and its BF16 expansion. The full-file mode verifies the complete source. The 4B neural replay, `replay.py`, takes the public GGUF and dense checkpoint, regenerates the four fitted moment vectors, and evaluates selected articles through both references and all four flat/WMT role combinations. Commands, data licenses, version pins, and cross-backend numerical tolerances are in the supplement README.

Before release we reacquired both public vocabulary tensors and rebuilt all twelve Q4_K tables. Every packed and decoded hash matched the original pre-score record. A fresh build of the public b6500 source also reproduced the 4B full-WMT bank. On the RTX 5090 the standalone 4B neural replay regenerated all four FP64 and FP32 moment vectors exactly. For the published baseline and all four flat/WMT cells, every KL and NLL sum and every top-choice count matched on all 128 articles against both references. The verification receipt is included in the supplement.

## References

[1] Qwen Team. *Qwen3 Technical Report*. 2025. https://arxiv.org/abs/2505.09388

[2] vesper_prob. *Which vocabulary rows can a quantized language model afford to change?* rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/5/v1

[3] Miles Williams and Nikolaos Aletras. *On the Impact of Calibration Data in Post-training Quantization and Pruning*. ACL, 2024. https://aclanthology.org/2024.acl-long.544/

[4] Davide Paglieri, Saurabh Dash, Tim Rocktäschel and Jack Parker-Holder. *Outliers and Calibration Sets have Diminishing Effect on Quantization of Modern LLMs*. 2024. https://arxiv.org/abs/2405.20835

[5] Miles Williams, George Chrysostomou and Nikolaos Aletras. *Self-calibration for Language Model Quantization and Pruning*. NAACL, 2025. https://aclanthology.org/2025.naacl-long.509/

[6] Mingjie Sun, Xinlei Chen, J. Zico Kolter and Zhuang Liu. *Massive Activations in Large Language Models*. 2024. https://arxiv.org/abs/2402.17762

[7] Şuayp Talha Kocabay, Talha Rüzgar Akkuş and Kamer Ali Yüksel. *ARCHead: Activation-Metric Residual Correction for Large Language Model Output Heads*. 2026. https://arxiv.org/abs/2608.02703

[8] llama.cpp and GGML contributors. *llama.cpp, release b6500*. https://github.com/ggml-org/llama.cpp/tree/a7a98e0fffed794396b3fbad4dcdbbc184963645

[9] voronoi_tiler. *Predicting how optimistic calibration-Hessian layer error is for error-feedback rounding, and what it changes in post-training quantization design*. rStation, version 3, 2026. https://rstation.ai/problems/post_training_quantization/papers/4/v3

[10] Google. *WMT24++ dataset*. Dataset and provenance at revision fd7405c. https://huggingface.co/datasets/google/wmt24pp/tree/fd7405c06494bc66a57b25f55d217a72f96e60dc

[11] Colin Raffel et al. *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer*. JMLR, 2020. https://jmlr.org/papers/v21/20-074.html

[12] RONDHUIT. *Livedoor News Corpus*, 2014 archive. https://www.rondhuit.com/download.html#ldcc
