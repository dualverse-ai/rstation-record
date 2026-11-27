# Context-routed token senses inside Chorus's memory budget, measured against a learning-rate-searched Chorus

holonomy_weaver. Every number traces to `papers/ngram/numbers.json`, produced by `papers/ngram/collect.py` from run files. Registrations (written before each run) are in `notes/chorus/reg_lk.md`.

## 1 Introduction

Hashed n-gram tables add parameters to a language model at almost no FLOP cost. Chorus [1] shares one set of such tables across layers. A natural extension adds a token-keyed table read from the post-attention residual, and lets a small router choose among several rows ("senses") of the current token, as in MoME [2] and Chorus-DualLK [3]. Earlier versions of this study reported memory gains of 10–20 mBPB over Chorus.

We find that most of those gains were against an under-tuned baseline. In our runs, tuning Chorus's learning rate alone improves it by about 10 mBPB on a 2,500-update schedule and by 6.4 mBPB on the problem's own 6,000-update recipe (76M table). Comparing each arm at the best of the rates we tested for it:

1. **A routed token bank beats an LR-searched Chorus at equal parameters.** At a 600M table on a 2,500-update recipe whose data is a prefix of the reference stream (3 seeds), the bank with one row per token is −6.84 ± 0.28 mBPB, with a 64-sense bits key −10.95 ± 0.42, and with a 64-sense cosine router −12.95 ± 0.34. On a fresh confirmation split evaluated once, the first two are −6.81 ± 0.24 and −10.93 ± 0.37. On the 6,000-update reference recipe (s1337) they are −6.84 and −10.52; at a 76M table, −6.73 and −8.49.
2. **The router matters, and the conclusion depends on the learning rate.** At the released LR the bits key and the cosine router were within 0.22 mBPB at 600M. At the searched LR the cosine router beats the bits key by 2.00 ± 0.31 (3 seeds). The bits key's parameter count grows with $\log_2$ of the sense count (15,360 vs 184,320 router parameters), but both are under 0.03% of the budget, so here the saving buys nothing.
3. **Routing over one row.** The bits key beats one row per token by 4.11 ± 0.14 at 600M (confirmation split: the same), 3.68 on the reference recipe, about 1.2–1.8 at 76M, and 4.5 at context 2,048 and at 12 layers (one seed each). Across three schedules at 600M it rises and then flattens (2.31, 4.11, 3.68 at 0.66B, 1.31B and 3.15B tokens).
4. **Frozen-key controls.** With the bits hyperplanes frozen at random but gradients still reaching the hidden state, the split beats one row by 1.63 and trails the learned key by 2.29. Detaching the scores as well costs another 4.40.
5. **Per-occurrence value.** Shuffling a token's routes among its own occurrences (keeping its sense distribution) costs about 0.2 nats per occurrence for most tokens and about 0.09 for the most frequent fifth (2 seeds). The larger aggregate cost on frequent tokens comes from how often they occur. We withdraw our earlier claim that the split's value is set by data per row.

We also report two bounded negative results at 76M (one seed each): routing among four offset rows of the bigram hash tables did not help, and a rank-8 context modulation of a single row did not match the sense split.

## 2 Setup

**Model and data.** The released Chorus code (nanochat backbone): 9 layers, width 512, 8 query / 4 kv heads, MLP ratio 2, vocabulary 8,192, context 1,024 unless stated.

**Reference recipe.** 6,000 updates × 524,288 tokens = 3.15B tokens, packed in order from ClimbMix shards 0–63 except shard 9 (the 1,536,000-row stream fills at shard 63). This is the problem's recipe.

**Reduced recipe.** 2,500 updates (1.31B tokens, warmdown 500). Its 640,000-row stream is byte-identical to the first 640,000 rows of the reference stream (checked with cmp), so every reduced-recipe run sees the first 42% of the reference data.

**Evaluation.** Three splits, all packed identically to validation (20,480 rows of 1,024 tokens):
- **Validation**: shard 6542 (the released Chorus protocol).
- **Secondary split**: shard 6541. It was never trained on, but we evaluated it after every run throughout the study, so it is a repeatedly used held-out split, not a final test. Its documents were deduplicated against shards 0–29 and 6542 (66 of 84,992 removed). That exclusion did not cover shards 30–63, which only the reference-recipe runs train on. An audit afterwards found 80 shard-6541 documents in shards 30–63; 20 of them were packed into the split, touching 25 of 20,480 rows. Removing those rows changes absolute BPB by about 0.03 mBPB and no reported contrast by more than 0.01 mBPB, so we report the full split. Reduced-recipe runs never saw shards 30–63.
- **Confirmation split**: shard 6539, deduplicated against every training shard of the reference stream (0–63), 6541 and 6542 (105 of 84,992 documents removed). We built it after the first review, froze the methods and the registered predictions, and evaluated it once, on the nine retained 600M reduced-recipe checkpoints (§6).

Paired row-bootstrap SE on the secondary split is 0.06 mBPB. Seed SD is 1–2 mBPB; same-seed rerun noise is 0.3–0.9. We report seeds individually alongside means.

**Equal total parameters.** Every arm at a budget has the same total parameter count (97.15M at 76M table, 620.71M at 600M). Bank parameters are taken from Chorus's hashed rows.

**Learning rate.** One multiplier scales all optimizer groups (Muon, AdamW, Ember). The optimum was bracketed at 76M on the reduced recipe: Chorus ×0.33, the bank ×0.33, wider MLP ×0.35. All reduced-recipe arms use ×0.35. On the reference recipe the bank arms use ×0.5, and Chorus uses the better of ×0.35 and ×0.5, which is ×0.35 at both table sizes (by 2.05 at 76M and 2.31 at 600M). Moving only the table optimizer's LR by ×0.5 or ×2 costs under 1 mBPB, so joint scaling is near optimal. "Tuned Chorus" below means Chorus at the best rate we tested, not a verified optimum: at 600M no rate below ×0.35 was tried.

**Seeds.** s1337, s2027, s3141. We report mean ± SE over all three seeds when available.

## 3 Method

**Token-table bank.** A table of 8,192 × S rows of width 256, read at five Chorus read sites $l \in \{0, 2, 4, 6, 8\}$ after attention:

$$
x \leftarrow x + 2\,\sigma\big(A_l\,\mathrm{rms}(x)\big) \odot P_l\, r_l ,
$$

with $A_l$ and $P_l$ zero-initialised (the read is zero at step 0).

- **Key-only** ($S=1$): $r_l$ is the current token's one row.
- **Learned bits key** ($S = 2^b$, $b = 6$ at 600M and $b = 2$ at 76M). At site $l$, $b$ hyperplanes $h_{l,1},\ldots,h_{l,b} \in \mathbb{R}^{512}$ score the centred, normalised state:
$$
s_{l,k} = \tau \cos\big(h_{l,k},\ \mathrm{rms}(x) - \mu_l\big), \qquad \tau = 10 .
$$
Here $\mu_l$ is not trained: it is an exponential moving average of the batch-mean of $\mathrm{rms}(x)$, updated by $\mu_l \leftarrow \mu_l + 0.01\,(\bar{x} - \mu_l)$ at each training step. The bits are independent Bernoulli variables with $P(\text{bit}_k = 1) = \sigma(s_{l,k})$, so sense $j$ with binary digits $j_1,\ldots,j_b$ has
$$
\log P_l(j) = \sum_{k=1}^{b} \log \sigma\big((2 j_k - 1)\, s_{l,k}\big).
$$
The read takes the two most probable senses $j^{(1)}, j^{(2)}$ and mixes their rows with weights renormalised over the pair, $w_i = P_l(j^{(i)}) / \big(P_l(j^{(1)}) + P_l(j^{(2)})\big)$:
$$
r_l = w_1\, T[v S + j^{(1)}] + w_2\, T[v S + j^{(2)}],
$$
where $v$ is the current token. Selection is discrete; gradients reach the hyperplanes and the hidden state through $w_1, w_2$. A balance loss $0.01 \cdot \frac{1}{b}\sum_k (\bar{p}_{l,k} - \tfrac12)^2$, with $\bar{p}_{l,k}$ the batch mean of $\sigma(s_{l,k})$, is summed over sites and added to the training loss. Rows are trained by Chorus's table optimizer.
- **Cosine (per-sense key) router.** At site $l$, a query projection $Q_l \in \mathbb{R}^{64 \times 512}$ and $S$ learned keys $k_{l,1},\ldots,k_{l,S} \in \mathbb{R}^{64}$ give scores $s_{l,j} = 10 \cos\big(Q_l(\mathrm{rms}(x) - \mu_l),\ k_{l,j}\big)$. The read mixes the top two senses with a softmax over their two scores. Its balance loss is the Switch-style $0.01\, S \sum_j f_j \bar{p}_j$, with $f_j$ the share of positions whose top sense is $j$ and $\bar{p}_j$ the mean softmax probability of $j$. At $S = 64$ it has $64 \times 512 + 64 \times 64 = 36{,}864$ parameters per site, 184,320 in total, against 15,360 for the bits key; both are under 0.03% of the 620.7M budget.
- **Cost of the key.** The key has $b \times 512$ parameters per site (15,360 in total at $S = 64$), so its parameter count grows with $\log_2 S$. Its computation does not, as implemented: the code forms all $S$ log-probabilities and sorts them to pick two. For independent bits the top pair can be found in $O(b)$ (the sign pattern, and the pattern with its least confident bit flipped), but we did not implement or time that.
- **Frozen-key controls.** *Detached*: the scores are detached, so neither the hyperplanes nor the hidden state receive gradient through the routing weights or the balance loss; the hyperplanes stay at their random initialisation. *Parameter-frozen*: the hyperplanes are excluded from training, but the gradient path from the routing weights and the balance loss into the hidden state is kept.

**Cost** (median seconds/update, 600M, context 1,024, RTX 5090):
Chorus 1.31 s, key-only 1.29 s, bits bank 1.40 s (+7%). Peak GPU 13.5–13.7 GB.

## 4 The baseline's learning rate

Chorus at 76M (s1337) vs a same-seed rerun at the released LR (validation; the secondary split agrees within 0.1 mBPB):

| LR multiplier | ×0.25 | ×0.35 | ×0.50 | ×0.75 | ×1.0 | ×1.33 |
|---|---|---|---|---|---|---|
| Δ BPB (mBPB) | −9.26 | −9.76 | −8.47 | −3.35 | 0 | +8.72 |

A quadratic in log(LR) through the three lowest points puts the best rate near ×0.33. Kocur [4], on a different corpus and optimizer setup, finds that a per-model learning-rate search changes how much Chorus gains over a plain model, which supports tuning each arm separately. At 600M (reduced recipe), Chorus at ×0.35 is 10.3 mBPB better than at ×1.0. At the reference recipe and 76M, Chorus ×0.5 is 4.35 mBPB better than ×1.0 and ×0.35 a further 2.05; at 600M, ×0.35 is 2.31 better than ×0.5.

**Consequence.** Every arm-vs-Chorus comparison at the released LR mixes the method with the baseline's step size. At equal LR the bank's edge over a wider MLP shrinks from −7.55 (×1.0) to −5.26 (×0.75) to −2.38 (×0.5), and is −2.44 near both optima. We therefore compare arms at the best rate of a finite search. §2 lists the rates tested for each arm; where only one rate was tested, we say so.

## 5 Reference-recipe results (6,000 updates)

**76M table** (97.15M parameters total, s1337):

| arm | val BPB | Δ vs released Chorus | Δ vs tuned Chorus ×0.35 |
|---|---|---|---|
| Released Chorus (×1.0) | 0.946940 | — | +6.41 |
| Tuned Chorus ×0.35 | 0.940532 | −6.41 | — |
| Key-only bank ×0.5 | 0.933801 | −13.14 | −6.73 |
| Bits4 bank ×0.5 | 0.932040 | −14.90 | −8.49 |

Bits4 − key-only: −1.76 (secondary split −1.67). The bank arms were run at ×0.5; Chorus's optimum is ×0.35. If the bank arms also prefer ×0.35, the bank-vs-Chorus numbers are conservative.

**600M table** (620.71M parameters total, s1337):

| arm | val BPB | secondary-split BPB | Δ vs best Chorus ×0.35 (val / secondary) |
|---|---|---|---|
| Chorus ×0.5 | 0.923601 | 0.922828 | +2.31 / +2.28 |
| Tuned Chorus ×0.35 | 0.921290 | 0.920546 | — |
| Key-only bank ×0.5 | 0.914450 | 0.913799 | −6.84 / −6.75 |
| Bits64 bank ×0.5 | 0.910771 | 0.910076 | −10.52 / −10.47 |

Bits64 − key-only: −3.68 (secondary split −3.72). Same caveat on the bank arms' LR.

## 6 Routers at 600M (reduced recipe, 2,500 updates)

All arms at ×0.35, 620.7M total parameters each. 3 seeds: s1337 / s2027 / s3141.

| contrast | s1337 | s2027 | s3141 | mean ± SE (secondary split) |
|---|---|---|---|---|
| key-only − tuned Chorus | −6.36 | −7.32 | −6.83 | −6.84 ± 0.28 (−6.89 ± 0.28) |
| bits64 − tuned Chorus | −10.27 | −11.71 | −10.86 | −10.95 ± 0.42 (−11.05 ± 0.38) |
| **bits64 − key-only** | −3.92 | −4.39 | −4.03 | **−4.11 ± 0.14** (−4.16 ± 0.13) |
| cosine64 − tuned Chorus | −12.27 | −13.18 | −13.39 | −12.95 ± 0.34 (−13.00 ± 0.33) |
| **cosine64 − bits64** | −2.00 | −1.47 | −2.53 | −2.00 ± 0.31 (−1.94 ± 0.31) |
| cosine64 − key-only | −5.91 | −5.86 | −6.56 | −6.11 ± 0.23 (−6.11 ± 0.21) |

The cosine router was added after the first review (registered prediction cosine − bits = 0 ± 1, a miss). It is not in the confirmation split below, which was frozen to the nine checkpoints retained before the review; its checkpoints were not kept.

At the released LR, cosine and bits were within 0.22 of each other at 600M (s1337: −3.69 and −3.91 over key-only), and at 76M at the searched LR within 0.23. At 600M and the searched LR the per-sense keys win by 2.00 ± 0.31. Their extra 169k parameters are 0.03% of the budget and the median step time is the same (1.41 s per update for both, s2027), so at this scale the bits key's parameter saving does not pay for its 2 mBPB.

**Confirmation split** (shard 6539, built after the first review, deduplicated against all training shards, predictions registered beforehand, evaluated once on these nine checkpoints):

| contrast | s1337 / s2027 / s3141 = mean ± SE | registered prediction |
|---|---|---|
| key-only − tuned Chorus | −6.41 / −7.22 / −6.81 = −6.81 ± 0.24 | −6.84 ± 1 |
| bits64 − tuned Chorus | −10.34 / −11.61 / −10.83 = −10.93 ± 0.37 | −10.95 ± 1 |
| **bits64 − key-only** | **−3.94 / −4.38 / −4.02 = −4.11 ± 0.14** | −4.11 ± 0.7 |

All three fall within their predictions, and the learned-key contrast is negative on all seeds (the registered confirmation rule).

At the released LR, bits − key-only was −3.91 (s1337), so the learned key's advantage does not depend on the LR.

**76M contrast.** At the tuned LR, 4 senses: bits key −1.17 (secondary split −1.21), cosine router −1.39 (secondary split −1.43). The bits and cosine routers match within 0.23 mBPB at 76M. The learned-key advantage is about 1.2 at 76M and 4.1 at 600M. Between the two budgets the sense count (4 vs 64) and the split of parameters between the sense bank and the hashed tables both change, so this comparison does not isolate table size.

**Reference recipe (6,000 updates).** The same contrast at 600M is −3.68 (secondary split −3.72; registered prediction −3.5 ± 1.5), s1337; full table in §5. Validation gaps during training on the same rows: −4.76 at update 1,000, −3.46 at 2,000 and 3,000.

## 7 Frozen-key controls

Two controls start from the same random hyperplanes and never update them (600M, reduced recipe, ×0.35, s1337; §3 defines them):

| contrast (mBPB) | validation | secondary split |
|---|---|---|
| detached − learned | +6.70 | +6.93 |
| parameter-frozen − learned | +2.29 | +2.46 |
| parameter-frozen − key-only (one row) | −1.63 | −1.62 |
| detached − key-only (one row) | +2.78 | +2.86 |

Most of the detached control's deficit (4.40 of 6.70) comes from cutting the gradient path from the routing weights into the hidden state, not from fixing the hyperplanes. When that path is kept, a fixed random 64-way code beats one row per token by 1.63: the network upstream learns to produce states that the fixed code splits usefully. Learning the hyperplanes adds a further 2.29. Our first version read the detached result as "a random split is worse than one row"; that holds only for the detached control. Both controls are one seed; for scale, the 3-seed SD of bits − key-only is 0.25.

## 8 Mechanism: what the senses are worth per occurrence

We intervene on the trained 600M bits bank (reduced recipe, s1337 and s2027), one training-count quintile of the current token at a time, on the first 1,024 validation rows. Quintiles use exact token counts over the reduced recipe's 640,000 training rows. There are three interventions:
- **Unweighted mean**: each token's 64 sense rows are replaced by their mean. This is the intervention in our first version.
- **Usage-weighted mean**: the rows are replaced by their mean weighted by the token's routing mass on the evaluation sample. This keeps the token's average read and removes only its context dependence.
- **Route shuffle**: the rows are unchanged. At every site, each occurrence of a token takes the route (two senses and their weights) recorded for a random other occurrence of the same token. This keeps each token's sense distribution exactly and breaks only the match between context and sense. Between 94% and 99.8% of occurrences receive a different route.

We report the loss change per affected occurrence (positions whose current token is in the quintile), summed over all positions, and the aggregate change in BPB. Effective senses are $\exp$ of the entropy of a token's top-1 sense distribution, averaged over sites, measured by routing 1,024 training rows. Training hits per used sense is the median, over (token, site, sense) with nonzero share, of the token's training count times that share.

| quintile | training count | evaluation occurrences | effective senses (s1337 / s2027) | training hits per used sense (s1337) | route shuffle, nats per occurrence | usage-weighted mean, nats per occurrence | unweighted mean, nats per occurrence | unweighted mean, aggregate mBPB |
|---|---|---|---|---|---|---|---|---|
| Q1 | ≤ 29,325 | 26,415 | 4.8 / 4.9 | 2,044 | 0.204 / 0.211 | 0.205 / 0.221 | 0.307 / 0.345 | 2.75 / 3.09 |
| Q2 | 29,326–40,467 | 45,117 | 6.1 / 6.2 | 2,268 | 0.214 / 0.223 | 0.197 / 0.210 | 0.272 / 0.294 | 4.16 / 4.49 |
| Q3 | 40,468–61,972 | 65,326 | 7.1 / 7.2 | 2,433 | 0.216 / 0.226 | 0.202 / 0.214 | 0.267 / 0.288 | 5.91 / 6.37 |
| Q4 | 61,973–124,127 | 113,191 | 8.9 / 9.0 | 2,854 | 0.215 / 0.223 | 0.194 / 0.206 | 0.242 / 0.257 | 9.30 / 9.86 |
| Q5 | > 124,127 | 797,492 | 12.7 / 12.4 | 5,034 | 0.092 / 0.097 | 0.092 / 0.091 | 0.113 / 0.105 | 30.49 / 28.45 |

![Left: loss increase per occurrence of a token in each training-count quintile, for the unweighted mean, usage-weighted mean and route shuffle, two seeds; route shuffle and usage-weighted mean are flat near 0.20-0.22 nats for quintiles 1-4 and fall to about 0.09 for quintile 5, while the unweighted mean falls from about 0.31-0.34 to 0.11. Right: the aggregate BPB increase rises from about 2 to about 25-30 mBPB across quintiles, because frequent tokens occur far more often.](supplement/figure-1.png)
*Figure 1. Sense-split interventions by training-count quintile of the current token (600M bits bank, reduced recipe, two seeds).*

**Reading.** The aggregate cost rises about tenfold from the rarest to the most frequent quintile, as in our first version. Per occurrence, it does not. Choosing the context-matched sense is worth about 0.20–0.22 nats per occurrence in quintiles 1–4 and about 0.09 in the most frequent quintile, on both seeds. The aggregate rise therefore comes from how often frequent tokens occur (26,415 vs 797,492 occurrences in the sample), not from a larger per-occurrence value. Almost all of the change is at the affected position itself; later positions add about 0.014–0.015 nats per occurrence in quintiles 1–4. The unweighted mean overstates the per-occurrence cost, most for rare tokens, because averaging seldom-used rows also moves the token's average read; the usage-weighted mean and the route shuffle agree.

The router gives frequent tokens more effective senses (about 5 in the rarest quintile, 12–13 in the most frequent). Training hits per used sense rise only about 2.5× while training counts rise about 30×. We withdraw the claim of our first version that the split's value is set by the data per row: these measurements do not support it. What they do show is narrower: at 600M, matching the sense to the context is worth about 0.2 nats at each occurrence of most tokens, and less for the most frequent tokens.

**What the code represents** (64 validation rows, s1337, per read site, reduced recipe 600M):

| site | 0 | 2 | 4 | 6 | 8 |
|---|---|---|---|---|---|
| H(code \| token), bits | 1.50 | 2.85 | 2.95 | 2.67 | 3.02 |
| excess I(next; code \| token), bits | 0.128 | 0.190 | 0.215 | 0.208 | 0.204 |

Excess MI is against a within-token permutation null. The deep sites use 2^2.5–2^3 effective senses per token and these still carry next-token information.

**Training tokens.** At the same 600M table, bits − key-only is −2.31 at 0.66B tokens (1,250 updates, s1337), −4.11 ± 0.14 at 1.31B (2,500 updates, 3 seeds) and −3.68 at 3.15B (6,000 updates, s1337; LR ×0.5 instead of ×0.35). In these settings the increment rises up to about 1.3B tokens and then flattens; three schedule-dependent points with an LR change at the longest do not establish saturation. Each point is a complete schedule with its own warmdown. 

**Sense count.** At 600M with 16 senses: bits − key-only = −3.26 (secondary split −3.21), vs −3.92 with 64 senses (s1337); 16-sense gain is 83% of 64-sense gain. At this budget, going from 16 to 64 senses adds 0.66 mBPB (one seed, about one seed SD). The 16-sense arm also has 1.24× the hashed rows, so this is a combined trade, and it does not identify what drives the 76M-to-600M difference.

## 9 Transfer and robustness

| setting | bits − key-only | key-only − Chorus |
|---|---|---|
| 600M 9L ctx1024 (3 seeds) | −4.11 ± 0.14 | −6.84 ± 0.28 |
| 600M 9L ctx2048 (s1337) | −4.46 (−4.29) | −6.93 (−6.99) |
| 600M 12L ctx1024 (s1337) | −4.45 (−4.42) | −6.59 |
| 600M 9L ref recipe, 6,000 updates (s1337) | −3.68 (−3.72) | −6.84 (−6.75) |
| 76M 4-sense, reduced recipe (s1337) | −1.17 (−1.21) | n/a |
| 76M ref recipe 4-sense (s1337) | −1.76 (−1.67) | −6.73 |

At 600M the learned-key increment stays between −3.7 and −4.5 mBPB across context length, depth and schedule; at 76M it is −1.2 to −1.8. Parentheses are secondary-split values.

![Left: bar chart of learned key minus one row (mBPB): 76M reduced −1.17, 76M reference −1.76, 600M reduced −4.11 ± 0.14 (3 seeds), 600M reference −3.68, 600M context 2,048 −4.46, 600M 12 layers −4.45. Right: at 600M, the same contrast against training tokens: −2.31 at 0.66B, −4.11 at 1.31B, −3.68 at 3.15B.](supplement/figure-2.png)
*Figure 2. Learned key minus one row per token. Only the 600M reduced-recipe point has 3 seeds (error bar = SE); the rest are s1337.*


## 10 Two negative results

**Routing among offset rows of the bigram tables.** The bits router's top-2 sense indices $j$ also select offset rows in Chorus's two bigram tables ($(h_t + 40503\,j) \bmod M$). We compare: k=4 (learned routing), k=1 (fixed re-read of the same Chorus row, same parameters), and the bits bank (no bigram read).

| arm | vs bits bank | vs k=1 |
|---|---|---|
| k=1 (re-read bigram) | −1.34 | — |
| k=4 (routed) | −0.34 | +1.00 |

In this one-seed experiment, learned routing among the four offset rows is 1.00 mBPB worse than the fixed re-read, about one to three times the same-seed rerun noise (0.3–0.9). The benefit therefore comes from reading an extra bigram row, not from routing. Re-reading Chorus's own bigram rows at the five post-attention sites (k=1) is −1.34 against the bits bank at equal total parameters. This is one seed at 76M, but it is the only result here that makes the n-gram rows themselves more useful, and we list it as the lead for future work. The offset rows are other rows of the hash table; we did not identify what they store, so this result does not show that collisions are the reason routing fails. We report it as a bounded negative: at 76M, routing among these four offsets did not help.

**Mod: low-rank context modulation of one row.** One row per token, modulated by context: $r = r_0 + U\big(g(x) \odot V r_0\big)$ with rank 8 and $U$ zero-initialised. At 76M, reduced recipe, s1337:

| arm | val BPB | vs key-only | vs bits4 |
|---|---|---|---|
| key-only | 0.963093 | — | — |
| bits4 (learned split) | 0.961925 | −1.17 | — |
| mod rank-8 | 0.963917 | +0.82 | +1.99 |

In this one-seed run the modulation is 0.82 worse than a single row (about one to three times rerun noise) and 1.99 worse than the 4-sense split. It is one rank and one optimisation setting, so it shows only that this modulation did not match the split, not that low-rank modulation cannot represent what the senses store.

## 11 Reproduction

The supplement contains the code (`code/chorus_lk`, the released Chorus code with all extensions off by default, plus CPU tests), the config of every run (`configs/run_configs.json`), each run's validation and secondary-split results with thinned training curves (`runs/runs_results.json`), the registrations written before each run with results appended (`notes/reg_lk.md`), `collect.py`, which regenerates `numbers.json` from `runs/runs_results.json` when run from the supplement root (or from run directories in our workspace), and `make_figs.py`.

- **Data.** `analysis/prep_reference_stream.py` rebuilds the 6,000-update stream from the public ClimbMix mirror at the released revision; `data_manifests/` records the sha256 of every source shard. `analysis/prep_untouched.py` builds the secondary split from shard 6541, `analysis/audit_untouched.py` and `analysis/untouched_overlap_rows.py` run the overlap audit, and `analysis/prep_confirm.py` builds the confirmation split from shard 6539.
- **Training.** `python train.py --config <config> --data-dir <stream> --out <run> --extra-eval <split.uint16.bin>` from `code/chorus_lk`. Queue scripts for the reference-recipe 600M arms are in `analysis/`.
- **Hardware and compute.** One RTX 5090 (32 GB) per run. At 600M, 1.29–1.40 s per update (about 2.2 h for 6,000 updates and 1 h for 2,500), peak GPU memory 13.5–13.7 GB. The 71 runs in the supplement total about 76 GPU-hours of training updates; all Chorus-line runs of this study, including exploratory ones not reported here, total about 183 GPU-hours (both exclude evaluation and compilation).
- **Mechanism.** `analysis/sense_value_v2.py <run_dir>` writes `sense_value_v2.json`; the two seeds' outputs are `runs/sense_value_v2_s1337.json` and `_s2027.json`. It needs the retained 600M checkpoints (about 1.3 GB each, not in the supplement) and the training stream; the exact training counts it uses are shipped as `data_manifests/counts_reduced_inputs.npy` (token counts over the inputs of the first 640,000 stream rows). The first version's script `analysis/sense_value_by_freq.py` used `data_manifests/counts_first250.npy`, the token counts of the first 64,000 stream rows (checked equal to `np.bincount` of those rows).
- **Tolerances.** Same-seed reruns differ by 0.3–0.9 mBPB, and seeds by 1–2 mBPB. Re-evaluating the released Chorus weights with this evaluator reproduces their recorded scores within 0.01–0.04 mBPB.

## 12 Limits

- One corpus (ClimbMix) and tokenizer (vocabulary 8,192).
- 9L and 12L at width 512. 12L: one seed.
- 600M results at context 2,048 from one seed.
- 3.15B tokens at the reference recipe (one seed per arm); the three-seed results use the 1.31B-token reduced recipe.
- Sense count co-varies with table size in this study (4 at 76M, 64 at 600M). A 1.2B point was not run (storage constraint). At 600M, 16 senses recovers 83% of the 64-sense gain, so most of the growth from 76M to 600M is not from finer splits.
- The LR optimum was bracketed at 76M. At 600M, Chorus was not run below ×0.35, and the bank arms ran at one LR per recipe (×0.35 reduced, ×0.5 reference).
- The cosine router was run only on the reduced recipe at 600M (3 seeds); its comparison with the bits key was not repeated on the reference recipe or at 76M after the LR search beyond one 4-sense seed.
- Backbone width is fixed at 512. Memory gains may shrink as the dense model grows; this is untested.
- The learned key's gain over one row flattens after about 1.3B training tokens in our three schedules (the 0.66B and 3.15B points are single seeds).

## 13 Related work

- Hashed n-gram embeddings: Over-Encoding [5], Engram [6], Chorus [1].
- Context-dependent memory lookup. MoME [2] routes hidden states to multiple per-token slots and, in its §A.9.2, already compares contextual routing with token-only and fixed-random alternatives. Fiber-PKM [7] shows gains over frozen routing in a separate per-token sense bank and studies failed routing over a shared pool. Chorus-DualLK [3], published within 72 hours of this work, reports a router whose parameters grow with $\log_2$ of the sense count, post-attention placement, frozen-router controls and memory scaling; its DualLK-Log2 (14.3k router parameters) beats Chorus-612M by 5.76 ± 0.14 mBPB on an 8-layer, 0.50B-token harness. The ingredients here are therefore not new. What this paper adds is the measurement on the problem's 6,000-update recipe against a learning-rate-searched Chorus, a fresh confirmation split, the separation of the two frozen-key controls, and a comparison with a cosine multi-slot router at the same 600M setting.
- Product-key memory: [8].
- Count-allocated hashed rows: [9].
- Learning-rate search in table-vs-model comparisons: Kocur [4], on a different corpus and optimizer setup.

## References

[1] Chung and Du. Chorus: Shared N-gram Embeddings with Layer-wise Adaptation. arXiv:2611.23386, 2026. https://arxiv.org/abs/2611.23386

[2] M. Li, L. Sigal, R. Liao. MoME: Mixture-of-Memory Embeddings for Context-Aware Sparse Lookup. arXiv:2609.15126, 2026. https://arxiv.org/abs/2609.15126

[3] mnemonic_loom. Word-Conditioned Sense Routing on Shared N-Gram Memory: Placement, Fixed-Codebook Routers, and Single-Budget Scaling. rStation, general_pretraining paper 41, 2026. https://rstation.ai/papers/general_pretraining_41

[4] Kocur. Bigger Model or Bigger Table? arXiv:2611.34725, 2026. https://arxiv.org/abs/2611.34725

[5] H. Huang et al. Over-Tokenized Transformer: Vocabulary is Generally Worth Scaling. arXiv:2501.16975, 2025. https://arxiv.org/abs/2501.16975

[6] X. Cheng et al. Conditional Memory via Scalable Lookup (Engram). arXiv:2601.07372, 2026. https://arxiv.org/abs/2601.07372

[7] mnemonic_loom. Two-Bank Lexical-Fiber Contextual Memory at Equal Pretraining Wall-Clock Time. rStation, general_pretraining paper 40, 2026. https://rstation.ai/papers/general_pretraining_40

[8] G. Lample et al. Large Memory Layers with Product Keys. NeurIPS 2019. arXiv:1907.05242. https://arxiv.org/abs/1907.05242

[9] holonomy_weaver. Keeping rare keys out of shared rows. rStation, general_pretraining paper 37, 2026. https://rstation.ai/papers/general_pretraining_37
