## 1. Problem and contribution

The task asks for pretraining architectures that lower held-out bits per byte (bpb) at fixed compute. On documents longer than the attention window, much of the next-token loss sits on tokens that repeat something said earlier in the same document. A 2K-window model cannot see that earlier text. An 8K-window model can, at a higher attention cost. We ask two questions. How much does an exact lookup into the earlier document lower the loss, alone and on top of each attention layout? And is it a better buy than spending about the same FLOPs on longer attention?

The lookup (the *document table*) is the rule ROSA uses in RWKV-8 [1]: find the longest suffix of the current context, of 1 to 4 tokens, that occurred earlier in the document, and return the token that followed its latest occurrence. We add a learned embedding of that token, and a learned embedding of (match order, log distance), to the input. All models are trained from scratch for the same 953 updates of $2^{19}$ tokens on identical target sequences, so arms differ only in architecture; Section 4.11 repeats five arms, and for claim 2 the 8K local-global model, at half and twice that length. Every model is scored in the format it was trained in, and the headline contrasts were confirmed on a fresh set of documents, fixed after all training and scored once.

Claims, on the long-document regime of Section 3 unless stated. Numbers are on the confirmation set; s44 / s45 are the two seeds.

1. **The lookup adds to every attention layout tested, at no extra matrix FLOPs.** It is not free: it adds 16.8M embedding parameters, and its sorts and gathers take 0.3% of training time and 0.12 GiB of memory (Section 4.2); its cost in online generation is unmeasured. Gains are .0320 / .0294 on a 2K model, .0113 / .0081 on an 8K model, and .0126 / .0076 on an 8K local-global model with 512-token local windows. Every 95% document-bootstrap interval excludes 0, and 91–100% of documents improve.
2. **At approximately matched estimated matrix FLOPs, local-global attention beats the lookup at the tested 953- and 1,906-update budgets.** The 8K local-global model costs 1.03 times the 2K model's estimated FLOPs per token and beats the 2K model with the lookup by .0051 / .0082 at 953 updates. At 1,906 updates its lead is .0095 / .0104, against .0057 / .0055 at 953 updates on the same sets; that comparison has one seed and uses the development sets only. At 477 updates the two are within .003 (Section 4.11). The best model at this cost is local-global attention with the lookup (1.04183 / 1.04715).
3. **Where the gain comes from depends on what attention can see, and on 8K models a structure-only embedding matches it.** On the 2K model, 78% of the gain comes from copies whose source lies outside the model's row. On the 8K models, copies inside the window still improve, and the largest class term comes from targets the table cannot predict: targets whose context-target bigram $(x_t, y_t)$ is new in the document (order 0). The token itself may have occurred before. In a registered control (Section 4.4), a lookup answered from another document gains nothing on this term. That lookup also finds no match more often (43% of positions against 23%), so the control does not separate the current document from the match rate. Trained and scored with its own fields thinned at random to the foreign lookup's no-match rate, the full lookup keeps .56–.58 of its order-0 term at seed 44 and .32–.39 at seed 45: thinning lowers the gain, and the thinned own fields still beat the foreign lookup, which has one seed. On both 8K layouts, the 29K-parameter embedding of (match order, log distance) alone, without the returned token, matches the full lookup. On the confirmation set it differs from the full lookup by +.0007 / −.0001 on the 8K model and +.0001 on the local-global model (positive = better). On the 2K model it gives 28% of the full gain: there the returned token is needed. About 90% of the structure-only order-0 gain is a higher log-probability of the target within its group (tokens already in the row, or new), not a shift of probability between those groups. Over four seeds this order-0 term ranges from .0033 to .0067 bpb on dev-val, and seed 44, the seed of our one-seed controls, gives the largest. We have not identified how the model uses the match structure.
4. **Evaluation must give the lookup and attention the same spans as in training.** When a strided evaluation cuts the lookup's span and the attention window at different points, in-window copies get worse. Our first version made this error on 8K models and reported a spurious "substitution" of induction by the lookup; our second version kept a smaller instance on 2K models. Separately, the 2K model's gain depends on how much context the evaluation gives it: .020 under stride-$T/2$ sliding windows against .035 in the training format (dev-val, Section 4.6). The ranking in claim 2 holds under both.
5. **On packed short documents we detected no meaningful improvement from the full lookup** (held-out +.0002, one seed). Its right guesses help and its wrong guesses hurt by about the same amount. The structure-only lookup of claim 3 gains +.0027, −.0002 and +.0050 at three seeds (held-out), which our registered rule leaves unresolved (Section 4.9). Both results are descriptive.
6. **Width, descriptive (one seed).** On the local-global model the gain is .0128, .0126 and .0098 at widths 384, 512 and 768. Width itself buys more: the width-768 model without the lookup beats the width-512 model with it by .0244, at twice the FLOPs (Section 4.7).
7. **Training length, descriptive except where registered (Section 4.11; development sets; two seeds of A and A + $G$ at the longest length, one for the other arms).** We trained five arms for 477, 953 and 1,906 updates, each with its full schedule. On the 2K model, on copies whose source lies in the lookup's 8,192-token chunk but before the model's row, so that only the lookup can reach it, the lookup removed 44–45% of the remaining loss at all three lengths. On the 8K model the total gains of the lookup and of the structure-only embedding shrank by 17–34% per doubling of training (to .0093 and .0090 on dev-val at 1,906 updates, seed 44), so the 8K gains at 953 updates may overstate those after longer training. In a registered test at two seeds, the structure-only embedding's order-0 gain on the 8K model shrank by 18–24% per doubling from 953 to 1,906 updates and its copy gain by 36–47%.

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
- **Field split.** The table with only $G$, the (match order, log distance) embedding and its no-match row (29K parameters), or only $E$, the (order, candidate) embedding (16.8M parameters). $G$ alone was run on A at four seeds, on LG512, on B and on packed ClimbMix at three seeds; $E$ alone on A. $G$ alone with dropout 0.5 was run on A at two seeds (Section 4.4).
- **Match rate and field position (TT, GR).** TT is A + table trained with each own field set to "no match" with probability .3664, so that 48.6% of training positions have no match, the foreign arm's rate. GR is A + $G$ trained and scored with the field at chunk position $t$ replaced by the field at position $\lfloor u t \rfloor$, with $u$ uniform on [0, 1) and drawn per position. Both were run at seeds 44 and 45 (Section 4.4).
- **Seeds 46 and 47.** A and A + $G$ were also trained at seeds 46 and 47, to measure how the order-0 term varies across initialisations (Section 4.4).
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

- LG512 (1.03 times the FLOPs) is better by .0051 [.0042, .0060] / .0082 [.0073, .0092]. On the development sets the margin is .0057 / .0080 (dev-val) and .0055 / .0084 (dev-held-out). H4 is confirmed. The margin depends on the training budget: at seed 44, on the development sets, it is within .003 of zero at 477 updates and .0095 / .0104 at 1,906 (Section 4.11).
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

### 4.4 What carries the order-0 gain

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

Right candidates give most of the gain on B and less as attention gets longer. On every arm, a wrong candidate on a copy costs something: the model sometimes follows the latest continuation when an earlier one was right. On the 8K models, order-0 targets with a wrong candidate give the largest term on A and the second-largest on LG512. The table cannot predict these targets, whose bigram is new in the document. The rest of this section asks what carries their gain. Each control was registered before it ran; the rules, our predictions and the outcomes are listed in `results/registrations_44.md`, and the dated entries are in `PROTOCOLS.md`.

*Candidate capacity or document structure?* Two readings fit Tables 4 and 5. Either the fields describe the current document in a way that helps predict new tokens, or the 16.8M-parameter candidate embedding $E$ acts as extra token-keyed capacity, as the bigram table does (+.0098 on B's order-0 targets). Table 6 gives three controls on A at seed 44.

**Table 6.** Variants of A + table against A (seed 44), training format, bpb contributions on dev-val / dev-held-out. "Copies" sums all order ≥ 2 classes; order 0, copies and order 1 add up to the total.

| Arm | Table parameters | Total gain | Order 0 | Copies | Order 1 |
|---|---|---|---|---|---|
| A + table | 16.8M + 29K | +.0112 / +.0123 | +.0073 / +.0079 | +.0025 / +.0032 | +.0014 / +.0012 |
| A + table, dropout 0.5 | 16.8M + 29K | +.0050 / +.0058 | +.0024 / +.0028 | +.0023 / +.0027 | +.0002 / +.0003 |
| A + foreign-document table | 16.8M + 29K | −.0011 / −.0010 | −.0007 / −.0008 | −.0001 / +.0001 | −.0003 / −.0004 |
| A + $G$ only (order, distance) | 29K | +.0125 / +.0131 | +.0067 / +.0072 | +.0037 / +.0039 | +.0021 / +.0021 |
| A + $E$ only (order, candidate) | 16.8M | +.0030 / +.0041 | +.0033 / +.0036 | +.0000 / +.0009 | −.0003 / −.0004 |

The foreign-document table keeps the tables, the fields and the suffix key, but answers each lookup from another document: the previous chunk of the microbatch in training, and the next document of the set in evaluation. It gains nothing, and its order-0 term is −.0007 / −.0008. It also finds no match more often (43% of positions against 23%), so it changes both the document and the match rate. With only $G$, the 29K-parameter embedding of (match order, log distance), A gains .0125 / .0131, more than with the full table, and its order-0 term is .0067 / .0072. With only $E$ it gains .0030 / .0041. On A, then, the order-0 gain does not appear with a foreign-document lookup and does not need the candidate token.

The structure-only result repeats on A at seed 45 ($G$ .0087 / .0094 against .0085 / .0093 for the full table) and on LG512 (.0136 / .0137 against .0123 / .0129). On the confirmation set, $G$ minus the full table is +.0007 [+.0004, +.0009] and −.0001 [−.0004, +.0002] on A at seeds 44 and 45, and +.0001 [−.0002, +.0004] on LG512 (positive = $G$ better; 95% document bootstrap). Without a candidate the model is never misled by the latest continuation. On copies with a wrong candidate, $G$ alone gains (+.0013, +.0011 and +.0010 on A at seed 44, A at seed 45 and LG512) where the full table loses (−.0015, −.0013, −.0024); on copies with a right candidate it gains less. B differs. There $G$ alone gains .0098 / .0097, 28% of the full table's gain, because the right-candidate copy term, most of B's gain, falls from .0329 to .0022. Where attention cannot reach the source, the candidate is needed. B's order-0 term is larger with $G$ alone (.0048 against .0034).

The order-0 gain is spread evenly over the chunk. With the full table it is about .04 nats per target throughout (+.056 at positions 1–16, +.040 from 4K to 8K; dev-val), and the same for targets whose token occurs earlier in the chunk (67% of order-0 targets) as for tokens new to the chunk; $G$ alone shows the same profile. At the first tokens of a document the fields say little, yet the gain is already there, so it is not information that the fields deliver at those positions. Table dropout keeps every copy term of A + table but cuts the order-0 term from .0073 to .0024 (Section 4.5).

*Match rate and the field's own position (Table 6c).* Two training arms each change one property of the own-document fields. TT trains A + table with each field set to "no match" with probability .3664, which makes its training no-match rate equal to the foreign arm's (48.6%). It is scored in distribution: its own fields are thinned at random at a probability set per evaluation set, so that the no-match rate on full-chunk positions equals the foreign lookup's (.40 on dev-val, .37 on dev-held-out). Its order-0 term is +.0043 / +.0044 at seed 44, .58 / .56 of A + table's, and +.0019 / +.0017 at seed 45, .39 / .32 of A + table's. Thinning the own fields therefore reduces their order-0 gain, and at the tested marginal rate the thinned fields still beat the foreign lookup (−.0007 / −.0008, seed 44 only). This does not divide the foreign arm's shortfall into a part due to the rate and a part due to the document. Thinning changes which fields are present and how they relate to the text, and the two can interact. Scored with its full own fields, an input it never saw in training, TT's order-0 term is negative at both seeds. On order-0 targets with a wrong candidate, it then puts more probability on that candidate than A does (.100 against .089 on average; seed 44, dev-val).

GR trains and scores A + $G$ with the field at chunk position $t$ replaced by the field at position $\lfloor u t \rfloor$, with $u$ uniform on [0, 1). In training $u$ is drawn per position, row and update; in evaluation one fixed pattern is shared by all rows. The replacement fields no longer describe the current context. Their distribution also changes, because a uniform draw over the prefix favours early positions, where matches are rarer and closer. GR keeps .65 of A + $G$'s order-0 term at seed 44 (+.0044 / +.0046) and none at seed 45 (−.0003 / −.0003). Its copy terms turn negative at both seeds, as expected once the fields no longer point at a source. By the registered rules, both TT and GR are unresolved, and for GR the two seeds disagree.

**Table 6c.** Training arms that vary the match rate (TT) and the field's position (GR), against A of the same seed; training format, bpb contributions on dev-val / dev-held-out, as in Table 6. TT is scored with its own fields thinned at the foreign lookup's evaluation rate (as in training) and with its full own fields (not seen in training).

| Arm | Seed | Order 0 | Copies | Order 1 | Total |
|---|---|---|---|---|---|
| A + table | 44 | +.0073 / +.0079 | +.0025 / +.0032 | +.0014 / +.0012 | +.0112 / +.0123 |
| A + table | 45 | +.0050 / +.0052 | +.0027 / +.0034 | +.0009 / +.0007 | +.0085 / +.0093 |
| A + foreign-document table | 44 | −.0007 / −.0008 | −.0001 / +.0001 | −.0003 / −.0004 | −.0011 / −.0010 |
| TT, thinned own fields | 44 | +.0043 / +.0044 | +.0011 / +.0017 | +.0008 / +.0009 | +.0062 / +.0070 |
| TT, thinned own fields | 45 | +.0019 / +.0017 | +.0009 / +.0014 | +.0000 / +.0002 | +.0028 / +.0032 |
| TT, full own fields | 44 | −.0009 / −.0008 | +.0042 / +.0046 | +.0017 / +.0018 | +.0050 / +.0057 |
| TT, full own fields | 45 | −.0025 / −.0028 | +.0037 / +.0042 | +.0009 / +.0011 | +.0021 / +.0025 |
| A + $G$ | 44 | +.0067 / +.0072 | +.0037 / +.0039 | +.0021 / +.0021 | +.0125 / +.0131 |
| A + $G$ | 45 | +.0043 / +.0044 | +.0032 / +.0038 | +.0012 / +.0012 | +.0087 / +.0094 |
| GR | 44 | +.0044 / +.0046 | −.0030 / −.0034 | +.0011 / +.0010 | +.0025 / +.0022 |
| GR | 45 | −.0003 / −.0003 | −.0005 / −.0001 | −.0006 / −.0004 | −.0014 / −.0008 |

*How trained checkpoints depend on their fields (Table 6b, Figure 3).* These tests re-score fixed checkpoints with altered fields. With every position set to "no match" (stride-$T/2$ evaluation, Section 4.6), A + table scores 1.16546 on dev-val, .149 worse than A, and it is worse than A on every target class, including copies that A handles well (0–512 back: 1.352 nats against 0.427). In the training format we re-scored the two A + $G$ checkpoints and the three checkpoints trained with table dropout. With their own fields, the re-scorings reproduce the training-format scores to within .00003 bpb. Table 6b reports three target populations. The first is order-0 targets (48–50% of targets). The second is copies whose source lies earlier in the document but before the target's 8,192-token chunk, which neither attention nor the table can reach ("outside the chunk", 4.6–6.6%). The third is copies whose source lies inside the chunk (25%). The registered rules pool the first two populations; they respond differently, so we report them apart. For each of the first two, a cell gives the retained share $(A - \text{altered}) / (A - \text{own})$, where each term is that model's summed loss in nats on those targets. A share of 1 keeps the gain that the own fields give over A, 0 is A's loss, and a negative share is worse than A. For copies inside the chunk the cell is the loss as a multiple of A's.

**Table 6b.** Field interventions at evaluation (training format, dev-val / dev-held-out). Rows "own" give the share of A's loss that the own fields remove. "Next document's": the fields of the next document of the set at the same offset, as in the foreign arm's evaluation. "Thinned": a seeded random fraction of positions (.40 on dev-val, .37 on dev-held-out) set to "no match", so that 48–50% of the input positions of these full chunks have no match, as with the next document's fields (18% with the own fields). Each model is compared with A of the same seed. n/a: the own fields' gain on that population is negative.

| Checkpoint | Fields at evaluation | Order 0, retained | Copies outside chunk, retained | Copies inside chunk, loss / A's | Total, bpb − A |
|---|---|---|---|---|---|
| A + G, seed 44 | own | 0.94% / 0.96% | 1.25% / 1.42% | 0.95 / 0.94 | −.0125 / −.0131 |
| A + G, seed 44 | next document's | −.50 / −.48 | −3.60 / −4.00 | 2.22 / 2.19 | +.0930 / +.0886 |
| A + G, seed 44 | none | −2.83 / −2.74 | −8.72 / −8.59 | 2.78 / 2.76 | +.1600 / +.1546 |
| A + G, seed 44 | own, random half removed | +.35 / +.32 | −.90 / −1.53 | 1.65 / 1.64 | +.0457 / +.0448 |
| A + G, seed 44 | own, thinned to the foreign rate | +.69 / +.74 | +.03 / −.39 | 1.46 / 1.41 | +.0285 / +.0242 |
| A + G, seed 45 | own | 0.60% / 0.59% | 1.21% / 1.15% | 0.96 / 0.94 | −.0087 / −.0094 |
| A + G, seed 45 | next document's | −1.15 / −1.20 | −3.49 / −4.88 | 2.24 / 2.21 | +.0974 / +.0934 |
| A + G, seed 45 | none | −4.39 / −4.57 | −7.74 / −9.91 | 2.74 / 2.73 | +.1573 / +.1546 |
| A + G, seed 45 | own, random half removed | +.27 / +.22 | −.62 / −1.52 | 1.59 / 1.57 | +.0439 / +.0426 |
| A + G, seed 45 | own, thinned to the foreign rate | +.71 / +.77 | +.15 / −.33 | 1.42 / 1.36 | +.0281 / +.0236 |
| A + table, dropout, seed 44 | own | 0.32% / 0.36% | −.18% / 0.13% | 0.96 / 0.95 | −.0049 / −.0058 |
| A + table, dropout, seed 44 | none | +.74 / +.76 | n/a / +.66 | 1.04 / 1.04 | +.0010 / .0000 |
| A + G, dropout, seed 44 | own | 0.47% / 0.50% | 0.47% / 0.64% | 0.96 / 0.96 | −.0070 / −.0074 |
| A + G, dropout, seed 44 | none | +.55 / +.56 | +.64 / +.42 | 1.01 / 1.01 | −.0017 / −.0020 |
| A + G, dropout, seed 45 | own | 0.23% / 0.23% | 0.41% / 0.38% | 0.96 / 0.96 | −.0046 / −.0048 |
| A + G, dropout, seed 45 | none | −.38 / −.31 | −.02 / −.16 | 1.02 / 1.02 | +.0027 / +.0023 |

![Figure 3: three panels of order-0 retained share for the two A + G checkpoints on dev-val. (a) Random removal with nested masks: the share rises slightly at a removed fraction of .1, is about .7 at the thinned rate (.40) and .35 / .27 at .5, reaches 0 near .55–.58, and is −1.2 / −2.0 at .8 and −2.8 / −4.4 with all fields removed (below the plotted range, marked ▼); the most repetitive third of documents falls earlier than the least repetitive third. (b) Removal of half of the fields in blocks of 1 to 2,048 positions: the share falls with block length, from .35 / .27 to −.69 / −1.36; for targets whose own field is intact it falls from .20 / .02 to −.17 / −.63. (c) Blocks of 2,048, targets with their own field intact, by distance back to the nearest removed field: about −3.6 / −5.0 at distance 1, below 0 up to 1,023 positions, .64 / .61 at 1,024 or more, and 1 with no removed field earlier in the chunk. Bars: 95% document-bootstrap intervals, conditional on the checkpoint and the mask.](supplement/figure-3.png)

Four observations hold in both A + $G$ checkpoints. First, own fields thinned at random to the foreign lookup's no-match rate keep .69–.77 of the order-0 gain, while the next document's fields make order-0 targets worse than A (−.48 to −1.20). At the same marginal rate the two inputs still differ in match order, distance, placement and dependence on the text, so this does not say which property matters. Second, every intervention leaves the model worse than A in total, by .024 to .160 bpb (1.8 to 18 times its gain), and the loss on copies inside the chunk rises to 1.4–2.8 times A's. These inputs never occur in training, so this measures sensitivity to a shifted input, not what attention would do without the fields. Third, the change reaches targets whose own field is unchanged. When half of the fields are removed in blocks of 2,048 positions, order-0 targets whose own field is intact keep only .64 [.55, .71] / .61 [.47, .72] of their gain (seeds 44 / 45, 95% document bootstrap) even when the nearest removed field lies 1,024 or more positions back (Figure 3c). Targets with no removed field earlier in their chunk reproduce their own-field loss exactly, as causal attention requires. Field changes more than 1,000 positions earlier therefore change order-0 predictions. Fourth, the retained share depends on how many fields are removed and how they are grouped. With nested random masks it falls smoothly on the sampled grid, to half at a removed fraction of .45–.46 and to zero near .55–.58, and it falls earlier in the most repetitive third of documents (Figure 3a). Removing half of the fields in contiguous blocks costs more than removing them at random: the share falls from .35 / .27 for single positions to −.69 / −1.36 for blocks of 2,048 (Figure 3b). A share at one removal rate, such as the thinned rows of Table 6b, is one point on these curves.

For the three dropout models, "no fields" is an input they saw in training. Without fields, their loss on copies inside the chunk is 1.01–1.04 times A's, against 2.7–2.8 times for A + $G$. Their retained order-0 share varies: .74 / .76 for the full-table dropout model (one seed), and .55 / .56 at seed 44 and −.38 / −.31 at seed 45 for the structure-only dropout model. The gains involved are small. Without fields, the full-table dropout model gains .0017 / .0021 bpb on order-0 and outside-chunk targets together, one to two times the difference between A's two seeds on the same targets (.0014 / .0011).

*Where the gain appears: output groups and attention.* For each target we split the vocabulary into three groups: the table's candidate, the other tokens already among the row's inputs ("context"), and tokens not yet in the row ("new"). The log-probability of the target is the log-probability of its group plus its log-probability within that group, so A + $G$'s gain over A splits into a group term and a within-group term. On order-0 targets the group term is .096 / .104 of the gain at seed 44 and .107 / .100 at seed 45 (95% document-bootstrap intervals within [.085, .124]), and the mean probability of each group changes by less than .002. About 90% of the order-0 gain is therefore a higher conditional log-probability of the target within its group. Most of it falls on targets whose token is already in the row: on dev-val, .0262 of the .0371 nats per target at seed 44 and .0129 of .0239 at seed 45. On copies the group term is .63–.72 of the gain, and A + $G$ moves probability onto the candidate.

If the fields help the model find earlier occurrences of the token that comes next, attention should weight those occurrences more. We measured this on the first 8,192 tokens of 40 documents of each development set. For each order-0 target whose token $y$ occurs earlier in the row (125,000 to 133,000 targets per set), we summed, in each head, the attention mass on all earlier positions holding $y$ and took the maximum of that sum over layers and heads. As a control we computed the same for another token $y'$ of the row, drawn with the same number of earlier occurrences where one exists and with the closest count otherwise; on average $y'$ occurs 27.4 / 27.8 times and $y$ 29.1 / 29.6 times. The control removes changes that reach any comparably frequent token of the row. It does not equalise where the occurrences sit, their baseline logits or which head attains the maximum, so the excess is a descriptive contrast (Table 6d).

**Table 6d.** Attention on earlier occurrences of the next token, for order-0 targets whose token $y$ occurs earlier in the row (first 8,192 tokens of 40 documents per set; dev-val / dev-held-out). Weight: the maximum over layers and heads of the summed attention mass on earlier positions holding $y$ (or the control token $y'$), averaged over targets. Excess: A + $G$ minus A on $y$, minus the same on $y'$, with 95% document-bootstrap intervals. Gain: A's loss minus A + $G$'s on these targets, in nats per target. The registered test is seeds 44 and 45 on dev-val. Dev-held-out at every seed, and seeds 46 and 47 on both sets (added after they trained), are descriptive.

| Seed | Weight on $y$, A → A + $G$ | Weight on $y'$, A → A + $G$ | Excess beyond control | Gain |
|---|---|---|---|---|
| 44 | .0661 → .0742 / .0658 → .0746 | .0386 → .0405 / .0389 → .0408 | +.0062 [.0051, .0073] / +.0069 [.0056, .0082] | .0383 / .0385 |
| 45 | .0645 → .0659 / .0644 → .0656 | .0358 → .0355 / .0362 → .0355 | +.0017 [.0008, .0025] / +.0019 [.0010, .0029] | .0198 / .0223 |
| 46 | .0668 → .0673 / .0667 → .0663 | .0413 → .0370 / .0409 → .0372 | +.0048 [.0029, .0070] / +.0032 [.0017, .0050] | .0266 / .0233 |
| 47 | .0707 → .0645 / .0700 → .0647 | .0400 → .0358 / .0405 → .0362 | −.0021 [−.0029, −.0012] / −.0010 [−.0019, −.0002] | .0156 / .0066 |

At seeds 44 and 45, the seeds of the registered test (dev-val; dev-held-out agrees), A + $G$ weights earlier occurrences of $y$ more than A does, beyond the control, and more so at seed 44, where the gain is larger. A + table at seed 44 shows the same excess (+.0061 / +.0053). The two later seeds show that this extra weight is not needed for a gain. At seed 46 the excess over the control comes from less weight on $y'$, not more on $y$. At seed 47, A + $G$ weights earlier occurrences of $y$ less than A does, by both measures, and still gains on these targets. What holds at all four seeds is an ordering: the excess ranks the seeds exactly as their gains on these targets, on both sets (44, 46, 45, 47). The layer with the largest excess also changes with the seed (layers 6, 3, 5 and 3 at seeds 44 to 47). Four seeds make this a weak association, and the measurement is correlational. For copies, the same kind of measurement points the other way. On copies 4–8K back, the largest weight any head puts on the induction key (the single position after the source) averages .140 in A and .069 in A + table, while A + table's loss on these copies is lower (1.008 against 1.047 nats).

*Seeds.* At seeds 44 and 45, the order-0 term of every lookup arm run at both seeds was smaller at seed 45, by .0020 to .0049, while the two seeds of each base model differ by .0002 to .0011 on the same targets. These six comparisons count as two initialisations, not six. Every arm is built and initialised in a fixed order, with the table embeddings zero-initialised after the shared layers, and the data loader uses fixed generators, so all arms of one seed start from the same weights in their shared layers and see the same data in the same order. We therefore trained A and A + $G$ at seeds 46 and 47. A + $G$'s order-0 term is +.0067 / +.0072, +.0043 / +.0044, +.0049 / +.0052 and +.0033 / +.0032 at seeds 44 to 47: mean +.0048 / +.0050, standard deviation .0015 / .0017. Our registered rule would have called seed 44 atypically high if both new seeds gave at most .0050 on both sets, and seed 45 atypically low if both gave at least .0060. Neither held (seed 46 gives .0052 on dev-held-out), so the rule reads as a spread across seeds. Four initialisations cannot establish the distribution across seeds or rule out an atypical one; the mean, range and standard deviation are the informative result. The copy term varies much less (+.0037, +.0033, +.0042 and +.0039 on dev-val), and the total gain is positive at every seed (+.0084 to +.0125 on dev-val). A's own order-0 loss varies less across the four seeds (standard deviation .0009 / .0010) and does not predict the gain: A is best on order-0 targets at seed 47, which has the smallest gain. Seed 44, the seed of the headline numbers and of the one-seed controls in Table 6, has the largest order-0 term of the four. Two-seed shares such as TT's and GR's are therefore imprecise.

In sum, on the 8K models the order-0 gain does not appear with a foreign-document lookup, does not need the candidate token, and shrinks when the own fields are thinned in training. Its size varies across initialisations (.0033 to .0067 bpb on dev-val for A + $G$) more than the base model's own order-0 loss does. Across four initialisations it ranks with how much more A + $G$ weights earlier occurrences of the next token than A does, but at one seed it appears without that extra weight. We have not shown how the fields produce it.

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

### 4.11 Training length (descriptive)

All gains above are at 953 updates. To see how they depend on the training budget, we trained B, B + table, A, A + table and A + $G$ for 477 updates (half the tokens; seed 44, with A and A + $G$ also at seed 45) and for 1,906 updates (twice the tokens; seed 44, with A and A + $G$ also at seed 45). Each length is a complete run: the learning-rate warmdown (the last half), the Muon momentum ramp and the weight-decay schedule are scaled to its number of updates. The 477-update runs use the first half of the original data order. The 1,906-update runs use an extended index whose first 62,538 chunks are the original index in order, followed by 72,199 chunks from 137 further long-document exports with the same length filter; the confirmation set's exports are excluded (Section 6). All numbers in this section are on the two development sets, which we consulted during the study. The confirmation set was not scored.

**Table 9.** Total gain (bpb, base minus arm), training format, dev-val / dev-held-out, and its ratio $r$ between consecutive lengths.

| Arm (seed) | 477 updates | 953 | 1,906 | $r$, 477 → 953 | $r$, 953 → 1,906 |
|---|---|---|---|---|---|
| B + table (44) | .0393 / .0389 | .0355 / .0346 | .0319 / .0303 | .90 / .89 | .90 / .88 |
| A + table (44) | .0147 / .0151 | .0112 / .0123 | .0093 / .0101 | .76 / .81 | .83 / .82 |
| A + $G$ (44) | .0174 / .0172 | .0125 / .0131 | .0090 / .0098 | .72 / .77 | .72 / .75 |
| A + $G$ (45) | .0122 / .0120 | .0087 / .0094 | .0057 / .0062 | .71 / .78 | .66 / .66 |

*Populations.* To see which targets keep their gain, we split copies at most 8K back by what can reach their source. Copy distance is measured over the whole document (Section 3.5), but the table searches only the target's 8,192-token chunk. A copy at most 8K back can therefore have its source in the previous chunk: on dev-val this holds for 9% of these copies and for half of those 4–8K back. A copy is *in chunk* if its source lies in the target's chunk. The table can then reach it, and on A so can attention, because A's row is the chunk. A copy *outside the chunk* cannot be reached by the table or by A's attention. On B we further split in-chunk copies by whether the source lies in B's 2K row. Table 10 gives the share of the base model's loss that each arm removes on each population, $f = (\ell_{\mathrm{base}} - \ell_{\mathrm{arm}}) / \ell_{\mathrm{base}}$, with $\ell$ the mean loss in nats per target. Board paper [19] compared a hashed n-gram table's gain across corpora in a similar unit, as a fraction of the dense model's bpb.

**Table 10.** Share $f$ of the base model's loss removed, dev-val / dev-held-out, at each training length. Copies at most 8K back, split by where the source lies; order 0 for comparison.

| Arm (seed) | Population | 477 updates | 953 | 1,906 |
|---|---|---|---|---|
| B + table (44) | in chunk, before B's row (only the table reaches it) | .452 / .453 | .446 / .446 | .442 / .440 |
| B + table (44) | in B's row (attention and table reach it) | .069 / .067 | .062 / .060 | .056 / .047 |
| B + table (44) | outside chunk (nothing reaches it) | −.009 / −.002 | −.003 / .004 | .000 / −.001 |
| A + table (44) | in chunk | .057 / .059 | .037 / .049 | .026 / .039 |
| A + table (44) | in chunk, 4–8K back | .109 / .123 | .036 / .047 | .037 / .046 |
| A + table (44) | outside chunk | .002 / .008 | .004 / .012 | .005 / .010 |
| A + $G$ (44) | in chunk | .092 / .090 | .051 / .059 | .030 / .040 |
| A + $G$ (44) | in chunk, 4–8K back | .187 / .192 | .066 / .074 | .054 / .059 |
| A + $G$ (44) | outside chunk | .014 / .016 | .013 / .015 | .009 / .011 |
| A + $G$ (45) | in chunk | .088 / .089 | .044 / .058 | .025 / .036 |
| A + $G$ (45) | in chunk, 4–8K back | .191 / .205 | .085 / .101 | .052 / .062 |
| A + $G$ (45) | outside chunk | .005 / .008 | .013 / .013 | .007 / .008 |
| B + table (44) | order 0 | .005 / .005 | .005 / .004 | .003 / .003 |
| A + table (44) | order 0 | .012 / .012 | .010 / .010 | .009 / .009 |
| A + $G$ (44) | order 0 | .010 / .010 | .009 / .009 | .007 / .008 |
| A + $G$ (45) | order 0 | .006 / .006 | .006 / .006 | .005 / .005 |

*On B.* Where only the table can reach the source, it removes 44–45% of B's loss at all three lengths, on both sets, while B's own loss on these copies falls by 7.5% and then 5.5%. So the gain in nats per target falls with B's loss (.974, .889 and .832 on dev-val), and the share changes by at most .013. Where B's attention can also see the source, the table's share is small and falls at each doubling (from .069 to .056 on dev-val and from .067 to .047 on dev-held-out). On copies whose source lies outside the chunk the table gains nothing at any length ($|f| \le .009$), as expected, since nothing reaches them.

*On A.* Both arms' shares of the in-chunk copy loss fall at each doubling, so their gains in nats fall faster than A's own loss on those copies, which falls by 13% and then 7% on dev-val. On copies 4–8K back most of the fall comes in the first doubling. On copies outside the chunk, which neither the table nor A's attention can reach, both arms still remove .002 to .016 of the loss, similar in size to their order-0 shares (.007 to .012). This part of their gain does not come from reaching the source. The two sets can disagree: for A + table between 477 and 953 updates, the in-chunk share falls by 34% on dev-val and by 17% on dev-held-out. At 1,906 updates the full table and $G$ alone gain about the same on A (.0093 / .0101 against .0090 / .0098 bpb). At 477 updates $G$ gained more (.0174 against .0147 on dev-val).

*Order 0 against copies (registered).* After the 953-update seed results of Section 4.4, we conjectured that on A the structure-only embedding's copy gain is a head start that training removes, while its order-0 gain lasts. Before either run we registered a test at seed 45 for 1,906 updates (LEN45). Let $r_o$ and $r_c$ be the ratios of A + $G$'s gain at 1,906 and 953 updates, in nats per target, on order-0 targets and on copies at most 8K back. The rule reads the order-0 gain as more durable if $r_o \ge .70$ and $r_o - r_c \ge .15$ on both development sets, as fading equally if $r_o - r_c < .05$ on both, and as mixed otherwise. Seed 45 gives $r_o$ = .76 / .82 and $r_c$ = .53 / .56, so the order-0 gain is the more durable, as at seed 44 (.78 / .82 and .56 / .64). It still shrinks by 18–24% per doubling, against 36–47% for copies. At seed 45 it held through the first doubling (.99 / .98) and fell in the second. Two doublings cannot tell slow decay from a plateau. At 1,906 updates the order-0 term is 57–59% of A + $G$'s total gain at both seeds. The copy gain is similar at the two seeds (.0140 / .0187 nats per target at seed 45, .0170 / .0214 at seed 44). The order-0 gain at seed 45 stays at .63 / .62 of seed 44's, as at 953 updates, while A's own order-0 losses at the two seeds agree to .0006 nats. Over this range, longer training does not remove the seed dependence of the order-0 gain. A further doubling would need more data than the extended index holds (`results/len45.txt`).

*Registered predictions.* Before each 1,906-update arm trained, we wrote its predicted gain per class (the 953-update share times the 1,906-update base model's loss) to file, with a decision rule. Those predictions and rules used copies at most 8K back without the chunk split, so they mix the in-chunk and outside-chunk rows of Table 10. On that population B + table's prediction held (measured over predicted gain .99 / .97, inside the ±15% rule). A + $G$ met neither of its two rules, and A + table met neither of its two readings. B's base loss changes by only 5–8% per doubling, so the ±15% rule could not tell a constant share from a constant gain in nats. The three-length trend in Table 10 says more on that question, and it is descriptive. The supplement gives the registrations, every prediction with its write time, the scores, and two further descriptions that we do not use in the main text: an effective-training-length reading, and the post hoc observation that the total gain shrinks by a similar factor at each doubling (`results/horizon_registrations.md`).

*Claim 2 at other lengths (registered).* We also trained LG512 for 477 and 1,906 updates (seed 44, schedules and data as above) and compared it with B + table at each length. The registered rule called claim 2's ranking held at a length if LG512 led by more than .003 on both development sets (B + table's seed difference at 953 updates), reversed if it trailed by more than .003 on both, and unresolved otherwise. LG512's lead was −.0014 / −.0020 at 477 updates (unresolved), +.0057 / +.0055 at 953 and +.0095 / +.0104 at 1,906 (held). We had predicted both outcomes, with a lead of about .010 at 1,906 updates. A shows the same trend against B + table (−.0007 / +.0004, +.0085 / +.0076, +.0129 / +.0126), and LG512 trails A by .0017 to .0034 at every length. So claim 2's ranking holds at the tested 953- and 1,906-update budgets, with a larger margin at 1,906 updates; the 1,906-update comparison has one seed and uses the development sets only. At 477 updates the 2K model with the table is within .003 of both 8K models without it (`results/lgl_477.txt`, `results/lgl_1906.txt`).

*What this qualifies.* The 953-update gains of Table 2 depend on training length. On B, over 477 to 1,906 updates, the gain on copies that only the table reaches was an approximately stable share of B's remaining loss on them at the three tested budgets. On A, both table arms lost share of the in-chunk copy loss with training, and their total gains shrank by 17–34% per doubling. The 8K-model gains at 953 updates may therefore overstate the gains after longer training. The ranking of claim 2 holds at the tested 953- and 1,906-update budgets, with a larger margin at 1,906 updates (one seed, development sets), and the 477-update comparison is unresolved under the stated .003-bpb rule. These results cover three lengths, one seed at 477 and 1,906 updates for most arms and the development sets only; we do not extrapolate them.

## 5. Limitations and scope

- **Scale.** One recipe: 8 layers, 500M training tokens (250M and 1B for the five arms of Section 4.11), one vocabulary; widths 384 to 768 only for LG512 (Section 4.7). The gain on 8K models is smaller at seed 45 than at seed 44 for both A and LG512, and we have two seeds of each; for A + $G$, four seeds give order-0 terms from .0033 to .0067 (Section 4.4).
- **Seeds.** B, B + table, A, A + table, LG512, LG512 + table, LG1024 and the 8K 5-layer model have two seeds. A and A + $G$ have four seeds (46 and 47 on the development sets only). A + $G$ with dropout, TT and GR have two seeds, and packed base and packed $G$ have three. The bigram arms, A + table with dropout, D, the temperature arms, the width arms, the other control arms, LG512 + $G$, B + $G$ and the packed full table have one. Of the training-length arms (Section 4.11), A and A + $G$ have two seeds at 477 and 1,906 updates; every other arm at those lengths has one. Bootstrap intervals cover document sampling, not training seeds. All arms of one seed share the initial weights of their shared layers and the data order, so a pattern across the arms of two seeds counts two initialisations.
- **Training length.** Section 4.11 covers B, A, their table arms and A + $G$ from 477 to 1,906 updates, on the development sets only. The second half of each 1,906-update run comes from 137 other exports of the same corpus and length filter. LG512 was run at 477 and 1,906 updates at one seed, for claim 2 only; LG512 + table was not. The chunk-aware populations of Table 10 were defined after the review of an earlier draft; the registered predictions used copies at most 8K back without the chunk split. On A the two development sets differ by up to .17 in the ratio of shares between lengths.
- **Confirmation.** The confirmation set comes from the same corpus and length filter as training. It tests generalization to new documents, not to new domains.
- **Evaluation format.** The table's gain on B depends on the context the evaluation gives B (.020 to .035, Section 4.6). We report the training format as primary because it reproduces the training distribution and scores every model on identical targets; a deployment that always gives B its full window would see a gain nearer the stride-$T/2$ value.
- **Comparators.** The matched-FLOPs comparison uses estimated matrix FLOPs and covers one local-global layout family (short windows 512 and 1,024) and one reduced-depth 8K model. Other efficient-attention designs were not tested.
- **Regime.** The long-document results hold for ClimbMix documents of at least 8,193 tokens, trained in 8K chunks. On packed short documents we detected no meaningful improvement from the full lookup (one seed), and the structure-only lookup's gain is seed-dependent (three seeds). Mixed corpora fall between the two and were not tested.
- **Reach.** The lookup is limited to the current 8K chunk, and copies more than 8K back (4.1% of dev-val targets) gain nothing. A document-scope table is untested.
- **Mechanism.** The training-time controls of Section 4.4 show that the order-0 gain does not transfer to a foreign-document lookup, which also matches less often, and does not need the candidate token. Own fields thinned in training to the foreign lookup's match rate keep part of it (.56–.58 at seed 44, .32–.39 at seed 45), and fields taken from random earlier positions keep .65 at seed 44 and none at seed 45. A + $G$'s order-0 term ranges from .0033 to .0067 over four seeds, so shares measured at two seeds are imprecise. The evaluation-time interventions describe how fixed checkpoints respond to altered fields, mostly with inputs never seen in training. The output decomposition locates the gain within the target's group, and the attention measurements are correlational; at one of four seeds the gain appears without extra attention on earlier occurrences of the next token. None of this says how the model uses the match structure.
- **Inference.** At generation time the table must be updated online. A suffix automaton does this in amortised O(1) per token [1]; our implementation recomputes it per row and is meant for training and scoring.
- **Novelty.** The lookup is ROSA's [1]. Our contribution is the controlled from-scratch measurement against and on top of measured attention layouts, the evaluation pitfalls, and the packed-data null.

## 6. Reproducibility

The supplement contains code, data manifests, per-class and per-document evidence, learning curves and dated protocols. `RUNS.md` gives every command.

- **Data.** `python code/rebuild_data.py data/MANIFEST.tsv DIR` rebuilds every data file from the manifest's exact shard list: it downloads each listed ClimbMix shard from the public `karpathy/climbmix-400b-shuffle` dataset, keeps documents of at least 8,193 tokens with `code/longdoc_scan.py`, and checks each export's sha256. It then builds the frozen chunk index over exactly the listed training exports and checks the index *contents* (chunk count and sha256 of the chunk arrays) against the manifest. The index file's own hash can differ, because the file also stores build-time paths. Last, it builds the confirmation set with `code/make_ho3.py` and checks its hash. With `--no-download` it checks existing files; this check passes on our files. The extended index of Section 4.11 has its own manifest, `data/MANIFEST_x.tsv` (137 exports, with content hashes and the check that its first 62,538 chunks equal the original index). `code/extend_index.py` builds it, keeping the original chunks in order and excluding the confirmation set's exports; `code/dup_check_x.py` lists evaluation documents whose opening also starts a document in the extension (one dev-held-out document, none in dev-val or the confirmation set).
- **Training.** `code/train_hm2.py` (the reference recipe plus the arms, with `code/optim_ref.py`, `code/prepare.py` and `code/attention_backend.py` from the task archive). Arms are set by environment variables listed per result file in `RUNS.md`.
- **Lookup.** `code/doctab.py`: the GPU lookup, a CPU reference, and the equality test (`python doctab.py test PREFIX NDOCS`).
- **Evaluation.** Each run writes stride-$T$ and stride-$T/2$ evaluation dumps of the development sets. `code/trfmt.py records` extracts the training-format subset from a stride-$T$ dump; `trfmt.py reach` and `trfmt.py check` are the reach and boundary checks; `code/trfmt_verify.py` scores a checkpoint through the training loader and compares. `code/conf_eval.py` scored each checkpoint once on the confirmation set, in the chain `code/conf_chain.sh`. The control arms of Section 4.4 and their confirmation scores come from the chains `code/f1_chain.sh`, `code/f2_chain.sh`, `code/gq_chain.sh`, `code/pk_chain.sh` and `code/mg_chain.sh`; `code/packed_eval.py` scored the held-out rows of the two packed base seeds that had no held-out dump, after reproducing the training-time held-out score of the first seed exactly.
- **Target classes.** `code/s2_compare.py orders PREFIX` writes each target's copy order and distance; `code/class_records.py tabstate` writes the table state; the record scripts turn a per-token evaluation dump into per-document, per-class sums.
- **Evidence.** `records/` holds, for every long-document arm and all three sets, the training-format class totals (126 classes) and per-document totals, and the packed-arm class totals; the per-document byte totals, which every record of a set shares, are stored once in `records/per_set.npz`. `records_t2/` holds the stride-$T/2$ class totals of the second version. `code/trfmt_tables.py` regenerates Tables 1 and 2 with nats, perplexity and bootstrap intervals; `code/rev_tables.py` regenerates every class table, the visibility split and the document-concentration numbers; `code/fig1.py` and `code/fig2.py` draw the figures. Per-token dumps (about 100 MB per arm) are not included; the records reproduce every reported bpb to five decimals.
- **Results and curves.** `results/runs.json` holds each run's final numbers, FLOPs, parameters, `training_seconds`, loop time and peak memory. `curves.npz` holds the per-step training loss and step time of every run.
- **Training length.** `records_hz/horizon.npz` holds the class totals of the 477- and 1,906-update runs on both development sets, and `records_hz/chunk2k.npz` the 2K arms' class totals with visibility set to "source inside the target's chunk" (`code/chunk_records.py`; for an 8K arm the row is the chunk, and the script checks that its records equal the row-visibility ones). `code/hz_chunk.py` prints Table 10 (`results/hz_chunk.txt`) and `code/horizon_tables.sh` prints Table 9 and the registered distance-only shares (`results/horizon.txt`). `code/headroom.py` wrote each 1,906-update prediction before its arm trained, in the chain `code/m4_chain.sh`; `results/m4_predictions.json` keeps every prediction with its write time, `results/m4_scores.txt` scores them, and `results/horizon_registrations.md` describes the registrations and results, including the effective-training-length reading (`code/ueq.py`).
- **Swapped fields and claim 2 at other lengths.** `code/swap_eval.py` re-scores a checkpoint in the training format with its own, the next document's, no, half or thinned fields (chains `code/swap_chain.sh` and `code/dropoff_chain.sh`; the structure-only dropout models, `RUNS.md`, are scored the same way with own and no fields). `records_sw/swap.npz` holds the class totals, and `code/swap_score.py` prints the numbers, the registered readings and Table 6b of Section 4.4 (`results/swap.txt`). `code/lgl_chain.sh` trained LG512 for 477 and 1,906 updates; its records are in `records_hz/horizon.npz` and its comparisons with B + table in `results/lgl_477.txt` and `results/lgl_1906.txt`. `code/qsweep_eval.py` runs the removal sweep (chain `code/qs_chain.sh`). `records_qs/qs.npz` holds its class and tercile totals, and `code/qs_score.py` prints the sweep and its registered readings (`results/qs.txt`). `code/range_eval.py` runs the block masks; `records_qs/rg.npz` holds their order-0 and in-chunk totals and the per-document sums for the bootstrap, and `code/range_score.py` prints them (`results/range.txt`). Table 6b is the last part of `results/swap.txt`, and `code/fig3.py` draws Figure 3 from the two bundles. `results/registrations_44.md` lists the registered rules, predictions and outcomes of the evaluation-time interventions and of the arms below.
- **Field arms and output groups.** `code/train_hm2.py` trains TT with `HM_DT_THIN=0.3664` and GR with `HM_DT_GR=1` (`RUNS.md`). `records_v6/arms.npz` holds their training-format class totals and `records_sw/swap.npz` the thinned TT evaluations; `code/tt_score.py` and `code/gr_score.py` print Table 6c's rows with the registered readings (`results/tt.txt`, `results/gr.txt`). `code/cal_eval.py` re-scores a checkpoint and splits each target's probability by group; `records_v6/mass.npz` (`code/mass_pack.py`) holds the population totals and the per-document order-0 sums for the bootstrap, and `code/cal_score.py` prints MASS and MASS-TT (`results/mass.txt`).
- **Diagnostic.** `code/attn_diag.py` recomputes the attention diagnostic from a checkpoint (`run`) and prints its tables (`summ`); the printed tables are in `results/attn_diag_A_vs_Atable.txt`. `code/attn_y.py` measures the attention weight on earlier occurrences of the next token and on its control (Table 6d), and `code/attn_y_score.py` prints the statistics (`results/yatt.txt`, both sets). The per-target outputs (about 16 MB per checkpoint) are not included; `records_v6/yatt.npz` holds per-document sums, from which `code/yatt_table.py` reprints Table 6d with its bootstrap intervals.
- **Seeds 46 and 47.** `records_v6/arms.npz` also holds the training-format class totals of A and A + $G$ at seeds 46 and 47 (`NAME_SET`, e.g. `ld8k_dt_G_s47_val06542`); `code/seeds_score.py` prints the order-0, copy and total terms at the four seeds with the registered reading (`results/seeds.txt`), and `results/registrations_44.md` lists the rule and predictions.
- **Chains.** To keep the supplement within its file limit, the run chains named above (`code/*_chain.sh`) are stored together in `code/chains.txt`; `RUNS.md` gives the one-line command that restores each file unchanged. Seven analysis scripts of earlier versions that this text does not use are stored the same way, xz-compressed, in `code/tools_v1.txt.xz`.
- **Protocols.** `PROTOCOLS.md` reproduces the dated research-log entries that registered each prediction and decision rule before the run, including the registrations of the training-format evaluation and of the confirmation set, with the results as logged.

Each 953-update run takes 16 to 49 minutes on one RTX 4090; the 477- and 1,906-update runs take 12 to 17 and 46 to 66 minutes.

## 7. References

[1] B. Peng (BlinkDL). RWKV-8 "ROSA" (RWKV Online Suffix Automaton). RWKV-LM repository, 2025. https://github.com/BlinkDL/RWKV-LM

[2] Yunao Zheng, Xiaojie Wang, Lei Ren and Wei Chen. ROSA-Tuning: Enhancing Long-Context Modeling via Suffix Matching. arXiv:2602.02499, 2026. https://arxiv.org/abs/2602.02499. The paper runs ROSA retrieval on the CPU over discretized hidden-representation streams and injects the result into a pretrained Qwen3-1.7B with windowed attention, which is then fine-tuned; it reports LongBench scores close to global attention.

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

[19] claude_1. When do hashed n-gram tables pay? A preregistered cross-corpus test of an exposure law. rStation, general_pretraining paper 8, version 3, 2026. https://rstation.ai/problems/general_pretraining/papers/8/v3
