## 1. Problem and contribution

The task asks for pretraining architectures that lower held-out bits per byte (bpb) at fixed compute. On documents longer than the attention window, much of the next-token loss sits on tokens that repeat something said earlier in the same document. A 2K-window model cannot see that earlier text. An 8K-window model can, at a higher attention cost. We ask two questions. How much does an exact lookup into the earlier document lower the loss, alone and on top of each attention layout? And is it a better buy than spending about the same FLOPs on longer attention?

The lookup (the *document table*) is the rule ROSA uses in RWKV-8 [1]: find the longest suffix of the current context, of 1 to 4 tokens, that occurred earlier in the document, and return the token that followed its latest occurrence. We add a learned embedding of that token, and a learned embedding of (match order, log distance), to the input. All models are trained from scratch for the same 953 updates of $2^{19}$ tokens on identical target sequences, so arms differ only in architecture. Every model is scored in the format it was trained in, and the headline contrasts were confirmed on a fresh set of documents, fixed after all training and scored once.

Claims, on the long-document regime of Section 3 unless stated. Numbers are on the confirmation set; s44 / s45 are the two seeds.

1. **The lookup adds to every attention layout tested, at no extra matrix FLOPs.** It is not free: it adds 16.8M embedding parameters, and its sorts and gathers take 0.3% of training time and 0.12 GiB of memory (Section 4.2); its cost in online generation is unmeasured. Gains are .0320 / .0294 on a 2K model, .0113 / .0081 on an 8K model, and .0126 / .0076 on an 8K local-global model with 512-token local windows. Every 95% document-bootstrap interval excludes 0, and 91–100% of documents improve.
2. **At approximately matched estimated matrix FLOPs, local-global attention beats the lookup.** The 8K local-global model costs 1.03 times the 2K model's estimated FLOPs per token and beats the 2K model with the lookup by .0051 / .0082. The best model at this cost is local-global attention with the lookup (1.04183 / 1.04715).
3. **Where the gain comes from depends on what attention can see, and on 8K models the match structure carries it.** On the 2K model, 78% of the gain comes from copies whose source lies outside the model's row. On the 8K models, copies inside the window still improve, and the largest class term comes from targets the table cannot predict: targets whose context-target bigram $(x_t, y_t)$ is new in the document (order 0). The token itself may have occurred before. Registered controls (Section 4.4) show that this term needs the current document: a lookup answered from another document gains nothing. On both 8K layouts, the 29K-parameter embedding of (match order, log distance) alone, without the returned token, matches the full lookup. On the confirmation set it differs from the full lookup by +.0007 / −.0001 on the 8K model and +.0001 on the local-global model (positive = better). On the 2K model it gives 28% of the full gain: there the returned token is needed. We have not identified how the model uses the match structure.
4. **Evaluation must give the lookup and attention the same spans as in training.** When a strided evaluation cuts the lookup's span and the attention window at different points, in-window copies get worse. Our first version made this error on 8K models and reported a spurious "substitution" of induction by the lookup; our second version kept a smaller instance on 2K models. Separately, the 2K model's gain depends on how much context the evaluation gives it: .020 under stride-$T/2$ sliding windows against .035 in the training format (dev-val, Section 4.6). The ranking in claim 2 holds under both.
5. **On packed short documents we detected no meaningful improvement from the full lookup** (held-out +.0002, one seed). Its right guesses help and its wrong guesses hurt by about the same amount. The structure-only lookup of claim 3 gains +.0027, −.0002 and +.0050 at three seeds (held-out), which our registered rule leaves unresolved (Section 4.9). Both results are descriptive.
6. **Width, descriptive (one seed).** On the local-global model the gain is .0128, .0126 and .0098 at widths 384, 512 and 768. Width itself buys more: the width-768 model without the lookup beats the width-512 model with it by .0244, at twice the FLOPs (Section 4.7).

## 2. Related work and distinction

*Exact-match retrieval of continuations.* ROSA [1] computes this lookup with a suffix automaton inside RWKV-8. ROSA-Tuning [2, Sections 3.2–3.4] runs ROSA over *learned discretized hidden-representation streams* of a pretrained Qwen3-1.7B with windowed attention and injects decoded features, then fine-tunes. Its retrieval keys and values are learned codes, not raw tokens. Our lookup runs on raw tokens with orders 1–4, and we test it in from-scratch pretraining of a Transformer.

*A latest-match copy head on this board.* Board paper [3, Section 5.3] adds a head that finds the most recent earlier position in the same document whose last $n \in \{1,2,3\}$ tokens match, and boosts the output logit of the token that followed it through learned gates. With corpus bigram and trigram tables on a backpropagation-trained d4/w256 model on packed ClimbMix, it moves bpb from 1.1107 to 1.1096. Our packed-data null (claim 5) agrees with that result. Three things differ: we inject the candidate at the input with a learned embedding rather than at the output logit, we use orders up to 4 with a distance embedding, and our main regime is long documents, where most matches lie outside a 2K window.

*In-context n-gram mechanisms.* Induction heads [4] copy by attention. Akyürek et al. [5] hard-wire n-gram heads that attend to positions after earlier occurrences of the current n-gram, and show that adding them improves natural-language modeling, including in Transformers; Section 6 of their paper discusses trie compression and recurrent querying of such heads. Exact in-context n-gram matching is therefore known to help language modeling. Our lookup is one such query, returning only the latest continuation, and we measure it against and on top of learned attention at matched training targets.

*Caches and retrieval memories.* The continuous cache [6] and pointer-sentinel mixtures [7] reuse recent hidden states at the output. Memorizing Transformers [8] and Landmark Attention [9] retrieve earlier keys by learned similarity. The document table retrieves by exact token match and injects at the input.

*Corpus-scope n-gram tables.* Hashed n-gram input embeddings [10, 11, 12] key on local context but store corpus statistics learned by gradient. Our bigram control is one of these. The document table keys on the same local context but takes its value from the current document.

*Long-range context use and efficient attention.* Sun et al. [13] found that long context helps mostly on tokens that copy earlier text. Our board post [14] measured this on the present recipe: 8K beats 2K by .028 bpb on identical targets, mostly on verbatim copies. Local-global layouts that mix short sliding windows with occasional full-context layers are standard in long-context models [15]; we use one as the comparator at matched FLOPs.

*Attention temperature.* QK-norm [16] fixes the logit scale, and SSMax [17] scales queries by log length. Board paper [18] studies post-QK-norm scaling at 2K. Section 4.8 tests the log-length factor at 8K.

## 3. Methods

### 3.1 Recipe and models

All models use the board's reference recipe: a Transformer of width 512 with 4 heads of dimension 128, QK-norm with logit scale $1/\sqrt{128}$, RoPE, value embeddings on alternate layers, a vocabulary of 8,192 tokens, Muon for matrices and AdamW for embeddings and scalars, and 953 updates of $2^{19}$ tokens (500M tokens). The seed is 44 unless stated. Each layer has a short (S) or long (L) sliding window, and the last layer is always long. B, A, D and the 5-layer 8K model use the reference pattern SSSL (three short layers, then a long one, repeated), with the short window at half the sequence length. The local-global models LG512 and LG1024 use a short window of 512 or 1,024 tokens in layers 1–7 and the full 8,192 in layer 8.

| Name | Sequence | Layers | Windows by layer | FLOPs per token | Parameters |
|---|---|---|---|---|---|
| B | 2,048 | 8 | 1K ×3, 2K, 1K ×3, 2K | $2.17\times 10^{8}$ | 50.3M |
| LG512 | 8,192 | 8 | 512 ×7, 8K | $2.23\times 10^{8}$ | 50.3M |
| LG1024 | 8,192 | 8 | 1K ×7, 8K | $2.43\times 10^{8}$ | 50.3M |
| 8K, 5 layers | 8,192 | 5 | 4K ×3, 8K, 8K | $2.27\times 10^{8}$ | 36.7M |
| A | 8,192 | 8 | 4K ×3, 8K, 4K ×3, 8K | $3.40\times 10^{8}$ | 50.3M |
| D | 8,192 | 12 | (4K ×3, 8K) ×3 | $4.97\times 10^{8}$ | 71.3M |

LG512 (1.03 times B's FLOPs per token) and the 5-layer 8K model (1.04 times) are the two measured 8K comparators within 5% of B. Section 4.7 adds LG512 at widths 384 and 768.

*Compute accounting.* FLOPs per token are the reference recipe's estimate of forward and backward matrix multiplies and attention. When we say two arms have matched FLOPs, we mean these estimates agree within 5%; we did not measure FLOPs on the hardware. All runs use activation checkpointing, which recomputes each block's forward pass once in the backward pass. This adds about one third of the block FLOPs to every arm alike (Table 3) and is not in the FLOPs column. The table lookup adds sorts, gathers and embedding updates but no matrix multiplies. We report its measured cost in time and memory instead (Section 4.2). `training_seconds` in the result files excludes the first 11 updates (compilation and warm-up); we also report the full loop time. All arms use $2^{17}$ tokens per microbatch and 4 microbatches per update. That is 64 rows at 2K and 16 rows at 8K. Holding tokens per microbatch fixed departs from the task's stated microbatch convention, which is given in rows.

### 3.2 Long-document regime

Training data is a frozen index of 62,538 chunks of 8,192 consecutive target tokens. The chunks are cut from ClimbMix documents of at least 8,193 tokens in 120 training exports (shards 20–102, 200–218 and 300–317, listed with checksums in `data/MANIFEST.tsv`) and put in a seeded permutation. A 2K model sees each chunk as 4 consecutive rows. An 8K model sees it as one row. Both therefore train on **identical targets in identical order**; only the context available to each target differs. Slot 0 of every row holds the BOS token. We checked that the 2K and 8K loaders give equal target streams and equal step-0 loss (9.0115).

*Evaluation sets.* Two development sets were used throughout the study: **dev-val**, the 322 documents of at least 8,193 tokens in ClimbMix shard 6542 (5.49M targets), and **dev-held-out**, the 669 such documents in shards 6540 and 6541 (10.3M targets). Registered decision rules consulted dev-val and, from the second experiment on, dev-held-out as well (`PROTOCOLS.md`), so neither is an untouched test set. Two dev-val and seven dev-held-out documents share their first 256 tokens with a training document; excluding them changes the headline gains by at most .0001. The **confirmation set** was fixed after every model had been trained and every decision made. It has 673 documents (10.3M tokens, 8.30M targets in full chunks) from two long-document exports, of shards 782 and 783, that had been built for an experiment that never ran. No model trained on them and no run scored them before. Five documents whose first 256 tokens match a training or development document were dropped. Before the first score we registered the contrasts, the evaluation, the uncertainty method and a confirmation rule (Section 3.6). Every checkpoint was then scored on the set once.

*Evaluation format.* All headline numbers use the **training format**. Each document is cut into its full 8,192-token chunks exactly as the index cuts training documents, and the remainder is dropped (17–19% of targets). A model with context $T$ scores each chunk as $8192/T$ rows with BOS in slot 0, and the table searches the chunk. All models thus score identical targets, and each target's pair of visible context and table state has the same distribution as in training. Two checks support this. Scoring three checkpoints through the training loader itself, including its table computation, reproduces the training-format bpb to $2\times 10^{-5}$. And in the training format no row crosses a chunk boundary: of 788,374 dev-val copies whose source a 2K model can see, 23 get no table match, all at chunk starts where slot 0 holds BOS.

The training format gives a 2K model 0 to 2,047 tokens of context per target (1,024 on average), against 1,024 to 2,047 under the common sliding-window evaluation with stride $T/2$. Section 4.6 reports that sliding-window evaluation as a secondary result, together with the reach mismatch it causes. We also report the standard ClimbMix val bpb (2K packed rows) for every arm. It is off-distribution for long-document models.

### 3.3 The document table

For position $t$ in a document, let $n^{*}(t)$ be the largest $n \in \{1,2,3,4\}$ such that the last $n$ input tokens $x_{t-n+1..t}$ occurred earlier, ending at some position $s < t$, and let $s(t)$ be the latest such $s$. The table returns the order $n^{*}$, the candidate token $\hat{y}_t = x_{s+1}$ and the distance $d_t = t - s$. If no single token matches, the result is "no match".

Two zero-initialised embedding tables, $E \in \mathbb{R}^{4V \times 512}$ and $G \in \mathbb{R}^{57 \times 512}$, turn the result into an input vector:

$$
e_t \leftarrow e_t + E[(n^{*}-1)V + \hat{y}_t] + G[(n^{*}-1)\cdot 14 + \min(\lfloor \log_2 d_t \rfloor, 13)].
$$

At no match, $G[56]$ is added and the $E$ term is omitted. The model starts identical to the base and learns, per order and distance bucket, how much to trust the candidate. The tables add 16.8M parameters and are trained by AdamW at the embedding learning rate.

*Reach.* The lookup searches only the current 8,192-token training chunk. For a 2K model, the reach is the whole chunk (up to three earlier rows plus the current row); for an 8K model, the row is the chunk. The training format reproduces this exactly. Section 4.6 shows what happens under sliding-window evaluation, where windows and chunks are cut at different points.

*Computation.* The lookup is exact. For each order, positions are keyed by the 13-bit tokens of the suffix and sorted stably per row on the GPU, and each position takes the previous equal key. We checked it against a CPU dictionary implementation on 277K positions, and checked the training loader and the evaluation paths against the same reference, with 0 mismatches. On packed ClimbMix rows the table is computed per row, with segments split at BOS so lookups never cross documents.

### 3.4 Arms and controls

- **B + bigram table.** A hashed bigram input table of 65,536 rows of width 512 (33.5M parameters, twice the document table), injected at the input as in board papers [10, 11]. It controls for added embedding parameters and is a strong corpus-memory baseline. **B + bigram + table** tests additivity.
- **A + table, LG512 + table.** The table on the 8K models, two seeds each. **A + table with dropout 0.5**: a random half of training rows gets no table hits; evaluation uses the full table.
- **Ablated table.** A trained table model evaluated with every position set to "no match".
- **Foreign-document table.** On A, each position's suffix is looked up in a different document: the previous chunk of the microbatch in training, the next document of the set in evaluation. Tables, fields and key are unchanged.
- **Field split.** The table with only $G$, the (match order, log distance) embedding and its no-match row (29K parameters), or only $E$, the (order, candidate) embedding (16.8M parameters). $G$ alone was run on A at two seeds, on LG512, on B and on packed ClimbMix at three seeds; $E$ alone on A.
- **ClimbMix 2K packed (C1).** The reference 2K recipe on packed ClimbMix rows, with and without the table.
- **Attention temperature.** On A, queries after QK-norm are multiplied by $g_h \log(\min(t, w)+1)/\log 2048$ (an SSMax-style log-length scale [17]) with a learnable per-head gain $g_h$ initialised to 1, or by $g_h$ alone.

### 3.5 Decomposition by target class

Target classes do not depend on the table. For target $y_t$ we find the largest $n \in \{1,\ldots,4\}$ such that the context $x_{t-n+1..t}$ occurred earlier in the same document *followed by the same token* $y_t$, and the distance to the latest such occurrence, over the whole document. A target of order $\geq 2$ is a *copy*, classed by that distance. Order 1 means only the bigram $(x_t, y_t)$ occurred before; order 0 means even that bigram is new in the document. A copy is *visible* if its source position lies inside the row the target is scored in. In the training format a 2K model sees a source 0–512 back only if it lies in the same 2K row, and an 8K model sees about half of the copies 4–8K back. Where we split by table state, the state (no match, candidate right, candidate wrong) is the one the model received. We report mean loss in nats per class and each class's contribution to the bpb difference between two arms; the contributions sum to the total.

### 3.6 Uncertainty and protocol

*Uncertainty.* For each paired contrast (two arms of the same seed, scored on the same targets) we report a 95% interval from a paired document bootstrap: documents are resampled with replacement 2,000 times, and the contrast is recomputed each time as summed nats over summed bytes. This interval reflects document sampling only. Training-seed variation is shown by reporting both seeds side by side. The main arms have two seeds, too few for a seed interval. The board's contrast standard deviation for this recipe on ClimbMix is about .002.

*Protocol.* Most experiments ran under decision rules registered in our research log before the run; the dated registrations are in `PROTOCOLS.md`. Those rules consulted the development sets. The confirmation protocol was registered after all training and before any score on the confirmation set. It fixed the checkpoints (no new training), the training-format evaluation, the bootstrap, and five headline contrasts: H1–H3, the table's gain on B, A and LG512; H4, LG512 against B + table; H5, the 8K 5-layer model against B + table. A contrast counts as confirmed if its registered sign holds with the interval excluding 0 at both seeds. We also predicted that each value would lie within ±.003 of its dev-held-out value. The training-format evaluation had been registered 13 minutes earlier, before any training-format number was computed; its registered prediction for B missed (Section 4.6).

## 4. Results

### 4.1 Main table

Table 1 gives bpb in the training format on the three long-document sets (lower is better). Arms marked "s44 / s45" have two seeds; the others have one (seed 44). `results/tables_summary.txt` gives the same numbers as nats per target and perplexity; for example, B + table and LG512 score 2.8014 and 2.7879 nats per target (perplexity 16.47 and 16.25) on the confirmation set at seed 44.

**Table 1.** Bits per byte, training format.

| Arm | Dev-val | Dev-held-out | Confirmation | ClimbMix val | FLOPs/token | Params |
|---|---|---|---|---|---|---|
| B (2K, 8L), s44 / s45 | 1.06675 / 1.06750 | 1.06935 / 1.07025 | 1.09148 / 1.09232 | 1.08687 / 1.08612 | $2.17\times 10^{8}$ | 50.3M |
| B + table, s44 / s45 | 1.03129 / 1.03434 | 1.03480 / 1.03802 | 1.05952 / 1.06296 | 1.07531 / 1.07852 | $2.17\times 10^{8}$ | 67.1M |
| B + bigram table | 1.05126 | 1.05443 | 1.07697 | 1.07195 | $2.17\times 10^{8}$ | 83.9M |
| B + bigram + table | 1.01973 | 1.02339 | 1.04799 | 1.06293 | $2.17\times 10^{8}$ | 100.7M |
| 8K, 5L, s44 / s45 | 1.05175 / 1.05739 | 1.05544 / 1.06086 | 1.08118 / 1.08604 | 1.12279 / 1.12791 | $2.27\times 10^{8}$ | 36.7M |
| LG512, s44 / s45 | 1.02555 / 1.02631 | 1.02934 / 1.02958 | 1.05444 / 1.05476 | 1.08737 / 1.08749 | $2.23\times 10^{8}$ | 50.3M |
| **LG512 + table, s44 / s45** | **1.01326 / 1.01838** | **1.01639 / 1.02153** | **1.04183 / 1.04715** | 1.07661 / 1.08005 | $2.23\times 10^{8}$ | 67.1M |
| LG1024, s44 / s45 | 1.02434 / 1.02548 | 1.02814 / 1.02925 | 1.05332 / 1.05442 | 1.08865 / 1.09000 | $2.43\times 10^{8}$ | 50.3M |
| A (8K, 8L), s44 / s45 | 1.02276 / 1.02484 | 1.02725 / 1.02907 | 1.05218 / 1.05405 | 1.09561 / 1.09543 | $3.40\times 10^{8}$ | 50.3M |
| A + table, s44 / s45 | 1.01161 / 1.01631 | 1.01497 / 1.01977 | 1.04087 / 1.04597 | 1.08026 / 1.08440 | $3.40\times 10^{8}$ | 67.1M |
| A + table, dropout 0.5 | 1.01780 | 1.02146 | 1.04692 | 1.08816 | $3.40\times 10^{8}$ | 67.1M |
| A + log-length query scale | 1.01846 | 1.02233 | 1.04743 | 1.09310 | $3.40\times 10^{8}$ | 50.3M |
| A + per-head gain | 1.01909 | 1.02323 | 1.04818 | 1.08933 | $3.40\times 10^{8}$ | 50.3M |
| D (8K, 12L) | 1.00874 | 1.01255 | 1.03753 | 1.07811 | $4.97\times 10^{8}$ | 71.3M |

The confirmation set is harder than the development sets (every arm is .022–.026 worse than on dev-held-out), and it has fewer copy targets: 24.9% of its targets are copies, against 31.9% on dev-val. On packed ClimbMix (2K rows, the board's standard regime), the reference model scores 0.99523 on val and 0.99445 on held-out; with the table, 0.99512 and 0.99423 (Section 4.9).

![Confirmation-set bpb (training format, mean of the seeds run) against estimated FLOPs per token. Arrows go from each base arm to the same arm with the document table: B (2.17e8) from 1.092 to 1.061, LG512 (2.23e8) from 1.055 to 1.045, A (3.40e8) from 1.053 to 1.043. The 8K 5-layer model (2.27e8, 1.084), LG1024 (2.43e8, 1.054) and D (4.97e8, 1.038) are base points only. At about 2.2e8 FLOPs, LG512 is below B + table, and LG512 + table is lowest.](supplement/figure-2.png)

### 4.2 Gains and the comparison at matched FLOPs

Table 2 lists the table's gain over the same-seed base arm, with the paired document-bootstrap interval on the confirmation set.

**Table 2.** Gain from adding the document table (bpb, base minus table arm), training format.

| Base arm | Dev-val, s44 / s45 | Dev-held-out, s44 / s45 | Confirmation, s44 [95% interval] / s45 [95% interval] | Documents improved (confirmation) |
|---|---|---|---|---|
| B | .0355 / .0332 | .0346 / .0322 | .0320 [.0299, .0341] / .0294 [.0273, .0315] | 99.7% / 100% |
| LG512 | .0123 / .0079 | .0129 / .0080 | .0126 [.0119, .0134] / .0076 [.0069, .0083] | 98.7% / 91.1% |
| A | .0112 / .0085 | .0123 / .0093 | .0113 [.0109, .0117] / .0081 [.0077, .0085] | 99.4% / 96.6% |
| B + bigram table | .0315 | .0310 | .0290 [.0270, .0310] | |

H1–H3 are confirmed: every gain is positive with an interval excluding 0, at both seeds. Every headline value (H1–H5) on the confirmation set lies within .003 of its dev-held-out value, as predicted; B's gain is closest to the edge (−.0026 / −.0028). Seed variation is the larger uncertainty for the 8K arms. The two seeds' gains differ by .0023–.0026 on B, .0027–.0032 on A and .0044–.0050 on LG512, over the three sets, while the confirmation intervals have half-widths of .0021 on B and .0004–.0008 on the 8K arms. We therefore read a gain of about .008 to .013 on 8K models at this scale. We had registered "adds to local-global attention" if the gain over LG512 was at least .005 on both development sets at both seeds; it is .0079 at worst in the training format (.0091 under the stride-$T/2$ evaluation in use when we registered the rule). On B + bigram, the gain is 0.89–0.91 times its gain on B; we had registered additivity at 0.6 times or more.

*Matched FLOPs.* Three measured arms lie within 5% of B's estimated FLOPs per token. Against B + table, on the confirmation set:

- LG512 (1.03 times the FLOPs) is better by .0051 [.0042, .0060] / .0082 [.0073, .0092]. On the development sets the margin is .0057 / .0080 (dev-val) and .0055 / .0084 (dev-held-out). H4 is confirmed.
- The 8K 5-layer model (1.04 times) is worse by .0217 / .0231. H5 is confirmed.
- LG512 + table is better by .0177 / .0158.

LG1024 (1.12 times) is better than B + table by .0062 / .0085. One full-context layer above seven 512-token layers is therefore a better use of about the same FLOPs than the table on a 2K model, and the table adds to it. B + bigram + table (1.04799, one seed) is worse than both seeds of LG512 + table, with 100.7M parameters against 67.1M.

*Cost beyond FLOPs.* Table 3 gives measured times on one RTX 4090.

**Table 3.** Measured cost. FLOPs exclude checkpoint recomputation; the "with recompute" column adds one forward pass of the blocks (about 4/3).

| Arm | FLOPs/token | with recompute | Train s | Loop s | Peak GiB |
|---|---|---|---|---|---|
| B | $2.17\times 10^{8}$ | $2.90\times 10^{8}$ | 1390 | 1415 | 5.50 |
| B + table | $2.17\times 10^{8}$ | $2.90\times 10^{8}$ | 1389 | 1414 | 5.62 |
| LG512 | $2.23\times 10^{8}$ | $2.97\times 10^{8}$ | 1453 | 1492 | 5.51 |
| LG512 + table | $2.23\times 10^{8}$ | $2.97\times 10^{8}$ | 1447 | 1486 | 5.64 |
| A | $3.40\times 10^{8}$ | $4.53\times 10^{8}$ | 1949 | 1995 | 5.51 |
| A + table | $3.40\times 10^{8}$ | $4.53\times 10^{8}$ | 1971 | 2003 | 5.64 |
| D | $4.97\times 10^{8}$ | $6.63\times 10^{8}$ | 2865 | 2930 | 6.46 |

"Train s" is the result files' `training_seconds`, which excludes the first 11 updates. "Loop s" is the full training loop. The table adds 0.12–0.13 GiB of peak memory. Its time cost is within run-to-run noise (seed pairs of the same arm differ by up to 20 s). Measured in isolation (`code/bench_doctab.py`), the lookup takes 1.19 ms per microbatch of 16 × 8,192 tokens, or 4.5 s over a run's 3,812 microbatches, 0.3% of B's training time.

### 4.3 Where the gain comes from, by target class

![Bar chart of bpb gain over B of the same seed on dev-val (training format), by target class, for B + table (two seeds), B + bigram and B + bigram + table. Document-table gains are spread over copies up to 8K back (about .006, .004, .007, .009 and .004 bpb for the bands 0–512, 512–1K, 1–2K, 2–4K and 4–8K, nearly identical for both seeds) and are near zero beyond 8K. The bigram table gains mostly on order-0 targets (.0098) and little on copies. The combination gains on both.](supplement/figure-1.png)

Table 4 splits each gain by target class (dev-val, bpb contribution). On dev-held-out every class term agrees with dev-val to within .0006, and on the confirmation set to within .0013 (`results/tables_classes.txt`).

**Table 4.** Gain from the table by target class, s44 / s45, each seed against the base of the same seed.

| Class (share of targets) | on B | on LG512 | on A |
|---|---|---|---|
| copy (0, 512] (14.9%) | .0059 / .0060 | .0007 / .0007 | .0012 / .0010 |
| copy (512, 1K] (3.4%) | .0040 / .0041 | .0009 / .0006 | .0003 / .0003 |
| copy (1K, 2K] (3.4%) | .0069 / .0069 | .0007 / .0006 | .0002 / .0003 |
| copy (2K, 4K] (3.4%) | .0086 / .0086 | .0010 / .0008 | .0004 / .0005 |
| copy (4K, 8K] (2.8%) | .0043 / .0042 | .0021 / .0021 | .0003 / .0004 |
| copy beyond 8K (4.1%) | .0001 / .0000 | .0001 / −.0001 | .0002 / .0003 |
| order 0 (47.8%) | .0034 / .0014 | .0059 / .0035 | .0073 / .0050 |
| order 1 (20.3%) | .0023 / .0021 | .0009 / −.0003 | .0014 / .0009 |

On B, copies give .0298 of the .0355, and copies whose source lies outside B's row give .0277 of it (78%). In the training format a copy can be invisible to B even when its source is close: 0.97% of targets are copies 0–512 back whose source is in the previous row, and for these the loss falls from 2.202 to 1.026 nats with the table. Visible copies gain .0021 in total. Copies more than 8K back, outside the table's reach, gain nothing.

On A, every copy band improves, but by much less (.0002 to .0012), because attention already reaches these sources. On LG512 the copy gains lie between. Seven of its eight layers see only 512 tokens, and copies 4–8K back gain .0021, almost all (.0020) on the half whose source lies inside the 8K row and so is visible only to the last layer. Their loss falls from 1.612 to 1.232 nats.

The order-0 term grows as attention gets longer, from .0034 on B to .0073 on A (seed 44), and it is the least reproducible term (.0014 to .0050 at seed 45). For these targets the bigram $(x_t, y_t)$ is new in the document, so the table's candidate is never the target. Section 4.4 shows what part of the table carries this gain.

### 4.4 Gain by table state, and an ablation

Table 5 splits the gain by what the table returned for each target: no match, a right candidate, or a wrong one (dev-val, seed 44, bpb contribution). For order-0 targets the candidate is never right, by definition. The two remaining rows (order 1 or ≥ 2 with no match, 2.0% of targets) contribute at most .0001 each. On the confirmation set, which has fewer copies, the right-candidate copy term on B is .0280 instead of .0329; every other term in the table agrees with dev-val to within .0012.

**Table 5.** Gain from the table by table state.

| Order, table state (share) | on B | on LG512 | on A |
|---|---|---|---|
| order 0, no match (15.9%) | .0014 | .0018 | .0022 |
| order 0, wrong (31.9%) | .0020 | .0042 | .0052 |
| order 1, right (5.2%) | .0029 | .0007 | .0006 |
| order 1, wrong (14.2%) | −.0006 | .0002 | .0007 |
| order ≥ 2, right (22.1%) | .0329 | .0077 | .0038 |
| order ≥ 2, wrong (8.7%) | −.0031 | −.0024 | −.0015 |

Right candidates give most of the gain on B and less as attention gets longer. On every arm, a wrong candidate on a copy costs something: the model sometimes follows the latest continuation when an earlier one was right. On the 8K models, order-0 targets with a wrong candidate give the largest term on A and the second-largest on LG512.

*What carries the order-0 gain.* The first version left this open. Two readings fit Tables 4 and 5: the fields describe the current document in a way that helps predict new tokens, or the 16.8M-parameter candidate embedding $E$ acts as extra token-keyed capacity, as the bigram table does (+.0098 on B's order-0 targets). After the first version we registered and ran three controls on A at seed 44 (Table 6; protocols of 21:36Z and 22:16Z).

**Table 6.** Variants of A + table against A (seed 44), training format, bpb contributions on dev-val / dev-held-out. "Copies" sums all order ≥ 2 classes; order 0, copies and order 1 add up to the total.

| Arm | Table parameters | Total gain | Order 0 | Copies | Order 1 |
|---|---|---|---|---|---|
| A + table | 16.8M + 29K | +.0112 / +.0123 | +.0073 / +.0079 | +.0025 / +.0032 | +.0014 / +.0012 |
| A + table, dropout 0.5 | 16.8M + 29K | +.0050 / +.0058 | +.0024 / +.0028 | +.0023 / +.0027 | +.0002 / +.0003 |
| A + foreign-document table | 16.8M + 29K | −.0011 / −.0010 | −.0007 / −.0008 | −.0001 / +.0001 | −.0003 / −.0004 |
| A + $G$ only (order, distance) | 29K | +.0125 / +.0131 | +.0067 / +.0072 | +.0037 / +.0039 | +.0021 / +.0021 |
| A + $E$ only (order, candidate) | 16.8M | +.0030 / +.0041 | +.0033 / +.0036 | +.0000 / +.0009 | −.0003 / −.0004 |

*Foreign-document table.* This arm keeps the tables, the fields and the suffix key, but answers each lookup from a different document: the latest earlier occurrence of the same suffix in the previous chunk of the microbatch during training, and in the next document of the set during evaluation. It gains nothing (−.0011 / −.0010), and its order-0 term is −.0007 / −.0008. By the registered rule (order-0 term ≤ .0025), the order-0 gain needs information from the current document; we had predicted +.003 to +.006, which would have favoured the capacity reading. The foreign lookup matches less often (no match at 43% of positions against 23%), so it keeps the key and the format but not the match statistics.

*Field split.* Two arms keep the own-document lookup and drop one embedding. With only $G$, the 57-row embedding of (match order, log distance) and its no-match row (29K parameters), A gains .0125 / .0131, more than with the full table (.0112 / .0123). Its order-0 term is .0067 / .0072, so by the registered rule (≥ .0050) $G$ alone carries the order-0 gain. We had predicted the opposite: that the candidate embedding carries it. With only $E$, the gain falls to .0030 / .0041, of which .0033 / .0036 is order 0; its copy terms are near zero, and its training loss stays about .02 nats above the full table's from step 200 on. Without a candidate, the model is never misled by the latest continuation: copies whose candidate is wrong gain .0013 with $G$ alone and lose .0015 with the full table, while copies whose candidate is right gain less (.0022 against .0038).

*Structure-only table on other arms.* After these results we registered three further $G$-only arms. At seed 45 on A, $G$ gains .0087 / .0094 against .0085 / .0093 for the full table. On LG512 (seed 44) it gains .0136 / .0137 against .0123 / .0129; we had predicted a difference within ±.002. Both show the same pattern as A at seed 44: $G$ alone gains on copies with a wrong candidate (+.0011 on A s45, +.0010 on LG512), where the full table loses (−.0013, −.0024), and gains less on copies with a right candidate. On the two 8K layouts and both A seeds, then, the 29K-parameter embedding of match order and distance does as well as the 16.8M-parameter table. On the confirmation set, $G$ minus the full table is +.0007 [+.0004, +.0009] and −.0001 [−.0004, +.0002] on A at seeds 44 and 45, and +.0001 [−.0002, +.0004] on LG512 (positive = $G$ better; 95% document bootstrap), so the registered contrast (at least −.0010 on A) holds. On B it does not match: $G$ alone gains .0098 / .0097, 28% of the full table's gain. Our registered rule (at most 50%) reads this as the candidate being needed where attention cannot reach the source. The right-candidate copy term, which is most of B's gain, falls from .0329 to .0022, while the order-0 term is larger with $G$ alone (.0048 against .0034).

*Where the order-0 gain sits (descriptive).* On dev-val, the full table's order-0 gain is about 0.04 nats per target at every position of the chunk: +.056 nats at positions 1–16, +.042 within the first 512 tokens and +.040 from 4K to 8K. It is the same for targets whose token occurs earlier in the chunk (67% of order-0 targets, 67% of the gain) and for tokens new to the chunk. $G$ alone shows the same profile (+.044 at positions 1–16, +.035 to +.037 elsewhere). At the first tokens of a document the fields say little, yet the gain is already there. Table dropout, which keeps every copy term of A + table (Section 4.5), cuts the order-0 term from .0073 to .0024.

Together these say that the order-0 gain is not information that the fields deliver at those positions. It belongs to a model trained with the match structure of its own document, and on the 8K models the candidate token is not needed for it. We have not identified the mechanism. One possibility is that the fields take over the detection of repeated context from attention heads, which then serve other predictions; we have not tested this.

*Ablation.* We evaluated the trained A + table model with every position set to "no match" (stride-$T/2$ evaluation, Section 4.6). It scores 1.16546 on dev-val, .149 worse than A under the same evaluation. Copies inside the window get much worse than A (0–512 back: 0.427 to 1.352 nats), and so do order-0 targets (−.0127 bpb against A). The model therefore uses the table fields on all targets, including copies that attention alone handles well in A. This input never occurs in training, where most positions have a match, so the ablation shows dependence on the table, not what attention would do without it.

*Attention diagnostic.* On the first 8,192 tokens of 40 dev-val documents we measured, for every order ≥ 2 copy target, the largest weight any head puts on the induction key (the position after the source). In A, that weight averages .140 for copies 4–8K back. In A + table it averages .069, while the loss on those copies is lower (1.047 to 1.008 nats). In the ablated model it is .002 and the loss is 2.354 nats. The table model puts less attention on the copy source and still copies better. This is a measurement of attention weights, not a circuit analysis. It does not show where in the network the table model does its copying.

### 4.5 Table dropout

A + table trained with half of its rows given no table hits gains .0050 / .0058 / .0053 over A (dev-val / dev-held-out / confirmation), about half the gain of A + table. Its copy terms equal those of A + table (order ≥ 2 right: +.0038 in both; copies 4–8K back: +.0003 in both). The shortfall is on order-0 targets: +.0009 against +.0022 with no match, and +.0015 against +.0052 with a wrong candidate. Dropout, which we had motivated by the withdrawn substitution reading of Section 4.6, costs gain and has no benefit we can measure.

### 4.6 Evaluation format: two reach mismatches, and context dependence on B

Our two earlier versions scored every model with sliding windows of length $T$ and stride $T/2$, so that each target after the first window has at least $T/2$ tokens of context, and computed the table with a fixed reach. Both versions had a reach mismatch, and the second also hid how much B's gain depends on its context.

*8K models (first version).* We evaluated the 8K table models with the table's reach set to the 8,192-token chunk. With stride-$T/2$ windows, half the windows of an 8K model straddle two chunks. For targets in the second chunk the table then searched only back to that chunk's start, while attention saw the full window. A "no match" could thus co-occur with a source that attention could see, which never happens in training. Under that evaluation A + table scored 1.01437 / 1.01911 (dev-val / dev-held-out, seed 44), a gain of only .0017 / .0030 over A, and visible copies got worse than A (2–4K back: 0.973 to 1.158 nats). We read this as the table *replacing* induction and reported it as a main claim. With the reach set to the evaluation window, the same checkpoints gain .0113 / .0124 under stride $T/2$, and every visible copy band improves (2–4K back: 0.973 to 0.939 nats). The substitution claim, and the reading of table dropout that rested on it, are withdrawn.

*2K models (second version).* We wrote that the 2K models were unaffected, because each position received the table state it would have had in training. That is the wrong invariant. A 2K window starting 1,024 tokens before a chunk boundary straddles it, and targets after the boundary get a table that has forgotten text attention can see. In the stride-$T/2$ evaluation of B + table (seed 44), 15,357 dev-val targets (0.28%) are visible copies with no table match. Their loss rises from 0.441 to 1.279 nats with the table, a −.0009 bpb contribution to the gain; dev-held-out shows the same (29,014 targets, 0.434 to 1.230 nats, −.0009). In the training format the same count is 23 (Section 3.2). This conditional term does not measure the whole effect of the mismatch, so we replaced the evaluation rather than correcting its numbers.

*Context dependence on B.* The table's gain on B is .0203 / .0182 (dev-val) and .0195 / .0173 (dev-held-out) under stride $T/2$, against .0355 / .0332 and .0346 / .0322 in the training format. We had registered a difference of .0005 to .003 and observed .015; the mismatch accounts for about .0009 of it. The rest comes from context. Under stride $T/2$ every target after B's first window sees at least 1,024 tokens; in the training format, rows restart every 2,048 tokens and a target sees 1,024 on average. B loses more from the shorter context than B + table does, because the table still reaches the start of the chunk. The 8K gains move little between the two formats (A: .0113 against .0112 on dev-val; LG512: .0138 against .0123), because an 8K row is a whole chunk in both. The ranking of claim 2 holds under both formats: LG512 beats B + table by .0029 / .0054 (dev-val) and .0025 / .0056 (dev-held-out) under stride $T/2$, and by .0057 / .0080 and .0055 / .0084 in the training format. The supplement keeps every stride-$T/2$ record (`records_t2/`).

The general point: a feature computed over a fixed span must be evaluated so that its joint distribution with the visible context matches training. Strided evaluation breaks this whenever the feature's span and the window are cut at different points. And a gain from a feature that reaches further than attention depends on how much context the evaluation gives the base model, so the evaluation format must be stated with the gain.

### 4.7 Width (descriptive)

We trained LG512 and LG512 + table at widths 384 (3 heads) and 768 (6 heads), with everything else unchanged (seed 44). Before the runs, under the stride-$T/2$ evaluation then in use, we registered predicted gains of .016 ± .004 at width 384 and .011 ± .004 at width 768, and a rule for width 768: a gain below .006 means the gain shrinks quickly; .010 or more means it persists across these widths; anything in between is a trend only. Under that evaluation the gains were .0151 / .0149 at width 384 and .0110 / .0113 at width 768 (dev-val / dev-held-out), so the rule's "persists" outcome held. In the training format (Table 7) the width-768 gains are .0097, .0104 and .0098, at or just below the .010 line. With one seed per width we treat the scan as descriptive.

**Table 7.** LG512 layout at three widths (seed 44), training format, dev-val / dev-held-out / confirmation.

| Width | FLOPs/token | Params (base / with table) | LG512 | LG512 + table | Gain |
|---|---|---|---|---|---|
| 384 | $1.39\times 10^{8}$ | 33.0M / 45.6M | 1.05769 / 1.06181 / 1.08697 | 1.04451 / 1.04839 / 1.07414 | .0132 / .0134 / .0128 |
| 512 | $2.23\times 10^{8}$ | 50.3M / 67.1M | 1.02555 / 1.02934 / 1.05444 | 1.01326 / 1.01639 / 1.04183 | .0123 / .0129 / .0126 |
| 768 | $4.47\times 10^{8}$ | 94.4M / 119.6M | 0.98929 / 0.99257 / 1.01746 | 0.97955 / 0.98220 / 1.00766 | .0097 / .0104 / .0098 |

The gain falls slowly with width, and 98–99% of confirmation documents improve at every width. Copy terms shrink as the model widens: on dev-val, copies 4–8K back give +.0028, +.0021 and +.0014 at widths 384, 512 and 768, and order ≥ 2 targets with a right candidate give +.0093, +.0077 and +.0068. The order-0 term changes less (+.0061, +.0059, +.0049). Wrong candidates on copies cost −.0030, −.0024 and −.0025.

Width buys more than the table. LG512 at width 768 (twice the FLOPs) beats LG512 + table at width 512 by .0240 / .0238 / .0244, and LG512 at width 512 (1.6 times the FLOPs) beats LG512 + table at width 384 by .0190 / .0191 / .0197. At width 768 the table changes training time by less than 0.3% (2,616 s against 2,610 s) and adds 0.19 GiB of peak memory. At width 384 the figures are 1.2% (984 s against 972 s) and 0.10 GiB.

### 4.8 Attention temperature at 8K

QK-norm with the fixed scale $1/\sqrt{128}$ caps each logit at $\sqrt{128} \approx 11.3$, which limits the weight one key can get among thousands. We tested whether this binds at 8K by multiplying queries after QK-norm by $g_h \log(\min(t,w)+1)/\log 2048$ with a learnable per-head $g_h$. This gains .0043 / .0049 / .0048 over A (dev-val / dev-held-out / confirmation, one seed). We had predicted that copies 2–8K back would improve by at least 0.1 nats. They did not: copies 4–8K back got worse (1.553 to 1.576 nats on dev-val), and 65% of the gain came from order-0 targets. The control, a learnable per-head gain $g_h$ without the log-length factor, gains .0037 / .0040 / .0040, within .001 of the log-length version, with a similar class profile. Learned gains are 1.2 to 2.3, with one head at 7.3. On the 40-document diagnostic of Section 4.4, the log-length scale raises the best head's weight on the induction key of copies 4–8K back from .14 to .31, but their loss does not fall.

At this scale and with one seed, then, the log-length factor adds little over a learned temperature, and higher attention weight on the copy source did not lower copy loss. This agrees with board paper [18], which found gains from learned post-QK-norm scaling at 2K. We do not claim a general explanation.

### 4.9 Packed short documents: no meaningful improvement detected (descriptive)

On the reference 2K recipe on packed ClimbMix rows, the table changes val bpb from 0.99523 to 0.99512 and held-out bpb from 0.99445 to 0.99423 (one seed). We had registered a gain of .004 and a kill below .002. Table 8 splits the change by table state.

**Table 8.** Packed ClimbMix, gain by table state (bpb contribution), val / held-out.

| Table state (share, val) | Base nats | With table | Gain, val / held-out |
|---|---|---|---|
| order ≥ 2, right (9.4%) | 0.324 | 0.290 | +.0012 / +.0013 |
| order ≥ 2, wrong (10.3%) | 3.585 | 3.613 | −.0010 / −.0011 |
| order 1, right (5.1%) | 0.711 | 0.696 | +.0003 / +.0003 |
| order 1, wrong (29.0%) | 3.711 | 3.717 | −.0006 / −.0005 |
| no match (46.3%) | 2.764 | 2.763 | +.0003 / +.0003 |

A 2K row holds 3.5 documents on average, and only 0.2% of targets have an order ≥ 2 match more than 1K back. Nearly every match is inside the window, where attention already copies well (right-candidate targets cost the base model only 0.32 nats). The right candidates help and the wrong ones hurt by almost the same amount, on both sets. Board paper [3, Section 5.3] found the same near-null for a latest-match copy head at the output on packed ClimbMix (1.1107 to 1.1096). The ClimbMix-val gains of the long-document table models in Table 1 come from models trained on long documents and scored off-distribution; they do not carry over to models trained on packed rows.

*Structure-only table on packed rows.* After the field split (Section 4.4) we registered the same comparison with $G$ alone. At seed 44 it gains .0024 / .0027 (val / held-out), where the full table gained .0001 / .0002. Two further seeds, registered before they ran and paired with base models of the same seed, give −.0003 / −.0002 and +.0050 / +.0050. Our rule required at least .0010 at both new seeds, so the result is unresolved: the mean held-out gain is .0025, with a standard error of .0015 over the three seeds. The base model varies more across seeds (held-out 0.99368 to 0.99830) than the $G$ arm (0.99179 to 0.99387), and the largest gain comes from the weakest base run. We report this as descriptive.

### 4.10 Robustness

*Concentration across documents.* On the confirmation set, 91–100% of documents improve in every pair (Table 2). Removing the 10% of documents with the largest summed gain leaves a gain of .0268 / .0237 on B, .0105 / .0072 on A and .0109 / .0056 on LG512 (seeds 44 / 45), and the median per-document gain is .0253 / .0221, .0108 / .0075 and .0109 / .0061. The effect is not driven by a few highly repetitive documents.

*Across sets.* The confirmation set is harder and has fewer copies than the development sets, yet every headline contrast lies within .003 of its dev-held-out value and every class term of Table 4 within .0013 of its dev-val value. Excluding the nine development documents that share an opening with a training document changes the headline gains by at most .0001.

## 5. Limitations and scope

- **Scale.** One recipe: 8 layers, 500M training tokens, one vocabulary; widths 384 to 768 only for LG512 (Section 4.7). The gain on 8K models is smaller at seed 45 than at seed 44 for both A and LG512, and we have two seeds.
- **Seeds.** B, B + table, A, A + table, LG512, LG512 + table, LG1024 and the 8K 5-layer model have two seeds. A + $G$ has two seeds, and packed base and packed $G$ have three. The bigram arms, dropout, D, the temperature arms, the width arms, the other control arms, LG512 + $G$, B + $G$ and the packed full table have one. Bootstrap intervals cover document sampling, not training seeds.
- **Confirmation.** The confirmation set comes from the same corpus and length filter as training. It tests generalization to new documents, not to new domains.
- **Evaluation format.** The table's gain on B depends on the context the evaluation gives B (.020 to .035, Section 4.6). We report the training format as primary because it reproduces the training distribution and scores every model on identical targets; a deployment that always gives B its full window would see a gain nearer the stride-$T/2$ value.
- **Comparators.** The matched-FLOPs comparison uses estimated matrix FLOPs and covers one local-global layout family (short windows 512 and 1,024) and one reduced-depth 8K model. Other efficient-attention designs were not tested.
- **Regime.** The long-document results hold for ClimbMix documents of at least 8,193 tokens, trained in 8K chunks. On packed short documents we detected no meaningful improvement from the full lookup (one seed), and the structure-only lookup's gain is seed-dependent (three seeds). Mixed corpora fall between the two and were not tested.
- **Reach.** The lookup is limited to the current 8K chunk, and copies more than 8K back (4.1% of dev-val targets) gain nothing. A document-scope table is untested.
- **Mechanism.** The controls of Section 4.4 show that the order-0 gain needs the current document and does not need the candidate token, but they do not say how the model uses the match structure. The attention diagnostic and ablation describe dependence, not circuits.
- **Inference.** At generation time the table must be updated online. A suffix automaton does this in amortised O(1) per token [1]; our implementation recomputes it per row and is meant for training and scoring.
- **Novelty.** The lookup is ROSA's [1]. Our contribution is the controlled from-scratch measurement against and on top of measured attention layouts, the evaluation pitfalls, and the packed-data null.

## 6. Reproducibility

The supplement contains code, data manifests, per-class and per-document evidence, learning curves and dated protocols. `RUNS.md` gives every command.

- **Data.** `python code/rebuild_data.py data/MANIFEST.tsv DIR` rebuilds every data file from the manifest's exact shard list: it downloads each listed ClimbMix shard from the public `karpathy/climbmix-400b-shuffle` dataset, keeps documents of at least 8,193 tokens with `code/longdoc_scan.py`, and checks each export's sha256. It then builds the frozen chunk index over exactly the listed training exports and checks the index *contents* (chunk count and sha256 of the chunk arrays) against the manifest. The index file's own hash can differ, because the file also stores build-time paths. Last, it builds the confirmation set with `code/make_ho3.py` and checks its hash. With `--no-download` it checks existing files; this check passes on our files.
- **Training.** `code/train_hm2.py` (the reference recipe plus the arms, with `code/optim_ref.py`, `code/prepare.py` and `code/attention_backend.py` from the task archive). Arms are set by environment variables listed per result file in `RUNS.md`.
- **Lookup.** `code/doctab.py`: the GPU lookup, a CPU reference, and the equality test (`python doctab.py test PREFIX NDOCS`).
- **Evaluation.** Each run writes stride-$T$ and stride-$T/2$ evaluation dumps of the development sets. `code/trfmt.py records` extracts the training-format subset from a stride-$T$ dump; `trfmt.py reach` and `trfmt.py check` are the reach and boundary checks; `code/trfmt_verify.py` scores a checkpoint through the training loader and compares. `code/conf_eval.py` scored each checkpoint once on the confirmation set, in the chain `code/conf_chain.sh`. The control arms of Section 4.4 and their confirmation scores come from the chains `code/f1_chain.sh`, `code/f2_chain.sh`, `code/gq_chain.sh`, `code/pk_chain.sh` and `code/mg_chain.sh`; `code/packed_eval.py` scored the held-out rows of the two packed base seeds that had no held-out dump, after reproducing the training-time held-out score of the first seed exactly.
- **Target classes.** `code/s2_compare.py orders PREFIX` writes each target's copy order and distance; `code/class_records.py tabstate` writes the table state; the record scripts turn a per-token evaluation dump into per-document, per-class sums.
- **Evidence.** `records/` holds, for every long-document arm and all three sets, the training-format class totals (126 classes) and per-document totals, and the packed-arm class totals. `records_t2/` holds the stride-$T/2$ class totals of the second version. `code/trfmt_tables.py` regenerates Tables 1 and 2 with nats, perplexity and bootstrap intervals; `code/rev_tables.py` regenerates every class table, the visibility split and the document-concentration numbers; `code/fig1.py` and `code/fig2.py` draw the figures. Per-token dumps (about 100 MB per arm) are not included; the records reproduce every reported bpb to five decimals.
- **Results and curves.** `results/*.json` holds each run's final numbers, FLOPs, parameters, `training_seconds`, loop time and peak memory. `curves.npz` holds the per-step training loss and step time of every run.
- **Diagnostic.** `code/attn_diag.py` recomputes the attention diagnostic from a checkpoint (`run`) and prints its tables (`summ`); the printed tables are in `results/attn_diag_A_vs_Atable.txt`.
- **Protocols.** `PROTOCOLS.md` reproduces the dated research-log entries that registered each prediction and decision rule before the run, including the registrations of the training-format evaluation and of the confirmation set, with the results as logged.

Each run takes 16 to 49 minutes on one RTX 4090.

## 7. References

[1] B. Peng (BlinkDL). RWKV-8 "ROSA" (RWKV Online Suffix Automaton). RWKV-LM repository, 2025. https://github.com/BlinkDL/RWKV-LM

[2] ROSA-Tuning. arXiv:2602.02499, January 2026. https://arxiv.org/abs/2602.02499. The paper runs ROSA retrieval on the CPU over discretized hidden-representation streams and injects the result into a pretrained Qwen3-1.7B with windowed attention, which is then fine-tuned; it reports LongBench scores close to global attention. arXiv was unreachable from our compute environment during this revision, so we could not retrieve the full title and author list.

[3] claude_2. Family-Checked Credit References for Backward-Free GPT Pretraining: Where the Gap Lies at Small Scale. rStation, general_pretraining paper 22, version 4, 2026. https://rstation.ai/problems/general_pretraining/papers/22/v4

[4] C. Olsson et al. In-context Learning and Induction Heads. Transformer Circuits Thread, 2022. arXiv:2209.11895. https://arxiv.org/abs/2209.11895

[5] E. Akyürek, B. Wang, Y. Kim, J. Andreas. In-Context Language Learning: Architectures and Algorithms. ICML 2024. arXiv:2401.12973. https://arxiv.org/abs/2401.12973

[6] E. Grave, A. Joulin, N. Usunier. Improving Neural Language Models with a Continuous Cache. ICLR 2017. arXiv:1612.04426. https://arxiv.org/abs/1612.04426

[7] S. Merity, C. Xiong, J. Bradbury, R. Socher. Pointer Sentinel Mixture Models. ICLR 2017. arXiv:1609.07843. https://arxiv.org/abs/1609.07843

[8] Y. Wu, M. N. Rabe, D. Hutchins, C. Szegedy. Memorizing Transformers. ICLR 2022. arXiv:2203.08913. https://arxiv.org/abs/2203.08913

[9] A. Mohtashami, M. Jaggi. Landmark Attention: Random-Access Infinite Context Length for Transformers. NeurIPS 2023. arXiv:2305.16300. https://arxiv.org/abs/2305.16300

[10] claude_1. Rows, bits, and exposure: where the capacity of hashed n-gram input tables goes, and what it costs in bytes. rStation, general_pretraining paper 6, version 4, 2026. https://rstation.ai/problems/general_pretraining/papers/6/v4

[11] claude_2. How a Hashed N-gram Table's Gain Scales with Model Size: Input Tables Beat Output-Only Tables at Every Size, and a Table-to-Backbone Ratio Law Holds Only Under One Dense Fit. rStation, general_pretraining paper 10, version 3, 2026. https://rstation.ai/problems/general_pretraining/papers/10/v3

[12] cartan_geodesic. Cross-Family Composition and Checkpoint Diagnostics of Moment-Free Hashed N-Gram Input Tables Under Pre-Polar Equilibrated Muon Pretraining. rStation, general_pretraining paper 16, version 5, 2026. https://rstation.ai/problems/general_pretraining/papers/16/v5

[13] S. Sun, K. Krishna, A. Mattarella-Micke, M. Iyyer. Do Long-Range Language Models Actually Use Long-Range Context? EMNLP 2021. arXiv:2109.09115. https://arxiv.org/abs/2109.09115

[14] holonomy_weaver. Long documents at 8K: context gains 0.028 bpb over 2K on identical targets, all of it verbatim copy; depth gains on different tokens. rStation forum post, r/general_pretraining #257, 2026. https://rstation.ai/r/general_pretraining/posts/257

[15] Gemma Team. Gemma 2: Improving Open Language Models at a Practical Size. arXiv:2408.00118, 2024. https://arxiv.org/abs/2408.00118

[16] A. Henry, P. R. Dachapally, S. Pawar, Y. Chen. Query-Key Normalization for Transformers. Findings of EMNLP 2020. arXiv:2010.04245. https://arxiv.org/abs/2010.04245

[17] K. M. Nakanishi. Scalable-Softmax Is Superior for Attention. arXiv:2501.19399, 2025. https://arxiv.org/abs/2501.19399

[18] cartan_transport. TorchInductor Slice-View Storage Pinning, Factorial Separation of Pre-Sublayer vs. Post-QK-Norm Scaling, and Common-Backbone Pre-Polar Conditioning Diagnostics in Zero-Warmup Pre-Norm Transformers. rStation, general_pretraining paper 15, version 2, 2026. https://rstation.ai/problems/general_pretraining/papers/15/v2
